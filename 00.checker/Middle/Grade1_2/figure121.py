import random
import math
from typing import List
import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl
import numpy as np
from matplotlib.path import Path
import random
import io
import sys 
import math
from PIL import Image
from matplotlib.patches import Arc
from matplotlib.transforms import IdentityTransform, TransformedBbox, Bbox

#plt.rcParams['text.usetex'] = True
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf8')

class AngleAnnotation(Arc):
    """
    Draws an arc between two vectors which appears circular in display space.
    """
    def __init__(self, xy, p1, p2, size=75, unit="points", ax=None,
                 text="", textposition="inside", text_kw=None, **kwargs):
        """
        Parameters
        ----------
        xy, p1, p2 : tuple or array of two floats
            Center position and two points. Angle annotation is drawn between
            the two vectors connecting *p1* and *p2* with *xy*, respectively.
            Units are data coordinates.

        size : float
            Diameter of the angle annotation in units specified by *unit*.

        unit : str
            One of the following strings to specify the unit of *size*:

            * "pixels": pixels
            * "points": points, use points instead of pixels to not have a
              dependence on the DPI
            * "axes width", "axes height": relative units of Axes width, height
            * "axes min", "axes max": minimum or maximum of relative Axes
              width, height

        ax : `matplotlib.axes.Axes`
            The Axes to add the angle annotation to.

        text : str
            The text to mark the angle with.

        textposition : {"inside", "outside", "edge"}
            Whether to show the text in- or outside the arc. "edge" can be used
            for custom positions anchored at the arc's edge.

        text_kw : dict
            Dictionary of arguments passed to the Annotation.

        **kwargs
            Further parameters are passed to `matplotlib.patches.Arc`. Use this
            to specify, color, linewidth etc. of the arc.

        """
        self.ax = ax or plt.gca()
        self._xydata = xy  # in data coordinates
        self.vec1 = p1
        self.vec2 = p2
        self.size = size
        self.unit = unit
        self.textposition = textposition

        super().__init__(self._xydata, size, size, angle=0.0,
                         theta1=self.theta1, theta2=self.theta2, **kwargs)

        self.set_transform(IdentityTransform())
        self.ax.add_patch(self)

        self.kw = dict(ha="center", va="center",
                       xycoords=IdentityTransform(),
                       xytext=(0, 0), textcoords="offset points",
                       annotation_clip=True)
        self.kw.update(text_kw or {})
        self.text = ax.annotate(text, xy=self._center, **self.kw)

    def get_size(self):
        factor = 1.
        if self.unit == "points":
            factor = self.ax.figure.dpi / 72.
        elif self.unit[:4] == "axes":
            b = TransformedBbox(Bbox.from_bounds(0, 0, 1, 1),
                                self.ax.transAxes)
            dic = {"max": max(b.width, b.height),
                   "min": min(b.width, b.height),
                   "width": b.width, "height": b.height}
            factor = dic[self.unit[5:]]
        return self.size * factor

    def set_size(self, size):
        self.size = size

    def get_center_in_pixels(self):
        """return center in pixels"""
        return self.ax.transData.transform(self._xydata)

    def set_center(self, xy):
        """set center in data coordinates"""
        self._xydata = xy

    def get_theta(self, vec):
        vec_in_pixels = self.ax.transData.transform(vec) - self._center
        return np.rad2deg(np.arctan2(vec_in_pixels[1], vec_in_pixels[0]))

    def get_theta1(self):
        return self.get_theta(self.vec1)

    def get_theta2(self):
        return self.get_theta(self.vec2)

    def set_theta(self, angle):
        pass

    # Redefine attributes of the Arc to always give values in pixel space
    _center = property(get_center_in_pixels, set_center)
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)
    width = property(get_size, set_size)
    height = property(get_size, set_size)

    # The following two methods are needed to update the text position.
    def draw(self, renderer):
        self.update_text()
        super().draw(renderer)

    def update_text(self):
        c = self._center
        s = self.get_size()
        angle_span = (self.theta2 - self.theta1) % 360
        angle = np.deg2rad(self.theta1 + angle_span / 2)
        r = s / 2
        if self.textposition == "inside":
            r = s / np.interp(angle_span, [60, 90, 135, 180],
                                          [3.3, 3.5, 3.8, 4])
        self.text.xy = c + r * np.array([np.cos(angle), np.sin(angle)])
        if self.textposition == "outside":
            def R90(a, r, w, h):
                if a < np.arctan(h/2/(r+w/2)):
                    return np.sqrt((r+w/2)**2 + (np.tan(a)*(r+w/2))**2)+5
                else:
                    c = np.sqrt((w/2)**2+(h/2)**2)
                    T = np.arcsin(c * np.cos(np.pi/2 - a + np.arcsin(h/2/c))/r)
                    xy = r * np.array([np.cos(a + T), np.sin(a + T)])
                    xy += np.array([w/2, h/2])
                    return np.sqrt(np.sum(xy**2))

            def R(a, r, w, h):
                aa = (a % (np.pi/4))*((a % (np.pi/2)) <= np.pi/4) + \
                     (np.pi/4 - (a % (np.pi/4)))*((a % (np.pi/2)) >= np.pi/4)
                return R90(aa, r, *[w, h][::int(np.sign(np.cos(2*a)))])

            bbox = self.text.get_window_extent()
            X = R(angle, r, bbox.width, bbox.height)
            trans = self.ax.figure.dpi_scale_trans.inverted()
            offs = trans.transform(((X-s/2), 0))[0] * 72
            self.text.set_position([offs*np.cos(angle), offs*np.sin(angle)])
            
def line_equation(p1, p2, x):
    y = ((p2[1]-p1[1])/(p2[0]-p1[0])) * (x-p1[0]) + p1[1]

    return y
    
# 막대 그래프
def drawBar(ax, xvalue, yvalue, xlabel='', ylabel=''):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    width = 0.35

    x = np.arange(len(xvalue))
    ax.bar(x=x-width/3, height=yvalue[0], width=width, color=random.choice(colors))
    ax.bar(x=width/3, height=yvalue[1], width=width, color=random.choice(colors))
    ax.bar(x=x+width/3, height=yvalue[2], width=width, color=random.choice(colors))
    '''
    for i in range(len(yvalue)):
        if i == 0:
            ax.bar(x=x-width/2, height=yvalue[i], width=width, color=random.choice(colors))
        else:
            ax.bar(x=x+width/2, height=yvalue[i], width=width, color=random.choice(colors))
    '''
    
    ax.set_ylabel(ylabel)
    ax.set_xticks(x)
    ax.set_xticklabels(xvalue)
    #ax.legend()

# 직선 또는 다각형 그리는 함수
def drawPolygon(ax, verts, fill=False, alpha=1, dash=False, lw=1):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    vert = verts
    vert.append(verts[0])
    codes = [Path.MOVETO]

    for i in range(0,len(vert)-2):
        codes.append(Path.LINETO)

    codes.append(Path.CLOSEPOLY)

    path = Path(vert,codes)
    
    if fill:
        if dash:
            pp = mpatches.PathPatch(path, fc=random.choice(colors), fill=True, lw=lw, ls='--', zorder=3, alpha=alpha)
        else:
            pp = mpatches.PathPatch(path, fc=random.choice(colors), fill=True, lw=lw, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.PathPatch(path, ec='black', fill=False, lw=lw, ls='--', zorder=3)
        else:
            pp = mpatches.PathPatch(path, ec='black', fill=False, lw=lw, zorder=3)
    ax.add_patch(pp)

# 정다각형 그리는 함수
def drawRegular(ax, center, n, radius, fill=False, alpha=1, dash=False, lw=1):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    if fill:
        if dash:
            pp = mpatches.RegularPolygon(xy=center, numVertices=n, radius=radius, orientation=0.1, fc=random.choice(colors), fill=True, ec='black', lw=lw, ls='--', zorder=3, alpha=alpha)
        else:
            pp = mpatches.RegularPolygon(xy=center, numVertices=n, radius=radius, orientation=0.1, fc=random.choice(colors), fill=True, ec='black', lw=lw, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.RegularPolygon(xy=center, numVertices=n, radius=radius, orientation=0.1, ec='black', fill=False, lw=lw, ls='--', zorder=3)
        else:
            pp = mpatches.RegularPolygon(xy=center, numVertices=n, radius=radius, orientation=0.1, ec='black', fill=False, lw=lw, zorder=3)

    ax.add_patch(pp)

    return pp.get_path(), pp.get_patch_transform()

def drawNormalPoly(ax, xy, radius, resolution, fill=False, alpha=1, dash=False, lw=1):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    pp = mpatches.CirclePolygon(xy=xy, radius=radius, resolution=resolution)

    ax.add_patch(pp)

# 원 그리는 함수
def drawCircle(ax,center, radius, fill=False, alpha=1, dash=False, position=None, lw=1):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    x_min = ax.get_xlim()[0]
    x_max = ax.get_xlim()[1]

    y_min = ax.get_ylim()[0]
    y_max = ax.get_ylim()[1]

    if center[0]-radius-0.5 < x_min:
        x_min = center[0]-radius-0.5
    if center[0]+radius+0.5 > x_max:
        x_max = center[0]+radius+0.5
    if center[1]-radius-0.5 < y_min:
        y_min = center[1]-radius-0.5
    if center[1]+radius+0.5 > y_max:
        y_max = center[1]+radius+0.5

    maxlim = max(x_max, y_max)
    minlim = min(x_min, y_min)

    ax.set_xlim(minlim, maxlim)
    ax.set_ylim(minlim, maxlim)

    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    if position != None and fill == False:
        if position == 'left':
            theta1 = 90
            theta2 = 270
        elif position == 'right':
            theta1 = -90
            theta2 = 90
        elif position == 'top':
            theta1 = 0
            theta2 = 180
        elif position == 'bottom':
            theta1 = 180
            theta2 = 360

        if dash:
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=lw, ls='--', fill=False, zorder=3)
        else:
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=lw, fill=False, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Circle(center,radius=radius, fc=random.choice(colors), ec='black', lw=lw, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Circle(center,radius=radius, fc=random.choice(colors), ec='black', lw=lw, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Circle(center,radius=radius, ec='black', lw=lw, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Circle(center,radius=radius, ec='black', lw=lw, fill=False, zorder=3)
    ax.add_patch(pp)

# 타원 그리는 함수
def drawEllipse(ax,center, width, height, fill=False, alpha=1, dash=False, position=None, lw=1):
    radius = max(width, height)/2

    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    x_min = ax.get_xlim()[0]
    x_max = ax.get_xlim()[1]

    y_min = ax.get_ylim()[0]
    y_max = ax.get_ylim()[1]

    if center[0]-radius-0.5 < x_min:
        x_min = center[0]-radius-0.5
    if center[0]+radius+0.5 > x_max:
        x_max = center[0]+radius+0.5
    if center[1]-radius-0.5 < y_min:
        y_min = center[1]-radius-0.5
    if center[1]+radius+0.5 > y_max:
        y_max = center[1]+radius+0.5

    maxlim = max(x_max, y_max)
    minlim = min(x_min, y_min)

    ax.set_xlim(minlim, maxlim)
    ax.set_ylim(minlim, maxlim)

    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    if position != None and fill == False:
        if position == 'left':
            theta1 = 90
            theta2 = 270
        elif position == 'right':
            theta1 = -90
            theta2 = 90
        elif position == 'top':
            theta1 = 0
            theta2 = 180
        elif position == 'bottom':
            theta1 = 180
            theta2 = 360

        if dash:
            pp = mpatches.Arc(center, width=width, height=height, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=lw, ls='--', zorder=3)
        else:
            pp = mpatches.Arc(center, width=width, height=height, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=lw, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=random.choice(colors), ec='black', lw=lw, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=random.choice(colors), ec='black', lw=lw, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, ec='black', lw=lw, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, ec='black', lw=lw, fill=False, zorder=3)

    ax.add_patch(pp)

# 각을 그리는 함수
def drawAngle(ax, p3, p2, p1):
    
    dx1 = p1[0] - p2[0]
    dy1 = p1[1] - p2[1]

    dx2 = p3[0] - p2[0]
    dy2 = p3[1] - p2[1]

    a1 = math.degrees(math.atan2(dy1,dx1))
    a2 = math.degrees(math.atan2(dy2,dx2))

    d = (math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)+math.sqrt((p3[0]-p2[0])**2+(p3[1]-p2[1])**2))/2
    #d = 4

    a1=round(a1)-6
    a2=round(a2)-6
    angle = round(a2 -a1)
    #print(a1,a2)
    if angle < 0:
        angle = 360 + angle

    if angle < 30:
        pp = mpatches.Arc(p2, angle=0, width=0.25*d, height=0.25*d, theta1=a1, theta2=a2, ec='red', zorder=3)
    elif angle > 90:
        pp = mpatches.Arc(p2, angle=0, width=0.2*d, height=0.2*d, theta1=a1, theta2=a2, ec='red', zorder=3)
    else:
        if angle == 90:
            if a1 == 0.0 and a2 ==90.0:
                verts = [
                    (p2[0]+0.1*d,p2[1]),
                    (p2[0]+0.1*d,p2[1]+0.1*d),
                    (p2[0],p2[1]+0.1*d)
                ]
            elif a1 == 90.0 and a2 == 180.0:
                verts = [
                    (p2[0]-0.1*d,p2[1]),
                    (p2[0]-0.1*d,p2[1]+0.1*d),
                    (p2[0],p2[1]+0.1*d)
                ]
            elif a1 == 180.0 and a2 == -90.0:
                verts = [
                    (p2[0]-0.1*d,p2[1]),
                    (p2[0]-0.1*d,p2[1]-0.1*d),
                    (p2[0],p2[1]-0.1*d)
                ]
            elif a1 == -90.0 and a2 == 0.0:
                verts = [
                    (p2[0]+0.1*d,p2[1]),
                    (p2[0]+0.1*d,p2[1]-0.1*d),
                    (p2[0],p2[1]-0.1*d)
                ]
            elif a1 == 45.0 and a2 == 135.0:
                verts = [
                    (p2[0]-math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d)),
                    (p2[0],p2[1]+2*math.sqrt(0.01*d)),
                    (p2[0]+math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d))
                ]
            elif a1 >= 135.0 and a2 <= -135.0:
                verts = [
                    (p2[0]-math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d)),
                    (p2[0]-2*math.sqrt(0.01*d),p2[1]),
                    (p2[0]-math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d))
                ]
            elif a1 == -135.0 and a2 == -45.0:
                verts = [
                    (p2[0]-math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d)),
                    (p2[0],p2[1]-2*math.sqrt(0.01*d)),
                    (p2[0]+math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d))
                ]
            else:
                verts = [
                    (p2[0]+math.sqrt(0.1*d),p2[1]+math.sqrt(0.1*d)),
                    (p2[0]+2*math.sqrt(0.1*d),p2[1]),
                    (p2[0]+math.sqrt(0.1*d),p2[1]-math.sqrt(0.1*d))
                ]
            
            codes = [
                    Path.MOVETO,
                    Path.LINETO,
                    Path.LINETO
                ]
            path = Path(verts,codes)

            pp = mpatches.PathPatch(path, ec='red', fill=False, zorder=3)
        else:
            pp = mpatches.Arc(p2, angle=0, width=0.2*d, height=0.2*d, theta1=a1, theta2=a2, ec='red', zorder=3)
        
    mid = ((p3[0]+p1[0])/2, (p3[1]+p1[1])/2)
    if mid[0]-p2[0] == 0:
        x = p2[0]
        if 0 <= a1 <= 90:
            y = p2[1]+0.2*d
        elif -180 <= a1 <= -90:
            y = p2[1]-0.2*d
    elif mid[1]-p2[1] == 0:
        y = p2[1]
        if 90 <= a1 <= 180:
            x = p2[0]-0.2*d
        elif -90 <= a1 <= 0:
            x = p2[0]+0.2*d
    else:
        n = (mid[1]-p2[1])/(mid[0]-p2[0])

        if 0 <= a1 < 90:
            if angle <= 90:
                x = p2[0]+0.08*d
            else:
                x = p2[0]-0.08*d
        elif 90 <= a1 < 180:
            x = p2[0]-0.08*d
        elif -180 <= a1 < -90:
            x = p2[0]-0.08*d
        else:
            x = p2[0]+0.08*d

        y = n*(x-p2[0])+p2[1]

    ax.add_patch(pp)

# bezier 곡선의 제어점의 좌표를 구하는 함수
def controlPoint(p1, p2, type):
    d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    #d = 2
    # 지나는 점 (p1, p2의 중점)
    mp = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

    if (p2[0]-p1[0]) == 0:
        if type == 'left' or type == 'top':
            cp = (mp[0]-0.2*d,mp[1])
        else:
            cp = (mp[0]+0.2*d,mp[1])

    elif (p2[1]-p1[1]) == 0:
        if type == 'bottom' or type == 'right':
            cp = (mp[0], mp[1]-0.2*d)
        else:
            cp = (mp[0], mp[1]+0.2*d)
    else:
        # 기울기
        m = - (p2[0]-p1[0])/(p2[1]-p1[1])
        #print(m)
        if m > 0:
            if m > 1:
                if m > 50:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.13*d
                    else:
                        x = mp[0] + 0.13*d
                elif 50 >= m > 30:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.15*d
                    else:
                        x = mp[0] + 0.15*d
                elif 30 >= m > 10:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.17*d
                    else:
                        x = mp[0] + 0.17*d
                elif 10 >= m > 5:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.12*d
                    else:
                        x = mp[0] + 0.12*d
                else:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.17*d
                    else:
                        x = mp[0] + 0.17*d
            else:
                if type == 'left' or type == 'bottom':
                    x = mp[0] - 0.17*d
                else:
                    x = mp[0] + 0.17*d
        else:
            if m < -1:
                if m < -50:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.13*d
                    else:
                        x = mp[0] + 0.13*d
                elif -50 < m <= -30:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.15*d
                    else:
                        x = mp[0] + 0.15*d
                elif -30 < m <= -10:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.17*d
                    else:
                        x = mp[0] + 0.17*d
                elif -10 < m <= -5:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.12*d
                    else:
                        x = mp[0] + 0.12*d
                else:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.17*d
                    else:
                        x = mp[0] + 0.17*d
            else:
                if type == 'left' or type == 'top':
                    x = mp[0] - 0.17*d
                else:
                    x = mp[0] + 0.17*d
        '''
        if 0 < abs(-1/m) < 1:
            if abs(-1/m) > 1/8:
                if -1/m < 0:
                    if type == 'bottom' or type == 'left':
                        x = mp[0] - 0.17*d
                    else:
                        x = mp[0] + 0.17*d
                else:
                    if type == 'bottom' or type == 'right':
                        x = mp[0] + 0.17*d
                    else:
                        x = mp[0] - 0.17*d
            else:
                if -1/m < 0:
                    if type == 'bottom' or type == 'left':
                        x = mp[0] - 0.12*d
                    else:
                        x = mp[0] + 0.12*d
                else:
                    if type == 'bottom' or type == 'right':
                        x = mp[0] + 0.12*d
                    else:
                        x = mp[0] - 0.12*d
        else:
            if -1/m < 0:
                if type == 'left' or type == 'bottom':
                    x = mp[0] - 0.1*d
                else:
                    x = mp[0] + 0.1*d
            else:
                if type == 'left' or type == 'top':
                    x = mp[0] - 0.1*d
                else:
                    x = mp[0] + 0.1*d
        '''

        y = m*(x-mp[0])+mp[1]
        # 제어점 (기울기가 m 이고 점 mp를 지나는 방정식 위의 점)
        cp = (x,y)

    return cp

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawArc(ax, p1, p2, position, text, boxed=False):
    #cp = controlPoint(p1,p2,position)
    cp = find_controlPoint_arc(p1,p2,position, distance=20)
    d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    l = len(text)
    vert = [
        p1,
        cp, # 제어점
        p2
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE3,
        Path.CURVE3
    ]

    path = Path(vert,codes)

    pp = mpatches.PathPatch(path, fc="none", transform=ax.transData, linestyle="--", zorder=3)
    ax.add_patch(pp)

    if boxed:
        if position == 'top':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16, bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16, bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]+0.03*l, cp[1], text, fontsize=16, bbox=dict(ec='black', fc='white'))
    else:
        if position == 'top':
            plt.text(cp[0]-0.5*l, cp[1]+0.3*l, text, fontsize=16)
        elif position == 'bottom':
            plt.text(cp[0]-0.5*l, cp[1]-0.3*l, text, fontsize=16)
        elif position == 'left':
            plt.text(cp[0]-0.9*l, cp[1], text, fontsize=16)
        elif position == 'right':
            plt.text(cp[0]-0.5*l, cp[1], text, fontsize=16)

# 점을 찍는 함수
def setPoints(ax,points,fill=False, text=[]):
    temp = []
    for p in points:
        if p not in temp:
            temp.append(p)
    points = temp
    if len(points) == 1:
        if len(text) == 0:
            text.append('')
        plt.text(points[0][0], points[0][1]+0.05, text[0], fontsize=16, zorder=3)
        if fill:
            ax.plot(points[0][0], points[0][1],"ko", zorder=3)
    else:
        if len(text) == 0:
            for t in range(len(points)):
                text.append('')

        for i in range(0,len(points)):

            plt.text(points[i][0]-0.5, points[i][1]+0.1, text[i], fontsize=16, zorder=3)

            if fill:
                ax.plot(points[i][0], points[i][1],"ko", zorder=3)
                

def setPoint(ax, point, fill=False, text="", position=5):
    if fill:
        ax.plot(point[0], point[1], "ko", zorder=3)

    if position == 1:
        plt.text(point[0]-0.7, point[1]-0.7, text, fontsize=16, zorder=3)
    elif position == 2:
        plt.text(point[0], point[1]-0.7, text, fontsize=16, zorder=3)
    elif position == 3:
        plt.text(point[0]+0.2 , point[1]-0.7, text, fontsize=16, zorder=3)
    elif position == 4:
        plt.text(point[0]-0.7, point[1], text, fontsize=16, zorder=3)
    elif position == 5:
        plt.text(point[0], point[1], text, fontsize=16, zorder=3)
    elif position == 6:
        plt.text(point[0]+0.2, point[1], text, fontsize=16, zorder=3)
    elif position == 7:
        plt.text(point[0]-0.7, point[1]+0.7, text, fontsize=16, zorder=3)
    elif position == 8:
        plt.text(point[0], point[1]+0.7, text, fontsize=16, zorder=3)
    elif position == 9:
        plt.text(point[0]+0.2, point[1]+0.7, text, fontsize=16, zorder=3)

# svg파일을 문자열로 반환하는 함수
def saveSvg():
    file = io.StringIO()
    plt.savefig(file, format='svg', dpi=300)
    file.seek(0)
    svg_data = file.getvalue()

    return svg_data

# png 저장 함수
def savePng(filename, rotate=0):
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    buf.seek(0)

    im = Image.open(buf)  #We open the current image saved in the buffer

    #We rotate the image and fill the background with white
    img_01=im.rotate(rotate, Image.NEAREST, expand = 1, fillcolor = (255,255,255))

    buf.close()

    ##MERGING THE TWO FIGURES##

    new_im = Image.new('RGB', (img_01.size[0],img_01.size[1]), 'white')
    mouse_mask = img_01.convert('RGBA')
    new_im.paste(img_01, (0,0))
    new_im.save("./result/{filename}.png".format(filename=filename), 'PNG')
    #new_im.show()

# matplotlib 차트 세팅 함수
def setChart(points=[]):
    # 한글 폰트(나눔 고딕)
    plt.rc('font', family='NanumGothic')  # For Windows
    if len(points) == 0:
        fig, ax = plt.subplots()
        plt.grid(True)

        return ax
    #mpl.font_manager._rebuild()
    x = []
    y = []

    for i in points:
        x.append(i[0])
        y.append(i[1])

    maxlim = max(max(x), max(y))
    minlim = min(min(x), min(y))

    fig, ax = plt.subplots(figsize=(5,5))

    #fig, ax = plt.subplots()

    #plt.grid(True)
    plt.axis("off")
    #plt.axis('scaled') 

    #ax.set_xlim(minlim-0.15*maxlim, maxlim+0.15*maxlim)
    #ax.set_ylim(minlim-0.15*maxlim, maxlim+0.15*maxlim)
    
    ax.set_xlim(minlim-0.15*maxlim, maxlim+0.15*maxlim)
    ax.set_ylim(minlim-0.15*maxlim, maxlim+0.15*maxlim)
    
    #plt.axis([min(x), max(x), min(y), max(y)])

    #ax.set_xlim(0, 10)
    #ax.set_ylim(0, 10)

    return ax

def distance(p1, p2):
    d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    return int(d)

def line_equation(p1, p2, x):
    y = ((p2[1]-p1[1])/(p2[0]-p1[0])) * (x-p1[0]) + p1[1]

    return y


