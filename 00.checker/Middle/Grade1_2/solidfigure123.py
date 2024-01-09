#from  draw2svg import *
import matplotlib.pyplot as plt
import numpy as np
import random
import fractions
import math
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
                    return np.sqrt((r+w/2)**2 + (np.tan(a)*(r+w/2))**2)
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
        plt.text(point[0]+0.7, point[1]-0.7, text, fontsize=16, zorder=3)
    elif position == 4:
        plt.text(point[0]-0.7, point[1], text, fontsize=16, zorder=3)
    elif position == 5:
        plt.text(point[0], point[1], text, fontsize=16, zorder=3)
    elif position == 6:
        plt.text(point[0]+0.7, point[1], text, fontsize=16, zorder=3)
    elif position == 7:
        plt.text(point[0]-0.7, point[1]+0.7, text, fontsize=16, zorder=3)
    elif position == 8:
        plt.text(point[0], point[1]+0.7, text, fontsize=16, zorder=3)
    elif position == 9:
        plt.text(point[0]+0.7, point[1]+0.7, text, fontsize=16, zorder=3)

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

    ax.set_xlim(minlim-0.15*maxlim, maxlim+0.15*maxlim)
    ax.set_ylim(minlim-0.15*maxlim, maxlim+0.15*maxlim)

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



def solidfigure123_Stem_007():
    stem = "꼭짓점의 개수가 $$수식$${n}$$/수식$$인 각기둥의 면의 개수를 $$수식$$x$$/수식$$ " \
            "모서리의 개수를 $$수식$$y$$/수식$$라 할 때, $$수식$$x+y$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 주어진 각기둥을 $$수식$$n$$/수식$$각기둥이라 하면\n" \
              "꼭짓점의 개수가 $$수식$${n}$$/수식$$이므로\n" \
              "$$수식$$2n={n}$$/수식$$  $$수식$$THEREFORE n={s1}$$/수식$$\n" \
              "즉, 주어진 각기둥은 {s}이다.\n" \
              "{s}의 면의 개수는 $$수식$${s1}+2={s2}$$/수식$$(개)이므로\n" \
              "$$수식$$x={s2}$$/수식$$\n" \
              "{s}의 모서리의 개수는 $$수식$${s1}\\times3={s3}$$/수식$$(개)이므\n" \
              "로 $$수식$$y={s3}$$/수식$$\n" \
              "$$수식$$THEREFORE x+y={ans}$$/수식$$\n"

    s1 = random.randint(5,10)
    if s1 == 5 :
      s = "오각기둥"
    elif s1 == 6 :
      s = "육각기둥"
    elif s1 == 7 :
      s = "칠각기둥"
    elif s1 == 8 :
      s = "팔각기둥"
    elif s1 == 9 :
      s = "구각기둥"
    elif s1 == 10 :
      s = "십각기둥"
    
    n = s1*2
    s2 = s1+2
    s3 = s1*3
    ans = s2+s3

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

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, s=s, s1=s1, s2=s2, s3=s3, ans=ans)

    return stem, answer, comment



def solidfigure123_Stem_008():
    stem = "밑면의 대각선의 개수가 $$수식$${n}$$/수식$$이 각뿔대는 몇 면체인가?\n" \
            "① {a1}   ② {a2}   ③ {a3}\n" \
            "④ {a4}   ⑤ {a5}\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 주어진 각뿔대를 $$수식$$n$$/수식$$각뿔대라 하며 밑면은 $$수식$$n$$/수식$$각형이므로\n" \
              "$$수식$${f}={n}$$/수식$$, $$수식$$n(n-3)={s1}={s2}\\times{s3}$$/수식$$\n" \
              "$$수식$$THEREFORE n={s4}$$/수식$$\n" \
              "따라서 {sf}의 면의 개수는 $$수식$${s4}+2={s5}$$/수식$$이므로 {sf2}이다.\n" \


    s4 = random.randint(5,10)
    if s4 == 5 :
      sf = "오각뿔대"
    elif s4 == 6 :
      sf = "육각뿔대"
    elif s4 == 7 :
      sf = "칠각뿔대"
    elif s4 == 8 :
      sf = "팔각뿔대"
    elif s4 == 9 :
      sf = "구각뿔대"
    elif s4 == 10 :
      sf = "십각뿔대"
    
    s3 = s4-3
    s2 = s4
    s1 = s2*s3
    n = int(s1/2)
    s5 = s4+2

    if s5 == 7 :
      sf2 = "칠면체"
    elif s5 == 8 :
      sf2 = "팔면체"
    elif s5 == 9 :
      sf2 = "구면체"
    elif s5 == 10 :
      sf2 = "십면체"
    elif s5 == 11 :
      sf2 = "십일면체"
    elif s5 == 12 :
      sf2 = "십이면체"
    
    ans = sf2

    s_list = ["오면체","육면체","칠면체","팔면체","구면체","십면체","십일면체","십이면체"]
    
    if s5<9 :
      idx = random.randint(0,1)
    elif s5>=9 and s5<12 :
      idx = random.randint(2,3)  
    elif s5 == 12 :
      idx = 3

    a_list = []
    
    for i in range(5):
      a_list.append(s_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    f = "\\frac{n(n-3)}{2}"
    

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, f=f, sf=sf, sf2=sf2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, ans=ans)

    return stem, answer, comment



