#from  draw2svg import *
import matplotlib.pyplot as plt
import numpy as np
import random
import fractions
import math
import pandas as pd
import matplotlib 
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
        
plt.rcParams["font.family"] = "NanumGothic"

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




def statistics124_Stem_002():
    stem = "다음 줄기와 잎 그림은 어느날 $$수식$$16$$/수식$$곳의 지역의 최고 기온을 조사하여 그린 것이다. " \
            "최고 기온이 $$수식$$25 DEG C$$/수식$$이상인 지역의 수를 $$수식$$a$$/수식$$곳, " \
            "$$수식$$23.5 DEG C$$/수식$$ 이하인 지역의 수를 $$수식$$b$$/수식$$곳이라 할 때, " \
            "$$수식$$a+b$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n최고 기온이 $$수식$$25 DEG C$$/수식$$ 이상인 지역은\n" \
              "$$수식$${s1}+{s2}={a}$$/수식$$(곳)이므로 $$수식$$a={a}$$/수식$$\n" \
              "최고 기온이 $$수식$$23.5 DEG C$$/수식$$이하인 지역은\n" \
              "$$수식$${s3}+{s4}={b}$$/수식$$(곳)이므로 $$수식$$b={b}$$/수식$$\n" \
              "$$수식$$THEREFORE a+b={a}+{b}={ans}$$/수식$$\n"

    list = []
    r_num = random.randint(220,269)

    while True :
        r_num = random.randint(220,270)
        if r_num not in list :
          list.append(r_num)
        if len(list) == 16 :
          break

    list.sort()
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []

    for i in range(0, len(list)):
      if list[i] >= 220 and list[i] < 230 :
        l2.append(str(list[i]%220))
      elif list[i] >= 230 and list[i] < 240 :
        l3.append(str(list[i]%230))
      elif list[i] >= 240 and list[i] < 250 :
        l4.append(str(list[i]%240))
      elif list[i] >= 250 and list[i] < 260 :
        l5.append(str(list[i]%250))
      elif list[i] >= 260 and list[i] < 270 :
        l6.append(str(list[i]%260))
    
    leaf_2 = ""
    for s in l2 :
        leaf_2 += s + "     "

    leaf_3 = ""
    for s in l3 :
        leaf_3 += s + "     "

    leaf_4 = ""
    for s in l4 :
        leaf_4 += s + "     "

    leaf_5 = ""
    for s in l5 :
        leaf_5 += s + "     "

    leaf_6 = ""
    for s in l6 :
        leaf_6 += s + "     "

    fig, ax =plt.subplots(1,1, figsize=(4,4))
    data=[[22,leaf_2],
          [23,leaf_3],
          [24,leaf_4],
          [25,leaf_5],
          [26,leaf_6]]
    column_labels=["줄기", "잎"]
    df=pd.DataFrame(data,columns=column_labels)
    ax.axis('tight')
    ax.axis('off')
    tb = ax.table(cellText=df.values,colLabels=df.columns, loc="center", cellLoc='left')
    tb.scale(1,1)
    tb.set_fontsize(20)
    tb.auto_set_column_width(False)

    s1 = len(l5)
    s2 = len(l6)
    a = s1+s2

    s3 = len(l2)
    s4 = 0

    for i in range(0, len(list)):
      if list[i]<=235 and list[i]>=230:
        s4 +=1
    b = s3+s4

    ans = a+b

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
    
    tb.set_fontsize(15)
    tb.scale(2, 2)
    
    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, a=a, b=b, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def statistics124_Stem_009():
    stem = "다음 도수분포표는 어느 수영반 학생 $$수식$${n}$$/수식$$명의 숨 참기 기록을 조사하여 나타낸 것이다. " \
            "도수가 가장 작은 계급의 도수를 $$수식$$a$$/수식$$명, 기록이 $$수식$$60$$/수식$$초 이상인 학생을 $$수식$$b$$/수식$$명이라 할 때, " \
            "$$수식$$a+b$$/수식$$의 값을 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n기록이 $$수식$$80$$/수식$$초 이상 $$수식$$100$$/수식$$초 미만인 계급의 도수는\n" \
              "$$수식$${n}-({n1}+{n2}+{n3}+{n4})={n5}$$/수식$$(명)\n" \
              "따라서 도수가 가장 작은 계급은 $$수식$${s1}$$/수식$$초 이상 $$수식$${s2}$$/수식$$\n" \
              "초 미만이므로\n" \
              "$$수식$$a={a}$$/수식$$\n" \
              "또, 기록이 $$수식$$60$$/수식$$초 이상인 학생은 $$수식$${n4}+{n5}={b}$$/수식$$(명)\n" \
              "이므로\n" \
              "$$수식$$b={b}$$/수식$$\n" \
              "$$수식$$THEREFORE a+b={a}+{b}={result}$$/수식$$\n"
    
    n = random.choice([30,40])

    while True :
      n1 = random.randint(1,10)
      n2 = random.randint(1,10)
      n3 = random.randint(1,10)
      n4 = random.randint(1,10)
      n5 = random.randint(1,10)
      sum = n1+n2+n3+n4+n5
      list = [n1,n2,n3,n4,n5]
      list2 = set(list)
      if sum == 30 and len(list) == len(list2):
        break

    if min(list) == n1 :
      s1 = 0
      s2 = 20
    elif min(list) == n2 :
      s1 = 20
      s2 = 40
    elif min(list) == n3 :
      s1 = 40
      s2 = 60
    elif min(list) == n4 :
      s1 = 60
      s2 = 80
    elif min(list) == n5 :
      s1 = 80
      s2 = 100
    
    a = min(list)
    b = n4+n5
    result = a+b

    fig, ax =plt.subplots(1,1, figsize=(4,4))
    data=[["0 이상 20 미만",n1],
          ["20 이상 40 미만",n2],
          ["40 이상 60 미만",n3],
          ["60 이상 80 미만",n4],
          ["80 이상 100 미만",""],
          ["합계",n]]
    column_labels=["기록(초)", "도수(명)"]
    df=pd.DataFrame(data,columns=column_labels)
    ax.axis('tight')
    ax.axis('off')
    tb = ax.table(cellText=df.values,colLabels=df.columns, loc="center", cellLoc='center')
    tb.scale(1,3)
    tb.set_fontsize(20)
    tb.auto_set_column_width(1)
    
    stem = stem.format(n=n)
    answer = answer.format(result=result)
    comment = comment.format(s1=s1, s2=s2, n=n, n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, a=a, b=b, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg  



def statistics124_Stem_011():
    stem = "다음 도수분포표는 {name}이네 반 학생 $$수식$${n}$$/수식$$명의 $$수식$$1$$/수식$$년 동안의 미술관 방문 횟수를 조사하여 나타낸 것이다. " \
            "이 때 미술관 방문 횟수가 $$수식$$12$$/수식$$회 이상인 학생은 전체의 몇 %인가?\n" \
            "① $$수식$${a1}%$$/수식$$  ② $$수식$${a2}%$$/수식$$   ③ $$수식$${a3}%$$/수식$$\n" \
            "④ $$수식$${a4}%$$/수식$$  ⑤ $$수식$${a5}%$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n미술관 방문 횟수가 $$수식$$12$$/수식$$회 이상 $$수식$$15$$/수식$$회 미만인 학생은\n\n" \
              "$$수식$${n}-({n1}+{n2}+{n3}+{n5})={n4}$$/수식$$(명)\n" \
              "따라서 미술과 방문 횟수가 $$수식$$12$$/수식$$회 이상인 학생은\n" \
              "$$수식$${n4}+{n5}={n6}$$/수식$$(명)이므로 전체의\n" \
              "$$수식$${f}\\times100={ans}(%)$$/수식$$이다.\n"

    name = random.choice(["수진","성찬","효진","유정","지윤","동혁"])
    n = 40

    while True :
      n1 = random.randint(1,12)
      n2 = random.randint(1,12)
      n3 = random.randint(1,12)
      n4 = random.randint(1,12)
      n5 = random.randint(1,12)
      sum = n1+n2+n3+n4+n5
      n6 = n4+n5
      if sum == n and n6*100%n == 0 :
        break
    
    n6 = n4+n5
    f = "\\frac{"+str(n6)+"}{"+str(n)+"}"
    ans = int(n6*100/n)

    fig, ax =plt.subplots(1,1, figsize=(4,4))
    data=[["3 이상 6 미만",n1],
          ["6 이상 9 미만",n2],
          ["9 이상 12 미만",n3],
          ["12 이상 15 미만",""],
          ["15 이상 18 미만",n5],
          ["합계",n]]
    column_labels=["방문 횟수(회)", "도수(명)"]
    df=pd.DataFrame(data,columns=column_labels)
    ax.axis('tight')
    ax.axis('off')
    tb = ax.table(cellText=df.values,colLabels=df.columns, loc="center", cellLoc='center')
    #tb.scale(1,3)
    tb.auto_set_column_width(True)
    
    tb.set_fontsize(20)
    tb.scale(1,3)

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

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, name=name)
    answer = answer.format(result=result)
    comment = comment.format(n=n, n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, n6=n6, f=f, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def statistics124_Stem_012():
    stem = "다음 표는 어느 학교 학생 $$수식$${n}$$/수식$$명의 몸무게를 조사하여 나타낸 도수분포표이다. " \
            "몸무게가 $$수식$$50``rm {{kg}}$$/수식$$ 이상 $$수식$$60``rm {{kg}}$$/수식$$ 미만인 학생이 전체의 $$수식$${p}%$$/수식$$일 때, " \
            "$$수식$$x$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$50``rm {{kg}}$$/수식$$ 이상 $$수식$$60``rm {{kg}}$$/수식$$ 미만인 학생이 전체의 $$수식$${p}%$$/수식$$이므로\n" \
              "$$수식$${n}\\times{f}={n7}$$/수식$$(명)\n" \
              "따라서 $$수식$${n4}+x={n7}$$/수식$$이므로 $$수식$$x={ans}$$/수식$$\n"

    n = 50

    while True :
      n1 = random.randint(1,12)
      n2 = random.randint(1,12)
      n3 = random.randint(1,12)
      n4 = random.randint(1,12)
      n5 = random.randint(1,12)
      n6 = random.randint(1,12)
      sum = n1+n2+n3+n4+n5+n6
      if sum == n and n5>4:
        break

    p = (n4+n5)*2
    f = "\\frac{"+str(p)+"}{100}"
    n7 = n4+n5
    ans = n5

    fig, ax =plt.subplots(1,1, figsize=(4.5,4.5))
    data=[["35 이상 40 미만",n1],
          ["40 이상 45 미만",""],
          ["45 이상 50 미만",n3],
          ["50 이상 55 미만",n4],
          ["55 이상 60 미만",'$x$'],
          ["60 이상 65 미만",n6],
          ["합계",n]]
    column_labels=["몸무게(kg)", "도수(명)"]
    df=pd.DataFrame(data,columns=column_labels)
    ax.axis('tight')
    ax.axis('off')
    tb = ax.table(cellText=df.values,colLabels=df.columns, loc="center", cellLoc='center')
    tb.scale(1,3)
    tb.set_fontsize(20)
    tb.auto_set_column_width(True)

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

    stem = stem.format(n=n, p=p, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(p=p, n=n, f=f, n7=n7, n4=n4, n5=n5, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg



def statistics124_Stem_013():
    stem = "다음은 직장인 $$수식$${n}$$/수식$$명의 헌혈 횟수를 조사하여 나타낸 도수분포표이다. " \
            "$$수식$$8$$/수식$$회 이상 $$수식$$12$$/수식$$회 미만인 계급의 도수가 " \
            "$$수식$$16$$/수식$$회 이상 $$수식$$20$$/수식$$회 미만인 계급의 도수의 $$수식$${k}$$/수식$$배라 할 때, 헌혈 횟수가 " \
            "$$수식$$12$$/수식$$회 이상인 직장인의 수는?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$16$$/수식$$회 이상 $$수식$$20$$/수식$$회 미만인 계급의 도수 $$수식$$A$$/수식$$명이라\n" \
              "하면 $$수식$$8$$/수식$$회 이상 $$수식$$12$$/수식$$회 미만인 계급의 도수는 $$수식$${k}A$$/수식$$명이므로\n" \
              "$$수식$${n1}+{n2}+{k}A+{n4}+A={n}$$/수식$$\n" \
              "$$수식$${k2}A={s1}$$/수식$$  $$수식$$THEREFORE A={n5}$$/수식$$\n" \
              "따라서 헌혈 횟수가 12회 이상인 직장인의 수는\n" \
              "$$수식$${n4}+{n5}={ans}$$/수식$$\n"

    n = 50
    
    while True :
      n1 = random.randint(1,17)
      n2 = random.randint(1,17)
      n4 = random.randint(1,17)
      k = random.randint(2,3)
      k2 = k+1
      n5 = random.randint(3,6)
      n3 = n5*k
      sum = n1+n2+n3+n4+n5
      s1 = n-(n1+n2+n4)
      if sum == n and s1%k2 == 0 :
        break

    ans = n4+n5

    fig, ax =plt.subplots(1,1, figsize=(4,4))
    data=[["0 이상 4 미만",n1],
          ["4 이상 8 미만",n2],
          ["8 이상 12 미만",""],
          ["12 이상 16 미만",n4],
          ["16 이상 20 미만",""],
          ["합계",n]]
    column_labels=["횟수(회)", "도수(명)"]
    df=pd.DataFrame(data,columns=column_labels)
    ax.axis('tight')
    ax.axis('off')
    tb = ax.table(cellText=df.values,colLabels=df.columns, loc="center", cellLoc='center')
    tb.scale(1,3)
    tb.set_fontsize(20)
    tb.auto_set_column_width(True)

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

    stem = stem.format(n=n, k=k, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(k=k, k2=k2, n=n, n1=n1, n2=n2, n4=n4, n5=n5, s1=s1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def statistics124_Stem_015():
    stem = "다음은 {name}이네 학교 학생 $$수식$${n}$$/수식$$명이 한달동안 학교 홈페이지에 접속한 횟수를 조사하여 나타낸 도수분포표이다. " \
            "접속 횟수가 $$수식$$4$$/수식$$회 미만인 학생이 전체의 $$수식$${p}%$$/수식$$일 때, 접속횟수가 $$수식$$6$$/수식$$회 이상인 학생은 전체의 몇 %인가?\n" \
            "① $$수식$${a1}%$$/수식$$  ② $$수식$${a2}%$$/수식$$   ③ $$수식$${a3}%$$/수식$$\n" \
            "④ $$수식$${a4}%$$/수식$$  ⑤ $$수식$${a5}%$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$0$$/수식$$회 이상 $$수식$$2$$/수식$$회 미만인 계급의 도수를 $$수식$$A$$/수식$$명, $$수식$$6$$/수식$$회\n" \
              "이상 $$수식$$8$$/수식$$회 미만인 계급의 도수를 $$수식$$B$$/수식$$명이라 하면\n" \
              "접속 횟수가 $$수식$$4$$/수식$$회 미만인 학생은 $$수식$$(A+{n2})$$/수식$$명이므로\n" \
              "$$수식$$A+{n2}={n}\\times{f1}, A+{n2}={s1}$$/수식$$\n" \
              "$$수식$$THEREFORE A={n1}$$/수식$$\n" \
              "$$수식$$THEREFORE B={n}-({n1}+{n2}+{n3}+{n5})={n}-{s2}={n4}$$/수식$$\n" \
              "따라서 접속 횟수가 $$수식$$6$$/수식$$회 이상인 학생 수는\n" \
              "$$수식$${n4}+{n5}={s3}$$/수식$$\n" \
              "$$수식$${f2}\\times100={ans}(%)$$/수식$$\n"

    name = random.choice(["미영","지원","지현","현석","도영","태현"])
    n = 50

    while True :
      n1 = random.randint(1,16)
      n2 = random.randint(1,16)
      n3 = random.randint(1,16)
      n4 = random.randint(1,16)
      n5 = random.randint(1,16)
      sum = n1+n2+n3+n4+n5
      if sum == n and n4 != n5 :
        break
    
    p = (n1+n2)*2
    f1 = "\\frac{"+str(p)+"}{100}"
    s1 = n1+n2
    s2 = n1+n2+n3+n5
    s3 = n4+n5
    f2 = "\\frac{"+str(s3)+"}{50}"
    ans = s3*2

    fig, ax =plt.subplots(1,1, figsize=(4,4))
    data=[["0 이상 2 미만",""],
          ["2 이상 4 미만",n2],
          ["4 이상 6 미만",n3],
          ["6 이상 8 미만",""],
          ["8 이상 10 미만",n5],
          ["합계",n]]
    column_labels=["횟수(회)", "도수(명)"]
    df=pd.DataFrame(data,columns=column_labels)
    ax.axis('tight')
    ax.axis('off')
    tb = ax.table(cellText=df.values,colLabels=df.columns, loc="center", cellLoc='center')
    tb.scale(1,3)
    tb.set_fontsize(20)
    tb.auto_set_column_width(True)

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

    stem = stem.format(n=n, p=p, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, name=name)
    answer = answer.format(result=result)
    comment = comment.format(n=n, n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, s1=s1, s2=s2, s3=s3, f1=f1, f2=f2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg



def statistics124_Stem_017():
    stem = "다음 히스토그램은 어느 해 $$수식$$8$$/수식$$월 한 달 동안의 일교차를 조사하여 나타낸 것이다. " \
            "계급의 크기를 $$수식$$a DEG C$$/수식$$, 계급의 개수를 $$수식$$b$$/수식$$라 하고 " \
            "도수가 가장 큰 계급의 도수를 $$수식$$c$$/수식$$일이라 할 때, $$수식$$a+b+c$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n계급의 크기는 $$수식$${a}DEG C$$/수식$$이므로 $$수식$$a={a}$$/수식$$\n" \
              "계급의 개수는 $$수식$${b}$$/수식$$이므로 $$수식$$b={b}$$/수식$$\n" \
              "도수가 가장 큰 계급은 $$수식$${t1}DEG C$$/수식$$이상 $$수식$${t2}DEG C$$/수식$$미만이고\n" \
              "이 계급의 도수는 $$수식$${c}$$/수식$$이므로 $$수식$$c={c}$$/수식$$\n" \
              "$$수식$$THEREFORE a+b+c={ans}$$/수식$$\n"

    data = []
    a = 2
    b = 5

    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0

    for i in range(30):
      data.append(random.randint(2,11))
    
    data.append(12)

    fig = plt.figure(figsize=(5,4))

    ax = fig.add_subplot(1,1,1)

    ax.hist(data, color = 'yellowgreen', alpha=0.6, bins = 5, edgecolor='black', zorder=3, rwidth=1)
    ax.grid(True)
    ax.set_xlabel("°C")
    ax.set_ylabel("(일)")
  

    for i in range(0, len(data)):
      if data[i] >= 2 and data[i] < 4 :
        n1 += 1
      elif data[i] >= 4 and data[i] < 6 :
        n2 += 1
      elif data[i] >= 6 and data[i] < 8 :
        n3 += 1
      elif data[i] >= 8 and data[i] < 10 :
        n4 += 1
      elif data[i] >= 10 and data[i] <= 12 :
        n5 += 1
    
    list = [n1,n2,n3,n4,n5]

    if max(list) == n1 :
      t1 = 2
      t2 = 4
      c = n1
    elif max(list) == n2 :
      t1 = 4
      t2 = 6
      c = n2
    elif max(list) == n3 :
      t1 = 6
      t2 = 8
      c = n3
    elif max(list) == n4 :
      t1 = 8
      t2 = 10
      c = n4
    elif max(list) == n5 :
      t1 = 10
      t2 = 12
      c = n5

    ans = a+b+c 

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
    comment = comment.format(a=a, b=b, c=c, t1=t1, t2=t2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def statistics124_Stem_020():
    stem = "다음 히스토그램은 {name}네 반 학생들의 몸무게를 조사하여 나타낸 것이다. " \
            "도수가 가장 큰 계급의 직사각형의 넓이와 도수가 가장작은 계급의 직사각형의 넓이의 합은?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n계급의 크기는 $$수식$$5``rm {{kg}}$$/수식$$이고 도수가 가장 큰 계급과\n" \
              "가장 작은 계급의 도수가 각각 $$수식$${s1}$$/수식$$명, $$수식$${s2}$$/수식$$명이므로\n" \
              "직사각형의 넓이의 합은\n" \
              "$$수식$$(5\\times{s1})+(5\\times{s2})={ans}$$/수식$$\n"

    name = random.choice(["경희","주희","지예","선우","은우","경수"])
    data = []

    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0

    for i in range(54):
      data.append(random.randint(30,60))
    data.append(30)
    data.append(60)

    fig = plt.figure(figsize=(5,4))

    ax = fig.add_subplot(1,1,1)

    ax.hist(data, color = 'lightblue', alpha=0.6, bins = 6, edgecolor='black', zorder=3, rwidth=1)
    ax.grid(True)
    ax.set_xlabel("kg")
    ax.set_ylabel("(명)")
    plt.xticks([30,35,40,45,50,55,60])
  
    for i in range(0, len(data)):
      if data[i] >= 30 and data[i] < 35 :
        n1 += 1
      elif data[i] >= 35 and data[i] < 40 :
        n2 += 1
      elif data[i] >= 40 and data[i] < 45 :
        n3 += 1
      elif data[i] >= 45 and data[i] < 50 :
        n4 += 1
      elif data[i] >= 50 and data[i] < 55 :
        n5 += 1
      elif data[i] >= 55 and data[i] <= 60 :
        n6 += 1 

    list = [n1,n2,n3,n4,n5,n6]

    s1 = max(list)
    s2 = min(list)

    ans = 5*s1+5*s2

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

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, name=name)
    answer = answer.format(result=result)
    comment = comment.format(s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg



def statistics124_Stem_023():
    stem = "다음 히스토그램은 {name}이네 반 학생들의 $$수식$$100``rm m$$/수식$$달리기 기록을 조사하여 나타낸 것이다. " \
            "{name}이가 상위 $$수식$$10%$$/수식$$이내에 들려면 기록이 몇초 미만이어야 하는지 구하시오.\n"
            
    answer = "(정답)\n$$수식$${result}$$/수식$$초"
    comment = "(해설)\n전체 학생 수는 $$수식$${n1}+{n2}+{n3}+{n4}+{n5}={n}$$/수식$$(명)이므\n" \
              "로 상위 $$수식$$10%$$/수식$$ 이내에 드는 학생 수는\n" \
              "$$수식$${n}\\times{f}={s}$$/수식$$\n" \
              "이 때 기록이 $$수식$$16$$/수식$$초 이상 $$수식$$17$$/수식$$초 미만인 학생이 $$수식$${s}$$/수식$$명\n" \
              "이므로 상위 $$수식$$10%$$/수식$$ 이내에 들려면 기록은 $$수식$$17$$/수식$$초 미\n" \
              "만이어야 한다.\n"

    name = random.choice(["태진","준영","상연","나은","연정","현진"])
    data = []

    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    
    f = "\\frac{10}{100}"

    n = random.choice([30,40])

    if n == 30 :
      s = 3
    elif n == 40 :
      s = 4

    for i in range(n-s-1):
      data.append(random.randint(17,20))
    data.append(21)

    for i in range(s):
      data.append(16)    

    fig = plt.figure(figsize=(5,4))

    ax = fig.add_subplot(1,1,1)

    ax.hist(data, color = 'pink', alpha=0.5, bins = 5, edgecolor='black', zorder=3, rwidth=1)
    ax.grid(True)
    ax.set_xlabel("(초)")
    ax.set_ylabel("(명)")
  
    for i in range(0, len(data)):
      if data[i] >= 16 and data[i] < 17 :
        n1 += 1
      elif data[i] >= 17 and data[i] < 18 :
        n2 += 1
      elif data[i] >= 18 and data[i] < 19 :
        n3 += 1
      elif data[i] >= 19 and data[i] < 20 :
        n4 += 1
      elif data[i] >= 20 and data[i] <= 21 :
        n5 += 1
    
    result = 17

    stem = stem.format(name=name)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, n=n, s=s, f=f)
    svg = saveSvg()
    return stem, answer, comment, svg



def statistics124_Stem_026():
    stem = "다음 그림은 {name1}이네 반 학생들이 $$수식$$1$$/수식$$분 동안 {name2}를 한 횟수를 조사하여 나타낸 도수분포다각형이다. " \
            "이 때 도수가 가장 큰 계급의 도수와 가장 작은 계급의 도수의 차를 구하시오.\n"

    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n도수가 가장 큰 계급은 $$수식$${t1}$$/수식$$회 이상 $$수식$${t2}$$/수식$$회 미만이므로\n" \
              "이 계급의 도수는 $$수식$${s1}$$/수식$$명이고, 도수가 가장 작은\n" \
              "계급은 $$수식$${t3}$$/수식$$회 이상 $$수식$${t4}$$/수식$$회 미만이므로 이 계급의 도수는\n" \
              "$$수식$${s2}$$/수식$$명이다.\n" \
              "따라서 구하는 차는 $$수식$${s1}-{s2}={result}$$/수식$$"

    name1 = random.choice(["경진","민정","예림","정인","태일","지훈"])
    name2 = random.choice(["윗몸일으키기","팔굽혀펴기","턱걸이"])
    data = []

    while True :
      n1 = random.randint(2,12)
      n2 = random.randint(2,12)
      n3 = random.randint(2,12)
      n4 = random.randint(2,12)
      n5 = random.randint(2,12)
      n6 = random.randint(2,12)
      n7 = random.randint(2,12)
      n8 = random.randint(2,12)
      sum = n1+n2+n3+n4+n5+n6+n7+n8
      list = [n1,n2,n3,n4,n5,n6,n7,n8]
      list2 = set(list)
      if sum == 50 and len(list)==len(list2):
        break
    
    list = [n1,n2,n3,n4,n5,n6,n7,n8]
    
    s1 = max(list)
    s2 = min(list)
    result = s1-s2

    if max(list) == n1 :
      t1 = 5
      t2 = 10
    elif max(list) == n2 :
      t1 = 10
      t2 = 15
    elif max(list) == n3 :
      t1 = 15
      t2 = 20
    elif max(list) == n4 :
      t1 = 20
      t2 = 25
    elif max(list) == n5 :
      t1 = 25
      t2 = 30  
    elif max(list) == n6 :
      t1 = 30
      t2 = 35
    elif max(list) == n7 :
      t1 = 35
      t2 = 40
    elif max(list) == n8 :
      t1 = 40
      t2 = 45

    if min(list) == n1 :
      t3 = 5
      t4 = 10
    elif min(list) == n2 :
      t3 = 10
      t4 = 15
    elif min(list) == n3 :
      t3 = 15
      t4 = 20
    elif min(list) == n4 :
      t3 = 20
      t4 = 25
    elif min(list) == n5 :
      t3 = 25
      t4 = 30  
    elif min(list) == n6 :
      t3 = 30
      t4 = 35
    elif min(list) == n7 :
      t3 = 35
      t4 = 40
    elif min(list) == n8 :
      t3 = 40
      t4 = 45

    fig = plt.figure(figsize=(5,4))

    ax = fig.add_subplot(1,1,1)
    
    x = [2.5,7.5,12.5,17.5,22.5,27.5,32.5,37.5,42.5,47.5]
    y = [0,n1,n2,n3,n4,n5,n6,n7,n8,0]

    ax.plot(x, y, marker="o", color = 'red')
    ax.grid(True)
    ax.set_xlabel("(회)")
    ax.set_ylabel("(명)")
    ax.xaxis.set_ticks([5,10,15,20,25,30,35,40,45])  

    stem = stem.format(name1=name1, name2=name2)
    answer = answer.format(result=result)
    comment = comment.format(t1=t1, t2=t2, t3=t3, t4=t4, s1=s1, s2=s2, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg  




def statistics124_Stem_031():
    stem = "다음은 한 상자에 들어 있는 {name} $$수식$${n}$$/수식$$개의 무게를 조사하여 나타낸 도수분포표이다. " \
            "$$수식$$45`` rm g$$/수식$$ 이상 $$수식$$50`` rm g$$/수식$$ 미만인 계급의 상대도수는?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$45`` rm g$$/수식$$ 이상 $$수식$$50`` rm g$$/수식$$ 미만인 계급의 도수는\n" \
              "$$수식$${n}-({n1}+{n2}+{n4}+{n5}+{n6})={n}-{s1}={n3}$$/수식$$(개)\n" \
              "이므로 구하는 상대도수는\n" \
              "$$수식$${f}={ans}$$/수식$$\n"

    name = random.choice(["귤","배","감","사과","딸기"])
    n = 40

    while True :
      n1 = random.randint(1,9)
      n2 = random.randint(1,9)
      n3 = random.randint(10,15)
      n4 = random.randint(1,9)
      n5 = random.randint(1,9)
      n6 = random.randint(1,9)
      sum = n1+n2+n3+n4+n5+n6
      list = [n1,n2,n3,n4,n5,n6]
      if sum == n and n3 % 2 == 0 :
        break

    s1 = n1+n2+n4+n5+n6
    f = "\\frac{"+str(n3)+"}{"+str(n)+"}"
    ans = n3/n
  
    fig, ax =plt.subplots(1,1, figsize=(4,5))
    data=[["35 이상 40 미만",n1],
          ["40 이상 45 미만",n2],
          ["45 이상 50 미만",""],
          ["50 이상 55 미만",n4],
          ["55 이상 60 미만",n5],
          ["60 이상 65 미만",n6],
          ["합계",n]]
    column_labels=["무게(g)", "도수(개)"]
    df=pd.DataFrame(data,columns=column_labels)
    ax.axis('tight')
    ax.axis('off')
    tb = ax.table(cellText=df.values,colLabels=df.columns, loc="center", cellLoc='center')
    tb.scale(1,3)
    tb.set_fontsize(20)
    tb.auto_set_column_width(True)

    aa_list = [ans-0.15, ans-0.1, ans-0.05, ans, ans+0.05, ans+0.1, ans+0.15]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    aa1, aa2, aa3, aa4, aa5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break   

    a1 = round(aa1,2)
    a2 = round(aa2,2)
    a3 = round(aa3,2)
    a4 = round(aa4,2)
    a5 = round(aa5,2)

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, name=name)
    answer = answer.format(result=result)
    comment = comment.format(f=f, n=n, n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, n6=n6, s1=s1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def statistics124_Stem_032():
    stem = "다음은 {name}이네 학교 도서반 학생 $$수식$${n}$$/수식$$명의 지난 해 독서량을 조사하여 나타낸 상대도수의 분포표이다. $$수식$$A+B$$/수식$$의 값을 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n전체 학생 수는 $$수식$${f1}={n}$$/수식$$이므로\n" \
              "$$수식$$A={r3}\\times{n}={s1}$$/수식$$, $$수식$$B={f2}={s2}$$/수식$$\n" \
              "$$수식$$THEREFORE A+B={result}$$/수식$$"

    name = random.choice(["세윤","나연","태연","민경","창민","민석","기범","동혁"])
    n = 20

    while True :
      n1 = random.randint(1,9)
      n2 = random.randint(1,9)
      n3 = random.randint(1,9)
      n4 = random.randint(1,9)
      n5 = random.randint(1,9)
      sum = n1+n2+n3+n4+n5
      if sum == n :
        break
   
    r2 = n2/n
    r3 = n3/n
    f1 = "\\frac{"+str(n2)+"}{"+str(r2)+"}"
    f2 = "\\frac{"+str(n4)+"}{20}"
    s1 = int(r3*n)
    s2 = n4/n
    result = s1+s2
  
    fig, ax =plt.subplots(1,1, figsize=(4.5,4))
    data=[["5 ~ 15",'',''],
          ["15  ~ 25",n2,r2],
          ["25  ~ 35","$A$",r3],
          ["35  ~ 45",n4,"$B$"],
          ["45  ~ 55",'',''],
          ["합계","",1]]
    column_labels=["독서량(권)", "도수(명)","상대도수"]
    df=pd.DataFrame(data,columns=column_labels)
    ax.axis('tight')
    ax.axis('off')
    tb = ax.table(cellText=df.values,colLabels=df.columns, loc="center", cellLoc='center')
    tb.scale(1.3,3)
    tb.set_fontsize(20)
    tb.auto_set_column_width(True)

    stem = stem.format(n=n, name=name)
    answer = answer.format(result=result)
    comment = comment.format(f1=f1, f2=f2, n=n, r2=r2, r3=r3, s1=s1, s2=s2, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg  




def statistics124_Stem_034():
    stem = "다음의 도수분포표는 어느 재래 시장의 상인 $$수식$${n}$$/수식$$명의 사업에 종사한 기간을 조사하여 나타낸 것이다. " \
            "이 때 종사기간이 $$수식$$30$$/수식$$년 이상 $$수식$$40$$/수식$$년 미만인 계급의 상대도수는?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n종사 기간이 $$수식$$30$$/수식$$년 이상 $$수식$$40$$/수식$$년 미만인 계급의 도수는\n" \
              "$$수식$${n}-({n1}+{n2}+{n4}+{n5})={n3}$$/수식$$(명)\n" \
              "따라서 구하는 상대도수는 $$수식$${f}={ans}$$/수식$$이다.\n"

    n = 40

    while True :
      n1 = random.randint(1,12)
      n2 = random.randint(1,12)
      n3 = random.randint(1,12)
      n4 = random.randint(1,12)
      n5 = random.randint(1,12)
      sum = n1+n2+n3+n4+n5
      list = [n1,n2,n3,n4,n5]
      if sum == n and n3 % 2 == 0 and max(list) == n3 :
        break
    
    f = "\\frac{"+str(n3)+"}{"+str(n)+"}"
    ans = n3/n
  
    fig, ax =plt.subplots(1,1, figsize=(4,4))
    data=[["10 이상 20 미만",n1],
          ["20 이상 30 미만",n2],
          ["30 이상 40 미만",""],
          ["40 이상 50 미만",n4],
          ["50 이상 60 미만",n5],
          ["합계",n]]
    column_labels=["종사 기간(년)", "도수(명)"]
    df=pd.DataFrame(data,columns=column_labels)
    ax.axis('tight')
    ax.axis('off')
    tb = ax.table(cellText=df.values,colLabels=df.columns, loc="center", cellLoc='center')
    tb.scale(1,3)
    tb.set_fontsize(20)
    tb.auto_set_column_width(True)

    aa_list = [ans-0.15, ans-0.1, ans-0.05, ans, ans+0.05, ans+0.1, ans+0.15]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    aa1, aa2, aa3, aa4, aa5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break   

    a1 = round(aa1,2)
    a2 = round(aa2,2)
    a3 = round(aa3,2)
    a4 = round(aa4,2)
    a5 = round(aa5,2)

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, f=f, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def statistics124_Stem_035():
    stem = "다음은 {name}이네 반 학생들이 여름방학 동안 읽은 책의 수를 조사하여 나타낸 히스토그램이다. " \
            "책을 $$수식$${b}$$/수식$$권 읽은 학생이 속한 계급의 상대도수는?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n도수의 총합은\n" \
              "$$수식$${n1}+{n2}+{n3}+{n4}+{n5}={n}$$/수식$$(명)\n" \
              "책을 $$수식$${b}$$/수식$$권 읽은 학생이 속한 계급은 $$수식$${b1}$$/수식$$권 이상\n" \
              "$$수식$${b2}$$/수식$$권 미만이고, 이 계급의 도수는 $$수식$${s}$$/수식$$$$/수식$$명이므로 구하는 상대도수는\n" \
              "$$수식$${f}={ans}$$/수식$$\n"

    name = random.choice(["한욱","영훈","승민","수빈","재민","원영","윤진","지민"])
    data = []

    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    
    n = 25

    for i in range(n-2):
      data.append(random.randint(3,21))
    data.append(2)
    data.append(22)

    fig = plt.figure(figsize=(5,4))

    ax = fig.add_subplot(1,1,1)

    ax.hist(data, color = 'pink', alpha=0.5, bins = 5,  edgecolor='black', zorder=3, rwidth=1)
    ax.grid(True)
    ax.set_xlabel("(초)")
    ax.set_ylabel("(명)")
    ax.xaxis.set_ticks([2,6,10,14,18,22])  
    
    for i in range(0, len(data)):
      if data[i] >= 2 and data[i] < 6 :
        n1 += 1
      elif data[i] >= 6 and data[i] < 10 :
        n2 += 1
      elif data[i] >= 10 and data[i] < 14 :
        n3 += 1
      elif data[i] >= 14 and data[i] < 18 :
        n4 += 1
      elif data[i] >= 18 and data[i] <= 22 :
        n5 += 1

    list = [n1,n2,n3,n4,n5]

    for i in range(0, len(data)):
      if max(list) == n1 :
        b = random.randint(2,5)
        b1 = 2
        b2 = 3
        s = n1
      elif max(list) == n2 :
        b = random.randint(7,9)
        b1 = 6
        b2 = 10
        s = n2
      elif max(list) == n3 :
        b = random.randint(11,13)
        b1 = 10
        b2 = 14
        s = n3
      elif max(list) == n4 :
        b = random.randint(15,17)
        b1 = 14
        b2 = 18
        s = n4
      elif max(list) == n5 :
        b = random.randint(19,21)
        b1 = 18
        b2 = 22
        s = n5

    f = "\\frac{"+str(s)+"}{"+str(n)+"}"
    ans = s/n

    aa_list = [ans-0.12, ans-0.08, ans-0.04, ans, ans+0.04, ans+0.08, ans+0.12]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    aa1, aa2, aa3, aa4, aa5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break   

    a1 = round(aa1,2)
    a2 = round(aa2,2)
    a3 = round(aa3,2)
    a4 = round(aa4,2)
    a5 = round(aa5,2)

    stem = stem.format(b=b, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, name=name)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, n=n, s=s, b1=b1, b2=b2, b=b, f=f, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def statistics124_Stem_036():
    stem = "다음 그림은 {name}이네 반 학생들의 몸무게를 조사하여 나타낸 도수분포다각형이다. " \
            "몸무게가 $$수식$$55``rm {{kg}}$$/수식$$ 이상인 계급들의 상대도수의 합은?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$\n" \
            "③ $$수식$${a3}$$/수식$$   ④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n도수의 총합은\n" \
              "$$수식$${n1}+{n2}+{n3}+{n4}+{n5}={n}$$/수식$$(명)\n" \
              "몸무게가 $$수식$$55``rm {{kg}}$$/수식$$ 이상인 계급드의 도수의 합은\n" \
              "$$수식$${n4}+{n5}={n6}$$/수식$$(명)이므로 구하는 상대도수는\n" \
              "$$수식$${f}={ans}$$/수식$$\n"

    name = random.choice(["지섭","주연","재현","영현","지성","수민","희정","유진"])
    data = []

    while True :
      n1 = random.randint(4,14)
      n2 = random.randint(4,14)
      n3 = random.randint(4,14)
      n4 = random.randint(4,14)
      n5 = random.randint(4,14)
      sum = n1+n2+n3+n4+n5
      n6 = n4+n5
      if sum == 40 and n6%2 == 0:
        break
    
    n = 40
    f = "\\frac{"+str(n6)+"}{40}"
    ans = n6/n

    fig = plt.figure(figsize=(5,4))

    ax = fig.add_subplot(1,1,1)
    
    x = [37.5,42.5,47.5,52.5,57.5,62.5,67.5]
    y = [0,n1,n2,n3,n4,n5,0]

    ax.plot(x, y, marker="o", color = 'purple')
    ax.grid(True)
    ax.set_xlabel("(kg)")
    ax.set_ylabel("(명)")
    ax.xaxis.set_ticks([40,45,50,55,60,65])  

    aa_list = [ans-0.15, ans-0.1, ans-0.05, ans, ans+0.05, ans+0.1, ans+0.15]
    a_list = []
    idx = random.randint(0,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    aa1, aa2, aa3, aa4, aa5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break   

    a1 = round(aa1,2)
    a2 = round(aa2,2)
    a3 = round(aa3,2)
    a4 = round(aa4,2)
    a5 = round(aa5,2)  

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, name=name)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, n6=n6, n=n, f=f, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def statistics124_Stem_037():
    stem = "어느 중학교 학생들의 {name}를 조사하였더니 상대도수가 $$수식$${r}$$/수식$$인 계급의 도수가 $$수식$${n}$$/수식$$명이었다. " \
            "이 때 전체 학생 수는?\n" \
            "① $$수식$${a1}$$/수식$$명   ② $$수식$${a2}$$/수식$$명   ③ $$수식$${a3}$$/수식$$명\n" \
            "④ $$수식$${a4}$$/수식$$명   ⑤ $$수식$${a5}$$/수식$$명\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$(전체 학생 수)={f1}$$/수식$$\n" \
              "   \t$$수식$$={f2}={ans}$$/수식$$(명)\n" 

    name = random.choice(["가슴둘레","허리둘레","몸무게"])

    r = 0.2
    n = random.choice([60,70,80,90])
    
    ans = int(n/r)

    aa_list = [ans-n*3, ans-n*2, ans-n, ans, ans+n, ans+n*2, ans+n*3]
    a_list = []
    if ans - n*3 < 120 :
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

    f1 = "\\frac{(계급의 도수)}{(계급의 상대도수)}"
    f2 = "\\frac{"+str(n)+"}{"+str(r)+"}"

    stem = stem.format(r=r, n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, name=name)
    answer = answer.format(result=result)
    comment = comment.format(f1=f1, f2=f2, ans=ans)
    
    return stem, answer, comment



def statistics124_Stem_038():
    stem = "어느 도수분포표에서 도수가 $$수식$${n1}$$/수식$$인 계급의 상대도수가 $$수식$${r1}$$/수식$$일 때, " \
            "도수가 $$수식$${n2}$$/수식$$인 계급의 상대도수는$$수식$$a$$/수식$$, 상대도수가 $$수식$${r2}$$/수식$$인 계급의 도수는 $$수식$$b$$/수식$$라 한다.\n" \
            "이 때, $$수식$$a+b$$/수식$$의 값을 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n도수의 총합은 $$수식$${f1}={n}$$/수식$$이므로" \
              "$$수식$$a={f2}={a}, b={r2}\\times{n}={b}$$/수식$$\n" \
              "$$수식$$THEREFORE a+b={result}$$/수식$$\n"
    
    r1 = random.choice([0.2,0.3])
    n = random.choice([50,60,80])
    n1 = int(r1*n)
    r2 = r1+0.05
    if r1 == 0.2 :
      a = 0.3
    elif r1 == 0.3 :
      a = 0.4
    n2 =int(a*n)
    bb = r2*n

    if bb.is_integer() :
      b = int(r2*n)
    else :
      b = bb

    f1 = "\\frac{"+str(n1)+"}{"+str(r1)+"}"
    f2 = "\\frac{"+str(n2)+"}{"+str(n)+"}"

    result = a+b

    stem = stem.format(r1=r1, r2=r2, n1=n1, n2=n2)
    answer = answer.format(result=result)
    comment = comment.format(f1=f1, f2=f2, r2=r2, n=n, a=a, b=b, result=result)

    return stem, answer, comment



def statistics124_Stem_046():
    stem = "다음 그림은 어느 중학교 학생들의 공던지기 기록에 대한 상대도수의 분포를 나타낸 그래프이다. " \
            "상대도수가 가장 큰 계급에 속하는 학생이 $$수식$${n}$$/수식$$명일 때, 이 중학교의 전체 학생 수는?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n상대도수가 가장 큰 계급은 $$수식$$35m$$/수식$$ 이상 $$수식$$40``rm m$$/수식$$ 미\n" \
              "만이고 이 계급의 상대도수는 $$수식$${r}$$/수식$$이므로\n" \
              "(전체 학생 수)=$$수식$${f}={ans}$$/수식$$\n"

    data = []

    while True :
      n1 = random.choice([0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26])
      n2 = random.choice([0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26])
      n3 = random.choice([0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26])
      n4 = random.choice([0.28,0.3])
      n5 = random.choice([0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26])
      n6 = random.choice([0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26])
      sum = n1+n2+n3+n4+n5+n6
      l = [n1,n2,n3,n4,n5,n6]
      l2 = set(l)
      if sum == 1 and len(l)==len(l2):
        break

    if n4 == 0.28 :
      n = 350
      ans = 1250
    elif n4 == 0.3 :
      n = 360
      ans = 1200

    r = n4
    f = "\\frac{"+str(n)+"}{"+str(n4)+"}"

    fig = plt.figure(figsize=(5,4))

    ax = fig.add_subplot(1,1,1)
    
    x = [17.5,22.5,27.5,32.5,37.5,42.5,47.5,52.5]
    y = [0,n1,n2,n3,n4,n5,n6,0]

    ax.plot(x, y, marker="o", color = 'purple')
    ax.grid(True)
    ax.set_xlabel("(m)")
    ax.set_ylabel("(상대도수)")
    ax.xaxis.set_ticks([20,25,30,35,40,45,50]) 

    plt.yticks([0,0.02,0.04,0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26,0.28,0.3,0.32,0.34], 
                 [0,'','','','',0.1, '','','','',0.2, '','','','', 0.3, '','']) 

    aa_list = [ans-150, ans-100, ans-50, ans, ans+50, ans+100, ans+150]
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
    comment = comment.format(r=r, f=f, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  




def statistics124_Stem_048():
    stem = "어느 중학교의 남학생과 여학생 수는 각각 $$수식$${n1}$$/수식$$명, $$수식$${n2}$$/수식$$명이다." \
            "학생들의 키를 조사하여 도수분포표를 만들었더니 키가 $$수식$$140``rm cm$$/수식$$ 이상 $$수식$$150``rm cm$$/수식$$ 미만인 " \
            "남학생 수와 여학생 수가 같았을 때, 이 계급의 남학생과 여학생의 상대도수의 비를 가장 간단한 자연수의 비로 나타내시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n키가 $$수식$$140``rm cm$$/수식$$ 이상 $$수식$$150``rm cm$$/수식$$ 미만인 남학생 수와\n" \
              "여학생 수를 각각 $$수식$$a$$/수식$$명이라 하면 남학생과 여학생\n" \
              "수가 각각 $$수식$${n1}$$/수식$$명, $$수식$${n2}$$/수식$$명이므로 이 계급의 남학생과\n" \
              "여학생의 상대도수 비는\n" \
              "$$수식$${f1}:{f2}={f3}:{f4}={result}$$/수식$$"

    while True :
       n1 = random.choice([250,300,350])
       n2 = random.choice([250,300,350])
       if n1 != n2 :
         break

    f1 = "\\frac{a}{"+str(n1)+"}"
    f2 = "\\frac{a}{"+str(n2)+"}"
    f3 = "\\frac{1}{"+str(n1)+"}"
    f4 = "\\frac{1}{"+str(n2)+"}"

    g = math.gcd(n1,n2)
    r1 = int(n2/g)
    r2 = int(n1/g)

    result = str(r1)+":"+str(r2)


    stem = stem.format(n1=n1, n2=n2)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, f1=f1, f2=f2, f3=f3, f4=f4, result=result)

    return stem, answer, comment



def statistics124_Stem_053():
    stem = "어느 $$수식$$1$$/수식$$학년 $$수식$$1$$/수식$$반과 $$수식$$2$$/수식$$반의 전체 학생 수의 비는 $$수식$${n1}:{n2}$$/수식$$이고 혈액형이 A형인 학생 수의 비는 " \
            "$$수식$${n3}:{n4}$$/수식$$일 때, $$수식$$1$$/수식$$반과 $$수식$$2$$/수식$$반에서 혈액형이 A형인 학생의 상대도수 비를 가장 간단한 자연수의 비로 나타내시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n$$수식$$1$$/수식$$반과 $$수식$$2$$/수식$$반의 전체 학생 수를 각각 $$수식$${n1}a$$/수식$$명, $$수식$${n2}a$$/수식$$명,\n" \
              "혈액형이 A형인 학생 수를 각각 $$수식$${n3}b$$/수식$$명, $$수식$${n4}b$$/수식$$명이라\n" \
              "하면 구하는 상대도수의 비는\n" \
              "$$수식$${f1}:{f2}={f3}:{f4}={result}$$/수식$$"

    while True :
      n1 = random.choice([3,4,5,7])
      n2 = random.choice([3,4,5,7])
      n3 = random.choice([4,5,7,9])
      n4 = random.choice([4,5,7,9])
      list = [n1,n2,n3,n4]
      if len(list) == len(set(list)) :
        break
    
    f1 = "\\frac{"+str(n3)+"b}{"+str(n1)+"a}"
    f2 = "\\frac{"+str(n4)+"b}{"+str(n2)+"a}"
    f3 = "\\frac{"+str(n3)+"}{"+str(n1)+"}"
    f4 = "\\frac{"+str(n4)+"}{"+str(n2)+"}"

    r1 = n3*n2
    r2 = n1*n4

    result = str(r1)+":"+str(r2)    

    stem = stem.format(n1=n1, n2=n2, n3=n3, n4=n4)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, f1=f1, f2=f2, f3=f3, f4=f4, result=result)

    return stem, answer, comment




def statistics124_Stem_054():
    stem = "다음은 어느 중학교 $$수식$$1$$/수식$$학년 남학생들의 팔굽혀 펴기 횟수에 대한 상대도수의 분포를 나타낸 그래프이다. " \
            "$$수식$$25$$/수식$$회 이상인 학생이 $$수식$$10$$/수식$$회 미만인 학생보다 $$수식$${n}$$/수식$$명 많다고 할 때, $$수식$$1$$/수식$$학년 전체 남학생 수는?\n" \
            "① $$수식$${a1}$$/수식$$   ② $$수식$${a2}$$/수식$$   ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$   ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$1$$/수식$$학년 전체 남학생 수를 $$수식$$a$$/수식$$라 하면\n" \
              "$$수식$${s1}\\times a={s2}\\times a+{n}$$/수식$$\n" \
              "$$수식$${s3}a={n}$$/수식$$ $$수식$$THEREFORE a={ans}$$/수식$$\n" \
              "따라서 $$수식$$1$$/수식$$학년 전체 남학생 수는 $$수식$${ans}$$/수식$$이다.\n"

    data = []

    ans = random.choice([200,300,400])
    s3 = 0.1
    n = int(ans*s3)
    s1 = random.choice([0.15,0.2])
    if s1 == 0.15 :
      s2 = 0.05
    elif s1 == 0.2 :
      s2 = 0.1

    k = int(ans*s1)
    k2 = int(ans*s2)

    list = []
    t = 0.01
    for i in range(1,101) :
      list.append(round(t*i,2))


    while True :
      n1 = random.choice(list)
      n2 = random.choice(list)
      n3 = random.choice(list)
      n4 = random.choice(list)
      n5 = round(n1+0.1,2)
      l = [n1,n2,n3,n4,n5]
      l2 = set(l)
      if n1+n2+n3+n4+n5 == 1 and min(l)>0.05 and max(l)<0.4 and len(l) == len(l2) :
        break
    
    for i in range(int(n1*ans)):
      data.append(5)

    for i in range(int(n2*ans)):
      data.append(11)

    for i in range(int(n3*ans)):
      data.append(16)

    for i in range(int(n4*ans)):
      data.append(21)

    for i in range(int(n5*ans)):
      data.append(30)

    fig = plt.figure(figsize=(5,4))

    ax = fig.add_subplot(1,1,1)

    ax.hist(data, color = 'orange', alpha=0.5, bins = 5, edgecolor='black', zorder=3, rwidth=1)
    ax.grid(True)
    ax.set_xlabel("(회)")
    ax.set_ylabel("(상대도수)")
    ax.tick_params(axis='y', left=False)

    if ans == 200 :
      plt.yticks([4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80], 
                 ['','','','',0.1, '','','','',0.2, '','','','', 0.3, '','','','',0.4]) 
    elif ans == 300 :
      plt.yticks([6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114,120], 
                 ['','','','',0.1, '','','','',0.2, '','','','', 0.3, '','','','',0.4]) 
    elif ans == 400 :
      plt.yticks([8,16,24,32,40,48,56,64,72,80,88,96,104,112,120,128,136,144,152,160], 
                 ['','','','',0.1, '','','','',0.2, '','','','', 0.3, '','','','',0.4]) 


    aa_list = [ans-n*3, ans-n*2, ans-n, ans, ans+n, ans+n*2, ans+n*3]
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
    comment = comment.format(s1=s1, s2=s2, s3=s3, n=n, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  