def create_p_polygon(n=3,scale=10,move_x=0,move_y=0):
    import random
    def new_p_angle(angle,length,p=[0,0]):
        angle_radiant = math.radians(angle)
        x = (math.cos(angle_radiant)*length) + p[0]
        y = (math.sin(angle_radiant)*length) + p[1]
        return (x,y)
    def move_to_center(p_list=list,center_index=-1):
        #calculate center point
        x_center = 0
        y_center = 0
        for p in p_list:
            x_center += p[0]
            y_center += p[1]
        x_center /= len(p_list)
        y_center /= len(p_list)
        new_p_list = []
        if center_index == -1: #center with calculated center point
            x_move = x_center * -1
            y_move = y_center * -1
        else: #center with center_index
            center_p = p_list[center_index]
            x_move = center_p[0] * -1
            y_move = center_p[1] * -1
        #make new list with new points
        for index in range(len(p_list)):
            if center_index == -1:
                p = p_list[index]
                new_p_list.append((p[0]+x_move,p[1]+y_move))
            else:
                if index == center_index:
                    new_p_list.append((0,0))
                else:
                    p = p_list[index]
                    new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    def rotate_p(p_list=list,angle=0):
        def cart2pol(x, y):
            import math
            r = math.sqrt(x**2 + y**2)
            angle_radians = math.atan2(y, x)
            return(r, angle_radians)
        def pol2cart(r, angle_radians):
            import math
            x = r * math.cos(angle_radians)
            y = r * math.sin(angle_radians)
            return(x, y)
        import math
        for i in range(len(p_list)):
            cart_x = p_list[i][0]
            cart_y = p_list[i][1]
            pol_r, pol_angle_radians = cart2pol(cart_x,cart_y)
            pol_angle_radians += math.radians(angle)
            cart_x,cart_y = pol2cart(pol_r,pol_angle_radians)
            p_list[i] = (cart_x,cart_y)
        return p_list
    temp_p = (0,0)
    angle = 180 * (n-2) / n
    random_angle = random.randint(-30,30)
    length = int(scale/2)
    random_length = random.randint(round(scale/10)*-1,round(scale/10))
    polygon = [(0,0)]
    for i in range(n-1):
        if random.randint(0,1):
            temp_p = new_p_angle(angle,length,temp_p)
        else:
            while True:
                random_angle = random.randint(-30,30)
                if abs(random_angle) > 10:
                    break
            random_length = random.randint(round(scale/10)*-1,round(scale/10))
            temp_p = new_p_angle(angle+random_angle,length+random_length,temp_p)
        polygon.append(temp_p)
        polygon = rotate_p(polygon,180-angle)
        temp_p = (rotate_p([temp_p],180-angle))[0]
    polygon = move_to_center(polygon)
    polygon = move_p(polygon,move_x,move_y)
    return polygon