def solidfigure123_Stem_009():
    stem = "{sf}을 밑면에 평행한 평면으로 자를 때 생기는 두 입체도형의 꼭짓점의 개수의 차는?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n{sf}을 밑면에 평행한 면으로 자를 때 생기는\n" \
              "두 입체도형은 {sf}와 {sf}대이다.\n" \
              "{sf}의 꼭짓점의 개수는 $$수식$${n}+1={s1},$$/수식$$\n" \
              "{sf}대의 꼭짓점의 개수는 $$수식$${n}\\times 2={s2}$$/수식$$\n" \
              "따라서 두 입체도형의 꼭짓점의 개수의 차는 $$수식$${s2}-{s1}={ans}$$/수식$$\n" \
    
    n = random.randint(7,10)

    if n == 7 :
      sf = "칠각뿔"
    elif n == 8 :
      sf = "팔각뿔"
    elif n == 9 :
      sf = "구각뿔"
    elif n == 10 :
      sf = "십각뿔"
    
    s1 = n+1
    s2 = n*2

    ans = s2-s1

    aa_list = [ans-6, ans-4, ans-2, ans, ans+2, ans+4, ans+6]
    a_list = []

    if n == 7 :
        idx = random.randint(1,2)
    else :
        idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break
    

    stem = stem.format(sf=sf, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(sf=sf, n=n, s1=s1, s2=s2, ans=ans)

    return stem, answer, comment



def solidfigure123_Stem_010():
    stem = "{sf}인 각기둥, 각뿔, 각뿔대의 꼭짓점의 개수의 합은?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n {sf}인 각기둥을 $$수식$$a$$/수식$$각기둥이라 하면\n" \
              "$$수식$$a+2={n}$$/수식$$ $$수식$$THEREFORE a={s1}$$/수식$$\n" \
              "{sf2}의 꼭짓점의 개수는 $$수식$${s1}\\times 2={s2}$$/수식$$\n" \
              "{sf}인 각뿔을 $$수식$$b$$/수식$$각뿔이라 하면\n" \
              "$$수식$$b+1={n}$$/수식$$ $$수식$$THEREFORE b={s3}$$/수식$$\n" \
              "{sf3}의 꼭짓점의 개수는 $$수식$${s3}+1={s4}$$/수식$$\n" \
              "{sf}인 각뿔대를 $$수식$$c$$/수식$$각뿔대라 하면\n" \
              "$$수식$$c+2={n}$$/수식$$ $$수식$$THEREFORE c={s5}$$/수식$$\n" \
              "{sf4}의 꼭짓점의 개수는 $$수식$${s5}\\times 2={s6}$$/수식$$\n" \
              "따라서 구하는 합은\n" \
              "$$수식$${s2}+{s4}+{s6}={ans}$$/수식$$\n"

    n = random.randint(6,10)
    s1 = n-2
    s2 = s1*2
    s3 = n-1
    s4 = s3+1
    s5 = n-2
    s6 = s5*2
    ans = s2+s4+s6

    if n == 6 :
      sf = "육면체"
      sf2 = "사각기둥"
      sf3 = "오각뿔"
      sf4 = "사각뿔대"
    elif n == 7 :
      sf = "칠면체"
      sf2 = "오각기둥"
      sf3 = "육각뿔"
      sf4 = "오각뿔대"
    elif n == 8 :
      sf = "팔면체"
      sf2 = "육각기둥"
      sf3 = "칠각뿔"
      sf4 = "육각뿔대"
    elif n == 9 :
      sf = "구면체"
      sf2 = "칠각기둥"
      sf3 = "팔각뿔"
      sf4 = "칠각뿔대"
    elif n == 10 :
      sf = "십면체"
      sf2 = "팔각기둥"
      sf3 = "구각뿔"
      sf4 = "팔각뿔대"

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
      

    stem = stem.format(sf=sf, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(sf=sf, sf2=sf2, sf3=sf3, sf4=sf4, n=n, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, ans=ans)

    return stem, answer, comment



def solidfigure123_Stem_011():
    stem = "다음 그림과 같은 입체도형의 이름과 옆면의 모양을 짝지은 것으로 옳은 것은?\n" \
            "① {a1}\n" \
            "② {a2}\n" \
            "③ {a3}\n" \
            "④ {a4}\n" \
            "⑤ {a5}\n" 
    answer = "(정답)\n{result}"
    comment = ""

    n = random.randint(4,6)
    
    fig, ax = plt.subplots(figsize=(3.5, 3.5))
    plt.axis("off")
    ax.autoscale()

    if n == 4 :
        g1 = (0.95,2.2)
        g2 = (0.5,1.8)
        g3 = (1.4,1.8)
        g4 = (1.85,2.2)

        g5 = (0.75,0.7)
        g6 = (0,0)
        g7 = (1.5,0)
        g8 = (2.25,0.7)

        #ax = setChart(points=[g5,g6,g7,g8])

        drawPolygon(ax=ax, verts=[g1,g2,g3,g4])

        drawLine(ax=ax, p1=g1, p2=g5, dash=True)
        drawLine(ax=ax, p1=g2, p2=g6)
        drawLine(ax=ax, p1=g3, p2=g7)
        drawLine(ax=ax, p1=g4, p2=g8)

        drawLine(ax=ax, p1=g5, p2=g6, dash=True)
        drawLine(ax=ax, p1=g6, p2=g7)
        drawLine(ax=ax, p1=g7, p2=g8)
        drawLine(ax=ax, p1=g8, p2=g5, dash=True)

        a1 = "사각기둥 - 삼각형"
        a2 = "사각기둥 - 사다리꼴"
        a3 = "사각뿔 - 삼각형"
        a4 = "사각뿔대 - 사다리꼴"
        a5 = "사각뿔대 - 직사각형"
    elif n == 5 :
        d1 = (0.8,1.4)
        d2 = (0.25,1.2)
        d3 = (0.5,0.9)
        d4 = (1.1,0.9)
        d5 = (1.35,1.2)

        d6 = (0.8,0.3)
        d7 = (0,0)
        d8 = (0.3,-0.4)
        d9 = (1.3,-0.4)
        d10 = (1.6,0)

        #ax = setChart(points=[d6,d7,d8,d9,d10])

        drawPolygon(ax=ax, verts=[d1,d2,d3,d4,d5])

        drawLine(ax=ax, p1=d1, p2=d6, dash=True)
        drawLine(ax=ax, p1=d2, p2=d7)
        drawLine(ax=ax, p1=d3, p2=d8)
        drawLine(ax=ax, p1=d4, p2=d9)
        drawLine(ax=ax, p1=d5, p2=d10)

        drawLine(ax=ax, p1=d6, p2=d7, dash=True)
        drawLine(ax=ax, p1=d7, p2=d8)
        drawLine(ax=ax, p1=d8, p2=d9)
        drawLine(ax=ax, p1=d9, p2=d10)
        drawLine(ax=ax, p1=d10, p2=d6, dash=True)
        
        a1 = "오각기둥 - 삼각형"
        a2 = "오각기둥 - 사다리꼴"
        a3 = "오각뿔 - 삼각형"
        a4 = "오각뿔대 - 사다리꼴"
        a5 = "오각뿔대 - 직사각형"
    elif n == 6 :
        p1 = (0.7,1.45)
        p2 = (0.4,1.3)
        p3 = (0.7,1.15)
        p4 = (1.1,1.15)
        p5 = (1.4,1.3)
        p6 = (1.1,1.45)

        p7 = (0.48,0.3)
        p8 = (0,0)
        p9 = (0.5,-0.3)
        p10 = (1.3,-0.3)
        p11 = (1.8,0)
        p12 = (1.32,0.3)
        
        #ax = setChart(points=[p7, p8, p9, p10, p11, p12])
        
        drawPolygon(ax=ax, verts=[p1,p2,p3,p4,p5,p6])

        drawLine(ax=ax, p1=p1, p2=p7, dash=True)
        drawLine(ax=ax, p1=p2, p2=p8)
        drawLine(ax=ax, p1=p3, p2=p9)
        drawLine(ax=ax, p1=p4, p2=p10)
        drawLine(ax=ax, p1=p5, p2=p11)
        drawLine(ax=ax, p1=p6, p2=p12, dash=True)

        drawLine(ax=ax, p1=p7, p2=p8, dash=True)
        drawLine(ax=ax, p1=p8, p2=p9)
        drawLine(ax=ax, p1=p9, p2=p10)
        drawLine(ax=ax, p1=p10, p2=p11)
        drawLine(ax=ax, p1=p11, p2=p12, dash=True)
        drawLine(ax=ax, p1=p12, p2=p7, dash=True)
        
        a1 = "육각기둥 - 삼각형"
        a2 = "육각기둥 - 사다리꼴"
        a3 = "육각뿔 - 삼각형"
        a4 = "육각뿔대 - 사다리꼴"
        a5 = "육각뿔대 - 직사각형"
        
    ax.autoscale()

    svg = saveSvg()
    
    result = answer_dict[3]
    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    return stem, answer, comment, svg  



def solidfigure123_Stem_041():
    stem = "다음 그림과 같은 사다리꼴을 직선 $$수식$$l$$/수식$$을 회전축으로 하여 $$수식$$1$$/수식$$회 전시킬 때 생기는 입체도형을 회전축을 포함하는 평면으로 잘랐다. 이때 생기는 단면의 넓이는?\n" \
            "① $$수식$${a1}rm cm^2$$/수식$$   ② $$수식$${a2}rm cm^2$$/수식$$   ③ $$수식$${a3}rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}rm cm^2$$/수식$$   ⑤ $$수식$${a5}rm cm^2$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 회전체는 다음 그림과 같으므로 구하는 단면의 넓이는\n" \
              "$$수식$$\\left[{f}\\times({n1}+{n2})\\times{n3}\\right]\\times 2$$/수식$$\n" \
              "$$수식$$={ans}(rm cm^2)$$/수식$$"

    while True :
      n3 = random.randint(4,9)
      n2 = n3+1
      n1 = int(n3/2)
      if n3%2 == 0 :
        break

    l1 = (0,2)
    l2 = (0,0)
    l3 = (0,-4)
    l4 = (0,-5.5)
    l5 = (0,-6.5)
    p1 = (-2,0)
    p2 = (-5,-4)
    p3 = (4,-2)
    p4 = (2,0)
    p5 = (5,-4)

    #ax = setChart(points=[l1,l2,l3,l4,p1,p2,p3])
    fig, ax = plt.subplots(figsize=(3.5, 3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=l3)

    x = [0,-2,-5,0,0]
    y = [0,0,-4,-4,0]

    ax.fill(x, y, color="skyblue",alpha = 0.5)

    x2 = [-0.3,-0.3,0]
    y2 = [0,-0.3,-0.3]

    ax.plot(x2,y2, c="black", linewidth = 0.5)

    x3 = [0,-0.3,-0.3]
    y3 = [-3.7,-3.7,-4]

    ax.plot(x3,y3, c="black", linewidth = 0.5)

    pp = mpatches.PathPatch(
    Path([(0,0), (-1,0.8), (-2,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp)

    pp2 = mpatches.PathPatch(
    Path([(-2,0), (-4.5,-1), (-5,-4)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([(-5,-4), (-2.5,-5.2), (0,-4)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp3)

    pp4 = mpatches.PathPatch(
    Path([(0,0), (1,-2), (0,-4)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp4)

    ax.text(-1.5,0.55, '${n1}$cm'.format(n1=n1), size = 12)
    ax.text(-5.2,-1.5, '${n2}$cm'.format(n2=n2), size = 12)
    ax.text(-3,-5.1, '${n2}$cm'.format(n2=n2), size = 12)
    ax.text(0.6,-2, '${n3}$cm'.format(n3=n3), size = 12)
    ax.text(-0.28,0.8, '$\circlearrowleft$', size = 16)
    ax.text(-0.1,2.3, '$l$', size = 12)
    
    ax.set_xlim(-5,5)

    svg1 = saveSvg()

    #ax2 = setChart(points=[l1,l2,l3,l4,p1,p2,p3,p4,p5])
    fig, ax2 = plt.subplots(figsize=(3.5, 3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax2, p1=l1, p2=l5)
    drawLine(ax=ax2, p1=p4, p2=p1)
    drawLine(ax=ax2, p1=p1, p2=p2)
    drawLine(ax=ax2, p1=p2, p2=p5)
    drawLine(ax=ax2, p1=p4, p2=p5)
    drawEllipse(ax=ax2, center=(0,0), width=4, height=1)
    drawEllipse(ax=ax2, center=(0,-4), width=10, height=2.4, position="bottom")
    drawEllipse(ax=ax2, center=(0,-4), width=10, height=2.4, position="top", dash=True)

    x4 = [0.5,0.5,0]
    y4 = [0,-0.5,-0.5]

    ax2.plot(x4,y4, c="black", linewidth = 0.5)

    x5 = [0,0.5,0.5]
    y5 = [-3.5,-3.5,-4]

    ax2.plot(x5,y5, c="black", linewidth = 0.5)

    pp = mpatches.PathPatch(
    Path([(0,0), (1,0.5), (2,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp)

    pp2 = mpatches.PathPatch(
    Path([(-2,0), (-4.5,-1), (-5,-4)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([(5,-4), (2.5,-5), (0,-4)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp3)

    pp4 = mpatches.PathPatch(
    Path([(0,0), (1,-2), (0,-4)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp4)

    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (4,-5.7), xy = (2.5,-4.4),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })

    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (2.6,1), xy = (1,0.2),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })

    ax2.text(2.6,0.8, '${n1}$cm'.format(n1=n1), size = 12)
    ax2.text(-5.6,-1.5, '${n2}$cm'.format(n2=n2), size = 12)
    ax2.text(4,-5.9, '${n2}$cm'.format(n2=n2), size = 12)
    ax2.text(0.6,-2, '${n3}$cm'.format(n3=n3), size = 12)
    ax2.text(-0.28,0.8, '$\circlearrowleft$', size = 16)
    ax2.text(-0.1,2.3, '$l$', size = 12)
    
    ax2.set_xlim(-5,10)

    svg2 = saveSvg()

    ans = (n1+n2)*n3
    f = "\\frac{1}{2}"

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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, n1=n1, n2=n2, n3=n3, ans=ans)
    svg = [svg1,svg2]
    return stem, answer, comment, svg



def solidfigure123_Stem_045():
    stem = "다음 그림과 같이 지름의 길이가 $$수식$${n}``rm cm$$/수식$$인 반원을 직선 $$수식$$l$$/수식$$을 회전축으로 하여 $$수식$$1$$/수식$$회전시킬 때 생기는 회전체를한 평면으로 자르려고 한다. 단면 의넓이가 최대가 되도록 자를 때, 이 단면의 넓이는?\n" \
            "① $$수식$${a1}\\pi``rm cm^2$$/수식$$  ② $$수식$${a2}\\pi``rm cm^2$$/수식$$   ③ $$수식$${a3}\\pi``rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm cm^2$$/수식$$  ⑤ $$수식$${a5}\\pi``rm cm^2$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 만들어지는 회전체는 구이고, 구는 어느 방향으로\n" \
              "잘라도 그 단면이 항상 원이므로 단면의 넓이가\n" \
              "최대가 되려면 구의 중심을 지나는 평면으로 잘라야 한다.\n" \
              "따라서 구하는 단면의 넓이는\n" \
              "$$수식$$\\pi\\times{r}^2={ans}\\pi(rm cm^2)$$/수식$$"

    while True :
      n = random.randint(6,16)
      if n%2 == 0 :
        break

    l1 = (0,2)
    l2 = (0,0)
    l3 = (0,-3)
    l4 = (0,-6)
    l5 = (0,-7.5)
    p1 = (-3,-3)
    p2 = (3,-3)

    #x = setChart(points=[l1,l2,l3,l4,l5,p1,p2])
    fig, ax = plt.subplots(figsize=(3.5, 3.5))
    plt.axis("off")
    ax.autoscale()
    ax.set_xlim(-3.5,6)

    drawLine(ax=ax, p1=l1, p2=l5)

    pp = mpatches.Wedge(l3, r=3, theta1=90,
                                theta2=270, fc='purple', fill=True, alpha=0.3)
    ax.add_patch(pp)

    pp2 = mpatches.Wedge(l3, r=3, theta1=90,
                                theta2=270, ec='black', fill=False, alpha=1)
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([(0,0), (2,-3), (0,-6)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp3)

    ax.text(1.2,-3, '${n}$cm'.format(n=n), size = 13)
    ax.text(-0.28,0.8, '$\circlearrowleft$', size = 16)
    ax.text(-0.1,2.3, '$l$', size = 14)

    r = int(n/2)
    ans = r*r

    aa_list = [(r-3)*(r-3), (r-2)*(r-2), (r-1)*(r-1), ans, (r+1)*(r+1), (r+2)*(r+2), (r+3)*(r+3)]
    a_list = []
    if r == 3 : 
      idx = 2
    elif r == 4 :
      idx = random.randint(1,2)
    else :
      idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break


    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, r=r, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def solidfigure123_Stem_047():
    stem = "다음 그림과 같은 도형을 직선 $$수식$$l$$/수식$$을 회전축으로 하여 $$수식$$1$$/수식$$회전 시킬 때 생기는 회전체를 회전축을 포함하는 평면으로 잘랐다. 이때 생기는 단면의 넓이는?\n" \
            "① $$수식$${a1}\\pi``rm cm^2$$/수식$$  ② $$수식$${a2}\\pi``rm cm^2$$/수식$$   ③ $$수식$${a3}\\pi``rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm cm^2$$/수식$$  ⑤ $$수식$${a5}\\pi``rm cm^2$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 회전체는 다음 그림과 같으므로 단면의 넓이는\n" \
              "$$수식$$\\left(\\pi \\times {r1}^2 \\times {f}+\\pi \\times {r2}^2 \\times {f}\\right)$$/수식$$\n" \
              "$$수식$$\\times 2 = {ans}\\pi(rm cm^2)$$/수식$$\n"
    
    while True :
      r1 = random.randint(2,6)
      if r1 % 2 == 0 :
        break
    r2 = r1*3
    r3 = r1*2

    l1 = (0,2)
    l2 = (0,0)
    l3 = (0,-3)
    l4 = (0,-9)
    l5 = (0,-10.5)
    p1 = (-6,-6)
    p2 = (6,-6)
    p3 = (-6,-3)

    #ax = setChart(points=[l1,l2,l3,l4,l5,p1,p2])
    fig, ax = plt.subplots(figsize=(4.5, 3.5))
    plt.axis("off")
    ax.autoscale()
    ax.set_xlim(-6.5,12)
    drawLine(ax=ax, p1=l1, p2=l5)

    pp = mpatches.Wedge(l3, r=6, theta1=180,
                                theta2=270, fc='yellowgreen', fill=True, alpha=0.4)
    ax.add_patch(pp)

    pp2 = mpatches.Wedge(l3, r=6, theta1=180,
                                theta2=270, ec='black', fill=False, alpha=1)
    ax.add_patch(pp2)

    pp3 = mpatches.Wedge(l3, r=2, theta1=90,
                                theta2=180, fc='yellowgreen', fill=True, alpha=0.4)
    ax.add_patch(pp3)

    pp4 = mpatches.Wedge(l3, r=2, theta1=90,
                                theta2=180, ec='black', fill=False, alpha=1)
    ax.add_patch(pp4)

    x2 = [-0.5,-0.5,0]
    y2 = [-3,-2.5,-2.5]
    ax.plot(x2,y2, c="black", linewidth = 0.3)

    pp5 = mpatches.PathPatch(
    Path([(0,-1), (1,-2), (0,-3)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp5)

    pp6 = mpatches.PathPatch(
    Path([(0,-3), (-1,-4), (-2,-3)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp6)

    pp7 = mpatches.PathPatch(
    Path([(-2,-3), (-4,-1.5), (-6,-3)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp7)

    pp8 = mpatches.PathPatch(
    Path([(0,-3), (2,-6), (0,-9)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp8)

    ax.text(0.6,-2.2, '${r1}$cm'.format(r1=r1), size = 12)
    ax.text(-2,-4.2, '${r1}$cm'.format(r1=r1), size = 12)
    ax.text(1.2,-6, '${r2}$cm'.format(r2=r2), size = 12)
    ax.text(-4.9,-1.9, '${r3}$cm'.format(r3=r3), size = 12)
    ax.text(-0.4,0.4, '$\circlearrowleft$', size = 16)
    ax.text(-0.1,2.3, '$l$', size = 14)

    svg1 = saveSvg()

    #ax2 = setChart(points=[l1,l2,l3,l4,l5,p1,p2])
    fig, ax2 = plt.subplots(figsize=(4.5, 3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax2, p1=l1, p2=l5)
    drawLine(ax=ax2, p1=l3, p2=p3)
    drawCircle(ax2, l3, radius=2, fill=False, position="top")
    drawCircle(ax2, l3, radius=6, fill=False, position="bottom")    
    drawEllipse(ax=ax2, center=(0,-3), width=12, height=3, position="bottom")
    drawEllipse(ax=ax2, center=(0,-3), width=12, height=3, position="top")
    drawEllipse(ax=ax2, center=(0,-3), width=4, height=1, position="bottom")
    drawEllipse(ax=ax2, center=(0,-3), width=4, height=1, position="top", dash=True)

    pp5 = mpatches.PathPatch(
    Path([(0,-1), (1,-2), (0,-3)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp5)

    pp6 = mpatches.PathPatch(
    Path([(0,-3), (-1,-4), (-2,-3)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp6)

    pp7 = mpatches.PathPatch(
    Path([(-2,-3), (-4,-1.5), (-6,-3)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp7)

    pp8 = mpatches.PathPatch(
    Path([(0,-3), (2,-6), (0,-9)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp8)

    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (-5,-1), xy = (-4,-2.4),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })
    
    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (-1.5,-5), xy = (-1,-3.4),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.2", 
              'arrowstyle':'->'
              })
    
    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (1.8,-0.8), xy = (0.3,-2),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })

    ax2.text(1.8,-0.8, '${r1}$cm'.format(r1=r1), size = 12)
    ax2.text(-2.4,-5.6, '${r1}$cm'.format(r1=r1), size = 12)
    ax2.text(1.2,-6, '${r2}$cm'.format(r2=r2), size = 12)
    ax2.text(-7,-1.2, '${r3}$cm'.format(r3=r3), size = 12)
    ax2.text(-0.4,0.4, '$\circlearrowleft$', size = 16)
    ax2.text(-0.1,2.3, '$l$', size = 14)
    
    ax2.set_xlim(-6,13)

    svg2 = saveSvg()
    
    f = "\\frac{90}{360}"
    ans = int(((r1*r1*90/360)+(r2*r2*90/360))*2)

    k = int(ans/4)

    aa_list = [ans-k*3, ans-k*2, ans-k, ans, ans+k, ans+k*2, ans+k*3]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(r1=r1, r2=r2, f=f, ans=ans)
    svg = [svg1,svg2]
    return stem, answer, comment, svg  



def solidfigure123_Stem_051():
    stem = "다음 그림과 같은 직사각형을 직선 $$수식$$l$$/수식$$을 회전축으로 하여 $$수식$$1$$/수식$$회전시킬 때 생기는 회전체의 전개도에서 $$수식$$a+b+c$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 회전체는 밑면의 반지름의 길이가 $$수식$${n1}``rm cm$$/수식$$, 높이가" \
              "$$수식$${n2}``rm cm$$/수식$$인 원기둥이므로\n" \
              "$$수식$$a={n1}, c={n2}$$/수식$$\n" \
              "전개도에서 직사각형의 가로의 길이는 원의 둘레의 길이와 같으므로\n" \
              "$$수식$$b\\pi=2\\pi\\times{n1}={s1}\\pi$$/수식$$에서 $$수식$$b={s1}$$/수식$$\n" \
              "$$수식$$THEREFORE a+b+c={ans}$$/수식$$\n"

    n1 = random.randint(3,5)
    n2 = n1*2+2
    s1 = 2*n1
    ans = n1+n2+s1

    l1 = (0,3)
    l2 = (0,0)
    l3 = (0,-8)
    l4 = (0,-9.5)
    p1 = (-3,0)
    p2 = (-3,-8)

    p3 = (10,1)
    p4 = (6.5,-1)
    p5 = (6.5,-6.5)
    p6 = (18.5,-6.5)
    p7 = (18.5,-1)
    p8 = (15,-8.5)
    p9 = (12,1)

    #ax = setChart(points=[l1,l2,l3,l4,p1,p2,p3,p4,p5,p6,p7,p8])
    fig, ax = plt.subplots(figsize=(4.5, 4.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=l3)

    drawLine(ax=ax, p1=p4, p2=p5)
    drawLine(ax=ax, p1=p5, p2=p6)
    drawLine(ax=ax, p1=p6, p2=p7)
    drawLine(ax=ax, p1=p7, p2=p4)

    drawLine(ax=ax, p1=p3, p2=p9)

    x = [0,-3,-3,0,0]
    y = [0,0,-8,-8,0]

    ax.fill(x, y, color="pink",alpha = 0.5)

    x2 = [6.5,6.5,18.5,18.5,6.5]
    y2 = [-1,-6.5,-6.5,-1,-1]

    ax.fill(x2, y2, color="pink",alpha = 0.5)

    ax.annotate('',
    ha = 'center', va = 'bottom',
    xytext = (2.5, -3.6),xy = (4, -3.6),arrowprops = {'facecolor' : 'grey', 'edgecolor' : 'grey', 'arrowstyle':'->'})

    pp = mpatches.Circle(p3, radius=2, fill=True, fc='pink', alpha=0.5)
    ax.add_patch(pp)

    pp2 = mpatches.Circle(p3, radius=2, fill=False, ec='black')
    ax.add_patch(pp2)

    pp3 = mpatches.Circle(p8, radius=2, fill=True, fc='pink', alpha=0.5)
    ax.add_patch(pp3)

    pp4 = mpatches.Circle(p8, radius=2, fill=False, ec='black')
    ax.add_patch(pp4)

    pp7 = mpatches.Circle(p3, radius=0.15, fill=True, ec='black',fc='black')
    ax.add_patch(pp7)

    pp5 = mpatches.PathPatch(
    Path([p1, (-5,-4), p2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp5)

    pp6 = mpatches.PathPatch(
    Path([p2, (-1.5,-9.5), l3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp6)

    pp8 = mpatches.PathPatch(
    Path([p4, (12.5,-3), p7],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp8)

    pp9 = mpatches.PathPatch(
    Path([p3, (11,2), p9],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp9)

    pp10 = mpatches.PathPatch(
    Path([p6, (20.5,-3.75), p7],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp10)

    if n2>= 10 :
      t = -8
    else :
      t = -7
    
    ax.text(t,-4.5, '${n2}$cm'.format(n2=n2), size = 10)
    ax.text(-3,-10, '${n1}$cm'.format(n1=n1), size = 10)
    ax.text(13,2.5, '$a$cm', size = 10)
    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (11,1), xy = (13,2.5),
    arrowprops = {
              'color':'black',
              'connectionstyle':"arc3,rad=-0.4",
              'edgecolor':'b', 
              'arrowstyle':'<-'
              })
    ax.text(10.8,-3.3, '$b\pi$ cm', size = 10)
    ax.text(19.8,-3.8, '$c$ cm', size = 10)
    ax.text(-0.7,0.7, '$\circlearrowleft$', size = 12)
    ax.text(-0.1,3.5, '$l$', size = 12)
    
    ax.set_xlim(-6, 25)
    ax.set_ylim(-24, 6)

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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, s1=s1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def solidfigure123_Stem_056():
    stem = "다음 그림과 같은 전개도에서 부채꼴의 반지름의 길이가 $$수식$${n}``rm cm$$/수식$$이고 중심각의 크기가 $$수식$$240 DEG $$/수식$$일 때,\n" \
            "이 전개도로 만들어지는 원뿔의 밑면의 넓이는?\n" \
            "① $$수식$${a1}\\pi``rm cm^2$$/수식$$  ② $$수식$${a2}\\pi``rm cm^2$$/수식$$" \
            "③ $$수식$${a3}\\pi``rm cm^2$$/수식$$  ④ $$수식$${a4}\\pi``rm cm^2$$/수식$$   ⑤ $$수식$${a5}\\pi``rm cm^2$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n 밑면의 둘레의 길이는 부채꼴의 호의 길이와 같으\n" \
              "므로 밑면의 반지름의 길이를 $$수식$$r``rm cm$$/수식$$라 하면\n" \
              "$$수식$$2\\pi\\times{n}\\times{f}=2\\pi r$$/수식$$ $$수식$$THEREFORE r={r}$$/수식$$\n" \
              "따라서 구하는 넓이는\n" \
              "$$수식$$\\pi\\times{r}^2={ans}\\pi(rm cm^2)$$/수식$$\n"
    while True :
      n = random.randint(6,12)
      if n%3 == 0 :
        break

    f = "\\frac{240}{360}"
    r = int(n*240/360)
    ans = r*r

    o = (0,0)
    p = (-8,-8) 
    p1 = (6,0)
    p2 = (6*math.cos(math.radians(120)),6*math.sin(math.radians(120)))
    o2 = (10*math.cos(math.radians(300)),10*math.sin(math.radians(300)))
    p3 = (14*math.cos(math.radians(300)),14*math.sin(math.radians(300)))
    p4 = (12,-12)

    #ax = setChart(points=[o,p,p1,p2,o2,p3,p4])
    fig, ax = plt.subplots(figsize=(3.5, 4))
    plt.axis("off")
    ax.autoscale()

    pp = mpatches.Wedge((0,0), r=6, theta1=120,
                                theta2=0, fc='orange', fill=True, alpha=0.4)
    ax.add_patch(pp)

    pp2 = mpatches.Wedge((0,0), r=6, theta1=120,
                                theta2=0, ec='black', fill=False)
    ax.add_patch(pp2)

    pp3 = mpatches.Circle(o2, radius=4, fill=True, fc='orange', alpha=0.4)
    ax.add_patch(pp3)

    pp4 = mpatches.Circle(o2, radius=4, fill=False, ec='black')
    ax.add_patch(pp4)

    pp5 = mpatches.PathPatch(
    Path([o, (0.6,4), p2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp5)

    a1 = AngleAnnotation(xy=o, p1=p2, p2=p1, text=r"240°",
                    textposition="outside", ax=ax, size=20)       
    
    ax.text(-0.2,3.1, '${n}$cm'.format(n=n), size = 12)

    aa_list = [(r-3)*(r-3), (r-2)*(r-2), (r-1)*(r-1), ans, (r+1)*(r+1), (r+2)*(r+2), (r+3)*(r+3)]
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

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, f=f, r=r, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def solidfigure123_Stem_057():
    stem = "다음 그림과 같은 직육면체의 겉넓이는?\n" \
            "① $$수식$${a1}rm cm^2$$/수식$$     ② $$수식$${a2}rm cm^2$$/수식$$    ③ $$수식$${a3}rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}rm cm^2$$/수식$$     ⑤ $$수식$${a5}rm cm^2$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n(직육면체의 겉넓이)\n" \
              "$$수식$$=({n1}\\times{n2})\\times 2+({n1}\\times 2+{n2}\\times 2)\\times{n3}$$/수식$$\n" \
              "$$수식$$={s1}+{s2}={ans}(rm cm^2)$$/수식$$"

    n1 = random.randint(3,6)
    n2 = n1+1
    n3 = n2+1
    s1 = n1*n2*2
    s2 = (n1*2+n2*2)*n3
    ans = s1+s2

    a = (0.5,0.5)
    b = (0,0)
    c = (0.9,0)
    d = (1.4,0.5)
    e = (0.5,-0.9)
    f = (0,-1.4)
    g = (0.9,-1.4)
    h = (1.4,-0.9)
      
    #ax = setChart(points=[a,b,c,d,e,f,g,h])
    fig, ax = plt.subplots(figsize=(3.5, 4))
    plt.axis("off")
    ax.autoscale()

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
    Path([a, (0.9, 0.8), d],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([a, (0, 0.5), b],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([b, (-0.4, -0.7), f],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp3)


    ax.text(0.85, 0.7, '${n1}$cm'.format(n1=n1), size = 12)
    ax.text(-0.2, 0.4, '${n2}$cm'.format(n2=n2), size = 12)
    ax.text(-0.55, -0.7, '${n3}$cm'.format(n3=n3), size = 12)

    aa_list = [ans-36, ans-24, ans-12, ans, ans+12, ans+24, ans+36]
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


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def solidfigure123_Stem_058():
    stem = "다음 그림과 같은 전개도로 만든 원기둥의 겉넓이는?\n" \
            "① $$수식$${a1}\\pi``rm cm^2$$/수식$$   ② $$수식$${a2}\\pi``rm cm^2$$/수식$$    ③ $$수식$${a3}\\pi``rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm cm^2$$/수식$$   ⑤ $$수식$${a5}\\pi``rm cm^2$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n 밑면의 반지름의 길이를 $$수식$$r rm cm$$/수식$$라 하면\n" \
              "$$수식$$2\\pi r={n1}\\pi$$/수식$$  $$수식$$THEREFORE r={r}$$/수식$$\n" \
              "따라서 원기둥의 겉넓이는\n" \
              "$$수식$$(\\pi\\times{r}^2)\\times 2+{n1}\\pi\\times{h}={s1}\\pi+{s2}\\pi$$/수식$$\n" \
              "     $$수식$$={ans}\pi(rm cm^2)$$/수식$$"

    while True :
      n1 = random.randint(8,16)
      if n1 % 2 == 0 :
        break
    r = int(n1/2)
    h = r+random.randint(0,2)
    s1 = r*r*2
    s2 = n1*h
    ans = s1+s2

    p3 = (0,3)
    p4 = (-4,1)
    p5 = (-4,-3.5)
    p6 = (9,-3.5)
    p7 = (9,1)
    p8 = (5,-5.5)
    p9 = (5,-7)

    #ax = setChart(points=[p3,p4,p5,p6,p7,p8,p9])
    fig, ax = plt.subplots(figsize=(3.5, 3))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p4, p2=p5)
    drawLine(ax=ax, p1=p5, p2=p6)
    drawLine(ax=ax, p1=p6, p2=p7)
    drawLine(ax=ax, p1=p7, p2=p4)

    x2 = [-4,-4,9,9,-4]
    y2 = [1,-3.5,-3.5,1,1]

    ax.fill(x2, y2, color="lightblue",alpha = 0.5)

    pp = mpatches.Circle(p3, radius=2, fill=True, fc='lightblue', alpha=0.5)
    ax.add_patch(pp)

    pp2 = mpatches.Circle(p3, radius=2, fill=False, ec='black')
    ax.add_patch(pp2)

    pp3 = mpatches.Circle(p8, radius=2, fill=True, fc='lightblue', alpha=0.5)
    ax.add_patch(pp3)

    pp4 = mpatches.Circle(p8, radius=2, fill=False, ec='black')
    ax.add_patch(pp4)

    pp8 = mpatches.PathPatch(
    Path([p4, (2.5,-1), p7],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp8)

    pp10 = mpatches.PathPatch(
    Path([p6, (10.5,-1.4), p7],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp10)

    ax.text(1.2,-0.8, '${n1}\pi$cm'.format(n1=n1), size = 10)
    ax.text(10,-1.55, '${h}$cm'.format(h=h), size = 10)

    aa_list = [ans-n1*3, ans-n1*2, ans-n1, ans, ans+n1, ans+n1*2, ans+n1*3]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, h=h, s1=s1, s2=s2, r=r, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def solidfigure123_Stem_059():
    stem = "겉넓이가 $$수식$${a}rm cm^2$$/수식$$인 정육면체의 한 모서리의 길이는?\n" \
            "① $$수식$${a1}``rm cm$$/수식$$   ② $$수식$${a2}``rm cm$$/수식$$   ③ $$수식$${a3}``rm cm$$/수식$$\n" \
            "④ $$수식$${a4}``rm cm$$/수식$$   ⑤ $$수식$${a5}``rm cm$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 정육면체의 한 모서리의 길이를 $$수식$$a``rm cm$$/수식$$라 하면\n" \
              "정육면체의 겉넓이는 정사각형인 면 $$수식$$6$$/수식$$개의 넓이의합과 같으므로\n" \
              "$$수식$$(a\\times a)\\times 6={a}, a^2={s1}={ans}^2$$/수식$$\n" \
              "$$수식$$THEREFORE a={ans}$$/수식$$\n" \
              "따라서 정육면체의 한 모서리의 길이는 $$수식$${ans}``rm cm$$/수식$$이다.\n"
    
    ans = random.randint(4,9)
    s1 = ans*ans
    a = s1*6

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


    stem = stem.format(a=a, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(a=a, s1=s1, ans=ans)

    return stem, answer, comment



def solidfigure123_Stem_060():
    stem = "다음 그림과 같은 삼각기둥의 겉넓이가 $$수식$${a}``rm cm^2$$/수식$$일 때, $$수식$$h$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\left({f}\\times{n1}\\times{n2}\\right)\\times 2+({n3}+{n2}+{n1})\\times h={a}$$/수식$$\n" \
              "이므로\n" \
              "$$수식$${s1}+{s2}h={a}$$/수식$$, $$수식$${s2}h={s3}$$/수식$$\n" \
              "$$수식$$THEREFORE h={ans}$$/수식$$\n"

    p1 = (0.25,0.6)
    p2 = (0,0)
    p3 = (1.7,0)

    p4 = (0.25,1.4)
    p5 = (0,0.8)
    p6 = (1.7,0.8)

    k = random.randint(1,2)
    n1 = 5*k
    n2 = 12*k
    n3 = 13*k

    f = "\\frac{1}{2}"
    ans = random.randint(6,9)
    s1 = n1*n2
    s2 = n1+n2+n3
    a = s1+s2*ans
    s3 = a-s1
      
    #ax = setChart(points=[p1,p2,p3,p4,p5,p6])
    fig, ax = plt.subplots(figsize=(4, 3.5))
    plt.axis("off")
    ax.autoscale()

    drawPolygon(ax=ax, verts=[p4,p5,p6])

    drawLine(ax=ax, p1=p2, p2=p5)
    drawLine(ax=ax, p1=p3, p2=p6)
    drawLine(ax=ax, p1=p2, p2=p3)
    drawLine(ax=ax, p1=p1, p2=p4, dash=True)
    drawLine(ax=ax, p1=p1, p2=p2, dash=True)
    drawLine(ax=ax, p1=p1, p2=p3, dash=True)

    x = [0.215,0.29,0.325]
    y = [0.6/0.25*0.215,0.49,0.57]

    ax.plot(x,y, c="black", linewidth = 0.6)

    x2 = [0.215,0.29,0.325]
    y2 = [0.6/0.25*0.215+0.8,0.49+0.8,0.57+0.8]

    ax.plot(x2,y2, c="black", linewidth = 0.6)
    
    pp1 = mpatches.PathPatch(
    Path([p4, (-0.2, 1.1), p5],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p5, (0.8, 0.5), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p6, (0.9, 1.5), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp3)

    pp4 = mpatches.PathPatch(
    Path([p6, (1.95, 0.4), p3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp4)

    ax.text(-0.3, 1.1, '${n1}$cm'.format(n1=n1), size = 14)
    ax.text(0.9, 1.35, '${n2}$cm'.format(n2=n2), size = 14)
    ax.text(0.7, 0.53, '${n3}$cm'.format(n3=n3), size = 14)
    ax.text(1.85, 0.38, '$h$cm', size = 14)

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

    stem = stem.format(a=a, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, f=f, a=a, s1=s1, s2=s2, s3=s3, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_061():
    stem = "다음 그림과 같은 원기둥의 겉넓이는?\n" \
            "① $$수식$${a1}\\pi``rm cm^2$$/수식$$   ② $$수식$${a2}\\pi``rm cm^2$$/수식$$    ③ $$수식$${a3}\\pi``rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm cm^2$$/수식$$   ⑤ $$수식$${a5}\\pi``rm cm^2$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n밑면의 반지름의 길이는 $$수식$${f}={r}(rm cm)$$/수식$$이므로\n" \
              "(겉넓이)$$수식$$=(\\pi\\times{r}^2)\\times2+2\\pi\\times{r}\\times{h}$$/수식$$\n" \
              "$$수식$$={s1}\\pi+{s2}\\pi={ans}\\pi(rm cm^2)$$/수식$$"
    while True :
      n1 = random.randint(8,16)
      if n1%2 == 0 :
        break
    n2 = n1+2

    f = "\\frac{"+str(n1)+"}{2}"
    r = int(n1/2)
    h = n2
    s1 = r*r*2
    s2 = 2*r*h
    ans = s1+s2

    p1 = (-4,0)
    p2 = (-4,-5)
    p3 = (-6,0)
    p4 = (-2,0)
    p5 = (-6,-5)
    p6 = (-2,-5)
    p = (0,-5)

    #ax = setChart(points=[p1,p2,p3,p4,p5,p6,p])
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax.autoscale()
    
    #ax.set_xlim(-20,4)

    drawEllipse(ax=ax, center=(-4, 0), width=4, height=1.8)
    drawEllipse(ax=ax, center=(-4, -5), width=4, height=1.8, position="bottom")
    drawEllipse(ax=ax, center=(-4, -5), width=4, height=1.8, position="top", dash=True)
    drawLine(ax=ax, p1=p3, p2=p5)
    drawLine(ax=ax, p1=p4, p2=p6)
    drawLine(ax=ax, p1=p3, p2=p4)

    ax.scatter(-4,0, c='black', edgecolor='black', s=20)

    pp1 = mpatches.PathPatch(
    Path([p3, (-4, 1), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p4, (-0.5, -2.5), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-2.5, 1.2), xy = p1,
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })
    
    ax.text(-2.5, 1.1, '${n1}$cm'.format(n1=n1), size = 12)
    ax.text(-1.1, -2.7, '${n2}$cm'.format(n2=n2), size = 12)

    aa_list = [ans-60, ans-40, ans-20, ans, ans+20, ans+40, ans+60]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, r=r, h=h, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_062():
    stem = "어떤 원기둥을 회전축을 포함하는 평면으로 잘랐더니 그 단면의 모양이 한 변의 길이가 $$수식$${n}``rm cm$$/수식$$인 정사각형이었다. 이때 원기둥의 겉넓이는?\n" \
            "① $$수식$${a1}\\pi``rm cm^2$$/수식$$   ② $$수식$${a2}\\pi``rm cm^2$$/수식$$   ③ $$수식$${a3}\\pi``rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm cm^2$$/수식$$   ⑤ $$수식$${a5}\\pi``rm cm^2$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n원기둥을 회전축을 포함하는 평면으로 자를 때 생기는 단면은 그림과 같으므로\n" \
              "(원기둥의 겉넓이)$$수식$$=(\\pi\\times{r}^2)\\times 2+2\\pi\\times{r}\\times{n}$$/수식$$\n" \
              "$$수식$$={s1}\\pi+{s2}\\pi$$/수식$$\n" \
              "$$수식$$={ans}\\pi$$/수식$$\n"
    
    n = random.choice([4,6,8,10,12])
    r = int(n/2)
    s1 = r*r*2
    s2 = 2*r*n
    ans = s1+s2

    a_list = [24,54,96,150,216]
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break
    
    fig, ax = plt.subplots(figsize=(0,0))
    svg1 = saveSvg()

    p1 = (-4,0)
    p2 = (-4,-4.5)
    p3 = (-6,0)
    p4 = (-2,0)
    p5 = (-6,-4.5)
    p6 = (-2,-4.5)
    p = (0,-4.5)

    l1 = (-4,2.5)
    l2 = (-4,-6)

    #ax = setChart(points=[p1,p2,p3,p4,p5,p6,p])
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax.autoscale()

    drawEllipse(ax=ax, center=(-4, 0), width=4, height=1.6)
    drawEllipse(ax=ax, center=(-4, -4.5), width=4, height=1.6, position="bottom")
    drawEllipse(ax=ax, center=(-4, -4.5), width=4, height=1.6, position="top", dash=True)
    drawLine(ax=ax, p1=p3, p2=p5)
    drawLine(ax=ax, p1=p4, p2=p6)
    drawLine(ax=ax, p1=p3, p2=p4)
    drawLine(ax=ax, p1=p5, p2=p6)
    drawLine(ax=ax, p1=l1, p2=l2)

    pp1 = mpatches.PathPatch(
    Path([p3, (-4, 0.8), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p4, (-0.8, -2.25), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p2, (-3, -5.2), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)


    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-2.3, 1.2), xy = (-3.1, 0.2),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-2, -5.5), xy = (-3, -4.8),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })    

    ax.text(-2.3, 1.1, '${n}$cm'.format(n=n), size = 12)
    ax.text(-2, -5.7, '${r}$cm'.format(r=r), size = 12)
    ax.text(-4.25,1.4, '$\circlearrowleft$', size = 16)
    ax.text(-4.1,2.8, '$l$', size = 12)
    ax.text(-1.25, -2.4, '${n}$cm'.format(n=n), size = 12)

    x = [-6,-6,-2,-2]
    y = [0,-4.5,-4.5,0]
    
    ax.fill(x, y, color="orange",alpha = 0.4)

    svg2 = saveSvg()

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(r=r, n=n, s1=s1, s2=s2, ans=ans)
    svg = [svg1,svg2]
    return stem, answer, comment, svg



def solidfigure123_Stem_068():
    stem = "다음 그림과 같은 삼각기둥의 부피는?\n" \
            "① $$수식$${a1}``rm cm^3$$/수식$$   ② $$수식$${a2}``rm cm^3$$/수식$$   ③ $$수식$${a3}``rm cm^3$$/수식$$\n" \
            "④ $$수식$${a4}``rm cm^3$$/수식$$   ⑤ $$수식$${a5}``rm cm^3$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n(부피)$$수식$$=\\left({f}\\times{n1}\\times{n2}\\right)\\times{h}={ans}(rm cm^3)$$/수식$$\n"
    
    while True :
      n2 = random.randint(4,8)
      if n2%2 == 0:
        break
    n3 = n2*2
    n1 = n3-2
    f = "\\frac{1}{2}"
    h = n3

    ans = int(n2*n1*h/2)

    p1 = (0.95,0.55)
    p2 = (0,0)
    p3 = (1.3,0)
    
    p4 = (0.95,1.85)
    p5 = (0,1.3)
    p6 = (1.3,1.3)

    #ax = setChart(points=[p1,p2,p3,p4,p5,p6])3
    fig, ax = plt.subplots(figsize=(3.5, 4))
    plt.axis("off")
    ax.autoscale()

    drawPolygon(ax=ax, verts=[p4,p5,p6])

    drawLine(ax=ax, p1=p2, p2=p5)
    drawLine(ax=ax, p1=p3, p2=p6)
    drawLine(ax=ax, p1=p2, p2=p3)
    drawLine(ax=ax, p1=p1, p2=p4, dash=True)
    drawLine(ax=ax, p1=p1, p2=p2, dash=True)
    drawLine(ax=ax, p1=p1, p2=p3, dash=True)

    x = [0.88,0.92,0.99]
    y = [0.55/0.95*0.88,0.45,0.492]

    ax.plot(x,y, c="black", linewidth = 0.6)

    x2 = [0.88,0.92,0.99]
    y2 = [0.55/0.95*0.88+1.3,0.45+1.3,0.492+1.3]

    ax.plot(x2,y2, c="black", linewidth = 0.6)
    
    pp1 = mpatches.PathPatch(
    Path([p4, (0.4,1.9), p5],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p4, (1.3, 1.8), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p6, (1.6, 0.6), p3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp3)


    ax.text(0.2,1.8, '${n1}$cm'.format(n1=n1), size = 12)
    ax.text(1.24, 1.7, '${n2}$cm'.format(n2=n2), size = 12)
    ax.text(1.48, 0.6, '${n3}$cm'.format(n3=n3), size = 12)

    k = int(ans/n2)

    aa_list = [ans-k*3, ans-k*2, ans-k, ans, ans+k, ans+k*2, ans+k*3]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, f=f, h=h, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_069():
    stem = "부피가 $$수식$${v}\\pi ``rm cm^3$$/수식$$인 원기둥의 높이가 $$수식$${h}``rm cm$$/수식$$일때, 밑면의 반지름의 길이를 구하시오.\n"
    answer = "(정답)\n$$수식$${result}``rm cm$$/수식$$"
    comment = "(해설)\n밑면의 반지름의 길이를 $$수식$$r``rm cm$$/수식$$라 하면\n" \
              "$$수식$$\\pi\\times r^2\\times{h}={v}\\pi,$$/수식$$ $$수식$$r^2={s1}$$/수식$$\n" \
              "$$수식$$THEREFORE r={result}$$/수식$$\n" \
              "따라서 반지름의 길이는 $$수식$${result}``rm cm$$/수식$$이다."

    result = random.randint(4,8)
    s1 = result*result
    h=random.randint(9,15)
    v = s1*h

    stem = stem.format(v=v, h=h)
    answer = answer.format(result=result)
    comment = comment.format(h=h, v=v, s1=s1,result=result)

    return stem, answer, comment



def solidfigure123_Stem_071():
    stem = "다음 그림과 같이 크기가 같은 정육면체 모양의 물통 세 개에 높이가 각각 $$수식$$a``rm cm, b``rm cm,c``rm cm$$/수식$$가 " \
            "되도록 물을 채웠다. 세 물통에 들어 있는 물의 부피가 각각 $$수식$${v1}``rm cm^3, {v2}``rm cm^3, {v3}``rm cm^3$$/수식$$일 때, $$수식$$a:b:c$$/수식$$는?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n세 물통의 밑넓이가 모두 같으므로 물의 부피의\n" \
              "비는 물의 높이의 비와 같다.\n" \
              "$$수식$$THEREFORE a:b:c={v1}:{v2}:{v3}={ans}$$/수식$$\n"

    ans = random.choice(["1:2:7","1:4:7","1:4:9","1:5:9","1:7:9"])
    a2 = int(ans[2])
    a3 = int(ans[4])

    v1 = random.randint(15,25)
    v2 = v1*a2
    v3 = v1*a3

    a = (0.5,0.5)
    b = (0,0)
    c = (1.1,0)
    d = (1.6,0.5)
    e = (0.5,-0.6)
    f = (0,-1.1)
    g = (1.1,-1.1)
    h = (1.6,-0.6)

    if a2 == 5 :
      e2y = 0
      f2y = -0.5
      g2y = -0.5
      h2y = 0
    elif a2 == 4 :
      e2y = -0.1
      f2y = -0.6
      g2y = -0.6
      h2y = -0.1
    elif a2 == 2 :
      e2y = -0.4
      f2y = -0.9
      g2y = -0.9
      h2y = -0.4
    elif a2 == 7 :
      e2y = 0.2
      f2y = -0.3
      g2y = -0.3
      h2y = 0.2      

    e_2 = (0.5, e2y)
    f_2 = (0, f2y)
    g_2 = (1.1, g2y)
    h_2 = (1.6, h2y)

    p1 = (-2.5,0.5)
    p2 = (-3,0)
    p3 = (-1.9,0)
    p4 = (-1.4,0.5)
    p5 = (-2.5,-0.6)
    p6 = (-3,-1.1)
    p7 = (-1.9,-1.1)
    p8 = (-1.4,-0.6)

    p5_2 = (-2.5,-0.5)
    p6_2 = (-3,-1)
    p7_2 = (-1.9,-1)
    p8_2 = (-1.4,-0.5)

    t1 = (3.5,0.5)
    t2 = (3,0)
    t3 = (4.1,0)
    t4 = (4.6,0.5)
    t5 = (3.5,-0.6)
    t6 = (3,-1.1)
    t7 = (4.1,-1.1)
    t8 = (4.6,-0.6)

    if a3 == 7 :
      t5y = 0.2
      t6y = -0.3
      t7y = -0.3
      t8y = 0.2    
    elif a3 == 9 :
      t5y = 0.4
      t6y = -0.1
      t7y = -0.1
      t8y = 0.4      

    t5_2 = (3.5,t5y)
    t6_2 = (3,t6y)
    t7_2 = (4.1,t7y)
    t8_2 = (4.6,t8y)
      
    #ax = setChart(points=[a,b,c,d,e,f,g,h,p1,p2,p3,p4,p5,p6,p7,p8,t1,t2,t3,t4,t5,t6,t7,t8])
    
    fig, ax = plt.subplots(figsize=(4.5, 1))
    plt.axis("off")
    ax.autoscale()

    drawPolygon(ax=ax, verts=[a,b,c,d])

    drawLine(ax=ax, p1=d, p2=h)
    drawLine(ax=ax, p1=b, p2=f)
    drawLine(ax=ax, p1=c, p2=g)
    drawLine(ax=ax, p1=f, p2=g)
    drawLine(ax=ax, p1=g, p2=h)
    drawLine(ax=ax, p1=f, p2=e, dash=True)
    drawLine(ax=ax, p1=a, p2=e, dash=True)
    drawLine(ax=ax, p1=e, p2=h, dash=True)

    drawPolygon(ax=ax, verts=[p1,p2,p3,p4])

    drawLine(ax=ax, p1=p4, p2=p8)
    drawLine(ax=ax, p1=p2, p2=p6)
    drawLine(ax=ax, p1=p3, p2=p7)
    drawLine(ax=ax, p1=p6, p2=p7)
    drawLine(ax=ax, p1=p7, p2=p8)
    drawLine(ax=ax, p1=p6, p2=p5, dash=True)
    drawLine(ax=ax, p1=p1, p2=p5, dash=True)
    drawLine(ax=ax, p1=p5, p2=p8, dash=True)

    drawPolygon(ax=ax, verts=[t1,t2,t3,t4])

    drawLine(ax=ax, p1=t4, p2=t8)
    drawLine(ax=ax, p1=t2, p2=t6)
    drawLine(ax=ax, p1=t3, p2=t7)
    drawLine(ax=ax, p1=t6, p2=t7)
    drawLine(ax=ax, p1=t7, p2=t8)
    drawLine(ax=ax, p1=t6, p2=t5, dash=True)
    drawLine(ax=ax, p1=t1, p2=t5, dash=True)
    drawLine(ax=ax, p1=t5, p2=t8, dash=True)

    x = [p6_2[0],p6[0],p7[0],p8[0],p8_2[0],p5_2[0],p6_2[0]]
    y = [p6_2[1],p6[1],p7[1],p8[1],p8_2[1],p5_2[1],p6_2[1]]
    ax.fill(x, y, color="lightblue",alpha = 0.3)

    x2 = [f_2[0],f[0],g[0],h[0],h_2[0],e_2[0],f_2[0]]
    y2 = [f_2[1],f[1],g[1],h[1],h_2[1],e_2[1],f_2[1]]
    ax.fill(x2, y2, color="lightblue",alpha = 0.3)

    x3 = [t6_2[0],t6[0],t7[0],t8[0],t8_2[0],t5_2[0],t6_2[0]]
    y3 = [t6_2[1],t6[1],t7[1],t8[1],t8_2[1],t5_2[1],t6_2[1]]
    ax.fill(x3, y3, color="lightblue",alpha = 0.3)

    pp1 = mpatches.PathPatch(
    Path([p6, (-3.1,-1.05), p6_2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([f, (-0.3,-0.8), f_2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([t6, (2.6, -0.6), t6_2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    ax.text(-3.8,-1.1, '${a}$cm', size = 10)
    ax.text(-0.95,-0.9, '${b}$cm', size = 10)
    ax.text(2.05, -0.7, '${c}$cm', size = 10)

    a_list = ["1:2:7","1:4:7","1:4:9","1:5:9","1:7:9"]
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    stem = stem.format(v1=v1, v2=v2, v3=v3, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(v1=v1, v2=v2, v3=v3, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg




def solidfigure123_Stem_073():
    stem = "다음 그림과 같이 원기둥 $$수식$$A$$/수식$$의 밑면의 반지름의 길이는 $$수식$${r1}``rm cm$$/수식$$이고, " \
            "원기둥 $$수식$$B$$/수식$$의 밑면의 반지름의 길이는 $$수식$${r2}``rm cm$$/수식$$, 높이는 $$수식$${h}``rm cm$$/수식$$이다. " \
            "원기둥 $$수식$$B$$/수식$$의 부피는 원기둥 $$수식$$A$$/수식$$의 부피의 $$수식$${k}$$/수식$$배일 때, 원기둥 $$수식$$A$$/수식$$의높이를 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n원기둥 $$수식$$B$$/수식$$의 부피는\n" \
              "$$수식$$\\pi\\times{r2}^2\\times{h}={v}\\pi(rm cm^3)$$/수식$$\n" \
              "원기둥 $$수식$$A$$/수식$$의 높이를 $$수식$$hcm$$/수식$$라 하면 원기둥 $$수식$$A$$/수식$$의 부피는 이므로\n" \
              "$$수식$$\\pi\\times{r1}^2\\times h={s1}h\\pi(rm cm^3)$$/수식$$\n" \
              "$$수식$${s1}h\\pi\\times{k}={v}\\pi$$/수식$$ $$수식$$THEREFORE h={result}$$/수식$$\n" \
              "따라서 원기둥 $$수식$$A$$/수식$$의 높이는 $$수식$${result}``rm cm$$/수식$$이다."

    while True :
        k = random.randint(2,4)
        r2 = random.randint(4,6)
        h = random.randint(9,12)
        v = r2*r2*h
        r1 = random.randint(6,9)
        s1 = r1*r1
        if v % (s1*k) == 0 :
            break
   
    result = int(v/(s1*k))
    k = result

    p1 = (0,0)
    p2 = (0,-5.5)
    p3 = (-2.25,0)
    p4 = (2.25,0)
    p5 = (-2.25,-5.5)
    p6 = (2.25,-5.5)

    a = (-17,-5.5)
    b = (4,-5.5)

    t1 = (-12,-5.5)
    t2 = (-16,-5.5)
    t3 = (-8,-5.5)
    t4 = (-12,-4)
    t5 = (-16,-4)
    t6 = (-8,-4)


    #ax = setChart(points=[p1,p2,p3,p4,p5,p6,a,b,t1,t2,t3,t4,t5,t6])
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax.autoscale()
    ax.set_xlim(-16, 4)

    drawEllipse(ax=ax, center=(0, 0), width=4.5, height=1.8)
    drawEllipse(ax=ax, center=(0, -5.5), width=4.5, height=1.8, position="bottom")
    drawEllipse(ax=ax, center=(0, -5.5), width=4.5, height=1.8, position="top", dash=True)
    drawLine(ax=ax, p1=p3, p2=p5)
    drawLine(ax=ax, p1=p4, p2=p6)
    drawLine(ax=ax, p1=p2, p2=p6)

    drawEllipse(ax=ax, center=t1, width=8, height=1.3, position="bottom")
    drawEllipse(ax=ax, center=t1, width=8, height=1.3, position="top", dash=True)
    drawEllipse(ax=ax, center=t4, width=8, height=1.3)
    drawLine(ax=ax, p1=t2, p2=t5)
    drawLine(ax=ax, p1=t3, p2=t6)
    drawLine(ax=ax, p1=t1, p2=t3)

    ax.scatter(0,-5.5, c='black', edgecolor='black', s=14)
    ax.scatter(-12,-5.5, c='black', edgecolor='black', s=14) 

    pp1 = mpatches.PathPatch(
    Path([p2, (1.125, -6), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p4, (3.5, -2.5), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([t1, (-10, -6), t3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (2.4, -6.6), xy = (1.125, -5.6),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })
    
    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-8.4, -6.8), xy = (-10, -5.6),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })
    
    ax.text(-8.3, -7.3, '${r1}$cm'.format(r1=r1), size = 10)
    ax.text(2.4, -7, '${r2}$cm'.format(r2=r2), size = 10)
    ax.text(3.1, -2.8, '${h}$cm'.format(h=h), size = 10)

    ax.text(-12.4, -10, '${A}$', size = 14)
    ax.text(-0.4, -10, '${B}$', size = 14)


    stem = stem.format(r1=r1, r2=r2, h=h, k=k)
    answer = answer.format(result=result)
    comment = comment.format(r1=r1, r2=r2, h=h, v=v, s1=s1, k=k, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg  



def solidfigure123_Stem_075():
    stem = "다음 그림과 같이 구멍이 뚫린 입체도형의 부피는?\n" \
            "① $$수식$${a1}\\pi ``rm cm^3$$/수식$$   ② $$수식$${a2}\\pi ``rm cm^3$$/수식$$   ③ $$수식$${a3}\\pi ``rm cm^3$$/수식$$\n" \
            "④ $$수식$${a4}\\pi ``rm cm^3$$/수식$$   ⑤ $$수식$${a5}\\pi ``rm cm^3$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n(부피)$$수식$$=(\\pi\\times{r1}^2)\\times{h}-(\\pi\\times{r2}^2)\\times{h}$$/수식$$\n" \
              " $$수식$$={s1}\\pi-{s2}\\pi={ans}\\pi(rm cm^3)$$/수식$$"

    n1 = random.randint(2,4)
    n2 = n1+1
    n3 = n2*2+1

    r1 = n1+n2
    r2 = n2
    h = n3
    s1 = r1*r1*h
    s2 = r2*r2*h
    ans = s1-s2

    p1 = (-4,0)
    p2 = (-4,-4.5)
    p3 = (-6,0)
    p4 = (-2,0)
    p5 = (-6,-4.5)
    p6 = (-2,-4.5)
    p = (0,-4.5)

    t1 = (-7.4,0)
    t2 = (-0.6,0)
    t3 = (-7.4,-4.5)
    t4 = (-0.6,-4.5)

    #ax = setChart(points=[p1,p2,p3,p4,p5,p6,p,t1,t2,t3,t4])
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax.autoscale()

    drawEllipse(ax=ax, center=(-4, 0), width=4, height=1.6)
    drawEllipse(ax=ax, center=(-4, -4.5), width=4, height=1.6, dash=True)
    drawLine(ax=ax, p1=p3, p2=p5, dash=True)
    drawLine(ax=ax, p1=p4, p2=p6, dash=True)

    drawEllipse(ax=ax, center=(-4, 0), width=6.8, height=3)
    drawEllipse(ax=ax, center=p2, width=6.8, height=3, position="bottom")
    drawEllipse(ax=ax, center=p2, width=6.8, height=3, position="top", dash=True)
    drawLine(ax=ax, p1=t1, p2=t3)
    drawLine(ax=ax, p1=t2, p2=t4)

    drawLine(ax=ax, p1=p1, p2=t2)

    ax.scatter(-4,0, c='black', edgecolor='black', s=20)

    pp1 = mpatches.PathPatch(
    Path([p1, (-3,0.5), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p4, (-1.3,0.5), t2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([t2, (0.5, -2.25), t4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-0.2,1), xy = (-1.3,0.2),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })
    
    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-3,1.8), xy = (-3,0.2),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'arrowstyle':'->'
              })
    
    ax.text(-0.2,0.8, '${n1}$cm'.format(n1=n1), size = 12)
    ax.text(-3.5,1.9, '${n2}$cm'.format(n2=n2), size = 12)
    ax.text(0.1, -2.3, '${n3}$cm'.format(n3=n3), size = 12)


    aa_list = [ans-18, ans-12, ans-6, ans, ans+6, ans+12, ans+18]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(r1=r1, r2=r2, h=h, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def solidfigure123_Stem_080():
    stem = "다음 그림과 같이 밑면은 한 변의 길이가 $$수식$${n}``rm cm$$/수식$$인 정사각형이고, " \
            "옆면은 모두 높이가 $$수식$${h}``rm cm$$/수식$$인 이등변삼각형인 사각뿔의 겉넓이는?\n" \
            "① $$수식$${a1}``rm cm^3$$/수식$$   ② $$수식$${a2}``rm cm^3$$/수식$$   ③ $$수식$${a3}``rm cm^3$$/수식$$\n" \
            "④ $$수식$${a4}``rm cm^3$$/수식$$   ⑤ $$수식$${a5}``rm cm^3$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n(겉넓이)$$수식$$={n}\\times{n}+\\left({f}\\times{n}\\times{h}\\right)\\times 4$$/수식$$\n" \
              "$$수식$$={s1}+{s2}$$/수식$$\n" \
              "$$수식$$={ans}(rm cm^2)$$/수식$$"

    n = random.randint(3,6)
    h = n*2+1
    f = "\\frac{1}{2}"
    s1 = n*n
    s2 = int(n*h*2)
    ans = s1+s2

    p1 = (-0.1,2)
    p2 = (-0.85,0.2)
    p3 = (0,0)
    p4 = (0.7,0.4)
    p5 = (-0.15,0.68)
    p6 = (0.35,0.2)

    #ax = setChart(points=[p1,p2,p3,p4,p5,p6])
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p1, p2=p5, dash=True)
    drawLine(ax=ax, p1=p5, p2=p2, dash=True)
    drawLine(ax=ax, p1=p5, p2=p4, dash=True)
    drawLine(ax=ax, p1=p2, p2=p3)
    drawLine(ax=ax, p1=p3, p2=p4)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p1, p2=p4)
    drawLine(ax=ax, p1=p1, p2=p6)

    x = [0.26,0.22,0.32]
    y = [0.14,0.28,0.34]
    ax.plot(x,y, c="black", linewidth = 0.5)

    x2 = [-0.73,-0.6,-0.73]
    y2 = [0.18,0.25,0.28]
    ax.plot(x2,y2, c="black", linewidth = 0.5)

    x3 = [-0.12,-0.015,0.11]
    y3 = [0.04,0.12,0.07]
    ax.plot(x3,y3, c="black", linewidth = 0.5)

    x4 = [0.58,0.47,0.6]
    y4 = [0.44,0.38,0.35]
    ax.plot(x4,y4, c="black", linewidth = 0.5)

    x5 = [-0.26,-0.14,-0.04]
    y5 = [0.62,0.59,0.66]
    ax.plot(x5,y5, c="black", linewidth = 0.5)

    p1 = (-0.1,2)
    p2 = (-0.85,0.2)
    p3 = (0,0)
    p4 = (0.7,0.4)
    p5 = (-0.15,0.68)
    p6 = (0.35,0.2)

    pp1 = mpatches.PathPatch(
    Path([p2, (-0.44,-0.2), p3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p3, (0.38,-0.1), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p1, (0.38,0.75), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (0.5, 1.4), xy = (0.1,1.2),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.3", 
              'arrowstyle':'->'
              })
    
    ax.text(0.35,-0.1, '${n}$cm'.format(n=n), size = 12)
    ax.text(-0.65,-0.2, '${n}$cm'.format(n=n), size = 12)
    ax.text(0.5, 1.35, '${h}$cm'.format(h=h), size = 12)

    k = n*2
    aa_list = [ans-k*3, ans-k*2, ans-k, ans, ans+k, ans+k*2, ans+k*3]
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

    stem = stem.format(n=n, h=h, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, f=f, h=h, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  





def solidfigure123_Stem_081():
    stem = "다음 그림과 같은 원뿔의 겉넓이는?\n" \
            "① $$수식$${a1}\\pi``rm cm^2$$/수식$$   ② $$수식$${a2}\\pi``rm cm^2$$/수식$$   ③ $$수식$${a3}\\pi``rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm cm^2$$/수식$$   ⑤ $$수식$${a5}\\pi``rm cm^2$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n(겉넓이)$$수식$$=\\pi\\times{r}^2+\\pi\\times{r}\\times{l}$$/수식$$\n" \
              "$$수식$$={s1}\\pi+{s2}\\pi$$/수식$$\n" \
              "$$수식$$={ans}\\pi(rm cm^2)$$/수식$$\n"

    r = random.randint(3,5)
    l = r*2-1
    s1 = r*r
    s2 = r*l
    ans = s1+s2

    p1 = (-4,0)
    p2 = (-4,-5.5)
    p3 = (-8,-5.5)
    p4 = (0,-5.5)

    #ax = setChart(points=[p1,p2,p3,p4])
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax.autoscale()

    drawEllipse(ax=ax, center=(-4, -5.5), width=8, height=2.4, position="bottom")
    drawEllipse(ax=ax, center=(-4, -5.5), width=8, height=2.4, position="top", dash=True)
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p1, p2=p4)
    drawLine(ax=ax, p1=p2, p2=p4)

    ax.scatter(-4,-5.5, c='black', edgecolor='black', s=12)

    pp1 = mpatches.PathPatch(
    Path([p1, (-0.2,-1.6), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p2, (-2, -6.4), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-0.6, -6.8), xy = (-2, -5.8),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })
    
    ax.text(-0.6, -7.1, '${r}$cm'.format(r=r), size = 12)
    ax.text(-1,-2, '${l}$cm'.format(l=l), size = 12)

    aa_list = [ans-r*3, ans-r*2, ans-r, ans, ans+r, ans+r*2, ans+r*3]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(r=r, l=l, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_082():
    stem = "다음 그림과 같이 밑면은 정오각형이고, 옆면은 모두 합동인 오각뿔의 옆넓이는?\n" \
            "① $$수식$${a1}rm cm^2$$/수식$$   ② $$수식$${a2}rm cm^2$$/수식$$   ③ $$수식$${a3}rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}rm cm^2$$/수식$$   ⑤ $$수식$${a5}rm cm^2$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n(옆넓이)$$수식$$=\\left({f}\\times{n}\\times{l}\\right)\\times 5$$/수식$$\n" \
              "$$수식$$={ans}(rm cm^2)$$/수식$$"

    f = "\\frac{1}{2}"
    while True :
      n = random.randint(3,6)
      l = n*2-1
      if (n*l)%2 == 0 :
        break

    ans = int(n*l/2*5)

    p1 = (-1,0)    
    p6 = (-2.5,-2.5)
    p7 = (-1,-1.9)
    p8 = (0.5,-2.5)
    p9 = (-0.1, -3.3)
    p10 = (-1.9,-3.3)
    p2 = (1,-4)
    p3 = (0.2,-2.9) 
    p4 = (0.05,-3.1)

    #ax = setChart(points=[p1, p2, p6, p7, p8, p9, p10])
    fig, ax = plt.subplots(figsize=(3.5, 4))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p6, p2=p7, dash=True)
    drawLine(ax=ax, p1=p7, p2=p8, dash=True)
    drawLine(ax=ax, p1=p8, p2=p9)
    drawLine(ax=ax, p1=p9, p2=p10)
    drawLine(ax=ax, p1=p10, p2=p6)

    drawLine(ax=ax, p1=p1, p2=p7, dash=True)
    drawLine(ax=ax, p1=p1, p2=p6)
    drawLine(ax=ax, p1=p1, p2=p8)
    drawLine(ax=ax, p1=p1, p2=p9)
    drawLine(ax=ax, p1=p1, p2=p10)

    drawLine(ax=ax, p1=p1, p2=p3)

    pp1 = mpatches.PathPatch(
    Path([p6, (-2.8,-3), p10],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p10, (-1,-4), p9],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p9, (0.8, -3), p8],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    pp4 = mpatches.PathPatch(
    Path([p1, (0, -1.8), p3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp4)

    x = [0.09,0.02,0.14]
    y = [-3.03,-2.89,-2.76]
    ax.plot(x,y, c="black", linewidth = 0.5)


    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (0, -0.9), xy = (-0.4, -1.2),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })
    
    ax.text(-3.1,-3, '${n}$cm'.format(n=n), size = 12)
    ax.text(-1.25,-3.9, '${n}$cm'.format(n=n), size = 12)
    ax.text(0.6, -3, '${n}$cm'.format(n=n), size = 12)
    ax.text(0, -1, '${l}$cm'.format(l=l), size = 12)

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


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, n=n, l=l, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_083():
    stem = "다음 그림과 같은 전개도로 만든 정사각뿔의 겉넓이는?\n" \
            "① $$수식$${a1}rm cm^2$$/수식$$   ② $$수식$${a2}rm cm^2$$/수식$$   ③ $$수식$${a3}rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}rm cm^2$$/수식$$   ⑤ $$수식$${a5}rm cm^2$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n(밑넓이)$$수식$$={n}\\times{n}={s1}(rm cm^2)$$/수식$$\n" \
              "(옆넓이)$$수식$$=\\left({f}\\times{n}\\times{n2}\\right)\\times 4={s2}(rm cm^2)$$/수식$$\n" \
              "$$수식$$THEREFORE$$/수식$$ (겉넓이)$$수식$$=$$/수식$$(밑넓이)$$수식$$+$$/수식$$(옆넓이)\n" \
              "$$수식$$={s1}+{s2}$$/수식$$\n" \
              " $$수식$$={ans}(rm cm^2)$$/수식$$"

    n = random.choice([6,8,10,12])
    n2 = n-2
    s1 = n*n
    s2 = int(n*n2/2*4)
    ans = s1+s2
    f = "\\frac{1}{2}"

    a = (1,1)
    b = (1,-5)
    c = (7,-5)
    d = (7,1)

    p = (4,5)
    p2 = (-3,-2)
    p3 = (4,-9)
    p4 = (11,-2)

    p5 = (4,1)
       
    #ax = setChart(points=[a,b,c,d,p,p2,p3,p4,p5])
    fig, ax = plt.subplots(figsize=(3.5, 3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=b, p2=c)
    drawLine(ax=ax, p1=c, p2=d)
    drawLine(ax=ax, p1=d, p2=a)

    drawLine(ax=ax, p1=a, p2=p, decoration="||")
    drawLine(ax=ax, p1=d, p2=p, decoration="||")
    drawLine(ax=ax, p1=a, p2=p2, decoration="||")
    drawLine(ax=ax, p1=b, p2=p2, decoration="||")
    drawLine(ax=ax, p1=b, p2=p3, decoration="||")
    drawLine(ax=ax, p1=c, p2=p3, decoration="||")
    drawLine(ax=ax, p1=c, p2=p4, decoration="||")
    drawLine(ax=ax, p1=d, p2=p4, decoration="||")
    
    drawLine(ax=ax, p1=p, p2=p5)

    x1 = [1,1.6,1.6]
    y1 = [0.4,0.4,1]
    ax.plot(x1,y1, c="black", linewidth = 0.5)

    x2 = [1,1.6,1.6]
    y2 = [-4.4,-4.4,-5]
    ax.plot(x2,y2, c="black", linewidth = 0.5)

    x3 = [6.4,6.4,7]
    y3 = [-5,-4.4,-4.4]
    ax.plot(x3,y3, c="black", linewidth = 0.5)

    x4 = [6.4,6.4,7]
    y4 = [1,0.4,0.4]
    ax.plot(x4,y4, c="black", linewidth = 0.5)

    x5 = [4,4.6,4.6]
    y5 = [1.6,1.6,1]
    ax.plot(x5,y5, c="black", linewidth = 0.5)

    x6 = [4,1,-3,1,4,7,11,7,4]
    y6 = [5,1,-2,-5,-9,-5,-2,1,5]
    ax.fill(x6, y6, color="yellowgreen",alpha = 0.4)

    pp = mpatches.PathPatch(
    Path([p, (3,3), p5],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp)

    pp2 = mpatches.PathPatch(
    Path([d, (5.4,-2), c],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp2)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (2,4.8), xy = (3.7,3.8),
    arrowprops = {
              'color':'black',
              'connectionstyle':"arc3,rad=-0.4", 
              'edgecolor':'b',
              'arrowstyle':'->'
              })
    
    if n < 10 :
      k = 4.1
    else :
      k = 3.6
    if n2 < 10 :
      k2 = 0.1
    else :
      k2 = -0.3

    ax.text(k,-2.2, '${n}$cm'.format(n=n), size = 10)
    ax.text(k2,4.5, '${n2}$cm'.format(n2=n2), size = 10)

    aa_list = [ans-n2*3, ans-n2*2, ans-n2, ans, ans+n2, ans+n2*2, ans+n2*3]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, n2=n2, f=f, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_085():
    stem = "밑면의 반지름의 길이가 $$수식$${r}``rm cm$$/수식$$이고 옆넓이가 $$수식$${n}\\pi ``rm cm^3$$/수식$$인 원뿔의 전개도에서 부채꼴의 중심각의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$   ② $$수식$${a2}DEG $$/수식$$   ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$   ⑤ $$수식$${a5}DEG $$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n원뿔의 모선의 길이를 $$수식$$lcm$$/수식$$라 하면\n" \
              "$$수식$$\\pi\\times{r}\\times l={n}\\pi$$/수식$$ $$수식$$THEREFORE l={s1}$$/수식$$\n" \
              "부채꼴의 중심각의 크기를 $$수식$$x DEG$$/수식$$라 하면\n" \
              "$$수식$$2\\pi\\times{s1}\\times{f}=2\\pi\\times{r}$$/수식$$  $$수식$$THEREFORE x={ans}$$/수식$$\n" \
              "따라서 부채꼴의 중심각의 크기는 $$수식$${ans} DEG$$/수식$$이다.\n"

    while True :
      ans = random.choice([120,140,160,180])
      s1  = random.randint(6,16)
      if s1*ans%360 == 0:
        break
    r = int(s1*ans/360)
    n = r*s1 
    
    f = "\\frac{x}{360}"

    aa_list = [ans-90, ans-60, ans-30, ans, ans+30, ans+60, ans+90]
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

    stem = stem.format(r=r, n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(r=r, n=n, s1=s1, f=f, ans=ans)

    return stem, answer, comment



def solidfigure123_Stem_086():
    stem = "다음 그림과 같은 원뿔대의 겉넓이는?\n" \
            "① $$수식$${a1}\\pi``rm cm^2$$/수식$$   ② $$수식$${a2}\\pi``rm cm^2$$/수식$$   ③ $$수식$${a3}\\pi``rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm cm^2$$/수식$$   ⑤ $$수식$${a5}\\pi``rm cm^2$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n(두 밑넓이의 합)$$수식$$=\\pi\\times{r1}^2+\\pi\\times{r2}^2$$/수식$$\n" \
              "$$수식$$={s1}\\pi+{s2}\\pi={s3}\\pi(rm cm^2)$$/수식$$\n" \
              "(옆넓이)$$수식$$=\\pi\\times{r2}\\times{l2}-\\pi\\times{r1}\\times{l1}$$/수식$$\n" \
              "$$수식$$={s4}\\pi-{s5}\\pi={s6}\\pi(rm cm^3)$$/수식$$\n" \
              "$$수식$$THEREFORE$$/수식$$ (겉넓이)$$수식$$={s3}\\pi+{s6}\\pi={ans}\\pi(rm cm^2)$$/수식$$\n"

    r1 = random.randint(2,4)
    r2 = r1*2
    l1 = r2+2
    l2 = l1*2
    s1 = r1*r1
    s2 = r2*r2
    s3 = s1+s2
    s4 = r2*l2
    s5 = r1*l1
    s6 = s4-s5
    ans = s3+s6

    p1 = (-4,0)
    p2 = (-4,-5.5)
    p3 = (-6.2,-5.5)
    p4 = (-1.8,-5.5)

    p5 = (-4,-2.6)
    p6 = (-5,-2.6)
    p7 = (-3,-2.6)

    #ax = setChart(points=[p1,p2,p3,p4,p5,p6,p7])
    fig, ax = plt.subplots(figsize=(3.5, 3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawEllipse(ax=ax, center=(-4, -5.5), width=4.4, height=1.5, position="bottom")
    drawEllipse(ax=ax, center=(-4, -5.5), width=4.4, height=1.5, position="top", dash=True)
    drawEllipse(ax=ax, center=(-4, -2.6), width=2, height=0.8)

    drawLine(ax=ax, p1=p1, p2=p6, dash=True)
    drawLine(ax=ax, p1=p1, p2=p7, dash=True)
    drawLine(ax=ax, p1=p6, p2=p3)
    drawLine(ax=ax, p1=p7, p2=p4)


    drawLine(ax=ax, p1=p2, p2=p4)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p5, p2=p7)

    pp1 = mpatches.PathPatch(
    Path([p1, (-5.6,-1), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p2, (-1.9, -6), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p5, (-3.5, -2.9), p7],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    pp4 = mpatches.PathPatch(
    Path([p1, (-2, -2.25), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp4)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-1.7, -3.2), xy = (-3.5, -2.6),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })
    
    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-3.6, -6.7), xy = (-2.9, -5.7),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })
    
    x = [-4,-3.7,-3.7 ]
    y = [-5.2,-5.2,-5.5]
    ax.plot(x,y, c="black", linewidth = 0.5)

    x2 = [-4,-3.7,-3.7 ]
    y2 = [-2.3,-2.3,-2.6]
    ax.plot(x2,y2, c="black", linewidth = 0.5)
    
    if r1 < 10 :
      k = -2.2
    elif r1>=10 :
      k = -2.5
    
    ax.text(-1.7, -3.4, '${r1}$cm'.format(r1=r1), size = 12)
    ax.text(k-4,-1.1, '${l1}$cm'.format(l1=l1), size = 12)
    ax.text(-4.7, -6.9, '${r2}$cm'.format(r2=r2), size = 12)
    ax.text(-2.4, -2.25, '${l2}$cm'.format(l2=l2), size = 12)

    aa_list = [ans-3*l1, ans-2*l1, ans-l1, ans, ans+l1, ans+2*l1, ans+3*l1]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(r1=r1, r2=r2, l1=l1, l2=l2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_087():
    stem = "다음 그림과 같은 직각삼각형을 직선 $$수식$$l$$/수식$$을 회전축으로 하여 $$수식$$1$$/수식$$회전시킬 때 생기는 입체도형의 겉넓이는?\n" \
            "① $$수식$${a1}\\pi``rm cm^2$$/수식$$   ② $$수식$${a2}\\pi``rm cm^2$$/수식$$   ③ $$수식$${a3}\\pi``rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm cm^2$$/수식$$   ⑤ $$수식$${a5}\\pi``rm cm^2$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n회전체는 다음 그림과 같으므로\n" \
              "구하는 겉넓이는\n" \
              "$$수식$$\\pi\\times{r}^2+\\pi\\times{r}\\times{l}$$/수식$$\n" \
              "$$수식$$={s1}\\pi+{s2}\\pi$$/수식$$\n" \
              "$$수식$$={ans}\\pi(rm cm^2)$$/수식$$"

    r = random.randint(4,6)
    l = r*2+1
    s1 = r*r
    s2 = r*l
    ans = s1+s2

    l1 = (0,2)
    l2 = (0,0)
    l3 = (0,-4)
    l4 = (0,-5)
    p1 = (-2,-4)
    p2 = (2,-4)

    #ax = setChart(points=[l1,l2,l3,l4,p1])
    fig, ax = plt.subplots(figsize=(3.5, 4.5))
    plt.axis("off")
    ax.autoscale()
    ax.set_xlim(-3, 2)

    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=l3)

    x = [0,-2,0,0]
    y = [0,-4,-4,0]

    ax.fill(x, y, color="pink",alpha = 0.5)

    x2 = [0,-0.3,-0.3]
    y2 = [-3.7,-3.7,-4]

    ax.plot(x2,y2, c="black", linewidth = 0.5)

    pp = mpatches.PathPatch(
    Path([l2, (-1.6,-1.3), p1],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp)

    pp2 = mpatches.PathPatch(
    Path([p1, (-1,-4.7), l3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp2)

    ax.text(-1.35,-4.7, '${r}$cm'.format(r=r), size = 12)
    ax.text(-2.3,-1.7, '${l}$cm'.format(l=l), size = 12)
    ax.text(-0.18,0.8, '$\circlearrowleft$', size = 16)
    ax.text(-0.07,2.3, '$l$', size = 14)

    svg1 = saveSvg()

    #ax2 = setChart(points=[l2,l3,p1,p2])
    fig, ax2 = plt.subplots(figsize=(3.5, 4.5))
    plt.axis("off")
    ax2.autoscale()
    ax2.set_xlim(-3, 2)

    drawLine(ax=ax2, p1=(l2[0]-4, l2[1]), p2=(p1[0]-4, p1[1]))
    drawLine(ax=ax2, p1=(l2[0]-4, l2[1]), p2=(p2[0]-4, p2[1]))
    drawLine(ax=ax2, p1=(p2[0]-4, p2[1]), p2=(l3[0]-4, l3[1]))
    drawEllipse(ax=ax2, center=(-4,-4), width=4, height=1, position="bottom")
    drawEllipse(ax=ax2, center=(-4, -4), width=4, height=1, position="top", dash=True)

    pp3 = mpatches.PathPatch(
    Path([(l2[0]-4, l2[1]), (-2.2,-1.4), (p2[0]-4, p2[1])],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp3)

    pp4 = mpatches.PathPatch(
    Path([(p2[0]-4, p2[1]), (-3,-4.5), (l3[0]-4, l3[1])],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp4)

    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (-2.2,-4.8), xy = (-3,-4.2),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })

    ax2.text(-2.2,-4.9, '${r}$cm'.format(r=r), size = 12)
    ax2.text(-2.4,-1.8, '${l}$cm'.format(l=l), size = 12)
    ax2.scatter(-4,-4, c='black', s=15, alpha=1)   

    svg2 = saveSvg()

    aa_list = [ans-r*3, ans-r*2, ans-r, ans, ans+r, ans+r*2, ans+r*3]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(r=r, l=l, s1=s1, s2=s2, ans=ans)
    svg = [svg1,svg2]
    return stem, answer, comment, svg  




def solidfigure123_Stem_091():
    stem = "모선의 길이가 밑면의 반지름의 길이의 $$수식$${k}$$/수식$$배인 원뿔이 있다.\n" \
            "이 원뿔의 겉넓이가 $$수식$${n}\\pi``rm cm^2$$/수식$$일 때, 밑면의 반지름의 길이는?\n" \
            "① $$수식$${a1}``rm cm$$/수식$$   ② $$수식$${a2}``rm cm$$/수식$$   ③ $$수식$${a3}``rm cm$$/수식$$\n" \
            "④ $$수식$${a4}``rm cm$$/수식$$   ⑤ $$수식$${a5}``rm cm$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n밑면의 반지름의 길이를 $$수식$$r rm cm$$/수식$$라 하면 모선의 길이는 $$수식$${k}``r rm cm$$/수식$$이므로\n" \
              "$$수식$$\\pi\\times r^2+\\pi\\times r\\times {k}r={n}\\pi$$/수식$$\n" \
              "$$수식$${k2}\\pi r^2={n}\\pi,r^2={s1}$$/수식$$ $$수식$$THEREFORE r={ans}$$/수식$$\n" \
              "따라서 밑면의 반지름의 길이는 $$수식$${ans}``rm cm$$/수식$$이다.\n" 

    ans = random.randint(4,6)
    s1 = ans*ans
    k = random.randint(3,4)
    k2 = k+1
    n = s1*k2

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

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, k=k)
    answer = answer.format(result=result)
    comment = comment.format(n=n, s1=s1, k=k, k2=k2, ans=ans)

    return stem, answer, comment



def solidfigure123_Stem_094():
    stem = "다음 그림과 같은 사각뿔의 부피는?\n" \
            "① $$수식$${a1}``rm cm^3$$/수식$$   ② $$수식$${a2}``rm cm^3$$/수식$$   ③ $$수식$${a3}``rm cm^3$$/수식$$\n" \
            "④ $$수식$${a4}``rm cm^3$$/수식$$   ⑤ $$수식$${a5}``rm cm^3$$/수식$$\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n(부피)$$수식$$={f}\\times({n1}\\times{n2})\\times{h}={ans}(rm cm^3)$$/수식$$\n"

    while True :
      n1 = random.randint(3,6)
      n2 = n1+1
      h = n1*2
      if (n1*n2*h)%3 == 0 :
        break

    f = "\\frac{1}{3}"
    ans = int(n1*n2*h/3)

    p1 = (-0.18,2)
    p2 = (-0.8,0)
    p3 = (0,0)
    p4 = (0.5,0.6)
    p5 = (-0.4,0.6)
    p6 = (-0.18,0.3)

    #ax = setChart(points=[p1,p2,p3,p4,p5,p6])
    fig, ax = plt.subplots(figsize=(3.5, 4.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=p1, p2=p5, dash=True)
    drawLine(ax=ax, p1=p5, p2=p2, dash=True)
    drawLine(ax=ax, p1=p5, p2=p4, dash=True)
    drawLine(ax=ax, p1=p2, p2=p3)
    drawLine(ax=ax, p1=p3, p2=p4)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p1, p2=p4)
    drawLine(ax=ax, p1=p1, p2=p6)

    x = [-0.28,-0.28,-0.18]
    y = [0.3,0.4,0.4]
    ax.plot(x,y, c="black", linewidth = 0.5)

    x2 = [-0.74,-0.64,-0.7]
    y2 = [0.08,0.08,0]
    ax.plot(x2,y2, c="black", linewidth = 0.5)

    x3 = [-0.1,-0.04,0.07]
    y3 = [0,0.08,0.08]
    ax.plot(x3,y3, c="black", linewidth = 0.5)

    x4 = [0.4,0.35,0.44]
    y4 = [0.6,0.53,0.53]
    ax.plot(x4,y4, c="black", linewidth = 0.5)

    x5 = [-0.45,-0.35,-0.28]
    y5 = [0.52,0.52,0.6]
    ax.plot(x5,y5, c="black", linewidth = 0.5)
    p1 = (-0.18,2)
    p2 = (-0.8,0)
    p3 = (0,0)
    p4 = (0.5,0.6)
    p5 = (-0.4,0.6)
    p6 = (-0.18,0.3)

    pp1 = mpatches.PathPatch(
    Path([p2, (-0.4,-0.3), p3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p3, (0.55,0.2), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p1, (0.05,1.15), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (0.3, 1.4), xy = (-0.08,1.15),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.3", 
              'arrowstyle':'->'
              })
    
    ax.text(-0.6,-0.3, '${n1}$cm'.format(n1=n1), size = 12)
    ax.text(0.45,0.2, '${n2}$cm'.format(n2=n2), size = 12)
    ax.text(0.25, 1.45, '${h}$cm'.format(h=h), size = 12)

    aa_list = [ans-h*3, ans-h*2, ans-h, ans, ans+h, ans+h*2, ans+h*3]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, n1=n1, n2=n2, h=h, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_095():
    stem = "다음 그림과 같은 원뿔의 부피는?\n" \
            "① $$수식$${a1}\\pi ``rm cm^3$$/수식$$  ② $$수식$${a2}\\pi ``rm cm^3$$/수식$$\n" \
            "③ $$수식$${a3}\\pi ``rm cm^3$$/수식$$  ④ $$수식$${a4}\\pi ``rm cm^3$$/수식$$\n" \
            "⑤ $$수식$${a5}\\pi ``rm cm^3$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n(부피)$$수식$$={f}\\times\\pi\\times{r}^2\\times{h}={ans}\\pi(rm cm^3)$$/수식$$\n"

    f = "\\frac{1}{3}"
    while True :
      r = random.randint(3,5)
      h = r*2+1
      if (r*r*h)%3 == 0:
        break

    ans = int(r*r*h/3)

    p1 = (-4,0)
    p2 = (-4,-5)
    p3 = (-6.2,-5)
    p4 = (-1.8,-5)

    #ax = setChart(points=[p1,p2,p3,p4])
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax.autoscale()

    drawEllipse(ax=ax, center=(-4, -5), width=4.4, height=2, position="bottom")
    drawEllipse(ax=ax, center=(-4, -5), width=4.4, height=2, position="top", dash=True)
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p1, p2=p4)
    drawLine(ax=ax, p1=p2, p2=p4)
    drawLine(ax=ax, p1=p1, p2=p2)

    pp1 = mpatches.PathPatch(
    Path([p1, (-4.6,-2.5), p2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p2, (-2.9, -5.6), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-2, -5.8), xy = (-2.9, -5.2),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })
    
    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-5.4, -1.7), xy = (-4.2,-2.5),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })
    
    x = [-4,-3.7,-3.7]
    y = [-4.7,-4.7,-5]
    ax.plot(x,y, c="black", linewidth = 0.5)
    
    ax.text(-2, -6, '${r}$cm'.format(r=r), size = 12)
    ax.text(-6.1, -1.55, '${h}$cm'.format(h=h), size = 12)

    aa_list = [ans-3*r, ans-2*r, ans-r, ans, ans+r, ans+2*r, ans+3*r]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, r=r, h=h, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_098():
    stem = "밑면의 반지름의 길이가 $$수식$${r}``rm cm$$/수식$$인 원뿔의 부피가 $$수식$${v}\\pi ``rm cm^3$$/수식$$일 때, 이 원뿔의 높이는?\n" \
            "① $$수식$${a1}``rm cm$$/수식$$   ② $$수식$${a2}``rm cm$$/수식$$\n" \
            "③ $$수식$${a3}``rm cm$$/수식$$   ④ $$수식$${a4}``rm cm$$/수식$$   ⑤ $$수식$${a5}``rm cm$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n원뿔의 높이를 $$수식$$h``rm cm$$/수식$$라 하면\n" \
              "$$수식$${f1}\\times(\\pi\\times{r}^2)\\times h={v}\\pi$$/수식$$\n" \
              "$$수식$${f2}\\pi h={v}\\pi$$/수식$$  $$수식$$THEREFORE h={ans}$$/수식$$\n" \
              "따라서 원뿔의 높이는 $$수식$${ans}``rm cm$$/수식$$이다.\n"

    while True :
      ans = random.randint(8,14)
      r = random.randint(3,6)
      if r*r*ans%3 == 0 :
        break

    v = int(r*r*ans/3)
    f1 = "\\frac{1}{3}"

    ff2 = fractions.Fraction(fractions.Fraction(r*r)/fractions.Fraction(3))
    f2 = "\\frac{"+str(ff2.numerator)+"}{"+str(ff2.denominator)+"}"

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

    stem = stem.format(r=r, v=v, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f1=f1, f2=f2, r=r, v=v, ans=ans)

    return stem, answer, comment



def solidfigure123_Stem_099():
    stem = "다음 그림은 밑면이 합동인 원뿔과 원기둥을 붙여 놓은 입체도형이다. 이 입체도형의 부피는?\n" \
            "① $$수식$${a1}\\pi ``rm cm^3$$/수식$$  ② $$수식$${a2}\\pi ``rm cm^3$$/수식$$\n" \
            "③ $$수식$${a3}\\pi ``rm cm^3$$/수식$$  ④ $$수식$${a4}\\pi ``rm cm^3$$/수식$$\n" \
            "⑤ $$수식$${a5}\\pi ``rm cm^3$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n(부피)=(원뿔의 부피)+(원기둥의 부피)\n" \
              "$$수식$$={f}\\times(\\pi\\times{r}^2)\\times{h1}+(\\pi\\times{r}^2)\\times{h2}$$/수식$$\n" \
              "$$수식$$={s1}\\pi+{s2}\\pi={ans}\\pi(rm cm^3)$$/수식$$\n"

    f = "\\frac{1}{3}"
    while True :
      r = random.randint(2,9)
      if (r*r*r)%3 == 0 :
        break

    h1 = r    
    h2 = r*2
    s1 = int(r*r*h1/3)
    s2 = int(r*r*h2)
    ans = s1+s2

    p1 = (-4,0)
    p2 = (-4,-5)
    p3 = (-6.5,0)
    p4 = (-1.5,0)
    p5 = (-6.5,-5)
    p6 = (-1.5,-5)

    p7 = (-4,2.5)

    #ax = setChart(points=[p1,p2,p3,p4,p5,p6,p7])
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax.autoscale()

    drawEllipse(ax=ax, center=(-4, 0), width=5, height=1.3, position="bottom")
    drawEllipse(ax=ax, center=(-4, 0), width=5, height=1.3, position="top", dash=True)
    drawEllipse(ax=ax, center=(-4, -5), width=5, height=1.3, position="bottom")
    drawEllipse(ax=ax, center=(-4, -5), width=5, height=1.3, position="top", dash=True)
    drawLine(ax=ax, p1=p3, p2=p5)
    drawLine(ax=ax, p1=p4, p2=p6)

    drawLine(ax=ax, p1=p7, p2=p2)
    drawLine(ax=ax, p1=p7, p2=p3)
    drawLine(ax=ax, p1=p7, p2=p4)

    drawLine(ax=ax, p1=p7, p2=p4)
    drawLine(ax=ax, p1=p7, p2=p4)
    drawLine(ax=ax, p1=p1, p2=p4)
    drawLine(ax=ax, p1=p1, p2=p4)
    drawLine(ax=ax, p1=p2, p2=p6)

    x = [-4,-3.7,-3.7]
    y = [-4.7,-4.7,-5]
    ax.plot(x,y, c="black", linewidth = 0.5)

    x2 = [-4, -3.7, -3.7]
    y2 = [0.3,0.3,0]
    ax.plot(x2,y2, c="black", linewidth = 0.5)

    pp1 = mpatches.PathPatch(
    Path([p7, (-4.5, 1.25), p1],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p1, (-5, -2.5), p2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p2, (-2.75, -4.4), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-5.3, 2), xy = (-4.2, 1.25),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })
    
    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-1, -3.8), xy = (-2.75, -4.8),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })
    
    ax.text(-6.2, 2.1, '${r}$cm'.format(r=r), size = 13)
    ax.text(-1, -3.9, '${r}$cm'.format(r=r), size = 13)
    if h2 >= 10 :
      k = -2
    elif h2 <10 :
      k = -1.8
    ax.text(k-4.3, -2.5, '${h2}$cm'.format(h2=h2), size = 13)

    aa_list = [ans-3*(h1+h2), ans-2*(h1+h2), ans-(h1+h2), ans, ans+(h1+h2), ans+2*(h1+h2), ans+3*(h1+h2)]
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


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, r=r, h1=h1, h2=h2, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_101():
    stem = "다음 그림과 같은 원뿔대의 부피는?\n" \
            "① $$수식$${a1}\\pi ``rm cm^3$$/수식$$   ② $$수식$${a2}\\pi ``rm cm^3$$/수식$$   ③ $$수식$${a3}\\pi ``rm cm^3$$/수식$$\n" \
            "④ $$수식$${a4}\\pi ``rm cm^3$$/수식$$   ⑤ $$수식$${a5}\\pi ``rm cm^3$$/수식$$\n"
            
    answer = "(정답)\n{result}"
    comment = "(해설)\n(부피)=(큰 원뿔의 부피)-(작은 원뿔의 부피)\n" \
              "$$수식$$={f}\\times\\pi\\times{r2}^2\\times{h1}-{f}\\times\\pi\\times{r1}^2\\times{h2}$$/수식$$\n" \
              "$$수식$${s1}\\pi-{s2}\\pi={ans}\\pi(rm cm^3)$$/수식$$\n"

    while True :
      r1 = random.randint(2,6)
      r2 = r1*3
      h_1 = r1+2
      h_2 = h_1*2
      h1 = h_1+h_2
      h2 = h_1
      if (r2*r2*h1)%3 == 0 and (r1*r1*h2)%3 == 0 :
        break
    
    f = "\\frac{1}{3}"
    s1 = int(r2*r2*h1/3)
    s2 = int(r1*r1*h2/3)
    ans = s1-s2

    p1 = (-4,0)
    p2 = (-4,-5)
    p3 = (-7,-5)
    p4 = (-1,-5)

    p5 = (-4,-1.6)
    p6 = (-4.9,-1.6)
    p7 = (-3.1,-1.6)

    #ax = setChart(points=[p1,p2,p3,p4,p5,p6,p7])
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax.autoscale()

    drawEllipse(ax=ax, center=(-4, -5), width=6, height=1.9, position="bottom")
    drawEllipse(ax=ax, center=(-4, -5), width=6, height=1.9, position="top", dash=True)
    drawEllipse(ax=ax, center=(-4, -1.6), width=1.8, height=0.6)

    drawLine(ax=ax, p1=p1, p2=p6, dash=True)
    drawLine(ax=ax, p1=p1, p2=p7, dash=True)
    drawLine(ax=ax, p1=p6, p2=p3)
    drawLine(ax=ax, p1=p7, p2=p4)

    drawLine(ax=ax, p1=p2, p2=p3)
    drawLine(ax=ax, p1=p1, p2=p5, dash=True)
    drawLine(ax=ax, p1=p5, p2=p2)
    drawLine(ax=ax, p1=p5, p2=p6)

    pp1 = mpatches.PathPatch(
    Path([p1, (-3.6,-0.8), p5],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p6, (-4.45, -1.4), p5],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p5, (-3.2, -3.3), p2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    pp4 = mpatches.PathPatch(
    Path([p2, (-5.5,-5.7), p3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp4)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-2.7, -0.3), xy = (-3.8,-0.8),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.3", 
              'arrowstyle':'->'
              })
    
    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-5.4, -0.8), xy = (-4.45, -1.4),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })
    
    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-1.7, -2.6), xy = (-3.6, -3.3),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.2", 
              'arrowstyle':'->'
              })
    
    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-6.8, -6), xy = (-5.5,-5.3),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.2", 
              'arrowstyle':'->'
              })
    
    x = [-4,-3.7,-3.7]
    y = [-4.7,-4.7,-5]
    ax.plot(x,y, c="black", linewidth = 0.5)

    x2 = [-4, -3.7, -3.7]
    y2 = [-1.9,-1.9,-1.6]
    ax.plot(x2,y2, c="black", linewidth = 0.5)
    
    if r2>10 :
      k = -4.2
    else :
      k = -4
    
    ax.text(-6.6, -0.9, '${r1}$cm'.format(r1=r1), size = 12)
    ax.text(-2.7, -0.45, '${h_1}$cm'.format(h_1=h_1), size = 12)
    ax.text(k-4, -6.2, '${r2}$cm'.format(r2=r2), size = 12)
    ax.text(-1.7, -2.7, '${h_2}$cm'.format(h_2=h_2), size = 12)

    aa_list = [ans-90, ans-60, ans-30, ans, ans+30, ans+60, ans+90]
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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, r1=r1, r2=r2, h1=h1, h2=h2, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def solidfigure123_Stem_106():
    stem = "밑면의 반지름의 길이가 $$수식$${r1}``rm cm$$/수식$$이고, 높이가 $$수식$${h1}``rm cm$$/수식$$인 원뿔 모양의 아이스크림의 가격이 $$수식$$500$$/수식$$원이다. " \
            "아이스크림의 가격은 아이스크림의 부피에 정비례 한다고 할 때, 밑면의 반지름의 길이가 $$수식$${r2}``rm cm$$/수식$$이고, " \
            "높이가 $$수식$${h2}``rm cm$$/수식$$인 원뿔 모양의 아이스크림의 가격은?\n" \
            "① $$수식$${a1}$$/수식$$원   ② $$수식$${a2}$$/수식$$원   ③ $$수식$${a3}$$/수식$$원\n" \
            "④ $$수식$${a4}$$/수식$$원   ⑤ $$수식$${a5}$$/수식$$원\n" 
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n$$수식$$500$$/수식$$원인 아이스크림의 부피는\n" \
              "$$수식$${f}\\times\\pi\\times{r1}^2\\times{h1}={v1}\\pi(rm cm^3)$$/수식$$\n" \
              "가격을 구하려는 아이스크림의 부피는\n" \
              "$$수식$${f}\\times\\pi\\times{r2}^2\\times{h2}={v2}\\pi(rm cm^3)$$/수식$$\n" \
              "아이스크림의 가격이 부피에 정비례하므로 구하는\n" \
              "아이스크림의 가격을 $$수식$$x$$/수식$$원이라 하면\n" \
              "$$수식$${v1}\\pi:{v2}\\pi=500:x$$/수식$$\n" \
              "$$수식$${s1}:{s2}=500:x$$/수식$$ $$수식$$THEREFORE x={ans}$$/수식$$\n" \
              "따라서 구하는 아이스크림의 가격은 $$수식$${ans}$$/수식$$원이다.\n"

    s1 = 1

    while True :
      r1 = random.randint(3,6)
      h1 = random.randint(8,12)
      if r1*r1*h1%3 == 0 :
        break
    
    v1 = int(r1*r1*h1/3)
    
    while True :
      r2 = random.randint(8,14)
      h2 = random.randint(14,16)
      if r2*r2*h2%3 == 0 and (r2*r2*h2/3)%v1 == 0 :
        break
    
    v2 = int(r2*r2*h2/3)

    s2 = int(v2/v1)
    ans = 500*s2

    f = "\\frac{1}{3}"

    aa_list = [ans-1500, ans-1000, ans-500, ans, ans+500, ans+1000, ans+1500]
    a_list = []
    if s2 <= 3 :
      idx = 2
    else :
      idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    stem = stem.format(r1=r1, r2=r2, h1=h1, h2=h2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, r1=r1, r2=r2, h1=h1, h2=h2, v1=v1, v2=v2, s1=s1, s2=s2, ans=ans)

    return stem, answer, comment



def solidfigure123_Stem_108():
    stem = "다음 그림과 같은 직각삼각형 $$수식$$ABC$$/수식$$를 $$수식$${ac}$$/수식$$를 회전축으로 하여 $$수식$$1$$/수식$$회전시킬 때 생기는 회전체의 부피를 구하시오.\n" \
            "① $$수식$${a1}\\pi ``rm cm^3$$/수식$$   ② $$수식$${a2}\\pi ``rm cm^3$$/수식$$   ③ $$수식$${a3}\\pi ``rm cm^3$$/수식$$\n" \
            "④ $$수식$${a4}\\pi ``rm cm^3$$/수식$$   ⑤ $$수식$${a5}\\pi ``rm cm^3$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n주어진 직각삼각형 $$수식$$ABC$$/수식$$를 $$수식$${ac}$$/수식$$를 회전축으로 하여\n" \
              "$$수식$$1$$/수식$$회전시킬 때 생기는 회전체는 다음 그림과 같다.\n" \
              "꼭짓점 $$수식$$B$$/수식$$에서 $$수식$${ac}$$/수식$$에 내린 수선의 발을 $$수식$$H$$/수식$$라 하고\n" \
              "$$수식$${bh}$$/수식$$의 길이를 $$수식$$``r rm cm$$/수식$$라 하면\n" \
              "$$수식$${f1}\\times{n1}\\times{n2}={f1}\\times{n3}\\times r$$/수식$$ $$수식$$THEREFORE``r={r}$$/수식$$\n" \
              "$$수식$$THEREFORE$$/수식$$ (부피)$$수식$$=$$/수식$$(높이가 $$수식$${ah}$$/수식$$인 원뿔의 부피)\n" \
              "   $$수식$$+$$/수식$$(높이가 $$수식$${ch}$$/수식$$인 원뿔의 부피)\n" \
              "$$수식$$={f2}\\times\\pi r^2 \\times$$/수식$$$$수식$${ah}+{f2}\\times\\pi r^2 \\times {ch}$$/수식$$\n" \
              "$$수식$$={f2}\\pi r^2 \\times $$/수식$$$$수식$$({ah}+{ch})$$/수식$$\n" \
              "$$수식$$={f2}\\pi r^2 \\times$$/수식$$$$수식$${ac}$$/수식$$\n" \
              "$$수식$$={f2}\\pi\\times\\left({r}\\right)^2\\times{n3}$$/수식$$\n" \
              "$$수식$$={ans}\\pi(rm cm^3)$$/수식$$\n"

    ac = "\\overline{AC}"
    bh = "\\overline{BH}"
    ah = "\\overline{AH}"
    ch = "\\overline{CH}"
    f1 = "\\frac{1}{2}"
    f2 = "\\frac{1}{3}"

    n1 = random.choice([3,6])

    if n1 == 3:
      n2 = 4
      n3 = 5
    elif n1 == 6:
      n2 = 8
      n3 = 10

    rr = fractions.Fraction(fractions.Fraction(n1*n2)/fractions.Fraction(n3))
    if rr.denominator == 1 :
        r = int(rr)
    else :
        r = "\\frac{"+str(rr.numerator)+"}{"+str(rr.denominator)+"}"
    
    an = fractions.Fraction(fractions.Fraction(rr*rr*n3)/fractions.Fraction(3))

    if an.denominator == 1 :
        ans = int(an)
    else :
        ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    a = (0,1.55)
    b = (0,0)
    c = (1.2,0)

    #ax = setChart(points=[a,b,c])
    fig, ax = plt.subplots(figsize=(3.5, 3.5))
    plt.axis("off")
    ax.autoscale()

    drawPolygon(ax=ax, verts=[a,b,c])

    x = [0,0,1.2]
    y = [1.55,0,0]
    ax.fill(x, y, color="orange",alpha = 0.5)

    x2 = [0,0.1,0.1]
    y2 = [0.1,0.1,0]
    ax.plot(x2,y2, c="black", linewidth = 0.5)

    pp1 = mpatches.PathPatch(
    Path([a, (-0.3, 0.775), b],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([b, (0.6,-0.3), c],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([c, (0.9,1), a],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    ax.add_patch(pp3)

    ax.text(0.45,-0.3, '${n1}$cm'.format(n1=n1), size = 16)
    if n2 < 10 :
      k = -0.44
    elif n2 >= 10 :
      k = -0.5
    ax.text(k, 0.775, '${n2}$cm'.format(n2=n2), size = 16)
    ax.text(0.68,1, '${n3}$cm'.format(n3=n3), size = 16)

    ax.text(-0.05,1.58, 'A', size = 21)
    ax.text(-0.12,-0.07, 'B', size = 21)
    ax.text(1.22,-0.07, 'C', size = 21)

    svg1 = saveSvg()
    
    aa_list = [an-rr*3, an-rr*2, an-rr, an, an+rr, an+rr*2, an+rr*3]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    aa1, aa2, aa3, aa4, aa5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == an:
        result = answer_dict[i]
        break

    if aa1.denominator == 1 :
        a1 = "\\frac{"+str(aa1.numerator*n3)+"}{"+str(aa1.denominator*n3)+"}"
    else :
        a1 = "\\frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"
        
    if aa2.denominator == 1 :
        a2 = "\\frac{"+str(aa2.numerator*n3)+"}{"+str(aa2.denominator*n3)+"}"
    else :
        a2 = "\\frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = "\\frac{"+str(aa3.numerator*n3)+"}{"+str(aa3.denominator*n3)+"}"
    else :
        a3 = "\\frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    if aa4.denominator == 1 :
        a4 = "\\frac{"+str(aa4.numerator*n3)+"}{"+str(aa4.denominator*n3)+"}"
    else :
        a4 = "\\frac{"+str(aa4.numerator)+"}{"+str(aa4.denominator)+"}"

    if aa5.denominator == 1 :
        a5 = "\\frac{"+str(aa5.numerator*n3)+"}{"+str(aa5.denominator*n3)+"}"
    else :
        a5 = "\\frac{"+str(aa5.numerator)+"}{"+str(aa5.denominator)+"}"
        
    # comment image
    fig, ax2 = plt.subplots(figsize=(4.5, 3.5))
    plt.axis("off")
    ax2.autoscale()
    
    ax2.set_ylim(-3, 6)
    
    h = (0,0)
    a = (0,5.5)
    b = (-3,0)
    c = (0,-3)
    d = (3,0)
    
    drawEllipse(ax=ax2, center=(0, 0), width=6, height=1, position="bottom")
    drawEllipse(ax=ax2, center=(0, 0), width=6, height=1, position="top", dash=True)
    drawPolygon(ax=ax2, verts=[a,b,c,d])
    
    x = [-3,0,3]
    y = [0,5.5,0]
    ax2.fill(x, y, color="orange",alpha = 0.3)
    
    x = [-3,0,3]
    y = [-0.05,-3,-0.05]
    ax2.fill(x, y, color="orange",alpha = 0.3)
    
    drawLine(ax=ax2, p1=a, p2=c)
    drawLine(ax=ax2, p1=b, p2=h)
    
    pp1 = mpatches.PathPatch(
    Path([a, (-2.5, 3.5), b],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp1)
    ax2.text(-3.2, 3.5, '${n2}$cm'.format(n2=n2), size=16)

    pp2 = mpatches.PathPatch(
    Path([b, (-2.5, -2), c],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp2)
    ax2.text(-3.4, -2.2, '${n1}$cm'.format(n1=n1), size=16)

    pp3 = mpatches.PathPatch(
    Path([c, (1.5, 1.5), a],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp3)
    ax2.text(0.8, 1, '${n3}$cm'.format(n3=n3), size=16)
    
    pp4 = mpatches.PathPatch(
    Path([b, (-1.5, 0.7), h],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp4)
    ax2.annotate('r cm', ha='center', va='bottom',
                xytext=(-3.7, 1), xy=(-1.5, 0.3), size=16,
                arrowprops={
                    'color': 'black',
                    'edgecolor': 'b',
                    'connectionstyle': "arc3,rad=-0.3",
                    'arrowstyle': '->'
                })
    
    ax2.text(a[0]-0.2, a[1]+0.2, 'A', size=16)
    ax2.text(b[0]-0.5, b[1]-0.2, 'B', size=16)
    ax2.text(h[0]+0.1, h[1]-0.2, 'H', size=16)
    ax2.text(c[0]-0.2, c[1]-0.8, 'C', size=16)
    
    svg2 = saveSvg()


    stem = stem.format(ac=ac, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ac=ac, bh=bh, ah=ah, ch=ch, n1=n1, n2=n2, n3=n3, f1=f1, f2=f2, r=r, ans=ans)
    svg = [svg1, svg2]
    return stem, answer, comment, svg  



def solidfigure123_Stem_116():
    stem = "다음 그림과 같은 평면도형을 직선 $$수식$$l$$/수식$$을 회전축으로 하여 $$수식$$1$$/수식$$회전시킬 때 생기는 회전체의 겉넓이는?\n" \
            "① $$수식$${a1}\\pi``rm cm^2$$/수식$$   ② $$수식$${a2}\\pi``rm cm^2$$/수식$$   ③ $$수식$${a3}\\pi``rm cm^2$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm cm^2$$/수식$$   ⑤ $$수식$${a5}\\pi``rm cm^2$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n주어진 평면도형을 직선 $$수식$$l$$/수식$$을 회전축으로 하여 \n" \
              "$$수식$$1$$/수식$$회전 시킬 때 생기는 회전체는 다음 그림과 같으므로\n" \
              "(겉넓이)=(원뿔의 옆넓이)+(반구의 겉넓이)+(큰 원의 넓이)-(작은 원의 넓이)\n" \
              "$$수식$$=\\pi\\times{r1}\\times{n1}+(4\\pi\\times{r2}^2)\\times{f}$$/수식$$\n" \
              "$$수식$$+(\\pi\\times{r1}^2-\\pi\\times{r2}^2)$$/수식$$\n" \
              "$$수식$$={s1}\\pi+{s2}\\pi+{s3}\\pi$$/수식$$\n" \
              "$$수식$$={ans}\\pi(rm cm^2)$$/수식$$\n"

    n_1 = random.randint(2,5)
    n_2 = n_1+2
    n_3 = n_1+n_2+2
    
    r1 = n_1+n_2
    n1 = n_3
    r2 = n_1
    f = "\\frac{1}{2}"
    s1 = r1*n1
    s2 = int(4*r2*r2/2)
    s3 = (r1*r1)-(r2*r2)
    ans = s1+s2+s3

    l1 = (0,2)
    l2 = (0,0)
    l3 = (0,-6)
    l4 = (0,-8)
    l4_2 = (0,-9)
    p1 = (-8,-6)
    p2 = (-3,-6)
    p3 = (8,-6)
    p4 = (3,-6)

    #ax = setChart(points=[l1,l2,l3,l4,p1,p2])
    fig, ax = plt.subplots(figsize=(3.5, 3.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=l2, p2=p1)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=l3, dash=True)

    x = [0,-8,0,0]
    y = [0,-6,-6,0]

    ax.fill(x, y, color="purple",alpha = 0.3)

    x2 = [0,-0.4,-0.4]
    y2 = [-5.6,-5.6,-6]

    ax.plot(x2,y2, c="black", linewidth = 0.5)

    pp = mpatches.Wedge(l3, r=3, theta1=90,
                                theta2=180, fc='white', fill=True, alpha=1)
    ax.add_patch(pp)

    x3 = []
    y3 = []

    for i in range(90,181) :
      x3.append(3*math.cos(math.radians(i)))
      y3.append(-6+3*math.sin(math.radians(i)))

    ax.plot(x3,y3, c="black", linewidth = 1)

    pp2 = mpatches.PathPatch(
    Path([l2, (-5,-1.8), p1],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p1, (-5.5,-7.3), p2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp3)

    pp4 = mpatches.PathPatch(
    Path([p2, (-1.5,-7.15), l3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp4)

    pp5 = mpatches.PathPatch(
    Path([l2, (1.1,-1.5), (0,-3)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp5)

    pp6 = mpatches.PathPatch(
    Path([(0,-3), (1.1,-4.5), l3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp6)

    ax.text(0.7,-1.5, '${n_1}$cm'.format(n_1=n_1), size = 14)
    ax.text(0.7,-4.5, '${n_1}$cm'.format(n_1=n_1), size = 14)
    ax.text(-2,-7.35, '${n_1}$cm'.format(n_1=n_1), size = 14)
    ax.text(-6,-7.4, '${n_2}$cm'.format(n_2=n_2), size = 14)
    ax.text(-5.5,-1.6, '${n_3}$cm'.format(n_3=n_3), size = 14)
    ax.text(-0.2,0.8, '$\circlearrowleft$', size = 16)
    ax.text(-0.07,2.3, '$l$', size = 14)

    svg1 = saveSvg()

    #ax2 = setChart(points=[l1,l2,l3,l4,p1,p2,p3,p4])
    fig, ax2 = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax2.autoscale()

    drawLine(ax=ax2, p1=(l1[0]-4,l1[1]), p2=(l4_2[0]-4, l4_2[1]))
    drawLine(ax=ax2, p1=(l2[0]-4,l2[1]), p2=(p1[0]-4, p1[1]))
    drawLine(ax=ax2, p1=(l2[0]-4, l2[1]), p2=(p3[0]-4, p3[1]))
    drawLine(ax=ax2, p1=(p1[0]-4,p1[1]), p2=(l3[0]-4, l3[1]))
    drawLine(ax=ax2, p1=(l2[0]-4,p1[1]), p2=(p3[0]-4, p3[1]))
    drawEllipse(ax=ax2, center=(-4,-6), width=16, height=2.2, position="bottom")
    drawEllipse(ax=ax2, center=(-4, -6), width=16, height=2.2, position="top", dash=True)
    drawCircle(ax2, (-4,-6), radius=3, fill=False, dash=True, position="top")
    drawEllipse(ax=ax2, center=(-4, -6), width=6, height=1.3, dash=True)

    pp7 = mpatches.PathPatch(
    Path([(l2[0]-4,l2[1]), (-9.5,-1.6), (p1[0]-4, p1[1])],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp7)

    pp8 = mpatches.PathPatch(
        Path([(p1[0]-4, p1[1]), (-9.5, -7.08), p2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp8)

    pp9 = mpatches.PathPatch(
        Path([(p2[0]-4, p2[1]), (-5.5, -7.02), (l3[0]-4, l3[1])],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp9)

    pp10 = mpatches.PathPatch(
    Path([(l2[0]-4,l2[1]), (-2.9,-1.5), (-4,-3)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp10)

    pp11 = mpatches.PathPatch(
    Path([(-4,-3), (-2.9,-4.5), (l3[0]-4,l3[1])],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp11)

    x3 = [-4,-4.6,-4.6]
    y3 = [-5.4,-5.4,-6]
    ax2.plot(x3,y3, c="black", linewidth = 0.5)

    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (-10.8,-7.8), xy = (-9.5,-6.4),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })
    
    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (-5.5,-8), xy = (-5.5,-6.3),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0", 
              'arrowstyle':'->'
              })
    
    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (-1,0), xy = (-3.6,-1.5),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })
    
    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (0.5,-1.8), xy = (-3.6,-4.5),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })

    ax2.text(-6.5,-8.7, '${n_1}$cm'.format(n_1=n_1), size = 11)
    ax2.text(-2,0.2, '${n_1}$cm'.format(n_1=n_1), size = 11)
    ax2.text(-0.4,-1.7, '${n_1}$cm'.format(n_1=n_1), size = 11)
    ax2.text(-12.9,-8.2, '${n_2}$cm'.format(n_2=n_2), size = 11)
    ax2.text(-10.8,-1.8, '${n_3}$cm'.format(n_3=n_3), size = 11)
    ax2.text(-4.5,0.8, '$\circlearrowleft$', size = 16)
    ax2.text(-4.07,2.3, '$l$', size = 12)

    svg2 = saveSvg()

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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(r1=r1, r2=r2, n1=n1, f=f, s1=s1, s2=s2, s3=s3, ans=ans)
    svg = [svg1,svg2]
    return stem, answer, comment, svg  



def solidfigure123_Stem_118():
    stem = "다음 그림과 같이 원기둥에 구와 원뿔이 꼭 맞게 들어있다. 구의 부피가 $$수식$${v}\\pi ``rm cm^3$$/수식$$일 때, " \
            "원뿔의 부피를 $$수식$$a``rm cm^3$$/수식$$, 원기둥의 부피를 $$수식$$b``rm cm^3$$/수식$$라 하자. 이때, $$수식$$a+b$$/수식$$의 값은?\n" \
            "① $$수식$${a1}\\pi$$/수식$$   ② $$수식$${a2}\\pi$$/수식$$   ③ $$수식$${a3}\\pi$$/수식$$\n" \
            "④ $$수식$${a4}\\pi$$/수식$$   ⑤ $$수식$${a5}\\pi$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n구의 반지름의 길이를 $$수식$$r``rm cm$$/수식$$라 하면\n" \
              "$$수식$${f1}\\pi r^3={v}\\pi$$/수식$$  $$수식$$THEREFORE r^3={s1}$$/수식$$\n" \
              "원뿔과 원기둥의 밑면의 반지름의 길이는 $$수식$$r``rm cm$$/수식$$,\n" \
              "높이는 $$수식$$2r``rm cm$$/수식$$이므로\n" \
              "$$수식$$a={f2}\\times\\pi r^2\\times 2r={f3}\\pi r^3={f3}\\pi\\times{s1}={s2}\\pi$$/수식$$\n" \
              "$$수식$$b=\\pi r^2\\times 2r=2\\pi r^3=2\\pi\\times{s1}={s3}\\pi$$/수식$$\n" \
              "$$수식$$THEREFORE a+b={ans}\\pi$$/수식$$\n"

    f1 = "\\frac{4}{3}"
    f2 = "\\frac{1}{3}"
    f3 = "\\frac{2}{3}"

    while True :
      v = random.randint(6,12)*4
      if (v*3/4)%3 == 0 :
        break
       
    s1 = int(v*3/4)
    s2 = int(s1*2/3)
    s3 = 2*s1
    ans = s2+s3

    p1 = (-4,0)
    p2 = (-4,-5)
    p3 = (-6.3,0)
    p4 = (-1.7,0)
    p5 = (-6.3,-5)
    p6 = (-1.7,-5)

    p7 = (-4,-0.2)

    #ax = setChart(points=[p1,p2,p3,p4,p5,p6,p7])
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax.autoscale()

    drawEllipse(ax=ax, center=(-4, 0), width=4.6, height=1.4)
    drawEllipse(ax=ax, center=(-4, -5), width=4.6, height=1.4)
    drawLine(ax=ax, p1=p3, p2=p5)
    drawLine(ax=ax, p1=p4, p2=p6)
    
    drawCircle(ax=ax, center=(-4, -2.5), radius=2.3)
    drawEllipse(ax=ax, center=(-4, -2.5), width=4.6, height=1.4, position="top", dash=True)
    drawEllipse(ax=ax, center=(-4, -2.5), width=4.6, height=1.4, position="bottom")

    drawLine(ax=ax, p1=p7, p2=p5)
    drawLine(ax=ax, p1=p7, p2=p6)

    k = 12

    aa_list = [ans-k*3, ans-k*2, ans-k, ans, ans+k, ans+k*2, ans+k*3]
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

    stem = stem.format(v=v, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(v=v, f1=f1, f2=f2, f3=f3, s1=s1, s2=s2, s3=s3, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def solidfigure123_Stem_124():
    stem = "다음 그림의 색칠한 부분을 직선 $$수식$$l$$/수식$$을 회전축으로 하여 $$수식$$1$$/수식$$회전시킬 때 생기는 회전체의 겉넓이는?\n" \
            "① $$수식$${a1}\\pi ``rm cm^3$$/수식$$   ② $$수식$${a2}\\pi ``rm cm^3$$/수식$$   ③ $$수식$${a3}\\pi ``rm cm^3$$/수식$$\n" \
            "④ $$수식$${a4}\\pi ``rm cm^3$$/수식$$   ⑤ $$수식$${a5}\\pi ``rm cm^3$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n회전체는 다음 그림과 같으므로\n" \
              "구하는 겉넓이는\n" \
              "$$수식$$4\\pi\\times{r}^2+2\\pi\\times{r}\\times{h}$$/수식$$\n" \
              "$$수식$$={s1}\\pi+{s2}\\pi$$/수식$$\n" \
              "$$수식$$={ans}\\pi(rm cm^3)$$/수식$$\n"

    r = random.randint(3,5)
    h = r*3
    s1 = 4*r*r
    s2 = 2*r*h
    ans = s1+s2

    l1 = (0,2)
    l2 = (0,0)
    l3 = (0,-9)
    l4 = (0,-11)
    p1 = (-3,0)
    p2 = (-3,-9)

    #ax = setChart(points=[l1,l2,l3,l4,p1,p2])
    fig, ax = plt.subplots(figsize=(2.5, 4))
    plt.axis("off")
    ax.autoscale()
    ax.set_xlim(-5,5)

    drawLine(ax=ax, p1=l1, p2=l4)
    drawLine(ax=ax, p1=l2, p2=p1, dash=True)
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p2, p2=l3, dash=True)

    x = [0,-3,-3,0]
    y = [0,0,-9,-9]

    ax.fill(x, y, color="lightpink",alpha = 0.5)

    pp = mpatches.Wedge(l3, r=3, theta1=90,
                                theta2=180, fc='white', fill=True, alpha=1)
    ax.add_patch(pp)

    pp2 = mpatches.Wedge(l2, r=3, theta1=180,
                                theta2=270, fc='white', fill=True, alpha=1)
    ax.add_patch(pp2)

    x2 = []
    y2 = []

    for i in range(180,271) :
      x2.append(3*math.cos(math.radians(i)))
      y2.append(3*math.sin(math.radians(i)))

    ax.plot(x2,y2, c="black", linewidth = 1)

    x3 = []
    y3 = []

    for i in range(90,181) :
      x3.append(3*math.cos(math.radians(i)))
      y3.append(-9+3*math.sin(math.radians(i)))

    ax.plot(x3,y3, c="black", linewidth = 1)

    pp3 = mpatches.PathPatch(
    Path([p1, (-1.5,1.2), l2],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp3)

    pp4 = mpatches.PathPatch(
    Path([l2, (1.2,-1.5), (0,-3)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp4)

    pp5 = mpatches.PathPatch(
    Path([(0,-3), (1.2,-4.5), (0,-6)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp5)

    pp6 = mpatches.PathPatch(
    Path([(0,-6), (1.2,-7.5), l3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp6)

    pp7 = mpatches.PathPatch(
    Path([p2, (-1.5,-10.2), l3],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp7)

    ax.text(-2.5,0.9, '${r}$cm'.format(r=r), size = 14)
    ax.text(0.8,-1.6, '${r}$cm'.format(r=r), size = 14)
    ax.text(0.8,-4.6, '${r}$cm'.format(r=r), size = 14)
    ax.text(0.8,-7.6, '${r}$cm'.format(r=r), size = 14)
    ax.text(-2.5,-10.5, '${r}$cm'.format(r=r), size = 14)
    ax.text(-0.32,0.8, '$\circlearrowleft$', size = 16)
    ax.text(-0.07,2.3, '$l$', size = 14)

    svg1 = saveSvg()

    p1 = (-4,0)
    p2 = (-4,-6)
    p3 = (-6,0)
    p4 = (-2,0)
    p5 = (-6,-6)
    p6 = (-2,-6)
    p = (0,-6)

    #ax2 = setChart(points=[p1,p2,p3,p4,p5,p6,p])
    fig, ax2 = plt.subplots(figsize=(4, 4))
    plt.axis("off")
    ax2.autoscale()

    drawEllipse(ax=ax2, center=(-4, 0), width=4, height=1.4)
    drawEllipse(ax=ax2, center=(-4, -6), width=4, height=1.4, position="bottom")
    drawEllipse(ax=ax2, center=(-4, -6), width=4, height=1.4, position="top", dash=True)
    drawLine(ax=ax2, p1=p3, p2=p5)
    drawLine(ax=ax2, p1=p4, p2=p6)
    drawLine(ax=ax2, p1=p1, p2=p4)
    drawLine(ax=ax2, p1=p2, p2=p6)

    pp1 = mpatches.PathPatch(
    Path([p1, (-3, 0.7), p4],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp1)

    pp2 = mpatches.PathPatch(
    Path([p4, (-0.5, -2.5), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp2)

    pp3 = mpatches.PathPatch(
    Path([p2, (-3, -6.7), p6],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")
    ax2.add_patch(pp3)


    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (-2.3, 1.2), xy = (-3, 0.3),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=0.4", 
              'arrowstyle':'->'
              })

    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (-2.2, -7), xy = (-3, -6.3),
    arrowprops = {
              'color':'black',
              'edgecolor':'b',
              'connectionstyle':"arc3,rad=-0.4", 
              'arrowstyle':'->'
              })    

    ax2.text(-2.3, 1.1, '${r}$cm'.format(r=r), size = 12)
    ax2.text(-2.25, -7.3, '${r}$cm'.format(r=r), size = 12)
    ax2.text(-1.1, -2.9, '${h}$cm'.format(h=h), size = 12)

    drawCircle(ax2, p2, radius=2, fill=False, dash=True, position="top")
    drawCircle(ax2, p1, radius=2, fill=False, dash=True, position="bottom")

    svg2 = saveSvg()

    aa_list = [ans-h*3, ans-h*2, ans-h, ans, ans+h, ans+h*2, ans+h*3]
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


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(r=r, h=h, s1=s1, s2=s2, ans=ans)
    svg = [svg1,svg2]
    return stem, answer, comment, svg


if __name__ == "__main__":
  stem, answer, comment, svg = solidfigure123_Stem_124()
  print(stem)
  print(answer)
  print(comment)
  plt.show()