def find_controlPoint_arc(p1,p2,position='top',distance=1):
    def round_p(p,roundNumber=5):
        p = (round(p[0],roundNumber),round(p[1],roundNumber))
        return p
    def find_linear_equation(p1,p2):
        x1,y1 = p1
        x2,y2 = p2
        if x1 == x2:
            return ('x',x1)
        if y1 == y2:
            return ('y',y1)
        slope = (y2-y1)/(x2-x1)
        y_intersect = y1 - slope*x1
        return (slope,y_intersect)
    def find_p_middle(p1=tuple,p2=tuple):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    def find_p_onLineInCertainDistance(equation,middle_point,distance):
        middle_x,middle_y = middle_point
        slope,y_intersect = equation
        new_x_positive = middle_x + math.sqrt(distance**2/((1/slope)**2+1))
        new_y_positive = -1/slope*new_x_positive + 1/slope*middle_x + middle_y
        new_x_negative = middle_x - math.sqrt(distance**2/((1/slope)**2+1))
        new_y_negative = -1/slope*new_x_negative + (1/slope)*middle_x + middle_y
        return (new_x_positive, new_y_positive),(new_x_negative, new_y_negative)
    def calculate_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

        return d
    p1,p2 = round_p(p1),round_p(p2)
    equation = find_linear_equation(p1,p2)
    slope, y_intersect = equation
    x1,y1 = p1
    x2,y2 = p2
    d = calculate_distance(p1,p2)
    if slope == 'x':
        cp_y = (y1+y2)/2
        if position == 'right':
            cp_x = y_intersect + distance
        elif position == 'left':
            cp_x = y_intersect - distance
        else: raise Exception('Invalid Position')
    elif slope == 'y':
        cp_x = (x1+x2)/2
        if position == 'top':
            cp_y = y_intersect + distance
        elif position == 'bottom':
            cp_y = y_intersect - distance
        else: raise Exception('Invalid Position')
    else:
        p_middle = find_p_middle(p1,p2)
        cp_positive, cp_negative = find_p_onLineInCertainDistance(equation,p_middle,distance)
        if slope > 0:
            if position in ['top','left']:#negative
                cp_x,cp_y = cp_negative
            elif position in ['bottom','right']:#positive
                cp_x,cp_y = cp_positive
            else: raise Exception('Invalid Position')
        elif slope < 0:
            if position in ['top','right']:#positive
                cp_x,cp_y = cp_positive
            elif position in ['bottom','left']:#negative
                cp_x,cp_y = cp_negative
            else: raise Exception('Invalid Position')
        else: raise Exception('Slope is 0')
    return (cp_x,cp_y)

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawArc2(ax, p1, p2, position, text, boxed=False):
    if 'top' in position: cp = find_controlPoint_arc(p1,p2,'top')
    elif 'bottom' in position: cp = find_controlPoint_arc(p1,p2,'bottom')
    elif 'right' in position: cp = find_controlPoint_arc(p1,p2,'right')
    elif 'left' in position: cp = find_controlPoint_arc(p1,p2,'left')

    p1 = (round(p1[0],5),round(p1[1],5))
    p2 = (round(p2[0],5),round(p2[1],5))
    l = len(text)
    if 'mathrm' in text: 
        l -= 1
    vert = [
        p1,
        cp, # 제어점
        p2
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE3,
        Path.CURVE3
    ]

    path = Path(vert,codes)

    pp = mpatches.PathPatch(path, fc="none", transform=ax.transData, linestyle="--", zorder=3)
    ax.add_patch(pp)

    if boxed:
        if position == 'top':
            plt.text(cp[0]-2*l, cp[1]+3.5, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
    else:
        if position == 'top':
            plt.text(cp[0], cp[1], text, fontsize=16, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0], cp[1], text, fontsize=16, zorder=3)
        elif position == 'left':
            plt.text(cp[0], cp[1], text, fontsize=16, zorder=3)
        elif position == 'right':
            plt.text(cp[0], cp[1], text, fontsize=16, zorder=3)
        elif position in ['top_r','right_t']:
            plt.text(cp[0]+l, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['top_l','left_t']:
            plt.text(cp[0]-l*8, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['bottom_r','right_b']:
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        elif position in ['bottom_l','left_b']:
            plt.text(cp[0]-l*8, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        else: raise Exception('no matching position')

def create_p_triangle(width_height=[],right_bottom_left=[],bottom_left_angle=[],move_x=0,move_y=0):
    import random
    import math
    def move_to_center(p_list=list,center_index=-1):
        #calculate center point
        x_center = 0
        y_center = 0
        for p in p_list:
            x_center += p[0]
            y_center += p[1]
        x_center /= len(p_list)
        y_center /= len(p_list)
        new_p_list = []
        if center_index == -1: #center with calculated center point
            x_move = x_center * -1
            y_move = y_center * -1
        else: #center with center_index
            center_p = p_list[center_index]
            x_move = center_p[0] * -1
            y_move = center_p[1] * -1
        #make new list with new points
        for index in range(len(p_list)):
            if center_index == -1:
                p = p_list[index]
                new_p_list.append((p[0]+x_move,p[1]+y_move))
            else:
                if index == center_index:
                    new_p_list.append((0,0))
                else:
                    p = p_list[index]
                    new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    def new_p_angle(angle,length,p=[0,0]):
        import math
        angle_radiant = math.radians(angle)
        x = round((math.cos(angle_radiant)*length),5) + p[0]
        y = round((math.sin(angle_radiant)*length),5) + p[1]
        return (x,y)
    scale = 100
    #points - p_top,p_right,p_center
    p_center = (0,0)
    if width_height != []:
        if len(width_height) != 2: raise Exception("Input is incomplete")
        len_width = width_height[0]
        len_height = width_height[1]
        angle = math.degrees(math.atan(len_height/len_width))
        len_left = abs(len_height/math.cos(math.radians(180-angle)))
        p_right = (len_width,0)
        p_top = new_p_angle(angle,len_left,p_center)
    elif right_bottom_left != []:
        if len(right_bottom_left) != 3: raise Exception("Input is incomplete")
        len_right = right_bottom_left[0]
        len_bottom = right_bottom_left[1]
        len_left = right_bottom_left[2]
        if len_right > len_bottom+len_left or len_bottom > len_right+len_left or len_left > len_right+len_bottom:
            raise Exception("Lengths of triangle are against the triangle inequality theorem, which means sum of two lengths is smaller than the other length")
        angle = math.degrees(math.acos((len_bottom**2+len_left**2-len_right**2)/(2*len_bottom*len_left)))
        p_right = (len_bottom,0)
        p_top = new_p_angle(angle,len_left,p_center)
    elif bottom_left_angle != []:
        if len(bottom_left_angle) != 3: raise Exception("Input is incomplete")
        len_bottom = bottom_left_angle[0]
        len_left = bottom_left_angle[1]
        angle = bottom_left_angle[2]
        p_right = (len_bottom,0)
        p_top = new_p_angle(angle,len_left,p_center)
    else: raise Exception("No input to make points for triangle")


    triangle = [p_top,p_right,p_center]
    triangle = move_p(triangle,move_x,move_y)
    return triangle

def resize_polygon(p_list=list,scale=90):
    def move_to_center(p_list=list,center_index=-1):
        #calculate center point
        x_center = 0
        y_center = 0
        for p in p_list:
            x_center += p[0]
            y_center += p[1]
        x_center /= len(p_list)
        y_center /= len(p_list)
        new_p_list = []
        if center_index == -1: #center with calculated center point
            x_move = x_center * -1
            y_move = y_center * -1
        else: #center with center_index
            center_p = p_list[center_index]
            x_move = center_p[0] * -1
            y_move = center_p[1] * -1
        #make new list with new points
        for index in range(len(p_list)):
            if center_index == -1:
                p = p_list[index]
                new_p_list.append((p[0]+x_move,p[1]+y_move))
            else:
                if index == center_index:
                    new_p_list.append((0,0))
                else:
                    p = p_list[index]
                    new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    #move to center
    p_list = move_to_center(p_list)
    #find the criteria point
    criteria_val = abs(p_list[0][0])

    for p in p_list:
        x = p[0]
        y = p[1]
        #compare
        if max(abs(x),abs(y)) > criteria_val:
            criteria_val = max(abs(x),abs(y))
    #find ratio
    ratio = scale/criteria_val
    #create new_p_num
    new_p_num = []

    for p in p_list:
        x_new = p[0] * ratio
        y_new = p[1] * ratio
        new_p_num.append((x_new,y_new))
    new_p_num = move_to_center(new_p_num)
    p_list = new_p_num
    return new_p_num

# 표
def drawTable(ax, data, labels, widths, align='center'):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    
    choice = random.choice(colors)
    colcolor = []
    for i in range(len(data[0])):
        colcolor.append(choice)
  
    ax.axis('tight')
    ax.axis('off')
    
    if len(widths) == 0:
        ax.table(cellText=data, colLabels=labels, loc=align,
                 colColours=colcolor*len(colcolor), cellLoc=align)
    else:
        ax.table(cellText=data, colLabels=labels, loc=align,
                 colColours=colcolor*len(colcolor), cellLoc=align, colWidths=widths)

# 히스토그램, 꺾은 선
def drawGraph(ax, bins, data, xlabel, ylabel, mode="hist", legend=None):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)
    
    color = random.choice(colors)
    
    x = []
    for i in range(len(data)):
        for j in range(data[i]):
            x.append((bins[i]+bins[i+1])/2)
            
    y, binEdges = np.histogram(x, bins=bins)
    bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
    
 
    if mode == "hist":
        ax.hist(x, bins=bins, histtype="bar", fc=color, ec="black",  zorder=3, label=legend)
    elif mode == "line":
        ax.hist(x, bins=bins, histtype="bar", fc=color, ec="black",  zorder=3, visible=False)
        ax.plot(bincenters, y, zorder=3, color=color, marker='o', label=legend)
    
    if legend != None:
        ax.legend()
    
    plt.xlabel(xlabel, loc="right")
    plt.ylabel(ylabel, loc="top", rotation=0)
    ax.grid(visible=True)

# 부채꼴
def drawSector(ax,center, radius, theta1, theta2, fill=False, alpha=1, dash=False, lw=1, arrow=False):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    x_min = ax.get_xlim()[0]
    x_max = ax.get_xlim()[1]

    y_min = ax.get_ylim()[0]
    y_max = ax.get_ylim()[1]

    if center[0]-radius-0.5 < x_min:
        x_min = center[0]-radius-0.5
    if center[0]+radius+0.5 > x_max:
        x_max = center[0]+radius+0.5
    if center[1]-radius-0.5 < y_min:
        y_min = center[1]-radius-0.5
    if center[1]+radius+0.5 > y_max:
        y_max = center[1]+radius+0.5

    maxlim = max(x_max, y_max)
    minlim = min(x_min, y_min)

    ax.set_xlim(minlim, maxlim)
    ax.set_ylim(minlim, maxlim)

    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    #if dash:
    #    pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=lw, ls='--', fill=False, zorder=3)
    #else:
    #    pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=lw, fill=False, zorder=3)
    
    if fill:
        if dash:
            pp = mpatches.Wedge(center=center, r=radius, theta1=theta1,
                                theta2=theta2, width=None, ec="black", fc=random.choice(colors), lw=lw, ls='--', zorder=3)
        else:
            pp = mpatches.Wedge(center=center, r=radius, theta1=theta1,
                                theta2=theta2, width=None, ec="black", fc=random.choice(colors), lw=lw, zorder=3)
    else:
        if dash:
                pp = mpatches.Wedge(center=center, r=radius, theta1=theta1,
                                theta2=theta2, width=None, ec="black", fill=False, lw=lw, ls='--', zorder=3)
        else:
            pp = mpatches.Wedge(center=center, r=radius, theta1=theta1,
                                theta2=theta2, width=None, ec="black", fill=False, lw=lw, zorder=3)
    
    if arrow:  
        circarrow(ax=ax, diameter=2*radius+0.5, centX=center[0], centY=center[1], startangle=theta1, angle=theta2-theta1, width=0,
                head_width=.1, head_length=.1, length_includes_head=True, startarrow=True, endarrow=True, color="black")
    
    ax.add_patch(pp)
    
def drawLine(ax, p1, p2, dash=None, lw=1, decoration=None):
    if p1[0] > p2[0]:
        temp = p1
        p1 = p2
        p2 = temp
        
    point = [p1, p2]
    
    if dash:
        ax.plot(*zip(*point), color="black", ls="--", lw=lw, zorder=3)
    else:
        ax.plot(*zip(*point), color="black", lw=lw, zorder=3)
        
    if decoration != None:
        # 중점
        center = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
        
        # 기울기
        m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
        m2 = -(1/m1)
        
        # 상수항
        b1 = center[1] - (m1*center[0])
        b2 = center[1] - (m2*center[0])
        
        if decoration == "|":
            point = [(center[0]-0.05, m2*(center[0]-0.05)+b2),
                     (center[0]+0.05, m2*(center[0]+0.05)+b2)]
            ax.plot(*zip(*point), color="black", lw=lw, zorder=3)
        elif decoration == "||":
            c1 = (center[0]-0.05, m1*(center[0]-0.05)+b1)
            c2 = (center[0]+0.05, m1*(center[0]+0.05)+b1)
            
            b3 = c1[1] - (m2*c1[0])
            b4 = c2[1] - (m2*c2[0])
            point1 = [(c1[0]-0.05, m2*(c1[0]-0.05)+b3),
                      (c1[0]+0.05, m2*(c1[0]+0.05)+b3)]
            
            point2 = [(c2[0]-0.05, m2*(c2[0]-0.05)+b4),
                      (c2[0]+0.05, m2*(c2[0]+0.05)+b4)]
           
            ax.plot(*zip(*point1), color="black", lw=lw, zorder=3)
            ax.plot(*zip(*point2), color="black", lw=lw, zorder=3)
        elif decoration == "o":
            ax.plot(*center, marker="o", color="black")
        elif decoration == ">":
            ax.arrow(x=p1[0], y=p1[1], dx=center[0]-p1[0],
                     dy=center[1]-p1[1], head_width=0.1, head_length=0.2, color="black")
        elif decoration == "<":
            ax.arrow(x=p2[0], y=p2[1], dx=center[0]-p2[0],
                     dy=center[1]-p2[1], head_width=0.1, head_length=0.2, color="black")


def circarrow(ax, diameter, centX, centY, startangle, angle, **kwargs):
    startarrow = kwargs.pop("startarrow", False)
    endarrow = kwargs.pop("endarrow", False)

    pp = mpatches.Arc([centX, centY], diameter, diameter, angle=startangle,
              theta1=0, theta2=angle, linestyle="-", color=kwargs.get("color", "black"), zorder=3)
    ax.add_patch(pp)

    if startarrow:
        startX = diameter/2*np.cos(np.radians(startangle))
        startY = diameter/2*np.sin(np.radians(startangle))
        startDX = +.000001*diameter/2 * \
            np.sin(np.radians(startangle)+kwargs.get("head_length", 1.5*3*.001))
        startDY = -.000001*diameter/2 * \
            np.cos(np.radians(startangle)+kwargs.get("head_length", 1.5*3*.001))
        ax.arrow(startX-startDX, startY-startDY,
                 startDX, startDY, **kwargs, zorder=3)

    if endarrow:
        endX = diameter/2*np.cos(np.radians(startangle+angle))
        endY = diameter/2*np.sin(np.radians(startangle+angle))
        endDX = -.000001*diameter/2 * \
            np.sin(np.radians(startangle+angle) -
                   kwargs.get("head_length", 1.5*3*.001))
        endDY = +.000001*diameter/2 * \
            np.cos(np.radians(startangle+angle) -
                   kwargs.get("head_length", 1.5*3*.001))
        ax.arrow(endX-endDX, endY-endDY, endDX, endDY, **kwargs, zorder=3)

import matplotlib.pyplot as plt
import numpy as np
import random
import fractions
import math


answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤",
    5: "⑥",
    6: "⑦",
    7: "⑧",
    8: "⑨",
    9: "⑩",
    10: "⑪",
    11: "⑫",
    12: "⑬",
    13: "⑭",
    14: "⑮"
}


def figure121_Stem_004():
    stem = "다음 그림과 같은 {angle}각기둥에서 교점의 개수를 $$수식$$a$$/수식$$, 교선의 개수를 $$수식$$b$$/수식$$, " \
            "면의 개수를 $$수식$$c$$/수식$$라 할 때, $$수식$$a+b+c$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$\n" \
            "③ $$수식$${a3}$$/수식$$     ④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"

    flag = random.randint(3,6)
    
    fig, ax = plt.subplots(figsize=(2.5,4))
    plt.axis("off")
    ax.autoscale()
    
    if flag == 3:
        angle = "삼"

        p1 = (0,0)
        p2 = (3,0)
        p3 = (1.5,-0.5)

        p4 = (0,-3)
        p5 = (3,-3)
        p6 = (1.5,-3.5)

        #ax = setChart(points=[p1, p2, p3, p4, p5, p6])

        drawPolygon(ax=ax, verts=[p1, p2, p3])

        drawLine(ax=ax, p1=p1, p2=p4)
        drawLine(ax=ax, p1=p3, p2=p6)
        drawLine(ax=ax, p1=p2, p2=p5)
        drawLine(ax=ax, p1=p4, p2=p6)
        drawLine(ax=ax, p1=p6, p2=p5)

        drawLine(ax=ax, p1=p4, p2=p5, dash=True)
    elif flag == 4:
        angle = "사"

        p1 = (0,0)
        p2 = (2,0)
        p3 = (-0.5,-0.5)
        p4 = (1.5,-0.5)

        p5 = (0,-3)
        p6 = (2,-3)
        p7 = (-0.5,-3.5)
        p8 = (1.5,-3.5)

        #ax = setChart(points=[p1, p2, p3, p4, p5, p6, p7, p8])

        drawPolygon(ax=ax, verts=[p1, p3, p4, p2])

        drawLine(ax=ax, p1=p3, p2=p7)
        drawLine(ax=ax, p1=p4, p2=p8)
        drawLine(ax=ax, p1=p2, p2=p6)
        drawLine(ax=ax, p1=p7, p2=p8)
        drawLine(ax=ax, p1=p8, p2=p6)

        drawLine(ax=ax, p1=p1, p2=p5, dash=True)
        drawLine(ax=ax, p1=p5, p2=p7, dash=True)
        drawLine(ax=ax, p1=p5, p2=p6, dash=True)
    elif flag == 5:
        angle = "오"

        p1 = (0,0)
        p2 = (1.5,0.6)
        p3 = (3,0)
        p4 = (2.4,-0.8)
        p5 = (0.6,-0.8)
        
        p6 = (0,-3)
        p7 = (1.5,-2.4)
        p8 = (3,-3)
        p9 = (2.4, -3.8)
        p10 = (0.6,-3.8)
            
        #ax = setChart(points=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])

        drawPolygon(ax=ax, verts=[p1, p2, p3, p4, p5])

        drawLine(ax=ax, p1=p1, p2=p6)
        drawLine(ax=ax, p1=p2, p2=p7, dash=True)
        drawLine(ax=ax, p1=p3, p2=p8)
        drawLine(ax=ax, p1=p4, p2=p9)
        drawLine(ax=ax, p1=p5, p2=p10)

        drawLine(ax=ax, p1=p6, p2=p7, dash=True)
        drawLine(ax=ax, p1=p7, p2=p8, dash=True)
        drawLine(ax=ax, p1=p8, p2=p9)
        drawLine(ax=ax, p1=p9, p2=p10)
        drawLine(ax=ax, p1=p10, p2=p6)
    else:
        angle = "육"

        p1 = (0, 0)
        p2 = (0.5, 0.5)
        p3 = (1.5, 0.5)
        p4 = (2, 0)
        p5 = (1.5, -0.5)
        p6 = (0.5, -0.5)     
        p7 = (0, -3)
        p8 = (0.5, -2.5)
        p9 = (1.5, -2.5)
        p10 = (2, -3)
        p11 = (1.5, -3.5)
        p12 = (0.5, -3.5)
            
        #ax = setChart(points=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12])

        drawPolygon(ax=ax, verts=[p1, p2, p3, p4, p5, p6])

        drawLine(ax=ax, p1=p1, p2=p7)
        drawLine(ax=ax, p1=p2, p2=p8, dash=True)
        drawLine(ax=ax, p1=p3, p2=p9, dash=True)
        drawLine(ax=ax, p1=p4, p2=p10)
        drawLine(ax=ax, p1=p5, p2=p11)
        drawLine(ax=ax, p1=p6, p2=p12)

        drawLine(ax=ax, p1=p7, p2=p12)
        drawLine(ax=ax, p1=p12, p2=p11)
        drawLine(ax=ax, p1=p11, p2=p10)
        drawLine(ax=ax, p1=p7, p2=p8, dash=True)
        drawLine(ax=ax, p1=p8, p2=p9, dash=True)
        drawLine(ax=ax, p1=p9, p2=p10, dash=True)

    a = flag*2
    b = flag*3
    c = flag+2

    ans = a+b+c

    aa_list = [ans-12, ans-8, ans-4, ans, ans+4, ans+8, ans+12]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break  

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$$a={a},``b={b},``c={c}$$/수식$$이므로 " \
              "$$수식$$a+b+c={ans}$$/수식$$\n"
    
    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, angle=angle)
    answer = answer.format(result=result)
    comment = comment.format(a=str(a), b=str(b), c=str(c), ans=str(ans))
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_012():
    stem = "다음 그림과 같이 직선 $$수식$$l$$/수식$$위에 있는 {count} 점 {points} 중 " \
            "두 점을 이어 만들 수 있는 서로 다른 직선의 개수를 $$수식$$x$$/수식$$, " \
            "반직선의 개수를 $$수식$$y$$/수식$$, 선분의 개수를 $$수식$$z$$/수식$$라 할 때, " \
            "$$수식$$x+y+z$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"


    flag = random.randint(2,4)

    if flag == 2:
      count = "두"
      points = "$$수식$$A, B$$/수식$$"
      p = ["A", "B"]

      abr = "\\overrightarrow{AB}"
      bar = "\\overrightarrow{BA}"

      ab = "\\overline{AB}"

      x = [0, 4, 8, 12]
      y = [5, 5, 5, 5]

      ans = 4

      r = "{abr}, {bar}".format(abr=abr, bar=bar)
      rr = "{ab}".format(ab=ab)

      yy = 2
      zz = 1
    elif flag == 3:
      count = "세"
      points = "$$수식$$A, B, C$$/수식$$"
      p = ["A", "B", "C"]

      acr = "\\overrightarrow{AC}"
      bcr = "\\overrightarrow{BC}"
      bar = "\\overrightarrow{BA}"
      car = "\\overrightarrow{CA}"

      ab = "\\overline{AB}"
      bc = "\\overline{BC}"
      ac = "\\overline{AC}"

      x = [0, 3, 6, 9, 12]
      y = [5, 5, 5, 5, 5]

      ans = 8

      r = "{acr}, {bcr}, {bar}, {car}".format(acr=acr, bcr=bcr, bar=bar, car=car)
      rr = "{ab}, {bc}, {ac}".format(ab=ab, bc=bc, ac=ac)

      yy = 4
      zz = 3
    else:
      count = "네"
      points = "$$수식$$A, B, C, D$$/수식$$"
      p = ["A", "B", "C", "D"]
      
      adr = "\\overrightarrow{AD}"
      bdr = "\\overrightarrow{BD}"
      cdr = "\\overrightarrow{CD}"
      bar = "\\overrightarrow{BA}"
      car = "\\overrightarrow{CA}"
      dar = "\\overrightarrow{DA}"

      ab = "\\overline{AB}"
      ac = "\\overline{AC}"
      ad = "\\overline{AD}"
      bc = "\\overline{BC}"
      bd = "\\overline{BD}"
      cd = "\\overline{CD}"

      x = [0,2,5,8,11,13]
      y = [5,5,5,5,5,5]

      ans = 13

      r = "{adr}, {bdr}, {cdr}, {bar}, {car}, {dar}".format(adr=adr, bdr=bdr, cdr=cdr, bar=bar, car=car, dar=dar)
      rr = "{ab}, {ac}, {ad}, {bc}, {bd}, {cd}".format(ab=ab, ac=ac, ad=ad, bc=bc, bd=bd, cd=cd)

      yy = 6
      zz = 6

    #plt.style.use('default')
    #plt.rcParams['figure.figsize'] = (5,5)
    plt.rcParams['font.size'] = 13

    #fig, ax = plt.subplots()

    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    ax.set_xlim(0,13)
    ax.set_ylim(0,13)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    plt.plot(x,y,'k',c="black")
    plt.scatter(x, y, c='black', edgecolor='black', s=10)

    for i in range(1, flag+1):
      plt.text(x[i]-0.3, 3.8, p[i-1], size = 11)
      
    plt.text(x[-1]+0.8, 4.5, '$l$', size = 12)

    aa_list = [ans-3, ans-2, ans-1, ans, ans+1, ans+2, ans+3]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break  

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n만들 수 있는 직선은 $$수식$$l$$/수식$$뿐이므로 $$수식$$x=1$$/수식$$ " \
              "반직선은 $$수식$${r}$$/수식$$이므로 $$수식$$y={yy}$$/수식$$ " \
              "선분은 $$수식$${rr}$$/수식$$이므로 $$수식$$z={zz}$$/수식$$ " \
              "$$수식$$THEREFORE x+y+z={ans}$$/수식$$\n"
    
    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, count=count, points=points)
    answer = answer.format(result=result)
    comment = comment.format(r=r, rr=rr, yy=yy, zz=zz, ans=str(ans))
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_013():
    stem = "다음 그림과 같이 원 위에 $$수식$${flag}$$/수식$$개의 점 $$수식$${points}$$/수식$$가 있다. " \
            "이 중 두 점을 지나는 서로 다른 직선의 개수를 $$수식$$a$$/수식$$, " \
            "서로 다른 반직선의 개수를 $$수식$$b$$/수식$$라 할 때, " \
            "$$수식$$b-a$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"

    r = 5

    flag = random.randint(2,5)
    if flag == 2:
      points = "A, B"

      ab = "\\overleftrightarrow{AB}"

      abr = "\\overrightarrow{AB}"
      bar = "\\overrightarrow{BA}"

      x2 = [r*math.cos(math.radians(180)), r*math.cos(math.radians(0))]
      y2 = [r*math.sin(math.radians(180)), r*math.sin(math.radians(0))]

      a = 1
      b = 2

      rr = "{ab}".format(ab=ab)
      rrr = "{abr}, {bar}".format(abr=abr, bar=bar)

    elif flag == 3:
      points = "A, B, C"

      ab = "\\overleftrightarrow{AB}"
      ac = "\\overleftrightarrow{AC}"
      bc = "\\overleftrightarrow{BC}"

      abr = "\\overrightarrow{AB}"
      acr = "\\overrightarrow{AC}"
      bcr = "\\overrightarrow{BC}"
      bar = "\\overrightarrow{BA}"
      car = "\\overrightarrow{CA}"
      cbr = "\\overrightarrow{CB}"

      x2 = [r*math.cos(math.radians(90)), r*math.cos(math.radians(-30)), r*math.cos(math.radians(210))]
      y2 = [r*math.sin(math.radians(90)), r*math.sin(math.radians(-30)), r*math.sin(math.radians(210))]

      a =  3
      b = 6

      rr = "{ab}, {ac}, {bc}".format(ab=ab, ac=ac, bc=bc)
      rrr = "{abr}, {acr}, {bcr}, {bar}, {car}, {cbr}".format(abr=abr, acr=acr, bcr=bcr, bar=bar, car=car, cbr=cbr)
    elif flag == 4:
      points = "A, B, C, D"

      ab = "\\overleftrightarrow{AB}"
      ac = "\\overleftrightarrow{AC}"
      ad = "\\overleftrightarrow{AD}"
      bc = "\\overleftrightarrow{BC}"
      bd = "\\overleftrightarrow{BD}"
      cd = "\\overleftrightarrow{CD}"

      abr = "\\overrightarrow{AB}"
      acr = "\\overrightarrow{AC}"
      adr = "\\overrightarrow{AD}"

      bar = "\\overrightarrow{BA}"
      bcr = "\\overrightarrow{BC}"
      bdr = "\\overrightarrow{BD}"

      cbr = "\\overrightarrow{CB}"
      car = "\\overrightarrow{CA}"
      cdr = "\\overrightarrow{CD}"

      dar = "\\overrightarrow{DA}"
      dbr = "\\overrightarrow{DB}"
      dcr = "\\overrightarrow{DC}"

      x2 = [r*math.cos(math.radians(135)), r*math.cos(math.radians(45)), r*math.cos(math.radians(-45)), r*math.cos(math.radians(225))]
      y2 = [r*math.sin(math.radians(135)), r*math.sin(math.radians(45)), r*math.sin(math.radians(-45)), r*math.sin(math.radians(225))]

      a =  6
      b = 12

      rr = "{ab}, {ac}, {ad}, {bc}, {bd}, {cd}".format(ab=ab, ac=ac, ad=ad, bc=bc, bd=bd, cd=cd)
      rrr = "{abr}, {acr}, {adr}, {bar}, {bcr}, {bdr}, {car}, {cbr}, {cdr}, {dar}, {dbr}, {dcr}".format(abr=abr, acr=acr, adr=adr, bar=bar, bcr=bcr, bdr=bdr, car=car, cbr=cbr, cdr=cdr, dar=dar, dbr=dbr, dcr=dcr)
    else:
      points = "A, B, C, D, E"

      ab = "\\overleftrightarrow{AB}"
      ac = "\\overleftrightarrow{AC}"
      ad = "\\overleftrightarrow{AD}"
      ae = "\\overleftrightarrow{AE}"
      bc = "\\overleftrightarrow{BC}"
      bd = "\\overleftrightarrow{BD}"
      be = "\\overleftrightarrow{BE}"
      cd = "\\overleftrightarrow{CD}"
      ce = "\\overleftrightarrow{CE}"
      de = "\\overleftrightarrow{DE}"

      abr = "\\overrightarrow{AB}"
      acr = "\\overrightarrow{AC}"
      adr = "\\overrightarrow{AD}"
      aer = "\\overrightarrow{AE}"
      bar = "\\overrightarrow{BA}"
      bcr = "\\overrightarrow{BC}"
      bdr = "\\overrightarrow{BD}"
      ber = "\\overrightarrow{BE}"
      car = "\\overrightarrow{CA}"
      cbr = "\\overrightarrow{CB}"
      cdr = "\\overrightarrow{CD}"
      cer = "\\overrightarrow{CE}"
      dar = "\\overrightarrow{DA}"
      dbr = "\\overrightarrow{DB}"
      dcr = "\\overrightarrow{DC}"
      der = "\\overrightarrow{DE}"
      ear = "\\overrightarrow{EA}"
      ebr = "\\overrightarrow{EB}"
      ecr = "\\overrightarrow{EC}"
      edr = "\\overrightarrow{ED}"

      x2 = [r*math.cos(math.radians(18)), r*math.cos(math.radians(90)), r*math.cos(math.radians(162)), 
          r*math.cos(math.radians(234)), r*math.cos(math.radians(306))]
      y2 = [r*math.sin(math.radians(18)), r*math.sin(math.radians(90)), r*math.sin(math.radians(162)), 
          r*math.sin(math.radians(234)), r*math.sin(math.radians(306))]

      rr = "{ab}, {ac}, {ad}, {ae}, {bc}, {bd}, {be}, {cd}, {ce}, {de}".format(ab=ab, ac=ac, ad=ad, ae=ae, bc=bc, bd=bd, be=be, cd=cd, ce=ce, de=de)
      rrr = "{abr}, {acr}, {adr}, {aer}, {bar}, {bcr}, {bdr}, {ber}, {car}, {cbr}, {cdr}, {cer}, {dar}, {dbr}, {dcr}, {der}, {ear}, {ebr}, {ecr}, {edr}".format(
        abr=abr, acr=acr, adr=adr, aer=aer, bar=bar, bcr=bcr, bdr=bdr, ber=ber, car=car, cbr=cbr, cdr=cdr, cer=cer, dar=dar, dbr=dbr, dcr=dcr, der=der, ear=ear, ebr=ebr, ecr=ecr, edr=edr)

      a = 10
      b = 20

    ans = b-a


    #plt.style.use('default')
    #plt.rcParams['figure.figsize'] = (5,5)
    plt.rcParams['font.size'] = 13

    #fig, ax = plt.subplots()
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    ax.set_xlim(-6,10)
    ax.set_ylim(-6,10)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    x = []
    y = []

    for theta in range(0,360) :
      x.append(r*math.cos(math.radians(theta)))
      y.append(r*math.sin(math.radians(theta)))

    plt.plot(x,y,c="black")

    plt.scatter(x2, y2, c='black', edgecolor='black', s=12)

    if flag == 2:
      plt.text(x2[0]-1.8, y2[0], "A", size = 12)
      plt.text(x2[1]+0.8, y2[1], "B", size = 12)
    elif flag == 3:
      plt.text(x2[0]-0.3, y2[0]+0.4, "A", size = 12)
      plt.text(x2[1]+0.5, y2[1]-0.4, "B", size = 12)
      plt.text(x2[2]-1.5, y2[2]-0.4, "C", size = 12)
    elif flag == 4:
      plt.text(x2[0]-1.5, y2[0]+0.4, "A", size = 12)
      plt.text(x2[1]+1.2, y2[1]+0.4, "B", size = 12)
      plt.text(x2[2]+1.2, y2[2]-0.4, "C", size = 12)
      plt.text(x2[3]-1.5, y2[3]-0.4, "D", size = 12)
    else:
      plt.text(x2[0]+0.2, y2[0]+0.2, "B", size = 12)
      plt.text(x2[1]-0.2, y2[1]+0.4, "A", size = 12)
      plt.text(x2[2]-0.8, y2[2]+0.4, "E", size = 12)
      plt.text(x2[3]-0.8, y2[3]-1.2, "D", size = 12)
      plt.text(x2[4], y2[4]-1.2, "C", size = 12)

    aa_list = [ans-5, ans, ans+5, ans+10, ans+15, ans+20]
    a_list = []
    idx = random.randint(0,1)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break 

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n직선은 $$수식$${rr}$$/수식$$ " \
              "의 $$수식$${a}$$/수식$$개이므로 $$수식$$a={a}$$/수식$$ " \
              "반직선은 $$수식$${rrr}$$/수식$$ " \
              "의 $$수식$${b}$$/수식$$개이므로 $$수식$$b={b}$$/수식$$ " \
              "$$수식$$THEREFORE b-a={b}-{a}={ans}$$/수식$$\n"


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, flag=str(flag), points=points)
    answer = answer.format(result=result)
    comment = comment.format(rr=rr, a=str(a), rrr=rrr, b=str(b), ans=str(ans))
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_019():
    stem = "다음 그림에서 점 $$수식$$M$$/수식$$은 $$수식$${ab}$$/수식$$의 중점이고, " \
            "점 $$수식$$N$$/수식$$은 $$수식$${mb}$$/수식$$의 중점이다. $$수식$${ab}={n}``rm {{cm}}$$/수식$$ " \
            "일 때, $$수식$${mn}$$/수식$$의 길이를 구하시오. " \

    ab = "\\overline{AB}"
    mb = "\\overline{MB}"
    mn = "\\overline{MN}"
    f = "\\frac{1}{2}"

    n_list = [12,16,20,24,28,32,36,40,44,48]
    n = random.choice(n_list)
    
    s1 = int(n/2)
    result = int(s1/2)

    #plt.style.use('default')
    #plt.rcParams['figure.figsize'] = (4,4)
    #plt.rcParams['font.size'] = 13
    #fig, ax = plt.subplots()
    
    fig, ax = plt.subplots(figsize=(3.5,1.5))
    plt.axis("off")
    ax.autoscale()

    ax.set_xlim(-2,30)
    ax.set_ylim(-2,28)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])

    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    x = [0,14,14+14/2,28]
    y = [14,14,14,14]


    plt.plot(x,y,'k',c="black")
    plt.scatter(x, y, c='black', edgecolor='black', s=10)


    pp1 = mpatches.PathPatch(
    Path([(0, 14), (28/2, 18), (28, 14)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp1)



    plt.text(x[0]-0.4, -1.6+12, "A", size = 11)
    plt.text(x[1]-0.4, -1.6+12, "M", size = 11)
    plt.text(x[2]-0.4, -1.6+12, "N", size = 11)
    plt.text(x[3]-0.4, -1.6+12, "B", size = 11)

    plt.text(28/2-1, 17, "{n}cm".format(n=n), size = 9)


    answer = "(정답)\n$$수식$${result}``rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n$$수식$${mb}={f}{ab}={f}\\times{n}={s1}(rm {{cm}})$$/수식$$ " \
              "$$수식$$THEREFORE {mn}={f}{mb}={f}\\times{s1}={result}(rm {{cm}})$$/수식$$\n"
    

    stem = stem.format(ab=ab, mb=mb, n=n, mn=mn)
    answer = answer.format(result=result)
    comment = comment.format(mb=mb,f=f, ab=ab, n=n, s1=s1, mn=mn, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_021():
    stem = "다음 그림에서 $$수식$${ab}$$/수식$$, $$수식$${bc}$$/수식$$의 중점이 각각 $$수식$$M$$/수식$$,$$수식$$N$$/수식$$이고, " \
            "$$수식$${ac}={n}``rm {{cm}}$$/수식$$일 때, $$수식$${mn}$$/수식$$의 길이를 구하시오. " \

    ab = "\\overline{AB}"
    bc = "\\overline{BC}"
    ac = "\\overline{AC}"
    mn = "\\overline{MN}"
    mb = "\\overline{MB}"
    bn = "\\overline{BN}"
    f = "\\frac{1}{2}"

    while True :
      n = random.randint(16,42)
      if n % 2 == 0 :
        break
    
    result = int(n/2)

    #plt.style.use('default')
    #plt.rcParams['figure.figsize'] = (5,5)
    #plt.rcParams['font.size'] = 13

    #fig, ax = plt.subplots()
    
    fig, ax = plt.subplots(figsize=(3.5,1.5))
    plt.axis("off")
    ax.autoscale()

    ax.set_xlim(-2,30)
    ax.set_ylim(-2,28)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    x = [0,28/3,28/3*2,28/3*2+(28/3)/2,28]
    y = [14,14,14,14,14]


    plt.plot(x,y,'k',c="black")
    plt.scatter(x, y, c='black', edgecolor='black', s=10)


    pp1 = mpatches.PathPatch(
    Path([(0, 14), (28/2, 18), (28, 14)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp1)



    plt.text(x[0]-0.4, -1.6+12, "A", size = 11)
    plt.text(x[1]-0.4, -1.6+12, "M", size = 11)
    plt.text(x[2]-0.4, -1.6+12, "B", size = 11)
    plt.text(x[3]-0.4, -1.6+12, "N", size = 11)
    plt.text(x[4]-0.4, -1.6+12, "C", size = 11)

    plt.text(28/2-1, 17, "{n}cm".format(n=n), size = 9)

    answer = "(정답)\n$$수식$${result}``rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n$$수식$${mb}={f}{ab},``{bn}={f}{bc}$$/수식$$이므로 " \
              "$$수식$${mn}={mb}+{bn}={f}({ab}+{bc})$$/수식$$ " \
              "$$수식$$={f}$$/수식$$$$수식$${ac}={f}\\times{n}={result}(rm {{cm}})$$/수식$$\n"


    stem = stem.format(ab=ab, bc=bc, ac=ac, n=n, mn=mn)
    answer = answer.format(result=result)
    comment = comment.format(mb=mb, f=f, ab=ab, bn=bn, bc=bc, mn=mn, ac=ac, n=n, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_022():
    stem = "다음 그림에서 점 $$수식$$M$$/수식$$은 $$수식$${ab}$$/수식$$의 중점이다. " \
            "$$수식$${ac}={n1}``rm {{cm}}, {bc}={n2}``rm {{cm}}$$/수식$$일 때, $$수식$${mb}$$/수식$$의\n길이를 구하시오. " \

    ab = "\\overline{AB}"
    bc = "\\overline{BC}"
    ac = "\\overline{AC}"
    mb = "\\overline{MB}"
    f = "\\frac{1}{2}"

    while True :
      n1 = random.randint(18,24)
      n2 = random.randint(4,6)
      s1 = n1-n2
      if s1 % 2 == 0 :
        break
    result = int(s1/2)

    #plt.style.use('default')
    #plt.rcParams['figure.figsize'] = (5,5)
    #plt.rcParams['font.size'] = 13

    #fig, ax = plt.subplots()
    
    fig, ax = plt.subplots(figsize=(3.5,1.5))
    plt.axis("off")
    ax.autoscale()

    ax.set_xlim(-2,25)
    ax.set_ylim(-2,25)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    x = [0,(n1-n2)/2,n1-n2,n1]
    y = [14,14,14,14]


    plt.plot(x,y,'k',c="black")
    plt.scatter(x, y, c='black', edgecolor='black', s=10)


    pp1 = mpatches.PathPatch(
    Path([(0, 14), (n1/2, 19), (n1, 14)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([(n1-n2, 14), (n1-(n2/2), 15.5), (n1, 14)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp2)


    plt.text(x[0]-0.4, -1.6+12, "A", size = 11)
    plt.text(x[1]-0.4, -1.6+12, "M", size = 11)
    plt.text(x[2]-0.4, -1.6+12, "B", size = 11)
    plt.text(x[3]-0.4, -1.6+12, "C", size = 11)

    plt.text(n1/2-1, 17, "{n1}cm".format(n1=n1), size = 9)
    plt.annotate('',ha = 'center', va = 'bottom',
    xytext = (n1-(n2/2),14.5), xy = (n1,16.5),
    arrowprops = {
              'color':'black',
              'connectionstyle':"arc3,rad=-0.4",
              'edgecolor':'b', 
              'arrowstyle':'<-'
              })
    plt.text(n1, 16, "{n2}cm".format(n2=n2), size = 9)

    answer = "(정답)\n$$수식$${result}``rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n$$수식$${ab}={ac}-{bc}={n1}-{n2}={s1}(rm {{cm}})$$/수식$$이므로 " \
              "$$수식$${mb}={f}{ab}={f}\\times{s1}={result}$$/수식$$"

    stem = stem.format(ab=ab, ac=ac, n1=n1, bc=bc, n2=n2, mb=mb)
    answer = answer.format(result=result)
    comment = comment.format(ab=ab, ac=ac, bc=bc, n1=n1, n2=n2, s1=s1, mb=mb, f=f, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_023():
    stem = "다음 그림에서 점 $$수식$$M$$/수식$$은 $$수식$${bc}$$/수식$$의 중점이고, $$수식$${ab}:{bc}={n1}:{n2}$$/수식$$이다. " \
            "$$수식$${bm}={n3}``rm {{cm}}$$/수식$$일 때, $$수식$${ac}$$/수식$$의 길이는?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"

    ab = "\\overline{AB}"
    bc = "\\overline{BC}"
    ac = "\\overline{AC}"
    bm = "\\overline{BM}"
    f = "\\frac{1}{2}"

    n1 = 3
    n2 = 4
    n3 = random.randint(6,8)

    
    s1 = 2 * n3
    f1 = "\\frac{" + str(n1) + "}{" + str(n2) + "}"
    s2 = int(s1*(n1/n2))
    ans = s1+s2

    #plt.style.use('default')
    #plt.rcParams['figure.figsize'] = (5,5)
    #plt.rcParams['font.size'] = 13

    #fig, ax = plt.subplots()
    
    fig, ax = plt.subplots(figsize=(3.5,1.5))
    plt.axis("off")
    ax.autoscale()

    ax.set_xlim(-2,34)
    ax.set_ylim(-2,34)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    x = [0,s1,s1+n3,s1+n3+n3]
    y = [17,17,17,17]


    plt.plot(x,y,'k',c="black")
    plt.scatter(x, y, c='black', edgecolor='black', s=10)


    pp1 = mpatches.PathPatch(
    Path([(s1, 17), (s1+n3/2, 19.5), (s1+n3, 17)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp1)

    plt.text(x[0]-0.4, -1.8+14, "A", size = 11)
    plt.text(x[1]-0.4, -1.8+14, "B", size = 11)
    plt.text(x[2]-0.4, -1.8+14, "M", size = 11)
    plt.text(x[3]-0.4, -1.8+14, "C", size = 11)

    plt.text(s1+n3/2-1.2, 19.2, "{n3}cm".format(n3=n3), size = 9)

    aa_list = [ans-3, ans-2, ans-1, ans, ans+1, ans+2, ans+3]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break  

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$${bc}=2{bm}=2\\times{n3}={s1}(rm {{cm}})$$/수식$$ " \
              "$$수식$${ab}:{bc}={n1}:{n2}$$/수식$$에서 $$수식$${n1}$$/수식$$$$수식$${bc}={n2}$$/수식$$$$수식$${ab}$$/수식$$ " \
              "$$수식$$THEREFORE {ab}={f1}{bc}={f1}\\times{s1}={s2}(rm {{cm}})$$/수식$$ " \
              "$$수식$$THEREFORE {ac}={ab}+{bc}={s2}+{s1}={ans}(rm {{cm}})$$/수식$$"


    stem = stem.format(ab=ab, ac=ac, n1=n1, bc=bc, n2=n2, n3=n3, bm=bm, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ab=ab, ac=ac, bc=bc, n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, bm=bm, f=f, f1=f1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_030():
    stem = "다음 그림에 대하여 다음 중 옳지 않은 것은?\n" \
            "① $$수식$${a1}$$/수식$$\n② $$수식$${a2}$$/수식$$\n" \
            "③ $$수식$${a3}$$/수식$$\n④ $$수식$${a4}$$/수식$$\n" \
            "⑤ $$수식$${a5}$$/수식$$\n"
    
    a = (4,13)
    b = (0,0)
    c = (15,2)
    d = (15,13)

    b2 = (-3,-6/15)
    c2 = (18,36/15)

    a2 = (64/13,16)
    b3 = (-20/13,-5)

    a3 = (-3.2,13)
    d2 = (18,13)

    d3 = (15,16)
    c3 = (15,-6)

    p1 = (14.2,13)
    p2 = (15,12.2)
    p3 = (14.2,12.2)
    
    #ax = setChart(points=[a,a2,a3,b,b2,b3,c,c2,c3,d,d2,d3,p1,p2])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=a3, p2=d2)
    drawLine(ax=ax, p1=d3, p2=c3)
    drawLine(ax=ax, p1=a2, p2=b3)
    drawLine(ax=ax, p1=b2, p2=c2)

    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p2, p2=p3)

    a1 = AngleAnnotation(xy=b, p1=c, p2=a, text=r"$65°$",
                    textposition="outside", ax=ax, size=30)   
    a2 = AngleAnnotation(xy=c, p1=d, p2=b, text=r"$100°$",
                    textposition="outside", ax=ax, size=30)   
    
    ax.text(2.5, 13.5, "A", size = 15)    
    ax.text(0.3, -1.6, "B", size = 15)   
    ax.text(15.3, 0.3, "C", size = 15)   
    ax.text(15.3,13.5, "D", size = 15)   

    aa1 = "\\angle ABC=65 DEG"
    aa2 = "\\angle ADC=90 DEG"
    aa3 = "\\angle BCD=100 DEG"
    aa4 = "\\angle CDA=100 DEG"
    ans = "\\angle CDA=100 DEG"

    a_list = [aa1,aa2,aa3,aa4,ans]
    a_list.sort()
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans :
        result = answer_dict[i]
        break 
    
    cmt = "\\angle CDA=90 DEG"

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n{result} $$수식$${cmt}$$/수식$$\n"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(result=result, cmt=cmt)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_031():
    stem = "다음 그림에서 $$수식$$x$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"
    
    op_list = ['+', '-']
    op = random.choice(op_list)

    while True :
      ans = random.randint(28,32)
      n1 = random.randint(2,3)
      s1 = n1+1
      s2 = s1*ans
      if s2 != 90 :
        break
        
    if s2 > 90 :
      op = '-'
      n2 = s2 - 90
    else :
      op = '+'
      n2 = 90 - s2
    
    p1 = (5.999,5.999)
    p2 = (6,0)
    p3 = (12,0)

    x = 6+6*math.cos(math.radians(60))
    y = 6*math.sin(math.radians(60))

    c = (x, y)
       
    #ax = setChart(points=[p1, p2, p3, c])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=p3)
    drawLine(ax=ax, p1=p2, p2=c)

    t1 = str(n1) + "x" + op + str(n2)

    AngleAnnotation(xy=p2, p1=p3, p2=c,
                    textposition="outside", ax=ax, size=30)
    ax.text(x=p2[0]+0.5, y=p2[1]+0.2, s=r"${t1}$".format(t1=t1))    
    AngleAnnotation(xy=p2, p1=c, p2=p1, text=r"$x$",
                    textposition="outside", ax=ax, size=30)  

    aa_list = [ans-3, ans-2, ans-1, ans, ans+1, ans+2, ans+3]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break  

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$$x+{n1}x{op}{n2}=90$$/수식$$이므로 " \
              "$$수식$${s1}x={s2}``````THEREFORE x={ans}$$/수식$$"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, op=op, n2=n2, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_032():
    stem = "다음 그림에서 $$수식$$x$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"

    
    angle_list = [30,35,40,45,50,55,60]  
    n1 = random.choice(angle_list)
    n2 = random.randint(3,5)

    op_list = ['+', '-']
    op = random.choice(op_list)
    s1 = n2 + 1


    while True :
      n_list = [10,15,20,25,30]
      n3 = random.choice(n_list)
      if op == '+' :
        s2 = 180 - n1 - n3
      else :
        s2 = 180 - n1 + n3
      if s2 % s1 == 0 :
        break

    
    ans = int(s2/s1)
    
    if op == '+' :
      a_z = n2*ans+n3
    else :
      a_z = n2*ans-n3


    p1 = (0,0)
    p2 = (5,0)
    p3 = (10,0)

    y_x = 5+5*math.cos(math.radians(a_z+ans))
    y_y = 5*math.sin(math.radians(a_z+ans))

    z_x = 5+5*math.cos(math.radians(a_z))
    z_y = 5*math.sin(math.radians(a_z))

    y = (y_x, y_y)
    z = (z_x, z_y)
       
    #ax = setChart(points=[p1, p2, p3, y, z])
    
    fig, ax = plt.subplots(figsize=(3.5,1.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p2, p2=y)
    drawLine(ax=ax, p1=p2, p2=z)

    t1 = 180 - ans - a_z
    t2 = str(n2) + "x" + op + str(n3)
    
    AngleAnnotation(xy=p2, p1=p3, p2=z, text=r"${t2}$".format(t2=t2),
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=p2, p1=z, p2=y, text=r"$x$",
                         textposition="edge",  text_kw=dict(xytext=(40, 40), arrowprops=dict(arrowstyle="->",
                              connectionstyle="arc3,rad=0.5")), ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=y, p2=p1, text=r"${t1}$".format(t1=t1),
                    textposition="outside", ax=ax, size=30)


    aa_list = [ans-15, ans-10, ans-5, ans, ans+5, ans+10, ans+15]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$${n1}+x+({n2}x{op}{n3})=180$$/수식$$이므로 " \
              "$$수식$${s1}x={s2}``````THEREFORE x={ans}$$/수식$$"
    

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, op=op, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_034():
    stem = "다음 그림에서 $$수식$$ANGLE x: ANGLE y: ANGLE z={n1}:{n2}:{n3}$$/수식$$일 때, " \
            "$$수식$$ANGLE y$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG$$/수식$$     ② $$수식$${a2}DEG$$/수식$$      ③ $$수식$${a3}DEG$$/수식$$\n" \
            "④ $$수식$${a4}DEG$$/수식$$     ⑤ $$수식$${a5}DEG$$/수식$$ " \

    k = random.randint(2,3)

    if k == 2 :
      list = [2,3,4]
      n_list = random.sample(list, 3)
      n1,n2,n3 = n_list
      a_z = 20 * n3
      a_y = a_z + 20 * n2
    else :
      list = [3,4,5]
      n_list = random.sample(list, 3)
      n1,n2,n3 = n_list
      a_z = 15 * n3
      a_y = a_z + 15 * n2

    f1 = "\\frac{" + str(n2) + "}{" + str(n1) + "+" + str(n2) + "+" + str(n3) + "}"

    ff2 = fractions.Fraction(fractions.Fraction(n2)/fractions.Fraction(n1+n2+n3))
    f2 = "\\frac{"+str(ff2.numerator)+"}{"+str(ff2.denominator)+"}"

    p1 = (0,0)
    p2 = (5,0)
    p3 = (10,0)

    y_x = 5+5*math.cos(math.radians(a_y))
    y_y = 5*math.sin(math.radians(a_y))

    z_x = 5+5*math.cos(math.radians(a_z))
    z_y = 5*math.sin(math.radians(a_z))

    y = (y_x, y_y)
    z = (z_x, z_y)
       
    #ax = setChart(points=[p1, p2, p3, y, z])
    
    fig, ax = plt.subplots(figsize=(4.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p2, p2=y)
    drawLine(ax=ax, p1=p2, p2=z)
    
    AngleAnnotation(xy=p2, p1=p3, p2=z, text=r"$z$",
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=p2, p1=z, p2=y, text=r"$y$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=y, p2=p1, text=r"$x$",
                    textposition="outside", ax=ax, size=30)

    ans = a_y - a_z
    
    aa_list = [ans-15, ans-10, ans-5, ans, ans+5, ans+10, ans+15]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$$ANGLE y=180 DEG \\times{f1}=180 DEG \\times{f2}={ans} DEG$$/수식$$\n"


    stem = stem.format(n1=n1, n2=n2, n3=n3, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f1=f1, f2=f2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_041():
    stem = "다음 그림에서 $$수식$$\\angle x:\\angle y = {n1}:{n2}$$/수식$$, $$수식$$\\angle x:\\angle z = {n3}:{n4}$$/수식$$ " \
            "일 때, $$수식$$\\angle y-\\angle z$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG$$/수식$$    ② $$수식$${a2}DEG$$/수식$$    ③ $$수식$${a3}DEG$$/수식$$\n" \
            "④ $$수식$${a4}DEG$$/수식$$    ⑤ $$수식$${a5}DEG$$/수식$$\n" 

    n1 = 1
    n2 = random.randint(2,3)

    if n2 == 3 :    
      n3 = 1
    elif n2 == 2:
      n3 = 2
    
    if n3 == 1 :
      n4 = 2
    else :
      n4 = 3

    if n1 == n3 :
      s1 = n1
      s2 = n2
      s3 = n4
    else :
      n = n1*n3
      s1 = n
      s2 = int(n2*(n/n1))
      s3 = int(n4*(n/n3))
 

    f1 = "\\frac{"+str(s2)+"}{"+str(s1)+"+"+str(s2)+"+"+str(s3)+"}"

    ff2 = fractions.Fraction(fractions.Fraction(s2)/fractions.Fraction(s1+s2+s3))
    if ff2.denominator == 1 :
        f2 = int(ff2)
    else :
        f2 = "\\frac{"+str(ff2.numerator)+"}{"+str(ff2.denominator)+"}"

    ss4 = fractions.Fraction(fractions.Fraction(ff2)*fractions.Fraction(180))
    if ss4.denominator == 1 :
        s4 = int(ss4)
    else :
        s4 = "\\frac{"+str(ss4.numerator)+"}{"+str(ss4.denominator)+"}"

    f3 = "\\frac{"+str(s3)+"}{"+str(s1)+"+"+str(s2)+"+"+str(s3)+"}"

    ff4 = fractions.Fraction(fractions.Fraction(s3)/fractions.Fraction(s1+s2+s3))
    if ff4.denominator == 1 :
        f4 = int(ff4)
    else :
        f4 = "\\frac{"+str(ff4.numerator)+"}{"+str(ff4.denominator)+"}"


    ss5 = fractions.Fraction(fractions.Fraction(ff4)*fractions.Fraction(180))
    if ss5.denominator == 1 :
        s5 = int(ss5)
    else :
        s5 = "\\frac{"+str(ss5.numerator)+"}{"+str(ss5.denominator)+"}"

    an = fractions.Fraction(ss4-ss5)
    if an.denominator == 1 :
        ans = int(an)
    else :
        ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"
    

    p1 = (0,0)
    p2 = (5,0)
    p3 = (10,0)

    y_x = 5+5*math.cos(math.radians(ss5+ss4))
    y_y = 5*math.sin(math.radians(ss5+ss4))

    z_x = 5+5*math.cos(math.radians(ss5))
    z_y = 5*math.sin(math.radians(ss5))

    y = (y_x, y_y)
    z = (z_x, z_y)
       
    #ax = setChart(points=[p1, p2, p3, y, z])
    
    fig, ax = plt.subplots(figsize=(4.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p2, p2=y)
    drawLine(ax=ax, p1=p2, p2=z)
    
    AngleAnnotation(xy=p2, p1=p3, p2=z, text=r"$z$",
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=p2, p1=z, p2=y, text=r"$y$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=y, p2=p1, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    

    aa_list = [ans-15, ans-10, ans-5, ans, ans+5, ans+10, ans+15]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break
    
    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$$\\angle x:\\angle y={n1}:{n2},`` \\angle x:\\angle z={n3}:{n4}$$/수식$$이므로 " \
              "$$수식$$\\angle x:\\angle y:\\angle z={s1}:{s2}:{s3}$$/수식$$ " \
              "$$수식$$THEREFORE \\angle y=180 DEG \\times {f1}=180 DEG \\times {f2}={s4} DEG$$/수식$$ " \
              "$$수식$$\\angle z=180 DEG \\times {f3}=180 DEG \\times {f4}={s5} DEG$$/수식$$ " \
              "$$수식$$THEREFORE \\angle y - \\angle z = {ans} DEG$$/수식$$\n"

    
    stem = stem.format(n1=n1, n2=n2, n3=n3, n4=n4, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, f1=f1, f2=f2, f3=f3, f4=f4, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_045():
    stem = "다음 그림에서 $$수식$$\\angle AOD$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG$$/수식$$     ② $$수식$${a2}DEG$$/수식$$     ③ $$수식$${a3}DEG$$/수식$$\n" \
            "④ $$수식$${a4}DEG$$/수식$$     ⑤ $$수식$${a5}DEG$$/수식$$\n"

    n2_list = [30,40,50]
    n4_list = [10,20,30]
    
    while True :
      n1 = random.randint(7,9)
      n2 = random.choice(n2_list)
      n4 = random.choice(n4_list)
      if (n2+n4) % 3 == 0 :
        break

    n3 = n1-3
    s1 = int((n2+n4)/3)

    ans = n1*s1-n2
    
    p2 = (10,0)

    c1 = int((180-ans)/2)

    a_x = 10+10*math.cos(math.radians(180-c1))
    a_y = 10*math.sin(math.radians(180-c1))

    b_x = 10+10*math.cos(math.radians(360-c1))
    b_y = 10*math.sin(math.radians(360-c1))

    c_x = 10+10*math.cos(math.radians(180+c1))
    c_y = 10*math.sin(math.radians(180+c1))

    d_x = 10+10*math.cos(math.radians(c1))
    d_y = 10*math.sin(math.radians(c1))

    a = (a_x, a_y)
    b = (b_x, b_y)
    c = (c_x, c_y)
    d = (d_x, d_y)

    #ax = setChart(points=[p2, a, b, c, d])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p2, p2=a)
    drawLine(ax=ax, p1=p2, p2=b)
    drawLine(ax=ax, p1=p2, p2=c)
    drawLine(ax=ax, p1=p2, p2=d)

    setPoint(ax=ax, point=a, fill=True)
    setPoint(ax=ax, point=b, fill=True)
    setPoint(ax=ax, point=c, fill=True)
    setPoint(ax=ax, point=d, fill=True)


    AngleAnnotation(xy=p2, p1=d, p2=a, text=r"${n1}x-{n2}$".format(n1=n1, n2=n2),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=c, p2=b, text=r"${n3}x+{n4}$".format(n3=n3, n4=n4),
                    textposition="outside", ax=ax, size=30)

    ax.text(a_x-0.5, a_y-2, "A", size = 14)
    ax.text(b_x-0.5, b_y-2, "B", size = 14)
    ax.text(c_x-0.5, c_y-2, "C", size = 14)
    ax.text(d_x-0.5, d_y-2, "D", size = 14)
    ax.text(11, -0.52, "O", size = 14)

    aa_list = [ans-15, ans-10, ans-5, ans, ans+5, ans+10, ans+15]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$${n1}x-{n2}={n3}x+{n4}$$/수식$$에서 $$수식$$x={s1}$$/수식$$ " \
              "$$수식$$THEREFORE \\angle AOD = {n1}x-{n2}={n1}\\times{s1}DEG -{n2}DEG$$/수식$$ " \
              "$$수식$$={ans} DEG$$/수식$$"
  
    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, s1=s1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_047():
    stem = "다음 그림에서 $$수식$$\\angle x+\\angle y$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG$$/수식$$     ② $$수식$${a2}DEG$$/수식$$     ③ $$수식$${a3}DEG$$/수식$$\n" \
            "④ $$수식$${a4}DEG$$/수식$$     ⑤ $$수식$${a5}DEG$$/수식$$\n"


    n_list = [5,10,15,20,25,30]

    while True :
      nn1 = random.randint(1,4)
      n2 = random.choice(n_list)
      n3 = random.choice(n_list)
      s1 = nn1+2
      s2 = n2+n3
      if (180-s2) % s1 == 0 :
        break

    if nn1 ==1 :
      n1 = ""
    else :
      n1 = nn1
    
    s3 = int((180-s2)/s1)
    s4 = n3+s3
    ans = s3+s4
    
    p1 = (0,0)
    p2 = (5,0)
    p3 = (10,0)

    z = nn1*s3+n2


    y_x = 5+5*math.cos(math.radians(z+s3))
    y_y = 5*math.sin(math.radians(z+s3))

    z_x = 5+5*math.cos(math.radians(z))
    z_y = 5*math.sin(math.radians(z))

    x2_x = 5+5*math.cos(math.radians(180+z))
    x2_y = 5*math.sin(math.radians(180+z))

    y2_x = 5+5*math.cos(math.radians(180+z+s3))
    y2_y = 5*math.sin(math.radians(180+z+s3))


    y = (y_x, y_y)
    z = (z_x, z_y)
    x2 = (x2_x, x2_y)
    y2 = (y2_x, y2_y)
       
    #ax = setChart(points=[p1, p2, p3, y, z, x2, y2])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p2, p2=y)
    drawLine(ax=ax, p1=p2, p2=z)
    drawLine(ax=ax, p1=p2, p2=x2)
    drawLine(ax=ax, p1=p2, p2=y2)
    

    AngleAnnotation(xy=p2, p1=z, p2=y, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=y, p2=p1, text=r"$y$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=p1, p2=x2, text=r"${n1}x+{n2}$".format(n1=n1, n2=n2),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=y2, p2=p3, text=r"$x+{n3}$".format(n3=n3),
                    textposition="outside", ax=ax, size=30)
    

    aa_list = [ans-15, ans-10, ans-5, ans, ans+5, ans+10, ans+15]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break
    
    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$$({n1}\\angle x+{n2} DEG )+\\angle x+(\\angle x+{n3} DEG )=180DEG$$/수식$$이므로 " \
              "$$수식$${s1}\\angle x+{s2} DEG =180DEG ``````THEREFORE \\angle x={s3} DEG$$/수식$$ " \
              "한편 $$수식$$\\angle y=\\angle x+{n3} DEG ={s4} DEG$$/수식$$이므로 " \
              "$$수식$$\\angle x+\\angle y={s3} DEG +{s4} DEG ={ans} DEG$$/수식$$\n"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3, s4=s4, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_048():
    stem = "다음 그림에서 $$수식$$y-x$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"

    n_list = [5,10,15]
    n_list2 = [20,25,30]

    n1 = random.randint(2,3)
    if n1 == 2:
      nn3 = 1
    else :
      nn3 = 2

    n2 = random.choice(n_list)
    n4 = random.choice(n_list2)
          
    s1 = n2+n4

    if nn3 == 1:
        n3 = ""
    else :
        n3 = nn3



    n_list3 = [15,20,25,30]

    n5 = random.choice(n_list3)
    s2 = 180-n5+n2
    s3 = s2-n1*s1

    ans = s3-s1
    
    p1 = (0,0)
    p2 = (5,0)
    p3 = (10,0)

    c1 = s3+n5

    y_x = 5+5*math.cos(math.radians(c1))
    y_y = 5*math.sin(math.radians(c1))

    z_x = 5+5*math.cos(math.radians(180+c1))
    z_y = 5*math.sin(math.radians(180+c1))

    y = (y_x, y_y)
    z = (z_x, z_y)

    #ax = setChart(points=[p1, p2, p3, y, z])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p2, p2=y)
    drawLine(ax=ax, p1=p2, p2=z)
    

    AngleAnnotation(xy=p2, p1=p3, p2=y, text=r"$y+{n5}$".format(n5=n5),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=y, p2=p1, text=r"${n1}x-{n2}$".format(n1=n1, n2=n2),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=z, p2=p3, text=r"${n3}x+{n4}$".format(n3=n3, n4=n4),
                    textposition="outside", ax=ax, size=30)
    

    aa_list = [ans-15, ans-10, ans-5, ans, ans+5, ans+10, ans+15]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$${n1}x-{n2}={n3}x+{n4}$$/수식$$이므로\n$$수식$$x={s1}$$/수식$$ " \
              "$$수식$$({n1}x-{n2})+(y+{n5})=180$$/수식$$이므로\n$$수식$${n1}x+y={s2}$$/수식$$ " \
              "$$수식$${n1}\\times{s1}+y={s2}``````THEREFORE y={s3}$$/수식$$ " \
              "$$수식$$THEREFORE y-x={ans}$$/수식$$\n"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, s1=s1, s2=s2, s3=s3, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_058():
    stem = "좌표평면 위에 두 점 $$수식$$P({p_x},{p_y}), Q({q_x},{q_y})$$/수식$$이 있다.  " \
            "점 $$수식$$P$$/수식$$에서 $$수식$$x$$/수식$$축과 $$수식$$y$$/수식$$축에 내린 수선의 발을 각 " \
            "각 $$수식$$A, B$$/수식$$라 하고, 점 $$수식$$Q$$/수식$$에서 $$수식$$x$$/수식$$축과 $$수식$$y$$/수식$$축에 내린 " \
            "수선의 발을 각각 $$수식$$C, D$$/수식$$라 할 때, 사각형 " \
            "$$수식$$ABCD$$/수식$$의 넓이는?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}\n"
    comment = "(해설)\n두 점 $$수식$$P, Q$$/수식$$에서 각각 $$수식$$x$$/수식$$축과 $$수식$$y$$/수식$$축에 " \
              "내린 수선의 발은 다음 그림과 같다. " \
              "사각형 $$수식$$ABCD$$/수식$$의 넓이는 " \
              "삼각형 $$수식$$ABC$$/수식$$의 넓이와 " \
              "삼각형$$수식$$ADC$$/수식$$의 넓이의 합과 같으므로 " \
              "$$수식$${f}\\times{s1}\\times{s2}+{f}\\times{s3}\\times{s4}={ans}$$/수식$$\n"
    
    f = "\\frac{1}{2}"

    p_x = random.randint(-4,-2)
    p_y = random.randint(2,4)

    q_x = random.randint(2,4)
    q_y = random.randint(-4,-2)

    a_x = p_x
    a_y = 0

    b_x = 0
    b_y = p_y

    c_x = q_x
    c_y = 0

    d_x = 0
    d_y = q_y

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (4,4)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-6,6)
    ax.set_ylim(-6,6)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-0.5, 5.5, "y", size = 10)
    plt.text(5.5, -0.5, "x", size = 10)
    plt.text(-0.6,-0.6, "O", size = 12)
    
    x = [a_x, b_x, c_x, d_x, a_x]
    y = [a_y, b_y, c_y, d_y, a_y]

    plt.plot(x,y,c="black")
    plt.fill_between(x, y, alpha=0.5)

    x2 = [a_x, p_x, b_x]
    y2 = [a_y, p_y, b_y]
    plt.plot(x2,y2,c="black", linestyle='dotted')

    x3 = [c_x, q_x, d_x]
    y3 = [c_y, q_y, d_y]
    plt.plot(x3,y3,c="black", linestyle='dotted')


    plt.text(p_x-0.3, p_y, "P", size = 12)
    plt.text(q_x+0.1, q_y-0.2, "Q", size = 12)
    plt.text(a_x-0.5, a_y+0.1, "A", size = 12)
    plt.text(b_x-0.6, b_y, "B", size = 12)
    plt.text(c_x, c_y+0.1, "C", size = 12)
    plt.text(d_x+0.1, d_y-0.5, "D", size = 12)

    plt.text(a_x-0.4, a_y-0.6, "{a_x}".format(a_x=a_x), size = 10)
    plt.text(b_x+0.2, b_y, "{b_y}".format(b_y=b_y), size = 10)
    plt.text(c_x+0.1, c_y-0.6, "{c_x}".format(c_x=c_x), size = 10)
    plt.text(d_x-0.7, d_y-0.4, "{d_y}".format(d_y=d_y), size = 10)
      
    s1 = c_x - a_x
    s2 = b_y
    s3 = s1
    s4 = abs(d_y)

    ans = int(0.5*s1*s2+0.5*s3*s4)


    aa_list = [ans-3, ans-2, ans-1, ans, ans+1, ans+2, ans+3]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break


    stem = stem.format(p_x=p_x, p_y=p_y, q_x=q_x, q_y=q_y, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, s1=s1, s2=s2, s3=s3, s4=s4, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_059():
    stem = "그림에서 점 $$수식$$A$$/수식$$와 $$수식$${obc}$$/수식$$사이의 거리를 $$수식$$x``rm {{cm}}$$/수식$$, " \
            "점 $$수식$$C$$/수식$$와 $$수식$${oab}$$/수식$$ 사이의 거리를 $$수식$$y``rm {{cm}}$$/수식$$, 점 $$수식$$D$$/수식$$와 " \
            "$$수식$${oab}$$/수식$$ 사이의 거리를 $$수식$$z``rm {{cm}}$$/수식$$라 할 때, " \
            "$$수식$$x+y+z$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n" 
    
    ab = random.randint(2,4)
    
    list = [8,12]
    bc = random.choice(list)
    
    if bc == 8 :
      dc = 6
      db = 10
    elif bc == 12 :
      d_list = [5,9]
      dc = random.choice(d_list)
      if dc == 5 :
        db = 13
      elif dc == 9 :
        db = 15

    s1 = ab
    s2 = bc
    s3 = bc

    ans = s1+s2+s3

    a_x = 0
    a_y = ab

    b_x = 0
    b_y = 0
    
    c_x = bc
    c_y = 0

    d_x = bc
    d_y = dc
    

    a = (a_x, a_y)
    b = (b_x, b_y)
    c = (c_x, c_y)
    d = (d_x, d_y)


    #plt.style.use('default')
    #plt.rcParams['figure.figsize'] = (4,4)
    #plt.rcParams['font.size'] = 13

    #fig, ax = plt.subplots()
    
    fig, ax = plt.subplots(figsize=(4.5,3.5))
    plt.axis("off")
    ax.autoscale()

    ax.set_xlim(-2,17)
    ax.set_ylim(-2,9)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    x = [a_x, b_x, c_x, a_x]
    y = [a_y, b_y, c_y, a_y]
    
    plt.plot(x,y,'k',c="black")

    x2 = [b_x, c_x, d_x, b_x]
    y2 = [b_y, c_y, d_y, b_y]
    
    plt.plot(x2,y2,'k',c="black")   


    pp1 = mpatches.PathPatch(
    Path([(a_x, a_y), (-1, ab/2), (b_x, b_y)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([(b_x, b_y), (bc/2, -2), (c_x, c_y)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([(d_x, d_y), (bc+2, dc/2), (c_x, c_y)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp3)

    pp4 = mpatches.PathPatch(
    Path([(d_x, d_y), (bc/2-1, dc/2+2), (b_x, b_y)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp4)


    plt.text(a_x-0.1, a_y+0.3, "A", size = 12)
    plt.text(b_x-0.5, b_y-0.9, "B", size = 12)
    plt.text(c_x+0.1, c_y-0.8, "C", size = 12)
    plt.text(d_x-0.1, d_y+0.3, "D", size = 12)

    plt.text(-2, ab/2, "{ab}cm".format(ab=ab), size = 9)    
    plt.text(bc/2-0.5, -1.8, "{bc}cm".format(bc=bc), size = 9)  
    plt.text(bc+1.2, dc/2, "{dc}cm".format(dc=dc), size = 9)  
    plt.text(bc/2-2, dc/2+1.4, "{db}cm".format(db=db), size = 9)
    
    aa_list = [ans-6, ans-4, ans-2, ans, ans+2, ans+4, ans+6]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break 

    oab = "\\overline{AB}"
    obc = "\\overline{BC}"


    answer = "(정답)\n{result}\n"
    comment = "(해설)\n점 $$수식$$A$$/수식$$와 $$수식$${obc}$$/수식$$ 사이의 거리는 $$수식$${oab}$$/수식$$의 길이와  " \
              "같으므로 $$수식$${s1}``rm {{cm}}$$/수식$$이다. " \
              "$$수식$$THEREFORE x={s1}$$/수식$$ " \
              "점 $$수식$$C$$/수식$$와 $$수식$${oab}$$/수식$$ 사이의 거리는 $$수식$${obc}$$/수식$$의 길이와 " \
              "같으므로 $$수식$${s2}``rm {{cm}}$$/수식$$이다. " \
              "$$수식$$THEREFORE y={s2}$$/수식$$ " \
              "점 $$수식$$D$$/수식$$와 $$수식$${oab}$$/수식$$ 사이의 거리는 $$수식$${obc}$$/수식$$의 길dl와 " \
              "같으므로 $$수식$${s3}``rm {{cm}}$$/수식$$이다. " \
              "$$수식$$THEREFORE z={s3}$$/수식$$ " \
              "$$수식$$THEREFORE x+y+z={ans}$$/수식$$\n"


    stem = stem.format(obc=obc, oab=oab, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(obc=obc, oab=oab, s1=s1, s2=s2, s3=s3, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_063():
    stem = "다음 그림과 같은 삼각뿔에서 모서리 $$수식$$AB$$/수식$$ 위에 있는 " \
            "꼭짓점의 개수를 $$수식$$a$$/수식$$, 면 $$수식$$BCD$$/수식$$ 위에 있지 않은 꼭짓점의 " \
            "개수를 $$수식$$b$$/수식$$라 할 때, $$수식$$a+b$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n" 

    b = (0,0)
    d = (3.5,0)
    c = (2,-1.2)
    a = (1.8,2.6)
      
    #ax = setChart(points=[a,b,c,d])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawPolygon(ax=ax, verts=[a,b,c])

    drawLine(ax=ax, p1=a, p2=d)
    drawLine(ax=ax, p1=c, p2=d)
    drawLine(ax=ax, p1=b, p2=d, dash=True)

    ax.text(1.7, 2.7, "A", size = 14)
    ax.text(-0.25, 0, "B", size = 14)
    ax.text(1.9, -1.5, "C", size = 14)
    ax.text(3.56, 0, "D", size = 14)

    ans = 3

    aa_list = [1,2,3,4,5,6,7]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break 

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n모서리 $$수식$$AB$$/수식$$ 위에 있는 꼭짓점은 점 $$수식$$A$$/수식$$, 점 $$수식$$B$$/수식$$의 " \
              "$$수식$$2$$/수식$$개이므로 $$수식$$a=2$$/수식$$ " \
              "면 $$수식$$BCD$$/수식$$ 위에 있지 않은 꼭짓점은 점 $$수식$$A$$/수식$$의 $$수식$$1$$/수식$$개 " \
              "이므로 $$수식$$b=1$$/수식$$ " \
              "$$수식$$THEREFORE a+b=3$$/수식$$\n"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_068():
    stem = "그림과 같은 정{n}각형에서 각 변을 연장한 " \
            "직선을 그을때, 직선 $$수식$$AB$$/수식$$와 한 점에서 만나는 " \
            "직선의 개수는?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"
    
    def regulerPoint(point, side, angle):
        result = [point]
        for i in range(1, side):
            x = point[1] * math.sin(angle*i)
            y = point[1] * math.cos(angle*i)
            
            result.append((x,y))
            
        return result
            
    n = random.randint(3,8) 
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    if n == 3:
        a = (0,1)
        points = regulerPoint(a, n, (2*math.pi*120)/360)
        print(points)
        a, b, c = points
        
        #ax = setChart(points=[a, b, c])

        drawPolygon(ax=ax, verts=[a, b, c])

        ax.text(a[0]-0.04, a[1]+0.07, "A", size=14)
        ax.text(b[0]+0.05, b[1]-0.03, "B", size=14)
        ax.text(c[0]-0.12, c[1]-0.03, "C", size=14)

        bc = "\\overleftrightarrow{BC}"
        ca = "\\overleftrightarrow{CA}"
       

        comments = bc + ",``" + ca
        
        n = "삼"
        nn = 2
    elif n == 4:
        #a = (0,1)
        #points = regulerPoint(a, n, (2*math.pi*90)/360)
        #a, b, c, d = points
        a = (-1,1)
        b = (1,1)
        c = (1,-1)
        d = (-1,-1)
        
        #ax = setChart(points=[a,b,c,d])

        drawPolygon(ax=ax, verts=[a,b,c,d])

        ax.text(a[0]-0.1, a[1]+0.07, "A", size = 14)
        ax.text(b[0]+0.05, b[1]+0.07, "B", size = 14)
        ax.text(c[0]+0.05, c[1]-0.07, "C", size = 14)
        ax.text(d[0]-0.1, d[1]-0.07, "D", size = 14)
        
        bc = "\\overleftrightarrow{BC}"
        da = "\\overleftrightarrow{DA}"

        
        comments = bc + ",``" + da
        
        n = "사"
        nn = 2
    elif n == 5:
        a = (0,1)
        points = regulerPoint(a, n, (2*math.pi*72)/360)
        a, b, c, d, e = points
        
        #ax = setChart(points=[a,b,c,d,e])

        drawPolygon(ax=ax, verts=[a,b,c,d,e])

        ax.text(a[0]-0.04, a[1]+0.07, "A", size = 14)
        ax.text(b[0]+0.03, b[1]-0.03, "B", size = 14)
        ax.text(c[0]+0.03, c[1]-0.03, "C", size = 14)
        ax.text(d[0]-0.12, d[1]-0.03, "D", size = 14)
        ax.text(e[0]-0.1, e[1]-0.03, "E", size = 14)
        
        bc = "\\overleftrightarrow{BC}"
        cd = "\\overleftrightarrow{CD}"
        de = "\\overleftrightarrow{DE}"
        ea = "\\overleftrightarrow{EA}"

        
        comments = bc + ",``" + cd + ",``" + de + ",``" + ea
        
        n = "오"
        nn = 4
    elif n == 6:
        a = (0,1)
        points = regulerPoint(a, n, (2*math.pi*60)/360)
        a, b, c, d, e, f = points
        
        #ax = setChart(points=[a,b,c,d,e,f])
        
        drawPolygon(ax=ax, verts=[a,b,c,d,e,f])

        ax.text(a[0]-0.04, a[1]+0.07, "A", size = 14)
        ax.text(b[0]+0.03, b[1]-0.03, "B", size = 14)
        ax.text(c[0]+0.03, c[1]-0.03, "C", size = 14)
        ax.text(d[0]-0.04, d[1]-0.13, "D", size = 14)
        ax.text(e[0]-0.12, e[1]-0.03, "E", size = 14)
        ax.text(f[0]-0.12, f[1]-0.03, "F", size = 14)
        
        bc = "\\overleftrightarrow{BC}"
        cd = "\\overleftrightarrow{CD}"
        ef = "\\overleftrightarrow{EF}"
        af = "\\overleftrightarrow{AF}"

        comments = bc + ",``" + cd + ",``" + ef + ",``" + af
        
        n = "육"
        nn = 4
    elif n == 7:
        a = (0,1)
        points = regulerPoint(a, n, (2*math.pi*51.42)/360)
        a, b, c, d, e, f, g = points
        
        #ax = setChart(points=[a,b,c,d,e,f,g])
        
        drawPolygon(ax=ax, verts=[a,b,c,d,e,f,g])

        ax.text(a[0]-0.03, a[1]+0.07, "A", size = 14)
        ax.text(b[0]+0.03, b[1]-0.01, "B", size = 14)
        ax.text(c[0]+0.03, c[1]-0.03, "C", size = 14)
        ax.text(d[0]+0.03, d[1]-0.1, "D", size = 14)
        ax.text(e[0]-0.1, e[1]-0.1, "E", size = 14)
        ax.text(f[0]-0.1, f[1]-0.03, "F", size = 14)
        ax.text(g[0]-0.12, g[1]-0.01, "G", size = 14)
        
        bc = "\\overleftrightarrow{BC}"
        cd = "\\overleftrightarrow{CD}"
        de = "\\overleftrightarrow{DE}"
        ef = "\\overleftrightarrow{EF}"
        fg = "\\overleftrightarrow{FG}"
        gh = "\\overleftrightarrow{GH}"
        ga = "\\overleftrightarrow{GA}"
        
        comments = bc + ",``" + cd + ",``" + de + ",``" + ef + ",``" + fg + ",``" + ga
        
        n = "칠"
        nn = 6
    elif n == 8: 
        a = (0,1)
        points = regulerPoint(a, n, (2*math.pi*45)/360)
        a, b, c, d, e, f, g, h = points
        
        #ax = setChart(points=[a,b,c,d,e,f,g,h])
        
        drawPolygon(ax=ax, verts=[a,b,c,d,e,f,g,h])

        ax.text(a[0]-0.03, a[1]+0.07, "A", size = 14)
        ax.text(b[0]+0.03, b[1], "B", size = 14)
        ax.text(c[0]+0.03, c[1]-0.02, "C", size = 14)
        ax.text(d[0]+0.03, d[1]-0.03, "D", size = 14)
        ax.text(e[0]-0.03, e[1]-0.12, "E", size = 14)
        ax.text(f[0]-0.1, f[1]-0.03, "F", size = 14)
        ax.text(g[0]-0.12, g[1]-0.02, "G", size = 14)
        ax.text(h[0]-0.12, h[1], "H", size = 14)
        
        bc = "\\overleftrightarrow{BC}"
        cd = "\\overleftrightarrow{CD}"
        de = "\\overleftrightarrow{DE}"
        fg = "\\overleftrightarrow{FG}"
        gh = "\\overleftrightarrow{GH}"
        ha = "\\overleftrightarrow{HA}"
        
        comments = bc + ",``" + cd + ",``" + de + ",``" + fg + ",``" + gh + ",``" + ha
        
        n = "팔"
        nn = 6

    aa_list = [3,4,5,6,7,8,9]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == 6 :
        result = answer_dict[i]
        break 


    answer = "(정답)\n{result}\n"
    comment = "(해설)\n다음 그림에서 직선 $$수식$$AB$$/수식$$와 " \
              "한 점에서 만나는 직선은 " \
              "$$수식$${comments}$$/수식$$ " \
              "의 $$수식$${nn}$$/수식$$개이다."

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(comments=comments, nn=nn)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_076():
    stem = "다음 그림과 같은 정육면체에서 모서리 $$수식$${side}$$/수식$$와 " \
            "꼬인위치가 아닌 모서리는?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n" 

    a = (0.5,0.5)
    b = (0,0)
    c = (1.1,0)
    d = (1.6,0.5)
    e = (0.5,-0.6)
    f = (0,-1.1)
    g = (1.1,-1.1)
    h = (1.6,-0.6)
    
    resize = (-2, 2)
    a = tuple(sum(elem) for elem in zip(a, resize))
    b = tuple(sum(elem) for elem in zip(b, resize))
    c = tuple(sum(elem) for elem in zip(c, resize))
    d = tuple(sum(elem) for elem in zip(d, resize))
    e = tuple(sum(elem) for elem in zip(e, resize))
    f = tuple(sum(elem) for elem in zip(f, resize))
    g = tuple(sum(elem) for elem in zip(g, resize))
    h = tuple(sum(elem) for elem in zip(h, resize))
      
    ax = setChart(points=[a,b,c,d,e,f,g,h])

    drawPolygon(ax=ax, verts=[a,b,c,d])

    drawLine(ax=ax, p1=d, p2=h)
    drawLine(ax=ax, p1=b, p2=f)
    drawLine(ax=ax, p1=c, p2=g)
    drawLine(ax=ax, p1=f, p2=g)
    drawLine(ax=ax, p1=g, p2=h)
    drawLine(ax=ax, p1=f, p2=e, dash=True)
    drawLine(ax=ax, p1=a, p2=e, dash=True)
    drawLine(ax=ax, p1=e, p2=h, dash=True)

    ax.text(-1.6, 2.55, "A", size = 14)
    ax.text(-2.15, 1.95, "B", size = 14)
    ax.text(-0.85, 1.9, "C", size = 14)
    ax.text(-0.4, 2.5, "D", size = 14)
    ax.text(-1.65, 1.4, "E", size = 14)
    ax.text(-2.15, 0.8, "F", size = 14)
    ax.text(-0.95, 0.75, "G", size = 14)
    ax.text(-0.38, 1.4, "H", size = 14)
    
    ax.autoscale()

    ab = "\\overline{AB}"
    ad = "\\overline{AD}"
    ae = "\\overline{AE}"
    bc = "\\overline{BC}"
    bf = "\\overline{BF}"
    cd = "\\overline{CD}"
    cg = "\\overline{CG}"
    dh = "\\overline{DH}"
    ef = "\\overline{EF}"
    eh = "\\overline{EH}"
    fg = "\\overline{FG}"
    gh = "\\overline{GH}"

    side_list = [ab, bc, cd, ad, ae, bf, cg, dh, ef, fg, gh, eh]
    side = random.choice(side_list)

    if side == ab:
        a_list = [cg, dh, fg, eh]
        s_list = [cd, ef, gh]
    elif side == bc:
        a_list = [ae, dh, ef, gh]
        s_list = [ad, fg, eh]
    elif side == cd:
        a_list = [ae, bf, eh, fg]
        s_list = [ab, ef, gh]
    elif side == ad:
        a_list = [bf, cg, ef, gh]
        s_list = [bc, fg, eh]
    elif side == ae:
        a_list = [bc, fg, cd, gh]
        s_list = [bf, cg, dh]
    elif side == bf:
        a_list = [ad, eh, cd, gh]
        s_list = [ae, cg, dh]
    elif side == cg:
        a_list = [ad, eh, ab, ef]
        s_list = [ae, bf, dh]
    elif side == dh:
        a_list = [bc, fg, ab, ef]
        s_list = [ae, bf, cg]
    elif side == ef:
        a_list = [cg, dh, ad, bc]
        s_list = [ab, cd, gh]
    elif side == fg:
        a_list = [ae, dh, ab, cd]
        s_list = [ad, bc, eh]
    elif side == gh:
        a_list = [ae, bf, ad, bc]
        s_list = [ab, cd, ef]
    elif side == eh:
        a_list = [bf, cg, ab, cd]
        s_list = [ad, bc, fg]

    while True:
        a_side = random.choice(side_list)
        if a_side not in a_list:
            a_list.append(a_side)
            if a_side in s_list:
                comments = "$$수식$${a_side}$$/수식$$은 $$수식$${side}$$/수식$$와 평행합니다.".format(a_side=a_side, side=side)
            else:
                comments = "$$수식$${a_side}$$/수식$$은 $$수식$${side}$$/수식$$와 한 점에서 만납니다.".format(a_side=a_side, side=side)
            break

    random.shuffle(a_list)

    for i in a_list:
        if i == a_side:
            result = answer_dict[a_list.index(i)]
            break
    
    a1 = a_list[0]
    a2 = a_list[1]
    a3 = a_list[2]
    a4 = a_list[3]
    a5 = a_list[4]
    
    answer = "(정답)\n{result}\n"
    comment = "(해설)\n{comments}"

    stem = stem.format(side =side, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(comments=comments)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_082():
    stem = "다음 중 다음 그림과 같이 밑면이 직각삼각형인 " \
            "삼각기둥에 대한 설명으로 옳지 않은 것은?\n" \
            "① 면 $$수식$$DEF$$/수식$$와 모서리 $$수식$$AC$$/수식$$는 평행하다.\n" \
            "② 면 $$수식$$DEF$$/수식$$에 평행한 모서리는 4개이다.\n" \
            "③ 면 $$수식$$BEFC$$/수식$$와 수직인 모서리는 $$수식$$4$$/수식$$개이다.\n" \
            "④ 모서리 $$수식$$CF$$/수식$$는 면 $$수식$$ABC$$/수식$$와 한 점에서 만난다.\n" \
            "⑤ 면 $$수식$$ABC$$/수식$$와 수직인 모서리들은 서로 평행하다." 
    answer = "(정답)\n{result}\n"
    comment = "(해설)\n{result} 면 $$수식$$BEFC$$/수식$$와 수직인 모서리는 $$수식$${ab},{de}$$/수식$$의 " \
              "$$수식$$2$$/수식$$개이다."

    a = (0,0)
    b = (0.45,-0.55)
    c = (1.2,0)
    d = (0,-1.3)
    e = (0.45,-1.85)
    f = (1.2,-1.3)
      
    #ax = setChart(points=[a,b,c,d,e,f])

    fig, ax = plt.subplots(figsize=(3,5))
    plt.axis("off")
    ax.autoscale()

    drawPolygon(ax=ax, verts=[a,b,c])

    drawLine(ax=ax, p1=a, p2=d)
    drawLine(ax=ax, p1=b, p2=e)
    drawLine(ax=ax, p1=c, p2=f)
    drawLine(ax=ax, p1=d, p2=e)
    drawLine(ax=ax, p1=e, p2=f)
    drawLine(ax=ax, p1=d, p2=f, dash=True)

    ax.text(-0.15, -0.05, "A", size = 14)
    ax.text(0.47, -0.68, "B", size = 14)
    ax.text(1.25, -0.05, "C", size = 14)
    ax.text(-0.18, -1.35, "D", size = 14)
    ax.text(0.4, -2, "E", size = 14)
    ax.text(1.25, -1.35, "F", size = 14)

    result = answer_dict[2]

    ab = "\\overline{AB}"
    de = "\\overline{DE}"

    answer = answer.format(result=result)
    comment = comment.format(result=result, ab=ab, de=de)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_084():
    stem = "다음 그림과 같은 직육면체에서 점 $$수식$$B$$/수식$$와 " \
            "면 $$수식$$EFGH$$/수식$$ 사이의 거리를 구하시오."

    fg = random.randint(4,8)
    gh = fg-1
    dh = fg+random.randint(1,2)

    a = (-1.5,2.5)
    b = (-2,2)
    c = (-0.9,2)
    d = (-0.4,2.5)
    e = (-1.5,1)
    f = (-2,0.5)
    g = (-0.9,0.5)
    h = (-0.4,1)
      
    ax = setChart(points=[a,b,c,d,e,f,g,h])

    drawPolygon(ax=ax, verts=[a,b,c,d])

    drawLine(ax=ax, p1=d, p2=h)
    drawLine(ax=ax, p1=b, p2=f)
    drawLine(ax=ax, p1=c, p2=g)
    drawLine(ax=ax, p1=f, p2=g)
    drawLine(ax=ax, p1=g, p2=h)
    drawLine(ax=ax, p1=f, p2=e, dash=True)
    drawLine(ax=ax, p1=a, p2=e, dash=True)
    drawLine(ax=ax, p1=e, p2=h, dash=True)
    
    pp1 = mpatches.PathPatch(
    Path([(-2, 0.5), (-2.7/2, 0.2), (-0.9, 0.5)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([(-0.9, 0.5), (-0.9+0.5, 0.65), (-0.4, 1)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([(-0.4, 2.5), (-0.1, 1.75), (-0.4, 1)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp3)


    ax.text(-1.6, 2.55, "A", size = 14)
    ax.text(-2.18, 1.95, "B", size = 14)
    ax.text(-0.85, 1.9, "C", size = 14)
    ax.text(-0.4, 2.5, "D", size = 14)
    ax.text(-1.68, 1, "E", size = 14)
    ax.text(-2.18, 0.4, "F", size = 14)
    ax.text(-9.5, 0.35, "G", size = 14)
    ax.text(-0.35, 0.95, "H", size = 14)

    ax.text(-3.2/2, 0.1, r'${fg} \mathrm{{cm}}$'.format(fg=fg), size = 14)
    ax.text(-0.9+0.45, 0.5, r'${gh} \mathrm{{cm}}$'.format(gh=gh), size = 14)
    ax.text(-0.1, 1.6, r'${dh}\mathrm{{cm}}$'.format(dh=dh), size = 14)

    ax.autoscale()
    result = dh
    bf = "\\overline{BF}"

    answer = "(정답)\n$$수식$${result}``rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n점 $$수식$$B$$/수식$$와 면 $$수식$$EFGH$$/수식$$ 사이의 거리는 $$수식$${bf}$$/수식$$의 길이와 " \
              "같으므로 $$수식$${result}``rm {{cm}}$$/수식$$이다."

    answer = answer.format(result=result)
    comment = comment.format(bf=bf, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_091():
    stem = "다음 그림과 같이 밑면이 정{n}각형인 {n}각기둥에서 " \
            "서로 평행한 두 면은 모두 몇 쌍인가?\n" \
            "① $$수식$${a1}$$/수식$$쌍      ② $$수식$${a2}$$/수식$$쌍       ③ $$수식$${a3}$$/수식$$쌍\n" \
            "④ $$수식$${a4}$$/수식$$쌍      ⑤ $$수식$${a5}$$/수식$$쌍\n"
            
    flag = random.randint(3, 6)
    
    fig, ax = plt.subplots(figsize=(3,5))
    plt.axis("off")
    ax.autoscale()
    
    if flag == 3:
        n = "삼"

        p1 = (-2, 2)
        p2 = (1, 2)
        p3 = (-0.5, 0.05)

        p4 = (-2, -1)
        p5 = (1, -1)
        p6 = (-0.5, -2.55)

        #ax = setChart(points=[p1, p2, p3, p4, p5, p6])

        drawPolygon(ax=ax, verts=[p1, p2, p3])

        drawLine(ax=ax, p1=p1, p2=p4)
        drawLine(ax=ax, p1=p3, p2=p6)
        drawLine(ax=ax, p1=p2, p2=p5)
        drawLine(ax=ax, p1=p4, p2=p6)
        drawLine(ax=ax, p1=p6, p2=p5)

        drawLine(ax=ax, p1=p4, p2=p5, dash=True)
        
        ax.text(-2.3,2.0, "A", size = 14)
        ax.text(-0.7,-0.1, "B", size = 14)
        ax.text(1.1,2.0, "C", size = 14)
        ax.text(-2.3,-1.0, "D", size = 14)
        ax.text(-0.7,-2.7, "E", size = 14)
        ax.text(1.1,-1.0, "F", size = 14)
        
        ans = 1
        comments = "면 $$수식$$ABC$$/수식$$와 면 $$수식$$DEF$$/수식$$"
    elif flag == 4:
        n = "사"

        p1 = (-2, 2)
        p2 = (0, 2)
        p3 = (-2.5, 1.0)
        p4 = (-0.5, 1.0)

        p5 = (-2, -1)
        p6 = (0, -1)
        p7 = (-2.5, -2.0)
        p8 = (-0.5, -2.0)

        #ax = setChart(points=[p1, p2, p3, p4, p5, p6, p7, p8])

        drawPolygon(ax=ax, verts=[p1, p3, p4, p2])

        drawLine(ax=ax, p1=p3, p2=p7)
        drawLine(ax=ax, p1=p4, p2=p8)
        drawLine(ax=ax, p1=p2, p2=p6)
        drawLine(ax=ax, p1=p7, p2=p8)
        drawLine(ax=ax, p1=p8, p2=p6)

        drawLine(ax=ax, p1=p1, p2=p5, dash=True)
        drawLine(ax=ax, p1=p5, p2=p7, dash=True)
        drawLine(ax=ax, p1=p5, p2=p6, dash=True)
        
        ax.text(-2.3, 2.0, "A", size=14)
        ax.text(-2.8, 0.8, "B", size=14)
        ax.text(-0.4, 0.8, "C", size=14)
        ax.text(0.1, 2.0, "D", size=14)
        ax.text(-2.3, -1.0, "E", size=14)
        ax.text(-2.8, -2.2, "F", size=14)
        ax.text(-0.4, -2.2, "G", size=14)
        ax.text(0.1, -1.0, "H", size=14)
        
        ans = 3
        comments = "면 $$수식$$ABCD$$/수식$$와 면 $$수식$$DEFF$$/수식$$,\n면 $$수식$$ABEF$$/수식$$와 면 $$수식$$DCGH$$/수식$$,\n면 $$수식$$ADHE$$/수식$$와 면 $$수식$$BCGF$$/수식$$"
    elif flag == 5:
        n = "오"

        p1 = (-2, 2)
        p2 = (-0.5, 2.6)
        p3 = (1, 2)
        p4 = (0.4, 1.2)
        p5 = (-1.4, 1.2)

        p6 = (-2, -1)
        p7 = (-0.5, -0.4)
        p8 = (1, -1)
        p9 = (0.4, -1.8)
        p10 = (-1.4, -1.8)

        #ax = setChart(points=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])

        drawPolygon(ax=ax, verts=[p1, p2, p3, p4, p5])

        drawLine(ax=ax, p1=p1, p2=p6)
        drawLine(ax=ax, p1=p2, p2=p7, dash=True)
        drawLine(ax=ax, p1=p3, p2=p8)
        drawLine(ax=ax, p1=p4, p2=p9)
        drawLine(ax=ax, p1=p5, p2=p10)

        drawLine(ax=ax, p1=p6, p2=p7, dash=True)
        drawLine(ax=ax, p1=p7, p2=p8, dash=True)
        drawLine(ax=ax, p1=p8, p2=p9)
        drawLine(ax=ax, p1=p9, p2=p10)
        drawLine(ax=ax, p1=p10, p2=p6)
        
        ax.text(-0.6, 2.8, "A", size=14)
        ax.text(-2.3, 2.0, "B", size=14)
        ax.text(-1.8, 1.0, "C", size=14)
        ax.text(0.5, 1.0, "D", size=14)
        ax.text(1.1, 2.0, "E", size=14)
        ax.text(-0.8, -0.3, "F", size=14)
        ax.text(-2.4, -1.0, "G", size=14)
        ax.text(-1.8, -2.0, "H", size=14)
        ax.text(0.5, -2.0, "I", size=14)
        ax.text(1.1, -1.0, "J", size=14)
        
        ans = 1
        comments = "면 $$수식$$ABCDE$$/수식$$와 면 $$수식$$FGHIJ$$/수식$$"
    else:
        n = "육"

        p1 = (-2, 2)
        p2 = (-1.5, 2.5)
        p3 = (-0.5, 2.5)
        p4 = (0, 2)
        p5 = (-0.5, 1.5)
        p6 = (-1.5, 1.5)

        p7 = (-2, -1)
        p8 = (-1.5, -0.5)
        p9 = (-0.5, -0.5)
        p10 = (0, -1)
        p11 = (-0.5, -1.5)
        p12 = (-1.5, -1.5)

        #ax = setChart(points=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12])

        drawPolygon(ax=ax, verts=[p1, p2, p3, p4, p5, p6])

        drawLine(ax=ax, p1=p1, p2=p7)
        drawLine(ax=ax, p1=p2, p2=p8, dash=True)
        drawLine(ax=ax, p1=p3, p2=p9, dash=True)
        drawLine(ax=ax, p1=p4, p2=p10)
        drawLine(ax=ax, p1=p5, p2=p11)
        drawLine(ax=ax, p1=p6, p2=p12)

        drawLine(ax=ax, p1=p7, p2=p12)
        drawLine(ax=ax, p1=p12, p2=p11)
        drawLine(ax=ax, p1=p11, p2=p10)
        drawLine(ax=ax, p1=p7, p2=p8, dash=True)
        drawLine(ax=ax, p1=p8, p2=p9, dash=True)
        drawLine(ax=ax, p1=p9, p2=p10, dash=True)
        
        ax.text(-1.7,2.7, "A", size = 14)
        ax.text(-2.3,2.0, "B", size = 14)
        ax.text(-1.8,1.2, "C", size = 14)
        ax.text(-0.4,1.2, "D", size = 14)
        ax.text(0.1,2, "E", size = 14)
        ax.text(-0.5,2.7, "F", size = 14)
        ax.text(-1.8,-0.4, "G", size = 14)
        ax.text(-2.3,-1.0, "H", size = 14)
        ax.text(-1.7,-1.7, "I", size = 14)
        ax.text(-0.4, -1.7, "J", size=14)
        ax.text(0.1,-1.0, "K", size = 14)
        ax.text(-0.4, -0.4, "L", size=14)

        ans = 4
        
        comments = "면 $$수식$$ABCDEF$$/수식$$와 면 $$수식$$GHIJKL$$/수식$$,\n면 $$수식$$ABHG$$/수식$$와 면 $$수식$$DEKJ$$/수식$$,\n면 $$수식$$BCIH$$/수식$$와 면 $$수식$$EFLK$$/수식$$,\n면 $$수식$$AFLG$$/수식$$와 면 $$수식$$CDJI$$/수식$$"
    result = answer_dict[ans-1]

    a1, a2, a3, a4, a5 = [1, 2, 3, 4, 5]
    
    answer = "(정답)\n{result}\n"
    comment = "(해설)\n서로 평행한 두 면은 " \
              "{comments}의 $$수식$${ans}$$/수식$$쌍이다."

    stem = stem.format(n=n,  a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(comments=comments, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 


def figure121_Stem_108():
    stem = "다음 그림에서 $$수식$$\\angle x$$/수식$$의 모든 엇각의 크기의 합은?\n" \
            "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"     

    ag1_list = [45,50,55]
    ag1 = random.choice(ag1_list)

    ag2_list = [65,70,75]
    ag2 = random.choice(ag2_list)

    p1 = (0,0)
    p1_1 = (-0.45,0)
    p1_2 = (-0.3,-0.4)
    p2 = (0.8,1.2)
    p2_1 = (0.45,1.6)
    p2_2 = (1.14,1.6)
    p3 = (1.6,0)
    p3_1 = (2.1,0)
    p3_2 = (1.9,-0.4)
    p4 = (0.8,1.2)
    p4_1 = (0.45,1.5)
    p4_2 = (1.14,1.5)
       
    #ax = setChart(points=[p1, p1_1, p1_2, p2, p2_1, p2_2, p3, p3_1, p3_2, p4, p4_1, p4_2])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1_1, p2=p3_1)
    drawLine(ax=ax, p1=p2_2, p2=p1_2)
    drawLine(ax=ax, p1=p2_1, p2=p3_2)

    
    AngleAnnotation(xy=p1, p1=p3, p2=p2, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=p3, p1=p2, p2=p1, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p4, p1=p4_2, p2=p4_1, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30)
    
    s1 = 180-ag1
    s2 = 180-ag2

    ans = s1+s2

    aa_list = [ans-60,ans-40,ans-20,ans,ans+20,ans+40,ans+60]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans :
        result = answer_dict[i]
        break 

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n($$수식$$\\angle x$$/수식$$의 모든 엇각의 크기의 합) " \
              "$$수식$$={s1}DEG + {s2}DEG = {ans}DEG$$/수식$$\n"
    
    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 




def figure121_Stem_110():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$일때, $$수식$$ ANGLE x + ANGLE y$$/수식$$의 " \
            "크기를 구하시오. " \

    ag1_list = [90,95,100]
    ag1 = random.choice(ag1_list)

    ag2_list = [40,45,50,55]
    ag2 = random.choice(ag2_list)

    l1 = (-0.7,0)
    l2 = (0,0)
    l3 = (1.55,0)

    m1 = (-0.7,-1)
    m2 = (0,-1)
    m3 = (1.55,-1)

    p1 = (-0.6,0.6/1.2)
    p2 = (1.2,-1)
    p3 = (1.55,-1.55/1.2)

    p4 = (0,0.55)
    p5 = (0,-1.55)
       
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1, p2, p3, p4, p5])
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p4, p2=p5)


    AngleAnnotation(xy=l2, p1=p1, p2=l1, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=m2, p1=l2, p2=m1, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=l2, p1=l3, p2=p4, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=m3, p2=p1, text=r"$y$",
                    textposition="outside", ax=ax, size=30)

    ax.text(1.63, -0.05, "l", size = 14)
    ax.text(1.6, -1.05, "m", size = 14)
    ax.autoscale()
    
    s1 = 180-ag1
    s2 = 180-ag2

    result = s1+s2

    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n$$수식$$\\angle x=180 DEG - {ag1}DEG = {s1}DEG$$/수식$$(동위각) " \
              "$$수식$$\\angle y=180 DEG - {ag2}DEG = {s2}DEG$$/수식$$(동위각) " \
              "$$수식$$THEREFORE \\angle x+\\angle y={result}DEG$$/수식$$"

    answer = answer.format(result=result)
    comment = comment.format(ag1=ag1, ag2=ag2, s1=s1, s2=s2, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_112():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$일때, $$수식$$\\angle x+\\angle y$$/수식$$의 크기를 구하시오.\n"

    ag1_list = [110,115,120]
    ag1 = random.choice(ag1_list)

    ag2_list = [95,100,105]
    ag2 = random.choice(ag2_list)

    l1 = (-0.6,0)
    l2 = (0,0)
    l3 = (1,0)
    l4 = (1.6,0)

    m1 = (-0.6,-1)
    m2 = (0.2/0.6,-1)
    m3 = (-7/-6,-1)
    m4 = (1.6,-1)

    p1 = (-0.2,0.6)
    p2 = (0.2/0.6+0.2,-0.6/0.2*(0.2/0.6+0.2))

    p3 = (0.9,0.6)
    p4 = (((-0.6/0.2*(0.2/0.6+0.2))-6)/-6,-0.6/0.2*(0.2/0.6+0.2))
      
    #ax = setChart(points=[l1, l2, l3, l4, m1, m2, m3, m4])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p3, p2=p4)
    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=m1, p2=m4)


    AngleAnnotation(xy=l2, p1=l1, p2=m2, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=m2, p1=m3, p2=l2, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m3, p1=m4, p2=l3, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=l3, p1=m3, p2=l4, text=r"$y$",
                    textposition="outside", ax=ax, size=30)   

    ax.text(1.7, -0.05, "l", size = 14)
    ax.text(1.65, -1.05, "m", size = 14)
    
    s1 = ag1
    s2 = 180-ag2
    result=s1+s2
    
    ax.autoscale()
    svg1 = saveSvg()
    
    # comment image
    #ax = setChart(points=[l1, l2, l3, l4, m1, m2, m3, m4])
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p3, p2=p4)
    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=m1, p2=m4)
    
    AngleAnnotation(xy=l2, p1=l1, p2=m2, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=m2, p1=m3, p2=l2, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m3, p1=m4, p2=l3, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=l3, p1=m3, p2=l4, text=r"$y$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=l3, p1=l4, p2=p3, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30)
    
    ax.text(1.7, -0.05, "l", size = 14)
    ax.text(1.65, -1.05, "m", size = 14)
    
    ax.autoscale()
    svg2 = saveSvg()
    
    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림에서 $$수식$$l//m$$/수식$$이므로 " \
              "$$수식$$\\angle x={s1}DEG$$/수식$$(엇각) " \
              "또, $$수식$${ag2}DEG +\\angle y=180 DEG$$/수식$$이므로 " \
              "$$수식$$\\angle y={s2}DEG$$/수식$$ " \
              "$$수식$$THEREFORE \\angle x+\\angle y={result}DEG$$/수식$$\n" 

    answer = answer.format(result=result)
    comment = comment.format(ag2=ag2, s1=s1, s2=s2, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg 



def figure121_Stem_113():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$, $$수식$$m//n$$/수식$$일 때, " \
            "$$수식$$\\angle x-\\angle y$$/수식$$의 크기를 구하시오. " \

    ag_list = [40,45,50,55]
    ag = random.choice(ag_list)

    l1 = (-0.75,1)
    l2 = (0.3/0.5,1)
    l3 = (1.5,1)

    m1 = (-0.75,0.5)
    m2 = (0.3,0.5)
    m3 = (1.5,0.5)

    n1 = (-0.75,0)
    n2 = (0,0)
    n3 = (1.5,0)

    p1 = (1,1*0.5/0.3)
    p2 = (-0.4,-0.4*0.5/0.3)
      
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, n1, n2, n3, p1, p2])
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=n1, p2=n3)


    AngleAnnotation(xy=l2, p1=l1, p2=m2, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=m2, p1=n2, p2=m3, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=n2, p1=n1, p2=p2, text=r"$y$",
                    textposition="outside", ax=ax, size=30)

    ax.text(1.58, 0.95, "l", size = 14)
    ax.text(1.55, 0.45, "m", size = 14)
    ax.text(1.57, -0.05, "n", size = 14)
    
    ax.autoscale()
    svg1 = saveSvg()
    
    s1 = 180-ag

    result = s1-ag

    # comment image
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, n1, n2, n3, p1, p2])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=n1, p2=n3)

    AngleAnnotation(xy=l2, p1=l1, p2=m2, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m2, p1=n2, p2=m3, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=n2, p1=n1, p2=p2, text=r"$y$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m2, p1=m1, p2=n2, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)
    
    ax.text(1.58, 0.95, "l", size = 14)
    ax.text(1.55, 0.45, "m", size = 14)
    ax.text(1.57, -0.05, "n", size = 14)
    
    ax.autoscale()
    
    svg2 = saveSvg()

    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림에서 $$수식$$l//m$$/수식$$이므로 " \
              "$$수식$${ag}DEG +\\angle x=180 DEG$$/수식$$ " \
              "$$수식$$THEREFORE \\angle x={s1}DEG$$/수식$$ " \
              "$$수식$$m//n$$/수식$$이므로 " \
              "$$수식$$\\angle y={ag}DEG$$/수식$$(동위각) " \
              "$$수식$$THEREFORE \\angle x-\\angle y={result}DEG$$/수식$$\n" 

    answer = answer.format(result=result)
    comment = comment.format(s1=s1, ag=ag, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg 



def figure121_Stem_119():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$일때, $$수식$$\\angle x$$/수식$$의 크기를 구하시오.\n"

    ag1 = random.randint(95,100)
    ag2 = random.randint(115,125)

    l1 = (-1,0)
    l2 = (0,0)
    l3 = (0.5,0)
    l4 = (1.3,0)

    m1 = (-1,-0.9)
    m2 = (-0.9/8,-0.9)
    m3 = (1.3,-0.9)

    p1 = (0.1,0.8)
    p2 = (-1.4/8,-1.4)

      
    #ax = setChart(points=[l1, l2, l3, l4, m1, m2, m3, p1, p2])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p1, p2=l3)
    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=m1, p2=m3)


    AngleAnnotation(xy=m2, p1=l2, p2=m1, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=p1, p1=l2, p2=l3, text=r"$x$",
                    textposition="outside", ax=ax, size=35)
    AngleAnnotation(xy=l3, p1=l4, p2=p1, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30) 
    
    ax.text(1.38, -0.05, "l", size = 14)
    ax.text(1.35, -0.95, "m", size = 14)
    
    svg1 = saveSvg()
    
    s1 = 180-ag1
    s2 = 180-ag2
    result = 180-s1-s2
    
    # comment image
    #ax = setChart(points=[l1, l2, l3, l4, m1, m2, m3, p1, p2])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p1, p2=l3)
    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=m1, p2=m3)

    AngleAnnotation(xy=m2, p1=l2, p2=m1, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p1, p1=l2, p2=l3, text=r"$x$",
                    textposition="outside", ax=ax, size=35)
    AngleAnnotation(xy=l3, p1=l4, p2=p1, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30)
    
    AngleAnnotation(xy=l2, p1=p1, p2=l1, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=l2, p1=l4, p2=p1, text=r"${ag1}°$".format(ag1=180-ag1),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(100, 100), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.4")))
    AngleAnnotation(xy=l3, p1=p1, p2=l2, text=r"${ag1}°$".format(ag1=180-ag2),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(110, 110), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.4")))
    
    ax.text(1.38, -0.05, "l", size = 14)
    ax.text(1.35, -0.95, "m", size = 14)
    
    svg2 = saveSvg()
    
    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림에서 삼각형의 세 내각의 " \
              "크기의 합이 $$수식$$180 DEG$$/수식$$이므로 " \
              "$$수식$$\\angle x+{s1}+{s2}=180 DEG$$/수식$$ " \
              "$$수식$$THEREFORE \\angle x={result}$$/수식$$\n"

    answer = answer.format(result=result)
    comment = comment.format(s1=s1, s2=s2, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg 



def figure121_Stem_120():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$일때, $$수식$$\\angle x+\\angle y$$/수식$$의 크기를 구하시오.\n"

    ag_list = [55,60,65]
    ag = random.choice(ag_list)


    l1 = (-0.7,1.2)
    l2 = (1.2/6,1.2)
    l3 = (0.6,1.2)
    l4 = (1.5,1.2)

    m1 = (-0.7,0)
    m2 = (0,0)
    m3 = (0.4,0)
    m4 = (1.5,0)

    p1 = (0.8/6,1.6)
    p2 = (2.8/6,-0.4)

    p3 = (0.8,1.6)
    p4 = (0.3,0.6)
    p5 = (-0.2,-0.4)
      
    #ax = setChart(points=[l1, l2, l3, l4, m1, m2, m3, m4, p1, p2, p3, p4, p5])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p3, p2=p5)
    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=m1, p2=m4)


    AngleAnnotation(xy=l3, p1=l2, p2=p4, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p4, p1=l2, p2=m2, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m3, p1=m4, p2=p4, text=r"$y$",
                    textposition="outside", ax=ax, size=30) 
    ax.text(1.58, 1.15, "l", size = 14)
    ax.text(1.55, -0.05, "m", size = 14)

    svg1 = saveSvg()
    
    # comment image
    
    #ax = setChart(points=[l1, l2, l3, l4, m1, m2, m3, m4, p1, p2, p3, p4, p5])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p3, p2=p5)
    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=m1, p2=m4)

    AngleAnnotation(xy=l3, p1=l2, p2=p4, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(80, 80), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.4")))
    AngleAnnotation(xy=p4, p1=l2, p2=m2, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m3, p1=m4, p2=p4, text=r"$y$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=l2, p1=p4, p2=l3, text=r"$180^\circ - \angle y$", textposition="outside", ax=ax, size=30,
                    text_kw=dict(xytext=(80, 80), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.4")))
    AngleAnnotation(xy=p4, p1=l3, p2=l2, text=r"$180^\circ - \angle x$", textposition="outside", ax=ax, size=30,
                    text_kw=dict(xytext=(200, 200), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.0")))
    AngleAnnotation(xy=m3, p1=p4, p2=m2, text=r"$180^\circ - \angle y$", textposition="outside", ax=ax, size=30,
                    text_kw=dict(xytext=(60, 60), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.4")))
    
    ax.text(1.58, 1.15, "l", size = 14)
    ax.text(1.55, -0.05, "m", size = 14)
    
    svg2 = saveSvg()
    
    result = 180+ag

    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림에서 삼각형의세 내각의 " \
              "크기의 합이 $$수식$$180 DEG$$/수식$$이므로 " \
              "$$수식$$(180 DEG - \\angle y)+(180 DEG - \\angle x)+{ag}DEG$$/수식$$ " \
              "$$수식$$=180 DEG$$/수식$$ " \
              "$$수식$$THEREFORE \\angle x+\\angle y={result}DEG$$/수식$$\n"

    answer = answer.format(result=result)
    comment = comment.format(ag=ag, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg 



def figure121_Stem_121():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$일때, $$수식$$\\angle x$$/수식$$의 크기를 구하시오. " \

    ag_list = [35,40,45]
    ag = random.choice(ag_list)

    while True :
      n1 = random.randint(2,3)
      n_list = [10,15,20,25]
      n2 = random.choice(n_list)
      n3 = random.choice(n_list)
      s1 = n1+1
      s2 = 180-ag-n2-n3
      if s2%s1 == 0 :
        break


    l1 = (-0.9,0)
    l2 = (0,0)
    l3 = (0.4,0)
    l4 = (1.5,0)

    m1 = (-0.9,-1.3)
    m2 = (-0.3,-1.3)
    m3 = ((-1.3-(0.52*0.4/0.28))*0.28/-0.52,-1.3)
    m4 = (1.5,-1.3)

    p1 = (0.12,1.3/0.3*0.12)
    p2 = (-0.4,1.3/0.3*-0.4)
    p3 = ((1.3/0.3*-0.4-(0.52*0.4/0.28))*0.28/-0.52,1.3/0.3*-0.4)

      
    #ax = setChart(points=[l1, l2, l3, l4, m1, m2, m3, m4, p1, p2, p3])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=m1, p2=m4)

    AngleAnnotation(xy=p1, p1=l2, p2=l3, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=40)
    AngleAnnotation(xy=l3, p1=m3, p2=l4, text=r"$x+{n3}°$".format(n3=n3),
                    textposition="outside", ax=ax, size=35)
    AngleAnnotation(xy=m2, p1=m3, p2=l2, text=r"${n1}x+{n2}°$".format(n1=n1, n2=n2),
                    textposition="outside", ax=ax, size=30) 
    
    ax.text(1.57, -0.05, "l", size = 14)
    ax.text(1.55, -1.35, "m", size = 14)
    
    svg1 = saveSvg()
    
    # comment image

    #ax = setChart(points=[l1, l2, l3, l4, m1, m2, m3, m4, p1, p2, p3])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=m1, p2=m4)

    AngleAnnotation(xy=p1, p1=l2, p2=l3, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=40, text_kw=dict(xytext=(50, 50), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")))
    AngleAnnotation(xy=l3, p1=m3, p2=l4, text=r"$x+{n3}°$".format(n3=n3),
                    textposition="outside", ax=ax, size=35)
    AngleAnnotation(xy=m2, p1=m3, p2=l2, text=r"${n1}x+{n2}°$".format(n1=n1, n2=n2),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(50, 50), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")))
    AngleAnnotation(xy=m3, p1=l3, p2=m2, text=r"$x+{n3}°$".format(n3=n3),
                    textposition="outside", ax=ax, size=40, text_kw=dict(xytext=(30, 30), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")))

    ax.text(1.57, -0.05, "l", size = 14)
    ax.text(1.55, -1.35, "m", size = 14)
    
    ax.autoscale()
    
    svg2 = saveSvg()

    result = int(s2/s1)

    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림에서 삼각형의 세 내각의 크기의 합이 " \
              "$$수식$$180 DEG$$/수식$$이므로 " \
              "$$수식$${ag}DEG + (\\angle {n1}x+{n2})$$/수식$$ " \
              "$$수식$$+(\\angle x+{n3})=180 DEG$$/수식$$ " \
              "$$수식$${s1}\\angle x={s2}$$/수식$$ " \
              "$$수식$$THEREFORE \\angle x={result}$$/수식$$"

    answer = answer.format(result=result)
    comment = comment.format(ag=ag, n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg 



def figure121_Stem_123():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$일때, $$수식$$\\angle x$$/수식$$의 크기를 구하시오. " \
    
    ag1 = random.randint(20,25)
    ag2 = random.randint(60,65)

    l1 = (-0.5,0)
    l2 = (0,0)
    l3 = (2,0)

    m1 = (-0.5,-1.7)
    m2 = (0.9,-1.7)
    m3 = (2,-1.7)

    p1 = (1.5,-0.7)

      
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=m2)
    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)


    AngleAnnotation(xy=l2, p1=p1, p2=l3, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=45)    
    AngleAnnotation(xy=p1, p1=l2, p2=m2, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m2, p1=m3, p2=p1, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30) 
    
    ax.text(2.08, -0.05, "l", size = 14)
    ax.text(2.05, -1.75, "m", size = 14)
    
    ax.autoscale()
    
    svg1 = saveSvg()
    
    # comment image
    p2 = (l1[0], p1[1])
    p3 = (l3[0], p1[1])
    
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=m2)
    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=p2, p2=p3)

    AngleAnnotation(xy=l2, p1=p1, p2=l3, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=45)
    AngleAnnotation(xy=m2, p1=m3, p2=p1, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p1, p1=l2, p2=p2, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=45)
    AngleAnnotation(xy=p1, p1=p2, p2=m2, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30)
    
    ax.text(2.08, -0.05, "l", size = 14)
    ax.text(2.05, -1.75, "m", size = 14)
    ax.text(2.08, -0.7, "n", size=14)

    ax.autoscale()

    svg2 = saveSvg()
    result = ag1+ag2

    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림과 같이 $$수식$$\\angle x$$/수식$$의 꼭짓점을 지나고 " \
              "두 직선 $$수식$$l,m$$/수식$$에 평행한 직선 $$수식$$n$$/수식$$을 그으면 " \
              "$$수식$$\\angle x={ag1}DEG + {ag2}DEG = {result}DEG$$/수식$$\n"

    answer = answer.format(result=result)
    comment = comment.format(ag1=ag1, ag2=ag2, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg 



def figure121_Stem_124():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$일때, $$수식$$\\angle x$$/수식$$의 크기를 구하시오. " \

    ag1_list = [120,125,130]
    ag1 = random.choice(ag1_list)

    ag2_list = [30,35,40]
    ag2 = random.choice(ag2_list)

    while True :
      n1 = random.randint(2,3)
      n_list = [10,15,20]
      n2 = random.choice(n_list)
      if (ag1-ag2-n2)%n1 == 0 :
        break

    l1 = (-1.6,0)
    l2 = (0,-0.01)
    l3 = (1.3,0)

    m1 = (-1.6,-1.6)
    m2 = (-1.1,-1.6)
    m3 = (1.3,-1.6)

    p1 = (-0.1,-0.8)

      
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=m2)
    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)


    AngleAnnotation(xy=l2, p1=p1, p2=l3, text=r"${n1}x+{n2}°$".format(n1=n1, n2=n2),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(50, 50), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")))
    AngleAnnotation(xy=p1, p1=l2, p2=m2, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m2, p1=m3, p2=p1, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(50, 50), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.0")))
    
    ax.text(1.38, -0.05, "l", size = 14)
    ax.text(1.35, -1.65, "m", size = 14)

    svg1 = saveSvg()
    
    # comment image
    
    p2 = (l1[0], p1[1])
    p3 = (l3[0], p1[1])
    
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=m2)
    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=p2, p2=p3)

    AngleAnnotation(xy=l2, p1=p1, p2=l3, text=r"${n1}x+{n2}°$".format(n1=n1, n2=n2),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(40, 40), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")))
    #AngleAnnotation(xy=p1, p1=l2, p2=m2, text=r"${ag1}°$".format(ag1=ag1),
    #                textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m2, p1=m3, p2=p1, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(50, 50), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.0")))
    AngleAnnotation(xy=p1, p1=p2, p2=m2, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(50, 50), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.0")))
    AngleAnnotation(xy=p1, p1=l2, p2=p2, text=r"${ag}°$".format(ag=ag1-ag2),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(40, 40), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.0")))
    
    #ax.text(l1[0], l1[1], "l1", size=14)
    #ax.text(l2[0], l3[1], "l2", size=14)
    #ax.text(l3[0], l2[1], "l3", size=14)
    #
    #ax.text(m1[0], m1[1], "m1", size=14)
    #ax.text(m2[0], m3[1], "m2", size=14)
    #ax.text(m3[0], m2[1], "m3", size=14)
    #
    #ax.text(p1[0], p1[1], "p1", size=14)
    
    ax.text(1.38, -0.05, "l", size = 14)
    ax.text(1.35, -1.65, "m", size = 14)
    ax.text(1.38, p1[1], "n", size=14)

    
    svg2 = saveSvg()
    

    s1 = ag1-ag2
    result = int((s1-n2)/n1)

    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림과 같이 두 직선 $$수식$$l, m$$/수식$$에 평핸한 직선 $$수식$$n$$/수식$$을 그으면 " \
              "$$수식$${n1}x+{n2}DEG = {s1}DEG$$/수식$$ " \
              "$$수식$$THEREFORE \\angle x={result}DEG$$/수식$$" 

    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, s1=s1, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg



def figure121_Stem_127():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$일때, $$수식$$\\angle x$$/수식$$의 크기를 구하시오. " \
    
    ag1_list = [80,85,90]
    ag1 = random.choice(ag1_list)

    ag2_list = [55,60,65]
    ag2 = random.choice(ag2_list)

    ag3_list = [20,25,30]
    ag3 = random.choice(ag3_list)

    l1 = (-1.6,0)
    l2 = (0,0)
    l3 = (1,0)

    m1 = (-1.6,-1.5)
    m2 = (-0.9,-1.5)
    m3 = (1,-1.5)

    p1 = (-0.55,-0.6)
    p2 = (0,-1.1)

    p3 = (l1[0], p1[1])
    p4 = (l3[0], p1[1])
    
    p5 = (l1[0], p2[1])
    p6 = (l3[0], p2[1])
    
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1, p2])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=m2)


    AngleAnnotation(xy=l2, p1=l1, p2=p1, text=r"$x$",
                    textposition="outside", ax=ax, size=35)    
    AngleAnnotation(xy=p1, p1=p2, p2=l2, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=p1, p2=m2, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30) 
    AngleAnnotation(xy=m2, p1=m3, p2=p2, text=r"${ag3}°$".format(ag3=ag3),
                    textposition="outside", ax=ax, size=45)
    
    ax.text(1.08, -0.05, "l", size = 14)
    ax.text(1.05, -1.55, "m", size = 14)
    
    svg1 = saveSvg()
    
    s1 = ag2-ag3
    result = ag1-s1
    
    # comment image
    
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1, p2])
    fig, ax = plt.subplots(figsize=(4,3 ))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=m2)
    drawLine(ax=ax, p1=p3, p2=p4)
    drawLine(ax=ax, p1=p5, p2=p6)

    AngleAnnotation(xy=l2, p1=l1, p2=p1, text=r"$x$",
                    textposition="outside", ax=ax, size=35)    
    AngleAnnotation(xy=p1, p1=p4, p2=l2, text=r"${result}°$".format(result=result),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=p1, p2=p5, text=r"${s1}°$".format(s1=s1),
                    textposition="outside", ax=ax, size=30) 
    AngleAnnotation(xy=m2, p1=m3, p2=p2, text=r"${ag3}°$".format(ag3=ag3),
                    textposition="outside", ax=ax, size=45)
    AngleAnnotation(xy=p2, p1=p5, p2=m2, text=r"${ag3}°$".format(ag3=ag3),
                    textposition="outside", ax=ax, size=45)
    AngleAnnotation(xy=p1, p1=p2, p2=p4, text=r"${s1}°$".format(s1=s1),
                    textposition="outside", ax=ax, size=30)
    
    ax.text(1.08, -0.05, "l", size = 14)
    ax.text(1.05, -1.55, "m", size = 14)
    ax.text(1.08, p1[1], "n", size = 14)
    ax.text(1.08, p2[1], "p", size = 14)
    
    svg2 = saveSvg()
    
    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림과 같이 크기가 $$수식$${ag1}DEG , {ag2}DEG$$/수식$$인 각의 " \
              "꼭짓점을 각각 지나고 두 직선 $$수식$$l, m$$/수식$$에 평행한\n직선 $$수식$$n, p$$/수식$$를 그으면 " \
              "$$수식$$\\angle x={result}DEG$$/수식$$"

    answer = answer.format(result=result)
    comment = comment.format(ag1=ag1, ag2=ag2, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg  



def figure121_Stem_128():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$일때, $$수식$$\\angle x$$/수식$$의 크기를 구하시오. " \

    n1 = random.randint(2,3)
    if n1 == 2:
      n3 = 3
    else :
      n3 = 4
    
    n_list = [10,15,20,25]
    n5_list = [5,10]
    while True :
      n2 = random.choice(n_list)
      n4 = random.choice(n_list)
      n5 = random.choice(n5_list)
      s1 = n2+n4
      if s1 > n5 :
        break

    l1 = (-1.5,0)
    l2 = (0,0)
    l3 = (1,0)

    m1 = (-1.5,-1.0)
    m2 = (-0.7,-1.0)
    m3 = (1,-1.0)

    p1 = (-0.7,-0.4)
    p2 = (0,-0.6)
    
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1, p2])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=m2)


    AngleAnnotation(xy=l2, p1=l1, p2=p1, text=r"$x+{n5}°$".format(n5=n5),
                    textposition="outside", ax=ax, size=45)    
    AngleAnnotation(xy=p1, p1=p2, p2=l2, text=r"${n1}x+{n2}°$".format(n1=n1, n2=n2),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p2, p1=p1, p2=m2, text=r"${n3}x-{n4}°$".format(n3=n3, n4=n4),
                    textposition="outside", ax=ax, size=30) 
    AngleAnnotation(xy=m2, p1=m3, p2=p2, text=r"$x$",
                    textposition="outside", ax=ax, size=45)
    
    ax.text(1.08, -0.05, "l", size = 14)
    ax.text(1.05, -1.55, "m", size = 14)

    result = s1-n5
    
    
    svg1 = saveSvg()
    
    # comment image
    
    p3 = (l1[0], p1[1])
    p4 = (l3[0], p1[1])
    
    p5 = (l1[0], p2[1])
    p6 = (l3[0], p2[1])
    
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1, p2])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=m2)
    drawLine(ax=ax, p1=p3, p2=p4)
    drawLine(ax=ax, p1=p5, p2=p6)

    AngleAnnotation(xy=l2, p1=l1, p2=p1, text=r"${s1}°$".format(s1=s1),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p1, p1=p4, p2=l2, text=r"${s1}°$".format(s1=s1),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p1, p1=p2, p2=p1, text=r"${n3}x-{n4}°$".format(n3=n3-1, n4=n4),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(80, 80), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")))
    AngleAnnotation(xy=p2, p1=p1, p2=p5, text=r"${n3}x-{n4}°$".format(n3=n3-1, n4=n4),
                    textposition="outside", ax=ax, size=30, text_kw=dict(xytext=(80, 80), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))) 
    AngleAnnotation(xy=p2, p1=p5, p2=m2, text=r"$x$",
                    textposition="outside", ax=ax, size=30) 
    AngleAnnotation(xy=m2, p1=m3, p2=p2, text=r"$x$",
                    textposition="outside", ax=ax, size=45)
    
    
    
    ax.text(1.08, -0.05, "l", size = 14)
    ax.text(1.05, -1.55, "m", size = 14)
    ax.text(1.08, p1[1], "n", size = 14)
    ax.text(1.08, p2[1], "p", size = 14)
    
    svg2 = saveSvg()
    
    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림과 같이 크기가 $$수식$${n1}\\angle x+{n2}DEG$$/수식$$, $$수식$${n3}\\angle x-{n4}DEG$$/수식$$인각의  " \
              "꼭짓점을 각각 지나고 두 직선 $$수식$$l, m$$/수식$$에 평행한 직선 " \
              "$$수식$$n, p$$/수식$$를 그으면 " \
              "$$수식$$\\angle x+{n5}DEG = {s1}DEG ``````THEREFORE \\angle x={result}DEG$$/수식$$"

    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, s1=s1, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg 



def figure121_Stem_133():
    stem = "다음 그림과 같이 평행한 두 직선 $$수식$$l, m$$/수식$$과 " \
            "정사각형 $$수식$$ABCD$$/수식$$가 각각 두 점 $$수식$$A, C$$/수식$$에서 " \
            "만날 때, $$수식$$\\angle x$$/수식$$의 크기를 구하시오. " \

    ag = random.randint(66,72)

    while True :
      n1 = random.randint(2,5)
      n2 = random.randint(2,7)
      if (ag-n2)%n1 == 0 :
        break

    l1 = (-1.9,0)
    l2 = (-0.25,-0.01)
    l3 = (0.7,0)

    m1 = (-1.9,-1.4)
    m2 = (-0.85,-1.4)
    m3 = (0.7,-1.4)

    p1 = (-1.2,-0.38)
    p2 = (0.1,-1.02)
    
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1, p2])
    fig, ax = plt.subplots(figsize=(5, 3))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=m2)
    drawLine(ax=ax, p1=m2, p2=p2)
    drawLine(ax=ax, p1=p2, p2=l2)
    
    x = [l2[0], p1[0], m2[0], p2[0], l2[0]]
    y = [l2[1], p1[1], m2[1], p2[1], l2[1]]
    #ax.fill_between(x, y, alpha=0.5,color = 'pink')
    drawPolygon(ax=ax, verts=[l2,p1,m2,p2], fill=False, alpha=1, dash=False, lw=1)

    AngleAnnotation(xy=l2, p1=p2, p2=l3, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=m2, p1=p1, p2=m1, text=r"${n1}x+{n2}°$".format(n1=n1, n2=n2),
                    textposition="outside", ax=ax, size=30)
    
    ax.text(0.78, -0.05, "l", size = 14)
    ax.text(0.75, -1.55, "m", size = 14)

    ax.text(-0.28,0.03, "A", size = 16)
    ax.text(-1.35,-0.4, "B", size = 16)
    ax.text(-0.9,-1.55, "C", size = 16)
    ax.text(0.14,-1.1, "D", size = 16)

    svg1 = saveSvg()
    
    result = int((ag-n2)/n1)
    
    # comment image
    p3 = (l1[0], p1[1])
    p4 = (l3[0], p1[1])
    p5 = (-0.13, p1[1])
    
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1, p2])
    fig, ax = plt.subplots(figsize=(5, 3))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l3)
    drawLine(ax=ax, p1=m1, p2=m3)
    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=m2)
    drawLine(ax=ax, p1=m2, p2=p2)
    drawLine(ax=ax, p1=p2, p2=l2)
    
    drawLine(ax=ax, p1=p3, p2=p4)

    x = [l2[0], p1[0], m2[0], p2[0], l2[0]]
    y = [l2[1], p1[1], m2[1], p2[1], l2[1]]
    drawPolygon(ax=ax, verts=[l2, p1, m2, p2],
                fill=False, alpha=1, dash=False, lw=1)

    AngleAnnotation(xy=l2, p1=p2, p2=l3, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p5, p1=l2, p2=p3, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=p1, p1=m2, p2=p4, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m2, p1=p1, p2=m1, text=r"${n1}x+{n2}°$".format(n1=n1, n2=n2),
                    textposition="outside", ax=ax, size=30)

    ax.text(0.78, -0.05, "l", size=14)
    ax.text(0.75, -1.55, "m", size=14)
    ax.text(0.78, p1[1], "n", size=14)

    ax.text(-0.28, 0.03, "A", size=16)
    ax.text(-1.35, -0.6, "B", size=16)
    ax.text(-0.9, -1.55, "C", size=16)
    ax.text(0.14, -1.1, "D", size=16)
    
    svg2 = saveSvg()

    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림과 같이 꼭짓점 $$수식$$B$$/수식$$를 지나고 " \
              "두 직선 $$수식$$l, m$$/수식$$에 평행한 직선 $$수식$$n$$/수식$$을 그으면 " \
              "$$수식$${n1}\\angle x+{n2}DEG ={ag}DEG$$/수식$$ " \
              "$$수식$$THEREFORE \\angle x={result}DEG$$/수식$$\n"

    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, ag=ag, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg 



def figure121_Stem_136():
    stem = "다음 그림에서 $$수식$$l//m$$/수식$$이고 $$수식$$\\angle ABC:\\angle CBE={n1}:{n2}$$/수식$$ " \
            "$$수식$$\\angle BAC:\\angle CAD={n3}:{n4}$$/수식$$일 때, " \
            "$$수식$$\\angle ACB$$/수식$$의 크기를\n구하시오." 

    list = [(2,1), (3,2), (3,1)]
    l = random.choice(list) 
    n1 = l[0]
    n2 = l[1]
    n3 = n1
    n4 = n2

    if n2 == 1 :
      nn2 = ""
    else :
      nn2 = n2

    if n4 == 1:
      nn4 = ""
    else :
      nn4 = n4

    l1 = (-0.4,0)
    l2 = (0,0)
    l3 = (2.1,0)
    l4 = (2.5,0)

    m1 = (-0.4,-1.5)
    m2 = (0.6,-1.5)
    m3 = (2.1,-1.5)
    m4 = (2.5,-1.5)

    p1 = (-0.15, -0.15*-1.5/0.6)
    p2 = (1.45,-0.9)
    p3 = (0.75, 0.75*-1.5/0.6)
    
    #ax = setChart(points=[l1, l2, l3, l4, m1, m2, m3, m4, p1, p2, p3])
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=m1, p2=m4)
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=l2, p2=p2)
    drawLine(ax=ax, p1=p2, p2=m2)

    x = [l3[0], m3[0]]
    y = [l3[1], m3[1]]

    ax.scatter(x, y, c='black', edgecolor='black', s=10)


    AngleAnnotation(xy=p2, p1=l2, p2=m2, text=r"",
                    textposition="outside", ax=ax, size=20)    
    
    ax.text(2.6, -0.05, "l", size = 12)
    ax.text(2.57, -1.55, "m", size = 12)

    ax.text(0,0.05, "A", size = 14)
    ax.text(0.4,-1.74, "B", size = 14)
    ax.text(1.47,-0.98, "C", size = 14)
    ax.text(2.02,0.09, "D", size = 14)
    ax.text(2.02,-1.79, "E", size = 14)
    
    s1 = n1+n2

    result = int(180/s1)
    
    svg1 = saveSvg()
    
    # comment image
    
    p4 = (l1[0], p2[1])
    p5 = (l4[0], p2[1])
    
    #ax = setChart(points=[l1, l2, l3, l4, m1, m2, m3, m4, p1, p2, p3])
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=m1, p2=m4)
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=l2, p2=p2)
    drawLine(ax=ax, p1=p2, p2=m2)
    drawLine(ax=ax, p1=p4, p2=p5)

    x = [l3[0], m3[0]]
    y = [l3[1], m3[1]]

    ax.scatter(x, y, c='black', edgecolor='black', s=10)


    AngleAnnotation(xy=l2, p1=p2, p2=l3, text=r"{nn2}a".format(nn2=nn2),
                    textposition="outside", ax=ax, size=45)
    AngleAnnotation(xy=l2, p1=m2, p2=p2, text=r"{n1}a".format(n1=n1),
                    textposition="outside", ax=ax, size=45)
    AngleAnnotation(xy=p2, p1=l2, p2=p4, text=r"{nn2}a".format(nn2=nn2),
                    textposition="outside", ax=ax, size=45)
    AngleAnnotation(xy=p2, p1=p4, p2=m2, text=r"{nn4}b".format(nn4=nn4),
                    textposition="outside", ax=ax, size=45)
    AngleAnnotation(xy=m2, p1=p2, p2=l2, text=r"{n3}b".format(n3=n3),
                    textposition="outside", ax=ax, size=45)
    AngleAnnotation(xy=m2, p1=m3, p2=p2, text=r"{nn4}b".format(nn4=nn4),
                    textposition="outside", ax=ax, size=45)
    
    ax.text(2.6, -0.05, "l", size = 12)
    ax.text(2.57, -1.55, "m", size = 12)
    ax.text(2.6, p2[1], "n", size=14)
    
    ax.text(0,0.05, "A", size = 14)
    ax.text(0.4,-1.74, "B", size = 14)
    ax.text(1.47,-0.9, "C", size = 14)
    ax.text(2.02,0.09, "D", size = 14)
    ax.text(2.02,-1.79, "E", size = 14)
        
    svg2 = saveSvg()
    
    

    answer = "(정답)\n$$수식$${result}DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림과 같이 점 $$수식$$C$$/수식$$를 지나고 두 직선 " \
              "$$수식$$l$$/수식$$, $$수식$$m$$/수식$$에 평행한 직선 $$수식$$n$$/수식$$을 긋는다. " \
              "$$수식$$\\angle DAC={nn2}a$$/수식$$, $$수식$$\\angle EBC={nn4}b$$/수식$$라 하면 " \
              "$$수식$$\\angle CAB = {n1}a,``\\angle CBA={n3}b$$/수식$$ " \
              "$$수식$$\\angle CAB = {s1}a+{s1}b=180 DEG$$/수식$$이므로 " \
              "$$수식$$a+b={result}DEG$$/수식$$ " \
              "$$수식$$THEREFORE \\angle ACB=a+b={result}DEG$$/수식$$\n"
    
    stem = stem.format(n1=n1, n2=n2, n3=n3, n4=n4)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, nn2=nn2, n3=n3, nn4=nn4, s1=s1, result=result)
    svg = [svg1, svg2]
    return stem, answer, comment, svg 



def figure121_Stem_143():
    stem = "다음 그림과 같이 직사각형 모양의 종이를 접었을 때, " \
            "$$수식$$\\angle x,``\\angle y$$/수식$$의 크기를 차례대로 구하시오.\n"

    ag = random.randint(120,130)

    l1 = (0,0)
    l2 = (0.85,-0.01)
    l3 = (1.7,0)
    l4 = (2.5,0)

    m1 = (0,-0.8)
    m2 = (1.1,-0.8)
    m3 = (2.5,-0.8)

    p1 = (0.7,0.6)
    p2 = (1.46,0.85)
    
    l1 = (l1[0]-1, l1[1]+1)
    l2 = (l2[0]-1, l2[1]+1)
    l3 = (l3[0]-1, l3[1]+1)
    l4 = (l4[0]-1, l4[1]+1)
    
    m1 = (m1[0]-1, m1[1]+1)
    m2 = (m2[0]-1, m2[1]+1)
    m3 = (m3[0]-1, m3[1]+1)
    
    p1 = (p1[0]-1, p1[1]+1)
    p2 = (p2[0]-1, p2[1]+1)

    
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1, p2])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l2)
    drawLine(ax=ax, p1=l2, p2=l4, dash=True)
    drawLine(ax=ax, p1=l4, p2=m3, dash=True)
    drawLine(ax=ax, p1=m3, p2=m2, dash=True)
    drawLine(ax=ax, p1=m2, p2=m1)
    drawLine(ax=ax, p1=m1, p2=l1)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=l3)
    drawLine(ax=ax, p1=l3, p2=m2)
    drawLine(ax=ax, p1=m2, p2=p1)
    
    x = [l1[0], m1[0], m2[0], l3[0]]
    y = [l1[1], m1[1], m2[1], l3[1]]
    plt.fill(x, y, alpha=0.3,color = 'coral')
    
    
    x2 = [p1[0], m2[0], l3[0], p2[0]]
    y2 = [p1[1], m2[1], l3[1], p2[1]]
    plt.fill(x2, y2, alpha=0.3,color = 'coral')

    AngleAnnotation(xy=l3, p1=m2, p2=l4, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=m2, p1=m3, p2=l3, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=l2, p1=m2, p2=l3, text=r"$y$",
                    textposition="outside", ax=ax, size=30)
    
    result1 = 180-ag
    result2 = 180 - result1 - result1
    
    svg1 = saveSvg()
    
    # comment image
    #ax = setChart(points=[l1, l2, l3, m1, m2, m3, p1, p2])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l2)
    drawLine(ax=ax, p1=l2, p2=l4, dash=True)
    drawLine(ax=ax, p1=l4, p2=m3, dash=True)
    drawLine(ax=ax, p1=m3, p2=m2, dash=True)
    drawLine(ax=ax, p1=m2, p2=m1)
    drawLine(ax=ax, p1=m1, p2=l1)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=l3)
    drawLine(ax=ax, p1=l3, p2=m2)
    drawLine(ax=ax, p1=m2, p2=p1)
    
    x = [l1[0], m1[0], m2[0], l3[0]]
    y = [l1[1], m1[1], m2[1], l3[1]]
    plt.fill(x, y, alpha=0.3,color = 'coral')
    
    
    x2 = [p1[0], m2[0], l3[0], p2[0]]
    y2 = [p1[1], m2[1], l3[1], p2[1]]
    plt.fill(x2, y2, alpha=0.3,color = 'coral')
    
    AngleAnnotation(xy=l3, p1=m2, p2=l4, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)    
    AngleAnnotation(xy=m2, p1=m3, p2=l3, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=l2, p1=m2, p2=l3, text=r"$y$",
                    textposition="outside", ax=ax, size=30)
    
    AngleAnnotation(xy=l3, p1=l2, p2=m2, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m2, p1=l2, p2=m1, text=r"$y$",
                    textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=m2, p1=l3, p2=l2, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    
    svg2 = saveSvg()

    answer = "(정답)\n $$수식$${result1} DEG$$/수식$$, $$수식$${result2} DEG$$/수식$$\n"
    comment = "(해설)\n다음 그림에서 " \
              "$$수식$$\\angle x=180 DEG - {ag}DEG = {result1}DEG$$/수식$$ " \
              "$$수식$$\\angle y+({result1}DEG + {result1}DEG ) = 180 DEG$$/수식$$ " \
              "에서 $$수식$$\\angle y={result2}DEG$$/수식$$\n" 

    answer = answer.format(result1=result1, result2=result2)
    comment = comment.format(ag=ag, result1=result1, result2=result2)
    svg = [svg1, svg2]
    return stem, answer, comment, svg 



def figure121_Stem_160():
    stem = "다음 중 삼각형의 세 변의 길이가 될 수 없는 것은?\n" \
            "① $$수식$${a1}$$/수식$$\n② $$수식$${a2}$$/수식$$\n③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$\n⑤ $$수식$${a5}$$/수식$$\n" 

    ans_list = [(2,2,3), (3,4,5), (6,6,6), (3,5,6), (2,4,5), (4,5,8), (5,6,10), (4,4,6), (4,6,9),]
    wr_list = [(5,5,10),(3,5,8),(2,3,5),(3,4,7),(4,6,10),(3,3,6),(2,4,6)]

    an_list = random.sample(ans_list,4)
    t1,t2,t3,t4 = an_list
    a = random.choice(wr_list)

    aa1 = str(t1[0])+"``rm {{cm}}, "+str(t1[1])+"``rm {{cm}}, "+str(t1[2])+"``rm {{cm}}"
    aa2 = str(t2[0])+"``rm {{cm}}, "+str(t2[1])+"``rm {{cm}}, "+str(t2[2])+"``rm {{cm}}"
    aa3 = str(t3[0])+"``rm {{cm}}, "+str(t3[1])+"``rm {{cm}}, "+str(t3[2])+"``rm {{cm}}"
    aa4 = str(t4[0])+"``rm {{cm}}, "+str(t4[1])+"``rm {{cm}}, "+str(t4[2])+"``rm {{cm}}"
    ans = str(a[0])+"``rm {{cm}}, "+str(a[1]) + \
        "``rm {{cm}}, "+str(a[2])+"``rm {{cm}}"

    a_list = [aa1, aa2, aa3, aa4, ans]
    a_list.sort()

    a1,a2,a3,a4,a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans :
        result = answer_dict[i]
        break 
    
    for i in range(0, len(a_list)):
      if a_list[i] == aa1 :
        aa1_idx = i
      elif a_list[i] == aa2 :
        aa2_idx = i
      elif a_list[i] == aa3 :
        aa3_idx = i
      elif a_list[i] == aa4 :
        aa4_idx = i
      elif a_list[i] == ans :
        ans_idx = i
    
    aa1_ex = str(t1[2])+"\\lt"+str(t1[0])+"+"+str(t1[1])
    aa2_ex = str(t2[2])+"\\lt"+str(t2[0])+"+"+str(t2[1])
    aa3_ex = str(t3[2])+"\\lt"+str(t3[0])+"+"+str(t3[1])
    aa4_ex = str(t4[2])+"\\lt"+str(t4[0])+"+"+str(t4[1])
    ans_ex = str(a[2])+"="+str(a[0])+"+"+str(a[1])

    a1_ex = (aa1_idx, aa1_ex)
    a2_ex = (aa2_idx, aa2_ex)
    a3_ex = (aa3_idx, aa3_ex)
    a4_ex = (aa4_idx, aa4_ex)
    an_ex = (ans_idx, ans_ex)

    ex_list = [a1_ex, a2_ex, a3_ex, a4_ex, an_ex]
    ex_list.sort()
    e1,e2,e3,e4,e5 = ex_list

    ex1 = e1[1]
    ex2 = e2[1]
    ex3 = e3[1]
    ex4 = e4[1]
    ex5 = e5[1]

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n①$$수식$${ex1}$$/수식$$    ② $$수식$${ex2}$$/수식$$    ③ $$수식$${ex3}$$/수식$$ " \
              "④ $$수식$${ex4}$$/수식$$    ⑤ $$수식$${ex5}$$/수식$$\n"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ex1=ex1, ex2=ex2, ex3=ex3, ex4=ex4, ex5=ex5)

    return stem, answer, comment


def figure121_Stem_161():
    stem = "삼각형의 세 변의 길이가 $$수식$${n1}``rm {{cm}}$$/수식$$, $$수식$${n2}``rm {{cm}}$$/수식$$, $$수식$$x``rm {{cm}}$$/수식$$일때,  " \
            "$$수식$$x$$/수식$$의 값이 될 수 있는 자연수의 개수를 구하시오.\n"
    while True :
      n1 = random.randint(7,13)
      n2 = random.randint(7,13)
      if n1 != n2 : 
        break
    
    s1 = n1+n2
    s2 = abs(n1-n2)

    start = s2+1
    end = s1-1

    result = end-start+1

    x1 = start
    x2 = x1+1
    x3 = x2+1
    x4 = end
    
    answer = "(정답)\n$$수식$${result}$$/수식$$개\n"
    comment = "(해설)\n(1) $$수식$$x``rm {{cm}}$$/수식$$가 가장 긴 변의 길이일 때 " \
              "$$수식$$\t x\\gt {n1}+{n2}$$/수식$$     $$수식$$THEREFORE x\\gt{s1}$$/수식$$ " \
              "(2) $$수식$${n2}``rm {{cm}}$$/수식$$가 가장 긴 변의 길이일 때 " \
              "$$수식$$\t {n2}\\gt{n1}+x$$/수식$$    $$수식$$THEREFORE x\\lt{s2}$$/수식$$ " \
              "(1),(2)에서 자연수 $$수식$$x$$/수식$$는 $$수식$${x1},{x2},{x3},\\cdot\\cdot\\cdot,{x4}$$/수식$$의 " \
              "$$수식$${result}$$/수식$$개이다.\n"

    stem = stem.format(n1=n1, n2=n2)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, s1=s1, s2=s2, x1=x1, x2=x2, x3=x3, x4=x4, result=result)

    return stem, answer, comment



def figure121_Stem_162():
    stem = "길이가 $$수식$${n1}``rm {{cm}},``{n2}``rm {{cm}},``{n3}``rm {{cm}},``{n4}``rm {{cm}}$$/수식$$인 막대가 각각 하나씩 있다. " \
            "이 중 $$수식$$3$$/수식$$개의 막대로 만들 수 있는 삼각형의 개수를 구하시오. " \
    
    n1 = random.randint(2,4)
    n2 = n1+1
    n3 = n2+1
    n4 = n3+1

    if n1 == 2:
      result = 3
    else :
      result = 4

    ex1 = str(n3)+"\\lt"+str(n1)+"+"+str(n2)
    if n1 == 2:
      ex2 = str(n4)+"="+str(n1)+"+"+str(n2)
    else :
      ex2 = str(n4)+"\\lt"+str(n1)+"+"+str(n2)
    ex3 = str(n4)+"\\lt"+str(n1)+"+"+str(n3)
    ex4 = str(n4)+"\\lt"+str(n2)+"+"+str(n3)

    if result == 3:
      s1 = "("+str(n1)+"``rm {{cm}}``, "+str(n2)+"``rm {{cm}}``, "+str(n3)+"``rm {{cm}})"
      s2 = "("+str(n1)+"``rm {{cm}}``, "+str(n3)+"``rm {{cm}}``, "+str(n4)+"``rm {{cm}})"
      s3 = "("+str(n2)+"``rm {{cm}}``, "+str(n3)+"``rm {{cm}}``, "+str(n4)+"``rm {{cm}})"
      s4 = ""
    else :
      s1 = "("+str(n1)+"``rm {{cm}}``, "+str(n2)+"``rm {{cm}}``, "+str(n3)+"``rm {{cm}})"
      s2 = "("+str(n1)+"``rm {{cm}}``, "+str(n2)+"``rm {{cm}}``, "+str(n4)+"``rm {{cm}})"
      s3 = "("+str(n1)+"``rm {{cm}}``, "+str(n3)+"``rm {{cm}}``, "+str(n4)+"``rm {{cm}}), "
      s4 = "("+str(n2)+"``rm {{cm}}``, "+str(n3)+"``rm {{cm}}``, "+str(n4)+"``rm {{cm}})"


    answer = "(정답)\n$$수식$${result}$$/수식$$개\n"
    comment = "(해설) $$수식$${ex1}, {ex2}, {ex3}, {ex4}$$/수식$$\n " \
              "이므로 만들 수 있는 삼각형의 세 변의 길이의 쌍은 " \
              "$$수식$${s1},{s2},$$/수식$$ " \
              "$$수식$${s3} {s4}$$/수식$$ " \
              "따라서 만들 수 있는 삼각형의 개수는 $$수식$${result}$$/수식$$이다.\n"

    stem = stem.format(n1=n1, n2=n2, n3=n3, n4=n4)
    answer = answer.format(result=result)
    comment = comment.format(ex1=ex1, ex2=ex2, ex3=ex3, ex4=ex4, s1=s1, s2=s2, s3=s3, s4=s4, result=result)

    return stem, answer, comment



def figure121_Stem_171():
    stem = "한 변의 길이가 $$수식$${n}``rm {{cm}}$$/수식$$이고 두 각의 크기가 $$수식$${ag1}DEG$$/수식$$, $$수식$${ag2}DEG$$/수식$$인 " \
            "삼각형의 개수를 구하시오.\n"   

    n = random.randint(5,9)

    ag_list = [50,55,60,65,70]
    
    while True :
      ag1 = random.choice(ag_list)
      ag2 = random.choice(ag_list)
      if ag1 != ag2 :
        break
    
    s1 = 180-ag1-ag2

    g_list = [s1,ag1,ag2]
    g_list.sort()
    g1,g2,g3 = g_list

    result = 3
    
    answer = "(정답)\n$$수식$${result}$$/수식$$개\n"
    comment = "(해설)\n나머지 한 각의 크기는 " \
              "$$수식$$180 DEG -({ag1}DEG + {ag2}DEG ) = {s1}DEG$$/수식$$ " \
              "즉, 한 변의 길이가 $$수식$${n}``rm {{cm}}$$/수식$$이고 " \
              "그 양 끝 각의 크기의 쌍은 " \
              "$$수식$$({g1}DEG ,{g2}DEG ), ({g1}DEG , {g3}DEG ), ({g2}DEG , {g3}DEG )$$/수식$$일 수 있다. " \
              "따라서 구하는 삼각형의 개수는 $$수식$${result}$$/수식$$개이다.\n"



    stem = stem.format(n=n, ag1=ag1, ag2=ag2)
    answer = answer.format(result=result)
    comment = comment.format(ag1=ag1, ag2=ag2, s1=s1, n=n, g1=g1, g2=g2, g3=g3, result=result)
    
    return stem, answer, comment



def figure121_Stem_173():
    stem = "아래 그림에서 $$수식$$\\triangle ABC \\equiv \\triangle PQR$$/수식$$일 때, 다음 중 " \
            "옳은 것을 모두 고르면? (정답 $$수식$$2$$/수식$$개)\n" \
            "① $$수식$$\\angle C={a1} DEG $$/수식$$       ② $$수식$$\\angle P={a2} DEG$$/수식$$        ③ $$수식$$\\angle Q={a3} DEG$$/수식$$\n" \
            "④ $$수식$${pq}={s1}``rm {{cm}}$$/수식$$       ⑤ $$수식$${pr}={s1}``rm {{cm}}$$/수식$$\n"
    answer = "(정답)\n{result1}, {result2}\n"
    comment = "(해설)\n① $$수식$$\\angle C=\\angle R={a1} DEG $$/수식$$\n" \
              "② $$수식$$\\angle P=180 DEG -({a1} DEG +60 DEG )={a4} DEG$$/수식$$\n" \
              "③ $$수식$$\\angle Q=\\angle B=60 DEG$$/수식$$\n" \
              "④ $$수식$${pq}$$/수식$$의 길이는 알 수 없다.\n" \
              "⑤ $$수식$${pr}={ac}={s1}``rm {{cm}}$$/수식$$\n"
              
    a1 = random.randint(40,50)
    a2 = a1 + 10
    a3 = a1 + 20
    a4 = 180 - (a1 + 60)
    
    s1 = random.randint(5, 15)
    
    pq = "\\overline{PQ}"
    pr = "\\overline{PR}"
    ac = "\\overline{AC}"

    result1 = answer_dict[0]
    result2 = answer_dict[4]

    a = (0.7,1.2)
    b = (0,0)
    c = (2.2,0)
    p = (4.6,1.2)
    q = (5.3,0)
    r = (3.1,0)
    
    resize = (-2,2)
    a = tuple(sum(elem) for elem in zip(a, resize))
    b = tuple(sum(elem) for elem in zip(b, resize))
    c = tuple(sum(elem) for elem in zip(c, resize))
    p = tuple(sum(elem) for elem in zip(p, resize))
    q = tuple(sum(elem) for elem in zip(q, resize))
    r = tuple(sum(elem) for elem in zip(r, resize))
    
    
          
    #ax = setChart(points=[a,b,c,p,q,r])
    fig, ax = plt.subplots(figsize=(5, 1.7))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=b, p2=c)
    drawLine(ax=ax, p1=c, p2=a)
    drawLine(ax=ax, p1=p, p2=q)
    drawLine(ax=ax, p1=q, p2=r)
    drawLine(ax=ax, p1=r, p2=p)


    pp1 = mpatches.PathPatch(
        Path([(0.7-2,1.2+2), (2.9/2+0.3-2, 1.1+2), (2.2-2,0+2)],
            [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
        fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)


    ax.text(0.6-2,1.25+2, "A", size = 14)
    ax.text(-0.3-2,-0.1+2, "B", size = 14)
    ax.text(2.23-2,-0.08+2, "C", size = 14)
    ax.text(4.5-2,1.25+2, "P", size = 14)
    ax.text(5.32-2,-0.08+2, "Q", size = 14)
    ax.text(2.83-2,-0.08+2, "R", size = 14)

    AngleAnnotation(xy=b, p1=c, p2=a, text=r"$60°$",
                textposition="outside", ax=ax, size=25)
    AngleAnnotation(xy=r, p1=q, p2=p, text=r"${a1}°$".format(a1=a1),
                textposition="outside", ax=ax, size=25)

    ax.text(2.9/2+0.1-2, 1+2, r"${s1}cm$".format(s1=s1), size = 13)


    stem = stem.format(pr=pr, pq=pq, a1=a1, a2=a2, a3=a3, s1=s1)
    answer = answer.format(result1=result1, result2=result2)
    comment = comment.format(pq=pq, pr=pr, ac=ac, a1=a1, a4=a4, s1=s1)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_175():
    stem = "다음 그림의 사각형 $$수식$$ABCD$$/수식$$와 사각형 $$수식$$EFGH$$/수식$$가 " \
            "서로 합동일 때, $$수식$$a+b$$/수식$$의 값을 구하시오. " \
            "(단, $$수식$${dc}$$/수식$$에 대응하는 변은 $$수식$${hg}이$$/수식$$다.)"

    dc = "\\overline{DC}"
    hg = "\\overline{HG}"
    he = "\\overline{HE}"
    da = "\\overline{DA}"

    n1 = random.randint(5,7)
    n2 = n1+2

    a = (0,2)
    b = (0,0)
    c = (1.3,0)
    d = (1.3,1.5)
    e = (2.5,0.25)
    f = (4.5,0.25)
    g = (4.5,1.6)
    h = (3,1.6)
    
    resize = (-2, 2)
    a = tuple(sum(elem) for elem in zip(a, resize))
    b = tuple(sum(elem) for elem in zip(b, resize))
    c = tuple(sum(elem) for elem in zip(c, resize))
    d = tuple(sum(elem) for elem in zip(d, resize))
    e = tuple(sum(elem) for elem in zip(e, resize))
    f = tuple(sum(elem) for elem in zip(f, resize))
    g = tuple(sum(elem) for elem in zip(g, resize))
    h = tuple(sum(elem) for elem in zip(h, resize))
          
    #ax = setChart(points=[a,b,c,d,e,f,g,h])
    
    fig, ax = plt.subplots(figsize=(5, 2))
    plt.axis("off")
    ax.autoscale()
      
    drawLine(ax=ax, p1=a, p2=d)
    drawLine(ax=ax, p1=d, p2=c)
    drawLine(ax=ax, p1=c, p2=b)
    drawLine(ax=ax, p1=b, p2=a)
    drawLine(ax=ax, p1=h, p2=g)
    drawLine(ax=ax, p1=g, p2=f)
    drawLine(ax=ax, p1=f, p2=e)
    drawLine(ax=ax, p1=e, p2=h)

    x = [-1.9,-1.9,-2]
    y = [2,2.1,2.1]

    ax.plot(x,y, c="black", linewidth = 0.5)

    x2 = [2.4,2.4,2.5]
    y2 = [3.6,3.5,3.5]

    ax.plot(x2,y2, c="black", linewidth = 0.5)

    pp1 = mpatches.PathPatch(
        Path([a, (-2.35, 3), b],
            [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
        fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
        Path([a, (1.3/2-1.8, 4.1), d],
            [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
        fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
        Path([h, ((3.1+2.5)/2-2.5, (0.25+1.6)/2+2.2), e],
            [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
        fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    ax.text(-2.15,4.05, "A", size = 14)
    ax.text(-2.25,1.8, "B", size = 14)
    ax.text(-0.68,1.8, "C", size = 14)
    ax.text(-0.68,3.4, "D", size = 14)
    ax.text(0.26,2.08, "E", size = 14)
    ax.text(2.55,2.08, "F", size = 14)
    ax.text(2.5,3.6, "G", size = 14)
    ax.text(0.75,3.62, "H", size = 14)

    AngleAnnotation(xy=a, p1=b, p2=d, text=r"70°",
                textposition="outside", ax=ax, size=30)
    AngleAnnotation(xy=f, p1=g, p2=e, text=r"$b°$",
                textposition="outside", ax=ax, size=25)

    ax.text(1.3/2-2, 4, "{n1}cm".format(n1=n1), size = 10)
    ax.text(-2.65, 3, "{n2}cm".format(n2=n2), size = 10)
    ax.text((3.1+2.5)/2-2.75, 1.65/2+2.2, "a cm", size = 10)

    result = 90+n1

    answer = "(정답)\n$$수식$${result}$$/수식$$\n"
    comment = "(해설)\n$$수식$${he}={da}={n1}``rm {{cm}}$$/수식$$이므로 $$수식$$a={n1}$$/수식$$ " \
              "$$수식$$\\angle F=\\angle B=90 DEG $$/수식$$이므로 $$수식$$b=90$$/수식$$ " \
              "$$수식$$THEREFORE a+b={result}$$/수식$$"

    stem = stem.format(dc=dc, hg=hg)
    answer = answer.format(result=result)
    comment = comment.format(he=he, da=da, n1=n1, n2=n2, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_193():
    stem = "그림과 같이 정사각형 $$수식$$ABCD$$/수식$$에서 $$수식$${bc}$$/수식$$의 연장선  " \
            "위에 점 $$수식$$F$$/수식$$를 잡아 정사각형 $$수식$$CFGE$$/수식$$를만들었다. " \
            "$$수식$${bc}={n1}``rm {{cm}}$$/수식$$, $$수식$${eg}={n2}``rm {{cm}}$$/수식$$, $$수식$${df}={n3}``rm {{cm}}$$/수식$$일 때,  " \
            "$$수식$${be}$$/수식$$의 길이는?\n" \
            "① $$수식$${a1}``rm {{cm}}$$/수식$$     ② $$수식$${a2}``rm {{cm}}$$/수식$$     ③ $$수식$${a3}``rm {{cm}}$$/수식$$\n" \
            "④ $$수식$${a4}``rm {{cm}}$$/수식$$     ⑤ $$수식$${a5}``rm {{cm}}$$/수식$$\n" 

    bc = "\\overline{BC}"
    dc = "\\overline{DC}"
    eg = "\\overline{EG}"
    df = "\\overline{DF}"
    be = "\\overline{BE}"
    ce = "\\overline{CE}"
    cf = "\\overline{CF}"

    n1 = random.randint(6,9)
    n2 = n1*2-1
    n3 = n2+2

    a = (0,0.85)
    d = (0.85,0.85)
    e = (0.85,1.65)
    g = (2.5,1.65)
    f = (2.5,0)
    c = (0.85,0)
    b = (0,0)

          
    #ax = setChart(points=[a,d,e,g,f,c,b])

    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
      
    drawLine(ax=ax, p1=a, p2=d)
    drawLine(ax=ax, p1=e, p2=c)
    drawLine(ax=ax, p1=e, p2=g)
    drawLine(ax=ax, p1=g, p2=f)
    drawLine(ax=ax, p1=d, p2=f)
    drawLine(ax=ax, p1=b, p2=f)
    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=e, p2=b)

    pp1 = mpatches.PathPatch(
        Path([(0, 0), (0.85/2, -0.3), (0.85, 0)],
            [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
        fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
        Path([(0.85, 1.65), ((0.85+2.5)/2, 2), (2.5,1.65)],
            [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
        fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
        Path([(0.85,0.85), ((0.85+2.5)/2+0.2, 1.65/2), (2.5,0)],
            [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
        fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)


    ax.text(-0.18,0.8, "A", size = 18)
    ax.text(0.66,0.87, "D", size = 18)
    ax.text(0.66,1.65, "E", size = 18)
    ax.text(2.52,1.65, "G", size = 18)
    ax.text(2.52,-0.1, "F", size = 18)
    ax.text(0.8,-0.2, "C", size = 18)
    ax.text(-0.18,-0.1, "B", size = 18)

    ax.text(0.85/2-0.18, -0.28, "{n1}cm".format(n1=n1), size = 13)
    ax.text((0.85+2.5)/2-0.17, 1.86, "{n2}cm".format(n2=n2), size = 13)
    ax.text((0.85+2.5)/2+0.1, 1.65/2-0.2, "{n3}cm".format(n3=n3), size = 13)

    ans = n3

    aa_list = [ans-3, ans-2, ans-1, ans, ans+1, ans+2, ans+3]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break


    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$$\\triangle BCE$$/수식$$와 $$수식$$\\triangle DCF$$/수식$$에서 " \
              "$$수식$${bc}={dc}$$/수식$$, $$수식$${ce}={cf},$$/수식$$ " \
              "$$수식$$\\angle BCE=\\angle DCF=90 DEG $$/수식$$ " \
              "따라서 $$수식$$\\triangle BCE \\equiv \\triangle DCF$$/수식$$($$수식$$SAS$$/수식$$ 합동)이므로 " \
              "$$수식$${be}={df}={ans}(rm {{cm}})$$/수식$$\n"

    stem = stem.format(bc=bc, eg=eg, df=df, be=be, n1=n1, n2=n2, n3=n3, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(bc=bc, dc=dc, ce=ce, cf=cf, be=be, df=df, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def figure121_Stem_196():
    stem = "다음 그림과 같은 정사각형 $$수식$$ABCD$$/수식$$에서 " \
            "$$수식$${ap}={cq}$$/수식$$일 때, $$수식$$\\angle PBQ$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$        ② $$수식$${a2}DEG $$/수식$$        ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$        ⑤ $$수식$${a5}DEG $$/수식$$\n"

    ap = "\\overline{AP}"
    cq = "\\overline{CQ}"
    ab = "\\overline{AB}"
    cb = "\\overline{CB}"
    bp = "\\overline{BP}"
    bq = "\\overline{BQ}"

    ag = random.randint(70,78)

    a = (0,1.85)
    p = (1,1.85)
    d = (1.85,1.85)
    b = (0,0)
    c = (1.85,0)
    q = (1.85,1)

    p1 = (0.487,1.88)
    p2 = (0.513,1.88)
    p3 = (0.487,1.82)
    p4 = (0.513,1.82)

    p5 = (1.82,0.513)
    p6 = (1.82,0.487)
    p7 = (1.88,0.513)
    p8 = (1.88,0.487)
          
    #ax = setChart(points=[a,p,d,b,c,q,p1,p2,p3,p4,p5,p6,p7,p8])
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

      
    drawLine(ax=ax, p1=a, p2=d)
    drawLine(ax=ax, p1=d, p2=c)
    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=b, p2=c)

    drawLine(ax=ax, p1=b, p2=p)
    drawLine(ax=ax, p1=p, p2=q)
    drawLine(ax=ax, p1=q, p2=b)

    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p2, p2=p4)

    drawLine(ax=ax, p1=p5, p2=p7)
    drawLine(ax=ax, p1=p6, p2=p8)

    AngleAnnotation(xy=b, p1=q, p2=p, text=r"",
                textposition="outside", ax=ax, size=40)
    AngleAnnotation(xy=p, p1=b, p2=q, text=r"${ag}°$".format(ag=ag),
                textposition="outside", ax=ax, size=40) 

    ax.text(-0.13,1.8, "A", size = 18)
    ax.text(0.95,1.88, "P", size = 18)
    ax.text(1.88,1.8, "D", size = 18)
    ax.text(1.88,0.95, "Q", size = 18)
    ax.text(1.88,-0.03, "C", size = 18)
    ax.text(-0.13,-0.03, "B", size = 18)

    ans = 180-ag-ag

    aa_list = [ans-6, ans-4, ans-2, ans, ans+2, ans+4, ans+6]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    answer = "(정답)\n{result}\n"
    comment = "(해설)\n$$수식$$\\triangle ABP$$/수식$$와 $$수식$$\\triangle CBQ$$/수식$$에서 " \
              "$$수식$${ap}={cq}, {ab}={cb},$$/수식$$ " \
              "$$수식$$\\angle BAP=\\angle BCQ=90 DEG $$/수식$$ " \
              "따라서 $$수식$$\\triangle ABP \\equiv \\triangle CBQ$$/수식$$($$수식$$SAS$$/수식$$ 합동)이므로 " \
              "$$수식$${bp}={bq}$$/수식$$ " \
              "즉, $$수식$$\\triangle BQP$$/수식$$가 $$수식$${bp}={bq}$$/수식$$인 이등변삼각형이므로 " \
              "$$수식$$\\angle PBQ=180 DEG -({ag}DEG +{ag}DEG )={ans}DEG $$/수식$$\n"

    stem = stem.format(ap=ap, cq=cq, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ap=ap, cq=cq, ab=ab, cb=cb, bp=bp, bq=bq, ag=ag, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 
