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
    ax.bar(x=x-width/3, height=yvalue[0],
           width=width, color=random.choice(colors))
    ax.bar(x=width/3, height=yvalue[1],
           width=width, color=random.choice(colors))
    ax.bar(x=x+width/3, height=yvalue[2],
           width=width, color=random.choice(colors))
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

    for i in range(0, len(vert)-2):
        codes.append(Path.LINETO)

    codes.append(Path.CLOSEPOLY)

    path = Path(vert, codes)

    if fill:
        if dash:
            pp = mpatches.PathPatch(path, fc=random.choice(
                colors), fill=True, lw=lw, ls='--', zorder=3, alpha=alpha)
        else:
            pp = mpatches.PathPatch(path, fc=random.choice(
                colors), fill=True, lw=lw, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.PathPatch(
                path, ec='black', fill=False, lw=lw, ls='--', zorder=3)
        else:
            pp = mpatches.PathPatch(
                path, ec='black', fill=False, lw=lw, zorder=3)
    ax.add_patch(pp)

# 정다각형 그리는 함수


def drawRegular(ax, center, n, radius, fill=False, alpha=1, dash=False, lw=1):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    if fill:
        if dash:
            pp = mpatches.RegularPolygon(xy=center, numVertices=n, radius=radius, orientation=0.1, fc=random.choice(
                colors), fill=True, ec='black', lw=lw, ls='--', zorder=3, alpha=alpha)
        else:
            pp = mpatches.RegularPolygon(xy=center, numVertices=n, radius=radius, orientation=0.1, fc=random.choice(
                colors), fill=True, ec='black', lw=lw, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.RegularPolygon(xy=center, numVertices=n, radius=radius,
                                         orientation=0.1, ec='black', fill=False, lw=lw, ls='--', zorder=3)
        else:
            pp = mpatches.RegularPolygon(
                xy=center, numVertices=n, radius=radius, orientation=0.1, ec='black', fill=False, lw=lw, zorder=3)

    ax.add_patch(pp)

    return pp.get_path(), pp.get_patch_transform()


def drawNormalPoly(ax, xy, radius, resolution, fill=False, alpha=1, dash=False, lw=1):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    pp = mpatches.CirclePolygon(xy=xy, radius=radius, resolution=resolution)

    ax.add_patch(pp)

# 원 그리는 함수


def drawCircle(ax, center, radius, fill=False, alpha=1, dash=False, position=None, lw=1):
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
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1,
                              theta2=theta2, ec='black', lw=lw, ls='--', fill=False, zorder=3)
        else:
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0,
                              theta1=theta1, theta2=theta2, ec='black', lw=lw, fill=False, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Circle(center, radius=radius, fc=random.choice(
                    colors), ec='black', lw=lw, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Circle(center, radius=radius, fc=random.choice(
                    colors), ec='black', lw=lw, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Circle(
                    center, radius=radius, ec='black', lw=lw, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Circle(center, radius=radius,
                                     ec='black', lw=lw, fill=False, zorder=3)
    ax.add_patch(pp)

# 타원 그리는 함수


def drawEllipse(ax, center, width, height, fill=False, alpha=1, dash=False, position=None, lw=1):
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
            pp = mpatches.Arc(center, width=width, height=height, angle=0,
                              theta1=theta1, theta2=theta2, ec='black', lw=lw, ls='--', zorder=3)
        else:
            pp = mpatches.Arc(center, width=width, height=height, angle=0,
                              theta1=theta1, theta2=theta2, ec='black', lw=lw, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=random.choice(
                    colors), ec='black', lw=lw, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=random.choice(
                    colors), ec='black', lw=lw, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height,
                                      angle=0, ec='black', lw=lw, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Ellipse(
                    center, width=width, height=height, angle=0, ec='black', lw=lw, fill=False, zorder=3)

    ax.add_patch(pp)

# 각을 그리는 함수


def drawAngle(ax, p3, p2, p1):

    dx1 = p1[0] - p2[0]
    dy1 = p1[1] - p2[1]

    dx2 = p3[0] - p2[0]
    dy2 = p3[1] - p2[1]

    a1 = math.degrees(math.atan2(dy1, dx1))
    a2 = math.degrees(math.atan2(dy2, dx2))

    d = (math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2) +
         math.sqrt((p3[0]-p2[0])**2+(p3[1]-p2[1])**2))/2
    #d = 4

    a1 = round(a1)-6
    a2 = round(a2)-6
    angle = round(a2 - a1)
    #print(a1,a2)
    if angle < 0:
        angle = 360 + angle

    if angle < 30:
        pp = mpatches.Arc(p2, angle=0, width=0.25*d, height=0.25*d,
                          theta1=a1, theta2=a2, ec='red', zorder=3)
    elif angle > 90:
        pp = mpatches.Arc(p2, angle=0, width=0.2*d, height=0.2*d,
                          theta1=a1, theta2=a2, ec='red', zorder=3)
    else:
        if angle == 90:
            if a1 == 0.0 and a2 == 90.0:
                verts = [
                    (p2[0]+0.1*d, p2[1]),
                    (p2[0]+0.1*d, p2[1]+0.1*d),
                    (p2[0], p2[1]+0.1*d)
                ]
            elif a1 == 90.0 and a2 == 180.0:
                verts = [
                    (p2[0]-0.1*d, p2[1]),
                    (p2[0]-0.1*d, p2[1]+0.1*d),
                    (p2[0], p2[1]+0.1*d)
                ]
            elif a1 == 180.0 and a2 == -90.0:
                verts = [
                    (p2[0]-0.1*d, p2[1]),
                    (p2[0]-0.1*d, p2[1]-0.1*d),
                    (p2[0], p2[1]-0.1*d)
                ]
            elif a1 == -90.0 and a2 == 0.0:
                verts = [
                    (p2[0]+0.1*d, p2[1]),
                    (p2[0]+0.1*d, p2[1]-0.1*d),
                    (p2[0], p2[1]-0.1*d)
                ]
            elif a1 == 45.0 and a2 == 135.0:
                verts = [
                    (p2[0]-math.sqrt(0.01*d), p2[1]+math.sqrt(0.01*d)),
                    (p2[0], p2[1]+2*math.sqrt(0.01*d)),
                    (p2[0]+math.sqrt(0.01*d), p2[1]+math.sqrt(0.01*d))
                ]
            elif a1 >= 135.0 and a2 <= -135.0:
                verts = [
                    (p2[0]-math.sqrt(0.01*d), p2[1]-math.sqrt(0.01*d)),
                    (p2[0]-2*math.sqrt(0.01*d), p2[1]),
                    (p2[0]-math.sqrt(0.01*d), p2[1]+math.sqrt(0.01*d))
                ]
            elif a1 == -135.0 and a2 == -45.0:
                verts = [
                    (p2[0]-math.sqrt(0.01*d), p2[1]-math.sqrt(0.01*d)),
                    (p2[0], p2[1]-2*math.sqrt(0.01*d)),
                    (p2[0]+math.sqrt(0.01*d), p2[1]-math.sqrt(0.01*d))
                ]
            else:
                verts = [
                    (p2[0]+math.sqrt(0.1*d), p2[1]+math.sqrt(0.1*d)),
                    (p2[0]+2*math.sqrt(0.1*d), p2[1]),
                    (p2[0]+math.sqrt(0.1*d), p2[1]-math.sqrt(0.1*d))
                ]

            codes = [
                Path.MOVETO,
                Path.LINETO,
                Path.LINETO
            ]
            path = Path(verts, codes)

            pp = mpatches.PathPatch(path, ec='red', fill=False, zorder=3)
        else:
            pp = mpatches.Arc(p2, angle=0, width=0.2*d, height=0.2*d,
                              theta1=a1, theta2=a2, ec='red', zorder=3)

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
            cp = (mp[0]-0.2*d, mp[1])
        else:
            cp = (mp[0]+0.2*d, mp[1])

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
        cp = (x, y)

    return cp

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수


def drawArc(ax, p1, p2, position, text, boxed=False):
    #cp = controlPoint(p1,p2,position)
    cp = find_controlPoint_arc(p1, p2, position, distance=20)
    d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    l = len(text)
    vert = [
        p1,
        cp,  # 제어점
        p2
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE3,
        Path.CURVE3
    ]

    path = Path(vert, codes)

    pp = mpatches.PathPatch(
        path, fc="none", transform=ax.transData, linestyle="--", zorder=3)
    ax.add_patch(pp)

    if boxed:
        if position == 'top':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16,
                     bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16,
                     bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16,
                     bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]+0.03*l, cp[1], text, fontsize=16,
                     bbox=dict(ec='black', fc='white'))
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


def setPoints(ax, points, fill=False, text=[]):
    temp = []
    for p in points:
        if p not in temp:
            temp.append(p)
    points = temp
    if len(points) == 1:
        if len(text) == 0:
            text.append('')
        plt.text(points[0][0], points[0][1]+0.05,
                 text[0], fontsize=16, zorder=3)
        if fill:
            ax.plot(points[0][0], points[0][1], "ko", zorder=3)
    else:
        if len(text) == 0:
            for t in range(len(points)):
                text.append('')

        for i in range(0, len(points)):

            plt.text(points[i][0]-0.5, points[i][1] +
                     0.1, text[i], fontsize=16, zorder=3)

            if fill:
                ax.plot(points[i][0], points[i][1], "ko", zorder=3)


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

    im = Image.open(buf)  # We open the current image saved in the buffer

    #We rotate the image and fill the background with white
    img_01 = im.rotate(rotate, Image.NEAREST, expand=1,
                       fillcolor=(255, 255, 255))

    buf.close()

    ##MERGING THE TWO FIGURES##

    new_im = Image.new('RGB', (img_01.size[0], img_01.size[1]), 'white')
    mouse_mask = img_01.convert('RGBA')
    new_im.paste(img_01, (0, 0))
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

    fig, ax = plt.subplots(figsize=(3.5,3.5))

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


def create_p_polygon(n=3, scale=10, move_x=0, move_y=0):
    import random

    def new_p_angle(angle, length, p=[0, 0]):
        angle_radiant = math.radians(angle)
        x = (math.cos(angle_radiant)*length) + p[0]
        y = (math.sin(angle_radiant)*length) + p[1]
        return (x, y)

    def move_to_center(p_list=list, center_index=-1):
        #calculate center point
        x_center = 0
        y_center = 0
        for p in p_list:
            x_center += p[0]
            y_center += p[1]
        x_center /= len(p_list)
        y_center /= len(p_list)
        new_p_list = []
        if center_index == -1:  # center with calculated center point
            x_move = x_center * -1
            y_move = y_center * -1
        else:  # center with center_index
            center_p = p_list[center_index]
            x_move = center_p[0] * -1
            y_move = center_p[1] * -1
        #make new list with new points
        for index in range(len(p_list)):
            if center_index == -1:
                p = p_list[index]
                new_p_list.append((p[0]+x_move, p[1]+y_move))
            else:
                if index == center_index:
                    new_p_list.append((0, 0))
                else:
                    p = p_list[index]
                    new_p_list.append((p[0]+x_move, p[1]+y_move))
        return new_p_list

    def move_p(p_list=list, x_move=0, y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move, p[1]+y_move))
        return new_p_list

    def rotate_p(p_list=list, angle=0):
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
            pol_r, pol_angle_radians = cart2pol(cart_x, cart_y)
            pol_angle_radians += math.radians(angle)
            cart_x, cart_y = pol2cart(pol_r, pol_angle_radians)
            p_list[i] = (cart_x, cart_y)
        return p_list
    temp_p = (0, 0)
    angle = 180 * (n-2) / n
    random_angle = random.randint(-30, 30)
    length = int(scale/2)
    random_length = random.randint(round(scale/10)*-1, round(scale/10))
    polygon = [(0, 0)]
    for i in range(n-1):
        if random.randint(0, 1):
            temp_p = new_p_angle(angle, length, temp_p)
        else:
            while True:
                random_angle = random.randint(-30, 30)
                if abs(random_angle) > 10:
                    break
            random_length = random.randint(round(scale/10)*-1, round(scale/10))
            temp_p = new_p_angle(angle+random_angle,
                                 length+random_length, temp_p)
        polygon.append(temp_p)
        polygon = rotate_p(polygon, 180-angle)
        temp_p = (rotate_p([temp_p], 180-angle))[0]
    polygon = move_to_center(polygon)
    polygon = move_p(polygon, move_x, move_y)
    return polygon


def find_controlPoint_arc(p1, p2, position='top', distance=1):
    def round_p(p, roundNumber=5):
        p = (round(p[0], roundNumber), round(p[1], roundNumber))
        return p

    def find_linear_equation(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            return ('x', x1)
        if y1 == y2:
            return ('y', y1)
        slope = (y2-y1)/(x2-x1)
        y_intersect = y1 - slope*x1
        return (slope, y_intersect)

    def find_p_middle(p1=tuple, p2=tuple):
        return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

    def find_p_onLineInCertainDistance(equation, middle_point, distance):
        middle_x, middle_y = middle_point
        slope, y_intersect = equation
        new_x_positive = middle_x + math.sqrt(distance**2/((1/slope)**2+1))
        new_y_positive = -1/slope*new_x_positive + 1/slope*middle_x + middle_y
        new_x_negative = middle_x - math.sqrt(distance**2/((1/slope)**2+1))
        new_y_negative = -1/slope*new_x_negative + \
            (1/slope)*middle_x + middle_y
        return (new_x_positive, new_y_positive), (new_x_negative, new_y_negative)

    def calculate_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

        return d
    p1, p2 = round_p(p1), round_p(p2)
    equation = find_linear_equation(p1, p2)
    slope, y_intersect = equation
    x1, y1 = p1
    x2, y2 = p2
    d = calculate_distance(p1, p2)
    if slope == 'x':
        cp_y = (y1+y2)/2
        if position == 'right':
            cp_x = y_intersect + distance
        elif position == 'left':
            cp_x = y_intersect - distance
        else:
            raise Exception('Invalid Position')
    elif slope == 'y':
        cp_x = (x1+x2)/2
        if position == 'top':
            cp_y = y_intersect + distance
        elif position == 'bottom':
            cp_y = y_intersect - distance
        else:
            raise Exception('Invalid Position')
    else:
        p_middle = find_p_middle(p1, p2)
        cp_positive, cp_negative = find_p_onLineInCertainDistance(
            equation, p_middle, distance)
        if slope > 0:
            if position in ['top', 'left']:  # negative
                cp_x, cp_y = cp_negative
            elif position in ['bottom', 'right']:  # positive
                cp_x, cp_y = cp_positive
            else:
                raise Exception('Invalid Position')
        elif slope < 0:
            if position in ['top', 'right']:  # positive
                cp_x, cp_y = cp_positive
            elif position in ['bottom', 'left']:  # negative
                cp_x, cp_y = cp_negative
            else:
                raise Exception('Invalid Position')
        else:
            raise Exception('Slope is 0')
    return (cp_x, cp_y)

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수


def drawArc2(ax, p1, p2, position, text, boxed=False):
    if 'top' in position:
        cp = find_controlPoint_arc(p1, p2, 'top')
    elif 'bottom' in position:
        cp = find_controlPoint_arc(p1, p2, 'bottom')
    elif 'right' in position:
        cp = find_controlPoint_arc(p1, p2, 'right')
    elif 'left' in position:
        cp = find_controlPoint_arc(p1, p2, 'left')

    p1 = (round(p1[0], 5), round(p1[1], 5))
    p2 = (round(p2[0], 5), round(p2[1], 5))
    l = len(text)
    if 'mathrm' in text:
        l -= 1
    vert = [
        p1,
        cp,  # 제어점
        p2
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE3,
        Path.CURVE3
    ]

    path = Path(vert, codes)

    pp = mpatches.PathPatch(
        path, fc="none", transform=ax.transData, linestyle="--", zorder=3)
    ax.add_patch(pp)

    if boxed:
        if position == 'top':
            plt.text(cp[0]-2*l, cp[1]+3.5, text, fontsize=16,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text, fontsize=16,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=16,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=16,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=16,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=16,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=16,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=16,
                     zorder=3, bbox=dict(ec='black', fc='white'))
    else:
        if position == 'top':
            plt.text(cp[0], cp[1], text, fontsize=16, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0], cp[1], text, fontsize=16, zorder=3)
        elif position == 'left':
            plt.text(cp[0], cp[1], text, fontsize=16, zorder=3)
        elif position == 'right':
            plt.text(cp[0], cp[1], text, fontsize=16, zorder=3)
        elif position in ['top_r', 'right_t']:
            plt.text(cp[0]+l, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['top_l', 'left_t']:
            plt.text(cp[0]-l*8, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['bottom_r', 'right_b']:
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        elif position in ['bottom_l', 'left_b']:
            plt.text(cp[0]-l*8, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        else:
            raise Exception('no matching position')


def create_p_triangle(width_height=[], right_bottom_left=[], bottom_left_angle=[], move_x=0, move_y=0):
    import random
    import math

    def move_to_center(p_list=list, center_index=-1):
        #calculate center point
        x_center = 0
        y_center = 0
        for p in p_list:
            x_center += p[0]
            y_center += p[1]
        x_center /= len(p_list)
        y_center /= len(p_list)
        new_p_list = []
        if center_index == -1:  # center with calculated center point
            x_move = x_center * -1
            y_move = y_center * -1
        else:  # center with center_index
            center_p = p_list[center_index]
            x_move = center_p[0] * -1
            y_move = center_p[1] * -1
        #make new list with new points
        for index in range(len(p_list)):
            if center_index == -1:
                p = p_list[index]
                new_p_list.append((p[0]+x_move, p[1]+y_move))
            else:
                if index == center_index:
                    new_p_list.append((0, 0))
                else:
                    p = p_list[index]
                    new_p_list.append((p[0]+x_move, p[1]+y_move))
        return new_p_list

    def move_p(p_list=list, x_move=0, y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move, p[1]+y_move))
        return new_p_list

    def new_p_angle(angle, length, p=[0, 0]):
        import math
        angle_radiant = math.radians(angle)
        x = round((math.cos(angle_radiant)*length), 5) + p[0]
        y = round((math.sin(angle_radiant)*length), 5) + p[1]
        return (x, y)
    scale = 100
    #points - p_top,p_right,p_center
    p_center = (0, 0)
    if width_height != []:
        if len(width_height) != 2:
            raise Exception("Input is incomplete")
        len_width = width_height[0]
        len_height = width_height[1]
        angle = math.degrees(math.atan(len_height/len_width))
        len_left = abs(len_height/math.cos(math.radians(180-angle)))
        p_right = (len_width, 0)
        p_top = new_p_angle(angle, len_left, p_center)
    elif right_bottom_left != []:
        if len(right_bottom_left) != 3:
            raise Exception("Input is incomplete")
        len_right = right_bottom_left[0]
        len_bottom = right_bottom_left[1]
        len_left = right_bottom_left[2]
        if len_right > len_bottom+len_left or len_bottom > len_right+len_left or len_left > len_right+len_bottom:
            raise Exception(
                "Lengths of triangle are against the triangle inequality theorem, which means sum of two lengths is smaller than the other length")
        angle = math.degrees(
            math.acos((len_bottom**2+len_left**2-len_right**2)/(2*len_bottom*len_left)))
        p_right = (len_bottom, 0)
        p_top = new_p_angle(angle, len_left, p_center)
    elif bottom_left_angle != []:
        if len(bottom_left_angle) != 3:
            raise Exception("Input is incomplete")
        len_bottom = bottom_left_angle[0]
        len_left = bottom_left_angle[1]
        angle = bottom_left_angle[2]
        p_right = (len_bottom, 0)
        p_top = new_p_angle(angle, len_left, p_center)
    else:
        raise Exception("No input to make points for triangle")

    triangle = [p_top, p_right, p_center]
    triangle = move_p(triangle, move_x, move_y)
    return triangle


def resize_polygon(p_list=list, scale=90):
    def move_to_center(p_list=list, center_index=-1):
        #calculate center point
        x_center = 0
        y_center = 0
        for p in p_list:
            x_center += p[0]
            y_center += p[1]
        x_center /= len(p_list)
        y_center /= len(p_list)
        new_p_list = []
        if center_index == -1:  # center with calculated center point
            x_move = x_center * -1
            y_move = y_center * -1
        else:  # center with center_index
            center_p = p_list[center_index]
            x_move = center_p[0] * -1
            y_move = center_p[1] * -1
        #make new list with new points
        for index in range(len(p_list)):
            if center_index == -1:
                p = p_list[index]
                new_p_list.append((p[0]+x_move, p[1]+y_move))
            else:
                if index == center_index:
                    new_p_list.append((0, 0))
                else:
                    p = p_list[index]
                    new_p_list.append((p[0]+x_move, p[1]+y_move))
        return new_p_list
    #move to center
    p_list = move_to_center(p_list)
    #find the criteria point
    criteria_val = abs(p_list[0][0])

    for p in p_list:
        x = p[0]
        y = p[1]
        #compare
        if max(abs(x), abs(y)) > criteria_val:
            criteria_val = max(abs(x), abs(y))
    #find ratio
    ratio = scale/criteria_val
    #create new_p_num
    new_p_num = []

    for p in p_list:
        x_new = p[0] * ratio
        y_new = p[1] * ratio
        new_p_num.append((x_new, y_new))
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
        ax.hist(x, bins=bins, histtype="bar", fc=color,
                ec="black",  zorder=3, label=legend)
    elif mode == "line":
        ax.hist(x, bins=bins, histtype="bar", fc=color,
                ec="black",  zorder=3, visible=False)
        ax.plot(bincenters, y, zorder=3, color=color, marker='o', label=legend)

    if legend != None:
        ax.legend()

    plt.xlabel(xlabel, loc="right")
    plt.ylabel(ylabel, loc="top", rotation=0)
    ax.grid(visible=True)

# 부채꼴


def drawSector(ax, center, radius, theta1, theta2, fill=False, alpha=1, dash=False, lw=1, arrow=False):
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




def planefigure122_Stem_002():
    stem = "다음 그림과 같은 $$수식$$\\triangle ABC$$/수식$$에서 $$수식$$\\angle x+ \\angle y$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$        ② $$수식$${a2}DEG $$/수식$$     ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$        ⑤ $$수식$${a5}DEG $$/수식$$"

    ag1_list = [125,130,135]
    ag1 = random.choice(ag1_list)
    ag2_list = [40,45,50] 
    ag2 = random.choice(ag2_list)

    #p1 = (0,0)
    #p2 = (2.4,0)

    #b = (0.4,0)
    #c = (2,0)
    
    p1 = (0, 2)
    p2 = (2.4, 2)

    b = (0.4, 2)
    c = (2, 2)

    a_x = 2+1.2*math.cos(math.radians(180-ag2))
    a_y = 1.2*math.sin(math.radians(180-ag2))

    a = (a_x,a_y+2)

       
    #ax = setChart(points=[p1, p2, a, b, c])
    fig, ax = plt.subplots(figsize=(4, 2))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=b, p2=a)
    drawLine(ax=ax, p1=a, p2=c)

    
    a1 = AngleAnnotation(xy=b, p1=a, p2=p1, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=20)    
    a2 = AngleAnnotation(xy=b, p1=c, p2=a, text=r"$x$",
                         textposition="outside", ax=ax, size=30)
    a3 = AngleAnnotation(xy=c, p1=p2, p2=a, text=r"$y$",
                    textposition="outside", ax=ax, size=20)
    a4 = AngleAnnotation(xy=c, p1=a, p2=b, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30)

    
    if ag2 == 40 :
      ax.text(1.02,2.85, "A", size = 15)
    elif ag2 == 45 :
      ax.text(1.08,2.93, "A", size = 15)
    elif ag2 == 50 :
      ax.text(1.17,2.96, "A", size = 15)

    ax.text(0.35,1.84, "B", size = 15)
    ax.text(1.9,1.83, "C", size = 15)

    s1 = 180-ag1
    s2 = 180-ag2

    ans = s1+s2

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

    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\angle x=180 DEG - {ag1}DEG = {s1}DEG $$/수식$$\n" \
              "$$수식$$\\angle y=180 DEG - {ag2}DEG = {s2}DEG $$/수식$$\n" \
              "$$수식$$THEREFORE \\angle x+\\angle y = {ans}DEG $$/수식$$\n"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag1=ag1, ag2=ag2, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_006():
    stem = "어떤 다각형의 한 내각의 크기가 $$수식$${ag}DEG $$/수식$$일 때, 이 내각에 대한 외각의 크기를 구하시오.\n" \

    ag_list = [35,40,45,50,55,60,65]
    ag = random.choice(ag_list)

    result = 180-ag


    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n (내각의 크기)+(외각의 크기)=$$수식$$180 DEG $$/수식$$이므로\n" \
              "$$수식$$180 DEG - {ag}DEG = {result}DEG $$/수식$$"

    stem = stem.format(ag=ag)
    answer = answer.format(result=result)
    comment = comment.format(ag=ag, result=result)

    return stem, answer, comment


def planefigure122_Stem_008():
    stem = "다음 조건을 만족시키는 다각형의 이름을 말하시오.\n" \
           "$$표$$" \
           "(가) 모든 변의 길이가 같다.\n" \
           "(나) 모든 내각의 크기가 같다.\n" \
           "(다) $$수식$${n}$$/수식$$개의 선분으로 둘러싸여 있다.$$/표$$\n"

    n = random.randint(7,12)

    if n == 7 :
      s1 = "칠"
      s2 = "각형"
      result = "정칠각형"
    elif n == 8 :
      s1 = "팔"
      s2 = "각형"
      result = "정팔각형"
    elif n == 9 :
      s1 = "구"
      s2 = "각형"
      result = "정구각형"
    elif n == 10 :
      s1 = "십"
      s2 = "각형"
      result = "정십각형"
    elif n == 11 :
      s1 = "십"
      s2 = "일각형"
      result = "정십일각형"
    elif n == 12 :
      s1 = "십"
      s2 = "이각형"
      result = "정십이각형"

    answer = "(정답)\n{result}"
    comment = "(해설)\n (다)에서 $$수식$${n}$$/수식$$개의 선분으로 둘러싸여 있으므로 {s1}\n" \
              "{s2}이고, (나), (다)에서 모든 변의 길이가 같고\n" \
              "모든 내각의 크기가 같으므로 정다각형이다.\n" \
              "따라서 구하는 다각형은 {result}이다."

    stem = stem.format(n=n)
    answer = answer.format(result=result)
    comment = comment.format(n=n, s1=s1, s2=s2, result=result)
    
    return stem, answer, comment




def planefigure122_Stem_011():
    stem = "다음 그림과 같은 $$수식$$\\triangle ABD$$/수식$$에서 $$수식$$\\angle x+ \\angle y$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$        ② $$수식$${a2}DEG $$/수식$$     ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$        ⑤ $$수식$${a5}DEG $$/수식$$\n" \

    ag1 = random.randint(80,86)
    ag2 = random.randint(20,25)
    ag3 = random.randint(30,35)

    a = (1,1.7)
    b = (0,0)
    c = (0.7,0)
    d = (1.6,0)

    p = (2.1,0)
      
    #ax = setChart(points=[a, b, c, d, p])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=b, p2=p)
    drawLine(ax=ax, p1=b, p2=a)
    drawLine(ax=ax, p1=a, p2=c)
    drawLine(ax=ax, p1=a, p2=d)
    
    a1 = AngleAnnotation(xy=a, p1=b, p2=c, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="edge",  text_kw=dict(xytext=(-40, -20), arrowprops=dict(arrowstyle="->",
                              connectionstyle="arc3,rad=0.4")), ax=ax, size=40)    
    a2 = AngleAnnotation(xy=b, p1=c, p2=a, text=r"$x$",
                         textposition="outside", ax=ax, size=30)
    a3 = AngleAnnotation(xy=a, p1=c, p2=d, text=r"${ag3}°$".format(ag3=ag3),
                    textposition="edge",  text_kw=dict(xytext=(30, -20), arrowprops=dict(arrowstyle="->",
                              connectionstyle="arc3,rad=-0.4")), ax=ax, size=40)   
    a4 = AngleAnnotation(xy=d, p1=p, p2=a, text=r"$y$",
                    textposition="outside", ax=ax, size=25)
    a5 = AngleAnnotation(xy=c, p1=d, p2=a, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)
    
    ax.text(0.95,1.73, "A", size = 16)
    ax.text(-0.14,-0.04, "B", size = 16)
    ax.text(0.64,-0.15, "C", size = 16)
    ax.text(1.55,-0.15, "D", size = 16)

    s1 = ag1-ag2
    s2 = ag3+ag1

    ans = s1+s2

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

    
    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\triangle ABC$$/수식$$에서 $$수식$$\\angle x={ag1}DEG - {ag2}DEG = {s1}DEG $$/수식$$\n" \
              "$$수식$$\\triangle ACD$$/수식$$에서 $$수식$$\\angle y={ag3}DEG + {ag1}DEG = {s2}DEG $$/수식$$\n" \
              "$$수식$$THEREFORE \\angle x+\\angle y={ans}$$/수식$$\n" 

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag1=ag1, ag2=ag2, ag3=ag3, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 




def planefigure122_Stem_012():
    stem = "다음 그림에서 $$수식$$\\angle x$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$        ② $$수식$${a2}DEG $$/수식$$     ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$        ⑤ $$수식$${a5}DEG $$/수식$$\n" \

    ag1 = random.randint(55,59)
    ag2 = random.randint(40,45)
    ag3 = random.randint(50,54)

    a = (0.4,1.7)
    b = (0,0)
    d = (2.05,1.6)
    e = (2,0.1)

    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=a, p2=e)
    drawLine(ax=ax, p1=b, p2=d)
    drawLine(ax=ax, p1=d, p2=e)

    
    a1 = AngleAnnotation(xy=a, p1=b, p2=e, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=35)    
    a2 = AngleAnnotation(xy=b, p1=d, p2=a, text=r"${ag2}°$".format(ag2=ag2),
                         textposition="outside", ax=ax, size=35)
    a3 = AngleAnnotation(xy=d, p1=b, p2=e, text=r"${ag3}°$".format(ag3=ag3),
                    textposition="outside", ax=ax, size=35)
    a4 = AngleAnnotation(xy=e, p1=d, p2=a, text=r"$x$",
                    textposition="outside", ax=ax, size=35)
    
    ax.text(0.35,1.75, "A", size = 15)
    ax.text(-0.08,-0.15, "B", size = 15)
    ax.text(1.11,0.75, "C", size = 15)
    ax.text(2,1.65, "D", size = 15)
    ax.text(1.96,-0.06, "E", size = 15)

    s1 = 180-(ag1+ag2)
    ans = 180-(ag3+s1)

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
          
    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\triangle ABC$$/수식$$에서\n" \
              "$$수식$$\\angle ACB=180 DEG - ({ag1}DEG + {ag2}DEG )={s1}DEG $$/수식$$\n" \
              "$$수식$$\\angle DCE=\\angle ACB={s1}DEG $$/수식$$(맞꼭지각)이므로\n" \
              "$$수식$$\\triangle CED$$/수식$$에서\n" \
              "$$수식$$\\angle x=180 DEG - ({ag3}DEG + {s1}DEG )={ans}DEG $$/수식$$\n"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag1=ag1, ag2=ag2, ag3=ag3, s1=s1,ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_014():
    stem = "다음 그림의 $$수식$$\\triangle ABC$$/수식$$에서$$수식$$\\angle A={ag}DEG $$/수식$$, " \
            "$$수식$${k1}\\angle B={k2}\\angle C$$/수식$$일 때, $$수식$$\\angle B$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$        ② $$수식$${a2}DEG $$/수식$$     ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$        ⑤ $$수식$${a5}DEG $$/수식$$\n"

    k = random.choice([[5,3],[5,4],[4,3]])
    
    b = (0,0)
    c = (1.7,0)
       
    #ax = setChart(points=[b,c])
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    if k == [5,3] :
      k1 = 5
      k2 = 3
      f1 = "\\frac{5}{3}"
      f2 = "\\frac{8}{3}"
      a = (1.4,1.5)
      ax.text(1.36,1.54, "A", size = 17)
    elif k == [5,4] :
      k1 = 5
      k2 = 4
      f1 = "\\frac{5}{4}"
      f2 = "\\frac{9}{4}"
      a = (1.0,1.5)
      ax.text(0.96,1.54, "A", size = 17)
    elif k == [4,3] :
      k1 = 4
      k2 = 3
      f1 = "\\frac{4}{3}"
      f2 = "\\frac{7}{3}"
      a = (0.8,1.5)
      ax.text(0.76,1.54, "A", size = 17)


    while True :
      ag = random.randint(50,60)
      s1 = 180-ag
      if (s1*k2)%(k1+k2) == 0:
        break

    ans = int((s1*k2)/(k1+k2))
    
    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=b, p2=c)
    drawLine(ax=ax, p1=c, p2=a)
   
    a1 = AngleAnnotation(xy=a, p1=b, p2=c, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=38)    
    a2 = AngleAnnotation(xy=b, p1=c, p2=a, text=r"",
                         textposition="outside", ax=ax, size=40)
    

    ax.text(-0.13,-0.05, "B", size = 17)
    ax.text(1.74,-0.05, "C", size = 17)

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

    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$${k1}\\angle B={k2}\\angle C$$/수식$$에서 $$수식$$\\angle C={f1}\\angle B$$/수식$$\n" \
              "이때 $$수식$$\\angle A+\\angle B+\\angle C=180 DEG $$/수식$$이므로\n" \
              "$$수식$${ag}DEG + \\angle B+{f1}\\angle B=180 DEG $$/수식$$\n" \
              "$$수식$${f2}\\angle B={s1}DEG $$/수식$$      $$수식$$THEREFORE \\angle B={ans}DEG $$/수식$$"

    stem = stem.format(ag=ag, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, k1=k1, k2=k2)
    answer = answer.format(result=result)
    comment = comment.format(f1=f1, f2=f2, ag=ag, k1=k1, k2=k2, s1=s1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_015():
    stem = "다음 그림과 같이 $$수식$${ac}$$/수식$$와 $$수식$${bd}$$/수식$$의 교점을 $$수식$$E$$/수식$$라 할 때, " \
            "$$수식$$\\angle x$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$        ② $$수식$${a2}DEG $$/수식$$     ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$        ⑤ $$수식$${a5}DEG $$/수식$$\n"

    ag1 = random.randint(66,70)
    ag2 = random.randint(60,64)

    if ag1 == 66 :
      ay = 0.8
      ay2 = 0.83
      ey = 0.46
      ex = 0.83
      ex2 = 0.775
      ey2 = 0.51
    elif ag1 == 67 :
      ay = 0.75
      ay2 = 0.78
      ey = 0.445
      ex = 0.79
      ex2 = 0.745
      ey2 = 0.49
    elif ag1 == 68 :
      ay = 0.7
      ay2 = 0.73
      ey = 0.425
      ex = 0.77
      ey2 = 0.48
      ex2 = 0.72
    elif ag1 == 69 :
      ay = 0.65
      ay2 = 0.68
      ey = 0.41
      ex = 0.76
      ex2 = 0.69
      ey2 = 0.47
    elif ag1 == 70 :
      ay = 0.6
      ay2 = 0.63
      ey = 0.39
      ex = 0.725
      ex2 = 0.65
      ey2 = 0.45

    if ag2 == 60 :
      dy = 1.1
      dy2 = 1.15
    elif ag2 == 61 :
      dy = 1.15
      dy2 = 1.2
    elif ag2 == 62 :
      dy = 1.2
      dy2 = 1.25
    elif ag2 == 63 :
      dy = 1.25
      dy2 = 1.3
    elif ag2 == 64 :
      dy = 1.3
      dy2 = 1.35
    

    a = (0,ay)
    b = (0,0)
    c = (2,0)
    d = (2,1.1)
    e = (ex,ey)
       
    #ax = setChart(points=[a,b,c,d,e])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=a, p2=c)
    drawLine(ax=ax, p1=b, p2=d)
    drawLine(ax=ax, p1=d, p2=c)
    drawLine(ax=ax, p1=b, p2=c)

    x = [0.06,0.06,0]
    y = [0,0.06,0.06]

    ax.plot(x,y, c="black", linewidth = 0.5)

    x2 = [1.94,1.94,2]
    y2 = [0,0.06,0.06]

    ax.plot(x2,y2, c="black", linewidth = 0.5)

    
    a1 = AngleAnnotation(xy=a, p1=b, p2=c, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)    
    a2 = AngleAnnotation(xy=d, p1=b, p2=c, text=r"${ag2}°$".format(ag2=ag2),
                         textposition="outside", ax=ax, size=30)
    a3 = AngleAnnotation(xy=e, p1=b, p2=c, text=r"x",
                    textposition="outside", ax=ax, size=25)

    
    ax.text(-0.05,ay2, "A", size = 16)
    ax.text(-0.12,-0.08, "B", size = 16)
    ax.text(2.02,-0.08, "C", size = 16)
    ax.text(1.95,1.15, "D", size = 16)
    ax.text(ex2,ey2, "E", size = 16)
    
    s1 = 180-(90+ag1)
    s2 = 180-(90+ag2)
    ans = 180-(s1+s2)

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

    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\triangle ABC$$/수식$$에서\n" \
              "$$수식$$\\angle ACB=180 DEG - (90 DEG + {ag1}DEG )={s1}DEG $$/수식$$\n" \
              "$$수식$$\\triangle BCD$$/수식$$에서\n" \
              "$$수식$$\\angle DBC=180 DEG - (90 DEG + {ag2}DEG )={s2}DEG $$/수식$$\n" \
              "$$수식$$\\triangle BCE$$/수식$$에서\n" \
              "$$수식$$\\angle x=180 DEG - ({s1}DEG + {s2}DEG )={ans}DEG $$/수식$$\n"

    ac = "\\overline{AC}"
    bd = "\\overline{BD}"

    stem = stem.format(ac=ac, bd=bd, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag1=ag1, ag2=ag2, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_016():
    stem = "다음 그림과 같은 $$수식$$\\triangle ABC$$/수식$$에서 $$수식$$x$$/수식$$의 값을 구하시오.\n" \

    ag = random.randint(100,108)

    while True :
      nn1 = random.randint(1,2)
      n2 = random.randint(10,20)
      s1 = nn1+1
      s2 = ag-n2
      if s2 % s1 == 0 :
        break

    if nn1 == 1:
        n1 = ""
    elif nn1 == 2:
        n1 = 2

    a = (-1.1,1.2)
    b = (-1.9,0)
    c = (0,0)
    p = (-1.4,(1.4*1.2)/1.1)
       
    #ax = setChart(points=[a,b,c,p])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=b, p2=c)
    drawLine(ax=ax, p1=c, p2=p)
   
    a1 = AngleAnnotation(xy=a, p1=p, p2=b, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=24)    
    a2 = AngleAnnotation(xy=b, p1=c, p2=a, text=r"",
                    textposition="outside", ax=ax, size=25)
    a3 = AngleAnnotation(xy=c, p1=a, p2=b, text=r"$x°$",
                    textposition="outside", ax=ax, size=30)
    
    ax.text(-1.08,1.24, "A", size = 15)
    ax.text(-1.73,0.1, "${n1}x°+{n2}°$".format(n1=n1,n2=n2), size = 10)
    ax.text(-2.08,-0.08, "B", size = 15)
    ax.text(0.05,-0.08, "C", size = 15)

    result = int(s2/s1)

    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n $$수식$${n1}x+{n2}+x={ag}$$/수식$$에서\n" \
              "$$수식$${s1}x={s2}$$/수식$$    $$수식$$THEREFORE x={result}$$/수식$$"

    answer = answer.format(result=result)
    comment = comment.format(ag=ag, n1=n1, n2=n2, s1=s1, s2=s2, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 




def planefigure122_Stem_020():
    stem = "다음 그림과 같은 $$수식$$\\triangle ABC$$/수식$$에서 $$수식$$\\angle BDC = {ag}DEG $$/수식$$이고, " \
            "$$수식$$\\angle ABD=\\angle DBC,$$/수식$$, $$수식$$\\angle ACD=\\angle DCB$$/수식$$일 때, $$수식$$\\angle x$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$   ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$    ⑤ $$수식$${a5}DEG $$/수식$$\n" 

    ag_list = [120,125,130]
    ag = random.choice(ag_list)

    a = (0.8,1.6)
    b = (0,0)
    c = (2,0)
    d = (0.9,0.5)
       
    #ax = setChart(points=[a,b,c,d])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=b, p2=c)
    drawLine(ax=ax, p1=c, p2=a)

    drawLine(ax=ax, p1=b, p2=d)
    drawLine(ax=ax, p1=d, p2=c)
    
    x = [0.17,0.14]
    y = [0.05,0.14]

    x2 = [1.74,1.78]
    y2 = [0.07,0.03]
    ax.plot(x2,y2, c="black", linewidth = 0.7)

    x3 = [1.78,1.74]
    y3 = [0.07,0.03]
    ax.plot(x3,y3, c="black", linewidth = 0.7)

    x4 = [1.78,1.82]
    y4 = [0.18,0.14]
    ax.plot(x4,y4, c="black", linewidth = 0.7)

    x5 = [1.82,1.78]
    y5 = [0.18,0.14]
    ax.plot(x5,y5, c="black", linewidth = 0.7)

    plt.scatter(x, y, c='black', edgecolor='black', s=8)
   
    a1 = AngleAnnotation(xy=d, p1=b, p2=c, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=27)    
    a2 = AngleAnnotation(xy=a, p1=b, p2=c, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    
    ax.text(0.75,1.65, "A", size = 16)
    ax.text(-0.13,-0.08, "B", size = 16)
    ax.text(2.02,-0.08, "C", size = 16)
    ax.text(0.84,0.55, "D", size = 16)

    s1 = 180-ag
    ans = 180-(2*s1)

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

    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\triangle DBC$$/수식$$에서\n" \
              "$$수식$$\\angle DBC+\\angle DCB=180 DEG - {ag}DEG ={s1}DEG $$/수식$$\n" \
              "따라서 $$수식$$\\triangle ABC$$/수식$$에서\n" \
              "$$수식$$\\angle x=180 DEG - (\\angle ABC+\\angle ACB)$$/수식$$\n" \
              "$$수식$$=180 DEG -2(\\angle DBC+\\angle DCB)$$/수식$$\n" \
              "$$수식$$=180 DEG - 2  TIMES  {s1}DEG = {ans}DEG $$/수식$$\n"

    stem = stem.format(ag=ag, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag=ag, s1=s1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_021():
    stem = "다음 그림과 같이 $$수식$$\\triangle ABC$$/수식$$에서 $$수식$$\\angle B$$/수식$$의 " \
            "이등분선과 $$수식$$\\angle C$$/수식$$의 외각의 이등분선의 교점을 $$수식$$D$$/수식$$라 하자. " \
            "$$수식$$\\angle A={ag}DEG $$/수식$$일 때, $$수식$$\\angle x$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$   ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$    ⑤ $$수식$${a5}DEG $$/수식$$\n" 

    while True :
      ag = random.randint(70,78)
      if ag % 2 == 0 :
        break

    if ag == 70 :
      ay = 1
      ay2 = 1.02
    elif ag == 72 :
      ay = 0.95
      ay2 = 0.97
    elif ag == 74 :
      ay = 0.9
      ay2 = 0.92
    elif ag == 76 :
      ay = 0.85
      ay2 = 0.87
    elif ag == 78 :
      ay = 0.8
      ay2 = 0.82


    a = (0.35,ay)
    b = (0,0)
    c = (1.6,0)
    d = (2.1,1.45)
    e = (2,0)
    p = (2.3,0)
       
    #ax = setChart(points=[a,b,c,d,e,p])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    
    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=b, p2=p)
    drawLine(ax=ax, p1=c, p2=a)

    drawLine(ax=ax, p1=b, p2=d)
    drawLine(ax=ax, p1=d, p2=c)
    
    x = [0.16,0.12]
    y = [0.06,0.17]

    x2 = [1.42,1.46]
    y2 = [0.07,0.03]
    ax.plot(x2,y2, c="black", linewidth = 0.7)

    x3 = [1.46,1.42]
    y3 = [0.07,0.03]
    ax.plot(x3,y3, c="black", linewidth = 0.7)

    x4 = [1.54,1.58]
    y4 = [0.12,0.08]
    ax.plot(x4,y4, c="black", linewidth = 0.7)

    x5 = [1.58,1.54]
    y5 = [0.12,0.08]

    ax.plot(x5,y5, c="black", linewidth = 0.7)

    plt.scatter(x, y, c='black', edgecolor='black', s=8)

    plt.scatter(2, 0, c='black', edgecolor='black', s=14)
   
    a1 = AngleAnnotation(xy=a, p1=b, p2=c, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)    
    a2 = AngleAnnotation(xy=d, p1=b, p2=c, text=r"$x$",
                    textposition="outside", ax=ax, size=35)
    
    ax.text(0.29,ay2, "A", size = 16)
    ax.text(-0.15,-0.08, "B", size = 16)
    ax.text(1.5,-0.2, "C", size = 16)
    ax.text(2.07,1.48, "D", size = 16)
    ax.text(1.94,-0.2, "E", size = 16)

    f = "\\frac{1}{2}"
    s1 = int(ag/2)
    ans = s1

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

    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\triangle ABC$$/수식$$에서\n" \
              "$$수식$$\\angle ACE={ag}DEG + \\angle ABC$$/수식$$이므로\n" \
              "$$수식$$\\angle DCE={f}\\angle ACE={f}({ag}DEG + 2\\angle DBC)$$/수식$$\n" \
              "     =$$수식$${s1}DEG + \\angle DBC$$/수식$$     $$수식$$\\cdot\\cdot\\cdot\\cdot\\cdot$$/수식$$㉠\n" \
              "$$수식$$\\triangle DBC$$/수식$$에서\n" \
              "$$수식$$\\angle DBC$$/수식$$에서\n" \
              "$$수식$$\\angle DCE=\\angle x+\\angle DBC$$/수식$$       $$수식$$\\cdot\\cdot\\cdot\\cdot\\cdot$$/수식$$㉡\n" \
              "㉠,㉡에서 $$수식$$\\angle x={ans}DEG $$/수식$$\n"

    stem = stem.format(ag=ag, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag=ag, f=f, s1=s1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_023():
    stem = "다음 그림에서 $$수식$${ac}={bc}={bd}$$/수식$$이고 $$수식$$\\angle DBE={ag}DEG $$/수식$$일 때, $$수식$$\\angle x$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$   ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$    ⑤ $$수식$${a5}DEG $$/수식$$\n" 

    while True :
      ag = random.randint(120,130)
      if ag % 3 == 0 :
        break

    if ag == 120 : 
      bx = 1.6
      bx2 = 1.54
      ex = 1.9
      ex2 = 1.85
      px = 2.1
      c = (0.8,0.7)
      cx = 0.7
      cy = 0.75
      x = [0.4,0.45]
      y = [0.4,0.34]
      x2 = [0.42,0.47]
      y2 = [0.42,0.36]
      x3 = [1.15,1.2]
      y3 = [0.34,0.4]
      x4 = [1.13,1.18]
      y4 = [0.36,0.42]
      x5 = [1.3,1.37]
      y5 = [0.47,0.51]
      x6 = [1.28,1.35]
      y6 = [0.49,0.53]    
    elif ag == 123 :
      bx = 1.65
      bx2 = 1.59
      ex = 1.95
      ex2 = 1.9
      px = 2.15
      c = (0.84,0.74)
      cx = 0.7
      cy = 0.75
      x = [0.4,0.45]
      y = [0.4,0.34]
      x2 = [0.42,0.47]
      y2 = [0.42,0.36]
      x3 = [1.21,1.26]
      y3 = [0.34,0.4]
      x4 = [1.19,1.24]
      y4 = [0.36,0.42]
      x5 = [1.32,1.39]
      y5 = [0.47,0.52]
      x6 = [1.3,1.37]
      y6 = [0.49,0.54] 
    elif ag == 126 :
      bx = 1.7
      bx2 = 1.64
      ex = 2
      ex2 = 1.95
      px = 2.2
      c = (0.85,0.74)
      cx = 0.7
      cy = 0.75
      x = [0.4,0.45]
      y = [0.4,0.34]
      x2 = [0.42,0.47]
      y2 = [0.42,0.36]
      x3 = [1.25,1.3]
      y3 = [0.34,0.4]
      x4 = [1.23,1.28]
      y4 = [0.36,0.42]
      x5 = [1.36,1.43]
      y5 = [0.45,0.5]
      x6 = [1.34,1.41]
      y6 = [0.47,0.52] 
    elif ag == 129 :
      bx = 1.75
      bx2 = 1.69
      ex = 2.05
      ex2 = 2
      px = 2.25
      c = (0.9,0.775)
      cx = 0.7
      cy = 0.75
      x = [0.4,0.45]
      y = [0.4,0.34]
      x2 = [0.42,0.47]
      y2 = [0.42,0.36]
      x3 = [1.32,1.37]
      y3 = [0.34,0.4]
      x4 = [1.3,1.35]
      y4 = [0.36,0.42]
      x5 = [1.39,1.46]
      y5 = [0.43,0.48]
      x6 = [1.37,1.44]
      y6 = [0.45,0.5] 

    a = (0,0)
    b = (bx,0)
    d = (1.08,0.95)
    e = (ex,0)
    p = (px,0)
       
    #ax = setChart(points=[a,b,c,d,e,p])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=a, p2=d)
    drawLine(ax=ax, p1=d, p2=b)
    drawLine(ax=ax, p1=a, p2=p)
    drawLine(ax=ax, p1=c, p2=b)
    
    ax.plot(x,y, c="black", linewidth = 0.7)
    ax.plot(x2,y2, c="black", linewidth = 0.7)
    ax.plot(x3,y3, c="black", linewidth = 0.7)
    ax.plot(x4,y4, c="black", linewidth = 0.7)    
    ax.plot(x5,y5, c="black", linewidth = 0.7)
    ax.plot(x6,y6, c="black", linewidth = 0.7)

    plt.scatter(ex, 0, c='black', edgecolor='black', s=14)
   
    a1 = AngleAnnotation(xy=b, p1=e, p2=d, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=25)    
    a2 = AngleAnnotation(xy=a, p1=b, p2=c, text=r"$x$",
                    textposition="outside", ax=ax, size=35)
  
    
    ax.text(-0.13,-0.06, "A", size = 15)
    ax.text(bx2,-0.17, "B", size = 15)
    ax.text(cx,cy, "C", size = 15)
    ax.text(1.05,0.98, "D", size = 15)
    ax.text(ex2,-0.17, "E", size = 15)

    ans = int(ag/3)

    if ag % 10 == 0 :
      aa_list = [ans-30, ans-20, ans-10, ans, ans+10, ans+20, ans+30]
    else :
      aa_list = [ans-9, ans-6, ans-3, ans, ans+3, ans+6, ans+9]
      
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

    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\triangle CAB$$/수식$$에서 $$수식$${ca}={cb}$$/수식$$이므로\n" \
              "$$수식$$\\angle CBA=\\angle CAB=\\angle x,$$/수식$$\n" \
              "$$수식$$\\angle BCD=\\angle x+\\angle x=2\\angle x$$/수식$$\n" \
              "$$수식$$\\triangle BCD$$/수식$$에서 $$수식$${bc}={bd}$$/수식$$이므로\n" \
              "$$수식$$\\angle BDC=\\angle BCD=2\\angle x$$/수식$$\n" \
              "따라서 $$수식$$\\triangle DAB$$/수식$$에서\n" \
              "$$수식$$2\\angle x+\\angle x={ag}DEG $$/수식$$\n" \
              "$$수식$$THEREFORE \\angle x={ans}DEG $$/수식$$" 

    ac = "\\overline{AC}"
    bc = "\\overline{BC}"
    bd = "\\overline{BD}"
    ca = "\\overline{CA}"
    cb = "\\overline{CB}"

    stem = stem.format(ac=ac, bc=bc, bd=bd, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, ag=ag)
    answer = answer.format(result=result)
    comment = comment.format(ca=ca, cb=cb, bc=bc, bd=bd, ag=ag, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_025():
    stem = "다음 그림과 같이 $$수식$${ab}={ac}$$/수식$$인 이등변삼각형 $$수식$$ABC$$/수식$$에서 " \
            "$$수식$$\\angle C$$/수식$$의 외각의 크기가 $$수식$${ag}DEG $$/수식$$일 때, $$수식$$\\angle x$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$   ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$    ⑤ $$수식$${a5}DEG $$/수식$$\n" 

    ag = random.choice([125,130,135])

    if ag == 125 :
      a = (1.05,1.5)
      ap = (1.3,1.5/1.05*1.3)
      ay = 1.5
      x = [0.47,0.53]
      y = [0.75,0.7]
      x2 = [0.49,0.55]
      y2 = [0.77,0.72]
      x3 = [1.57,1.62]
      y3 = [0.7,0.75]
      x4 = [1.55,1.6]
      y4 = [0.72,0.77]
    elif ag == 130 :
      a = (1.05,1.3)
      ap = (1.3,1.3/1.05*1.3)
      ay = 1.3
      x = [0.47,0.53]
      y = [0.65,0.6]
      x2 = [0.49,0.55]
      y2 = [0.67,0.62]
      x3 = [1.57,1.62]
      y3 = [0.6,0.65]
      x4 = [1.55,1.6]
      y4 = [0.62,0.67]
    elif ag == 135 :
      a = (1.05,1.1)
      ap = (1.3,1.1/1.05*1.3)
      ay = 1.1      
      x = [0.54,0.6]
      y = [0.62,0.57]
      x2 = [0.56,0.62]
      y2 = [0.64,0.59]
      x3 = [1.5,1.55]
      y3 = [0.57,0.62]
      x4 = [1.48,1.53]
      y4 = [0.59,0.64]

    b = (0,0)
    c = (2.1,0)

    cp = (2.5,0)
       
    
    #ax = setChart(points=[a,b,c,ap,cp])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=b, p2=ap)
    drawLine(ax=ax, p1=a, p2=c)
    drawLine(ax=ax, p1=b, p2=cp)


    ax.plot(x,y, c="black", linewidth = 0.7)
    ax.plot(x2,y2, c="black", linewidth = 0.7)
    ax.plot(x3,y3, c="black", linewidth = 0.7)
    ax.plot(x4,y4, c="black", linewidth = 0.7)
   
    a1 = AngleAnnotation(xy=c, p1=cp, p2=a, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=25)    
    

    a2 = AngleAnnotation(xy=a, p1=c, p2=ap, text=r"$x$",
                    textposition="outside", ax=ax, size=25)
    
    s1 = 180-ag
    ans = 2*s1
    
    ax.text(0.9,ay, "A", size = 15)
    ax.text(-0.15,-0.06, "B", size = 15)
    ax.text(2,-0.18, "C", size = 15)

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


    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\angle ACB=180 DEG - {ag}DEG ={s1}DEG $$/수식$$이므로\n" \
              "$$수식$$\\triangle ABC$$/수식$$에서\n" \
              "$$수식$$\\angle x=2 TIMES {s1}DEG = {ans}DEG $$/수식$$\n" 

    ab = "\\overline{AB}"
    ac = "\\overline{AC}"

    stem = stem.format(ab=ab, ac=ac, ag=ag, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag=ag, s1=s1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_029():
    stem = "다음 그림에서 $$수식$$\\angle PAB=\\angle CAB, \\angle QAD=\\angle CAD$$/수식$$일 때, $$수식$$\\angle x$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$     ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$    ⑤ $$수식$${a5}DEG $$/수식$$\n"

    while True :
      ag = random.randint(40,46)
      if ag % 2 == 0 :
        break

    a_y = (-0.1,0.4)
    a = (0,0)
    b = (-0.7,-1)
    b_x = (-1.05,-1.12)
    b_y = (-1.3*0.7,-1.3)
    c = (0.25,-1.25)
    p = (-0.85,0)
    q = (1.05,0)
    p2 = (-1.05,0)
    q2 = (1.35,0)

    if ag == 40 :
      d = (1.15,-0.82)
      d_x = (1.4,-0.78)
      d_y = (1.1/0.8,-1)
      dx = 1.03
      dy = -0.98
    elif ag == 42 :
      d = (1.1,-0.8)
      d_x = (1.35,-0.75)
      d_y = (1.1/0.8,-1)
      dx = 1
      dy = -0.98
    elif ag == 44 :
      d = (1.05,-0.8)
      d_x = (1.25,-0.75)
      d_y = (1.1/0.8,-1.05)
      dx = 0.95
      dy = -0.98    
    elif ag == 46 :
      d = (1,-0.8)
      d_x = (1.2,-0.75)
      d_y = (1.1/0.8,-1.1)
      dx = 0.9
      dy = -0.96
      
    
    #ax = setChart(points=[a,b,c,d,a_y,b_x,b_y,d_x,d_y,p,q,p2,q2])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p2, p2=q2)
    drawLine(ax=ax, p1=a_y, p2=c)
    drawLine(ax=ax, p1=a, p2=b_y)
    drawLine(ax=ax, p1=a, p2=d_y)
    drawLine(ax=ax, p1=b_x, p2=d_x)

    x = [-0.85,1.05]
    y = [0,0]
    plt.scatter(x, y, c='black', edgecolor='black', s=15)

    x2 = [0.05,0.12]
    y2 = [-0.09,-0.03]
    plt.scatter(x2, y2, c='black', edgecolor='black', s=7)

    x3 = [-0.07,-0.11]
    y3 = [-0.07,-0.03]
    ax.plot(x3,y3, c="black", linewidth = 0.7)

    x4 = [-0.11,-0.07]
    y4 = [-0.07,-0.03]
    ax.plot(x4,y4, c="black", linewidth = 0.7)

    x5 = [-0.01,-0.05]
    y5 = [-0.14,-0.1]
    ax.plot(x5,y5, c="black", linewidth = 0.7)

    x6 = [-0.05,-0.01]
    y6 = [-0.14,-0.1]
    ax.plot(x6,y6, c="black", linewidth = 0.7)

    a1 = AngleAnnotation(xy=d, p1=a, p2=b, text=r"${ag}°$".format(ag=ag),
                    textposition="outside", ax=ax, size=30)  
    a2 = AngleAnnotation(xy=b, p1=c, p2=a, text=r"$x$",
                    textposition="outside", ax=ax, size=30)
    
    ax.text(0,0.05, "A", size = 16)
    ax.text(-0.75,-1.25, "B", size = 16)
    ax.text(0.05,-1.12, "C", size = 16)
    ax.text(dx,dy, "D", size = 16)
    ax.text(-0.9,-0.2, "P", size = 16)
    ax.text(0.98,-0.2, "Q", size = 16)

    ans = 180-(90+ag)

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

    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\angle PAB=\\angle CAB,$$/수식$$ $$수식$$\\angle QAD=\\angle CAD$$/수식$$이므로\n" \
              "$$수식$$\\angle PAC+\\angle QAC=2\\angle BAC+2\\angle CAD$$/수식$$\n" \
              "$$수식$$=2(\\angle BAC+\\angle CAD)=180 DEG $$/수식$$\n" \
              "$$수식$$THEREFORE \\angle BAD=\\angle BAC+\\angle CAD=90 DEG $$/수식$$\n" \
              "따라서 $$수식$$\\triangle ABD$$/수식$$에서\n" \
              "$$수식$$\\angle x=180 DEG - (90 DEG + {ag}DEG )={ans}DEG $$/수식$$\n"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag=ag, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_030():
    stem = "다음 그림과 같은 $$수식$$\\triangle ABC$$/수식$$에서 $$수식$$\\angle ABD=\\angle DBC$$/수식$$이고 " \
            "$$수식$$\\angle A={ag2}DEG $$/수식$$, $$수식$$\\angle BDC={ag1}DEG $$/수식$$일 때, $$수식$$\\angle x$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$     ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$    ⑤ $$수식$${a5}DEG $$/수식$$\n" 

    while True :
      ag1 = random.randint(80,86)
      ag2 = random.randint(52,58)
      if ag1 % 2 == 0 and ag2 % 2 == 0 :
        break  
    
    if ag2 == 52 :
      a = (1.2,1.65)
      ay = 1.68
    elif ag2 == 54 :
      a = (1.2,1.6)
      ay = 1.63
    elif ag2 == 56 :
      a = (1.2,1.55)
      ay = 1.58
    elif ag2 == 58 :
      a = (1.2,1.5)
      ay = 1.53

    if ag1 == 80 :
      if ag2 == 52 :
        d = (1.47,0.75)
      elif ag2 == 58 :
        d = (1.45,0.75)
      else :
        d = (1.46,0.75)
      dx = 1.5
      dy = 0.72
    elif ag1 == 82 :
      if ag2 == 52 :
        d = (1.475,0.7)
      else :
        d = (1.47,0.7)
      dx = 1.5
      dy = 0.65
    elif ag1 == 84 :
      dx = 1.5
      dy = 0.65
      if ag2 == 52 :
        d = (1.485,0.65)
      elif ag2 == 58 :
        d = (1.48,0.65)
      else :
        d = (1.485,0.65)
    elif ag1 == 86 :
      if ag2 == 52 :
        d = (1.505,0.6)
      else :
        d = (1.495,0.6)
      dx = 1.52
      dy = 0.6      

    b = (0,0)
    c = (1.7,0)
    p = (2.2,0)

    
    #ax = setChart(points=[a,b,c,d,p])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=b, p2=p)
    drawLine(ax=ax, p1=c, p2=a)
    drawLine(ax=ax, p1=b, p2=d)
    
    x = [0.16,0.12]
    y = [0.04,0.1]

    plt.scatter(x, y, c='black', edgecolor='black', s=7)
  
    a1 = AngleAnnotation(xy=a, p1=b, p2=d, text=r"${ag2}°$".format(ag2=ag2),
                    textposition="outside", ax=ax, size=30)
    a2 = AngleAnnotation(xy=d, p1=b, p2=c, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=30)       
    a3 = AngleAnnotation(xy=c, p1=p, p2=a, text=r"$x$",
                    textposition="outside", ax=ax, size=25)

    ax.text(1.15,ay, "A", size = 16)
    ax.text(-0.15,-0.06, "B", size = 16)
    ax.text(1.64,-0.17, "C", size = 16)
    ax.text(dx,dy, "D", size = 16)

    s1 = ag1-ag2
    ans = s1+ag1

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

    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\triangle ABD$$/수식$$에서\n" \
              "$$수식$$\\angle ABD={ag1}DEG - {ag2}DEG = {s1}DEG $$/수식$$\n" \
              "따라서 $$수식$$\\angle DBC={s1}DEG $$/수식$$이므로 $$수식$$\\angle DBC$$/수식$$에서\n" \
              "$$수식$$\\angle x={s1}DEG + {ag1}DEG = {ans}DEG $$/수식$$\n"

    stem = stem.format(ag1=ag1, ag2=ag2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag1=ag1, ag2=ag2, s1=s1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_034():
    stem = "다음 그림의 $$수식$$\\triangle ABE$$/수식$$에서 $$수식$${bd}={cd}={ac}={ae}$$/수식$$이고 " \
            "$$수식$$\\angle B={ag}DEG $$/수식$$일 때, $$수식$$\\angle x$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$     ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$    ⑤ $$수식$${a5}DEG $$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$$\\triangle DBC$$/수식$$에서 $$수식$$\\angle CDA=2 TIMES {ag}DEG = {s1}DEG $$/수식$$\n" \
              "$$수식$$\\triangle CDA$$/수식$$에서 $$수식$$\\angle CAD=\\angle CDA={s1}DEG $$/수식$$\n" \
              "$$수식$$\\triangle ABC$$/수식$$에서 $$수식$$\\angle ACE={ag}DEG + {s1}DEG ={s2}DEG $$/수식$$\n" \
              "$$수식$$\\triangle ACE$$/수식$$에서 $$수식$$\\angle AEC=\\angle ACE={s2}DEG $$/수식$$\n" \
              "따라서 $$수식$$\\triangle ABE$$/수식$$에서\n" \
              "$$수식$$\\angle x={ag}DEG + {s2}DEG = {ans}DEG $$/수식$$\n"

    while True :
      ag = random.randint(22,30)
      if ag%2 == 0 :
        break
        
    s1 = ag*2
    s2 = ag+s1
    ans = ag+s2

    if ag == 22:
      a = (8.32*math.cos(math.radians(ag)),8.32*math.sin(math.radians(ag)))
      b = (0,0)
      c = (7*math.cos(math.radians(0)),7*math.sin(math.radians(0)))
      d = (3.8*math.cos(math.radians(ag))),3.8*math.sin(math.radians(ag))
      e = (8.5*math.cos(math.radians(0)),8.5*math.sin(math.radians(0)))
      a2 = (10*math.cos(math.radians(ag)),10*math.sin(math.radians(ag)))
      e2 = (10*math.cos(math.radians(0)),10*math.sin(math.radians(0)))     
    elif ag == 24 :
      a = (8.32*math.cos(math.radians(ag)),8.32*math.sin(math.radians(ag)))
      b = (0,0)
      c = (6.8*math.cos(math.radians(0)),6.8*math.sin(math.radians(0)))
      d = (3.7*math.cos(math.radians(ag))),3.7*math.sin(math.radians(ag))
      e = (8.5*math.cos(math.radians(0)),8.5*math.sin(math.radians(0)))
      a2 = (10*math.cos(math.radians(ag)),10*math.sin(math.radians(ag)))
      e2 = (10*math.cos(math.radians(0)),10*math.sin(math.radians(0)))
    elif ag == 26 :
      a = (8.32*math.cos(math.radians(ag)),8.32*math.sin(math.radians(ag)))
      b = (0,0)
      c = (6.6*math.cos(math.radians(0)),6.6*math.sin(math.radians(0)))
      d = (3.7*math.cos(math.radians(ag))),3.7*math.sin(math.radians(ag))
      e = (8.5*math.cos(math.radians(0)),8.5*math.sin(math.radians(0)))
      a2 = (10*math.cos(math.radians(ag)),10*math.sin(math.radians(ag)))
      e2 = (10*math.cos(math.radians(0)),10*math.sin(math.radians(0)))
    elif ag == 28 :
      a = (8.32*math.cos(math.radians(ag)),8.32*math.sin(math.radians(ag)))
      b = (0,0)
      c = (6.4*math.cos(math.radians(0)),6.4*math.sin(math.radians(0)))
      d = (3.7*math.cos(math.radians(ag))),3.7*math.sin(math.radians(ag))
      e = (8.5*math.cos(math.radians(0)),8.5*math.sin(math.radians(0)))
      a2 = (10*math.cos(math.radians(ag)),10*math.sin(math.radians(ag)))
      e2 = (10*math.cos(math.radians(0)),10*math.sin(math.radians(0)))
    elif ag == 30 :
      a = (8.32*math.cos(math.radians(ag)),8.32*math.sin(math.radians(ag)))
      b = (0,0)
      c = (6.1*math.cos(math.radians(0)),6.1*math.sin(math.radians(0)))
      d = (3.6*math.cos(math.radians(ag))),3.6*math.sin(math.radians(ag))
      e = (8.5*math.cos(math.radians(0)),8.5*math.sin(math.radians(0)))
      a2 = (10*math.cos(math.radians(ag)),10*math.sin(math.radians(ag)))
      e2 = (10*math.cos(math.radians(0)),10*math.sin(math.radians(0)))

       
    
    #ax = setChart(points=[a,b,c,d,e,a2,e2])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=d, p2=a2)
    drawLine(ax=ax, p1=b, p2=d,decoration="||")
    drawLine(ax=ax, p1=b, p2=e2)
    drawLine(ax=ax, p1=a, p2=e)
    drawLine(ax=ax, p1=d, p2=c, decoration="||")
    drawLine(ax=ax, p1=a, p2=c)
   
    a1 = AngleAnnotation(xy=a, p1=e, p2=a2, text=r'$x$',
                    textposition="outside", ax=ax, size=25)  
    a2 = AngleAnnotation(xy=b, p1=c, p2=d, text=r"${ag}°$".format(ag=ag),
                    textposition="edge",  text_kw=dict(xytext=(20, -20), arrowprops=dict(arrowstyle="->",
                              connectionstyle="arc3,rad=0.5")), ax=ax, size=40) 
    
    ae = ((a[0]+e[0])/2,(a[1]+e[1])/2)
    ac = ((a[0]+c[0])/2,(a[1]+c[1])/2)

    x = [ae[0]-0.16,ae[0]+0.12]
    y = [ae[1]+0.02,ae[1]+0.08]
    ax.plot(x,y, c="black", linewidth = 0.7)

    x2 = [ae[0]-0.14,ae[0]+0.14]
    y2 = [ae[1]-0.1,ae[1]-0.04]
    ax.plot(x2,y2, c="black", linewidth = 0.7)

    x3 = [ac[0]-0.14,ac[0]+0.14]
    y3 = [ac[1]+0.08,ac[1]+0.02]
    ax.plot(x3,y3, c="black", linewidth = 0.7)

    x4 = [ac[0]-0.16,ac[0]+0.12]
    y4 = [ac[1]-0.04,ac[1]-0.1]
    ax.plot(x4,y4, c="black", linewidth = 0.7)
    
    ax.text(a[0]-0.55,a[1]+0.15, "A", size = 16)
    ax.text(b[0]-0.65,b[1]-0.2, "B", size = 16)
    ax.text(c[0]-0.3,c[1]-0.8, "C", size = 16)
    ax.text(d[0]-0.5,d[1]+0.1, "D", size = 16)
    ax.text(e[0]-0.2,e[1]-0.8, "E", size = 16)

    bd = "\\overline{BD}"
    cd = "\\overline{CD}"
    ac = "\\overline{AC}"
    ae = "\\overline{AE}"

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


    stem = stem.format(bd=bd, cd=cd, ac=ac, ae=ae, ag=ag, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag=ag, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_036():
    stem = "{p}의 한 꼭짓점에서 그을 수 있는 대각선의 개수를 $$수식$$a$$/수식$$,내부의 한 점에서 각 꼭짓점에 선분을 그었을 때 생기는 삼각형의 개수를 $$수식$$b$$/수식$$라 할 때, $$수식$$a+b$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$    ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$    ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n {p}의 한 꼭짓점에서 그을 수 있는 대각선의\n" \
              "개수는 $$수식$${n}-3={s1}$$/수식$$(개)       $$수식$$THEREFORE a={s1}$$/수식$$\n" \
              "{p}의 내부의 한 점에서 각 꼭짓점에 선분을\n" \
              "그었을 때 생기는 삼각형의 개수는 $$수식$${n}$$/수식$$이므로\n" \
              "$$수식$$b={n}$$/수식$$\n" \
              "$$수식$$THEREFORE a+b={ans}$$/수식$$\n"
    
    n = random.randint(11,15)

    if n == 11 :
      p = "십일각형"
    elif n == 12 :
      p = "십이각형"
    elif n == 13:
      p = "십삼각형"
    elif n == 14:
      p = "십사각형"
    elif n == 15 :
      p = "십오각형"

    s1 = n-3
    ans = s1+n

    aa_list = [ans-9, ans-6, ans-3, ans, ans+3, ans+6, ans+9]
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
       

    stem = stem.format(p=p, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(p=p, n=n, s1=s1, ans=ans)

    return stem, answer, comment



def planefigure122_Stem_037():
    stem = "대각선의 개수가 $$수식$${n}$$/수식$$인 다각형은?\n" \
            "① {a1}    ② {a2}     ③ {a3}\n" \
            "④ {a4}    ⑤ {a5}\n" 
    answer = "(정답)\n {result}"
    comment = "(해설)\n 구하는 다각형을 $$수식$$n$$/수식$$각형이라 하면\n" \
              "$$수식$${f}={n}, n(n-3)={s1}={s2} TIMES {s3}$$/수식$$\n" \
              "$$수식$$n={s4}$$/수식$$\n" \
              "따라서 구하는 다각형은 {ans}이다.\n"

    f = "\\frac{n(n-3)}{2}"

    s4 = random.randint(10,14)
    s2 = s4
    s3 = s4-3
    s1 = s2*s3
    n = int(s1/2)

    if s4 == 10 :
      ans = "십각형"
    elif s4 == 11 :
      ans = "십일각형"
    elif s4 == 12 :
      ans = "십이각형"
    elif s4 == 13 :
      ans = "십삼각형"
    elif s4 == 14 :
      ans = "십사각형"

    
    p_list = ["팔각형","구각형","십각형","십일각형","십이각형","십삼각형","십사각형","십오각형"]
    a_list = []
    
    if s4 < 12 :
      idx = random.randint(0,1)
    elif s4 >= 12 :
      idx = random.randint(2,3)

    for i in range(5):
      a_list.append(p_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break


    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, n=n, s1=s1, s2=s2, s3=s3, s4=s4, ans=ans)

    return stem, answer, comment



def planefigure122_Stem_039():
    stem = "어떤 다각형의 내부의 한 점에서 각 꼭짓점에 선분을 그었을 때 생기는 삼각형의 개수가 $$수식$${n}$$/수식$$이다. " \
            "이 다각형의 한 꼭짓점에서 그을 수 있는 대각선의 개수는?\n" \
            "① $$수식$${a1}$$/수식$$    ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$    ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 내부의 한 점에서 각 꼭짓점에 선분을 그었을 때\n" \
              "생기는 삼각형의 개수가 $$수식$${n}$$/수식$$이므로 주어진 다각형은\n" \
              "{p}이다.\n" \
              "따라서 {p}의 한 꼭짓점에서 그을 수 있는\n대각선의 개수는\n" \
              "$$수식$${n}-3={ans}$$/수식$$(개)\n" 

    n = random.randint(8,12)

    if n == 8 :
      p = "팔각형"
    elif n == 9 :
      p = "구각형"
    elif n == 10 :
      p = "십각형"
    elif n == 11 :
      p = "십일각형"
    elif n == 12 :
      p = "십이각형"

    ans = n-3

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
    

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(p=p, n=n, ans=ans)

    return stem, answer, comment



def planefigure122_Stem_042():
    stem = "다음 그림과 같은 정{angle}각형에서 대각선 $$수식$${side}$$/수식$$와 한점에서 만나는 대각선의 개수는?\n"\
            "① $$수식$${a1}$$/수식$$    ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$    ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n 대각선 $$수식$${side}$$/수식$$와 한 점에서 만나도록 꼭짓점 $$수식$$A$$/수식$$에서\n" \
              "그을 수 있는 대각선의 개수는\n" \
              "{comment1}"\
              "따라서 구하는 대각선의 개수는\n" \
              "{comment2}"

    def regulerPoint(point, side, angle):
        result = [point]
        for i in range(1, side):
            x = point[1] * math.sin(angle*i)
            y = point[1] * math.cos(angle*i)
            
            result.append((x,y))
            
        return result
    
    n = random.randint(5, 9)
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    if n == 5:
        angle = "오"
        
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
        
        s_list = ["AC", "AD"]
        side = random.choice(s_list)
        
        if side == "AC":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n"
        elif side == "AD":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n"
              
        comment2 = "$$수식$$1 TIMES 2 + 1 TIMES 2 = 4$$/수식$$(개)"
        
    elif n == 6:
        angle = "육"
        
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
        
        s_list = ["AC", "AD", "AE"]
        side = random.choice(s_list)
        
        if side == "AC":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$3$$/수식$$(개)\n"
            comment2 = "$$수식$$2 TIMES 2 + 3 = 7$$/수식$$(개)"
            
            ans = 7
        elif side == "AD":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n"
            comment2 = "$$수식$$2 TIMES 2 + 2 TIMES 2 = 8$$/수식$$(개)"
            
            ans = 8
        elif side == "AE":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$D$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n"
            comment2 = "$$수식$$2 TIMES 2 + 1 TIMES 3 = 7$$/수식$$(개)"
            
            ans = 7
        
    elif n == 7:
        angle = "칠"
        
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

        s_list = ["AC", "AD", "AE", "AF"]
        side = random.choice(s_list)
        
        if side == "AC":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$4$$/수식$$(개)\n"
            comment2 = "$$수식$$3 TIMES 2 + 4 = 10$$/수식$$(개)"
            
            ans = 10
        elif side == "AD":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$3$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$3$$/수식$$(개)\n"
            comment2 = "$$수식$$3 TIMES 2 + 3 TIMES 2 = 12$$/수식$$(개)"
            
            ans = 12
        elif side == "AE":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$D$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n"
            comment2 = "$$수식$$3 TIMES 2 + 2 TIMES 3 = 12$$/수식$$(개)"
            
            ans = 12
        elif side == "AF":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$D$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$E$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n"
            comment2 = "$$수식$$3 TIMES 2 + 1 TIMES 4 = 10$$/수식$$(개)"
            
            ans = 10
        
    elif n == 8:
        angle = "팔"
        
        a = (0, 1)
        points = regulerPoint(a, n, (2*math.pi*45)/360)
        a, b, c, d, e, f, g, h = points

        
        #ax = setChart(points=[a, b, c, d, e, f, g, h])
        drawPolygon(ax=ax, verts=[a, b, c, d, e, f, g, h])

        ax.text(a[0]-0.03, a[1]+0.07, "A", size=14)
        ax.text(b[0]+0.03, b[1], "B", size=14)
        ax.text(c[0]+0.03, c[1]-0.02, "C", size=14)
        ax.text(d[0]+0.03, d[1]-0.03, "D", size=14)
        ax.text(e[0]-0.03, e[1]-0.12, "E", size=14)
        ax.text(f[0]-0.1, f[1]-0.03, "F", size=14)
        ax.text(g[0]-0.12, g[1]-0.02, "G", size=14)
        ax.text(h[0]-0.12, h[1], "H", size=14)
        
        s_list = ["AC", "AD", "AE", "AF", "AG"]
        side = random.choice(s_list)
        
        if side == "AC":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$5$$/수식$$(개)\n"
            comment2 = "$$수식$$4 TIMES 2 + 5 = 13$$/수식$$(개)"
            
            ans = 13
        elif side == "AD":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$4$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$4$$/수식$$(개)\n"
            comment2 = "$$수식$$4 TIMES 2 + 4 TIMES 2 = 16$$/수식$$(개)"
            
            ans = 16
        elif side == "AE":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$3$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$3$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$D$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$3$$/수식$$(개)\n"
            comment2 = "$$수식$$4 TIMES 2 + 3 TIMES 3 = 17$$/수식$$(개)"
            
            ans = 17
        elif side == "AF":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$D$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$E$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n"
            comment2 = "$$수식$$4 TIMES 2 + 2 TIMES 4 = 16$$/수식$$(개)"
            
            ans =16
        elif side == "AG":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$D$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$E$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$F$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n"
            comment2 = "$$수식$$4 TIMES 2 + 1 TIMES 5 = 13$$/수식$$(개)"
            
            ans = 13
        
    else:
        angle = "구"
        
        a = (0, 1)
        points = regulerPoint(a, n, (2*math.pi*40)/360)
        a, b, c, d, e, f, g, h, i = points
        
        
        #ax = setChart(points=[a,b,c,d,e,f,g,h,i])

        drawPolygon(ax=ax, verts=[a,b,c,d,e,f,g,h,i])
    
        ax.text(a[0]-0.03, a[1]+0.07, "A", size=14)
        ax.text(b[0]+0.03, b[1], "B", size=14)
        ax.text(c[0]+0.03, c[1]-0.02, "C", size=14)
        ax.text(d[0]+0.03, d[1]-0.03, "D", size=14)
        ax.text(e[0]-0.03, e[1]-0.12, "E", size=14)
        ax.text(f[0]-0.1, f[1]-0.12, "F", size=14)
        ax.text(g[0]-0.12, g[1]-0.03, "G", size=14)
        ax.text(h[0]-0.12, h[1]-0.02, "H", size=14)
        ax.text(i[0]-0.12, i[1], "I", size=14)
        
        s_list = ["AC", "AD", "AE", "AF", "AG", "AH"]
        side = random.choice(s_list)
        
        if side == "AC":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$6$$/수식$$(개)\n"
            comment2 = "$$수식$$5 TIMES 2 + 6 = 16$$/수식$$(개)"
            
            ans = 16
        elif side == "AD":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$5$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$5$$/수식$$(개)\n"
            comment2 = "$$수식$$5 TIMES 2 + 5 TIMES 2 = 20$$/수식$$(개)"
            
            ans = 20
        elif side == "AE":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$4$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$4$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$D$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$4$$/수식$$(개)\n"
            comment2 = "$$수식$$5 TIMES 2 + 4 TIMES 3 = 22$$/수식$$(개)"
            
            ans = 22
        elif side == "AF":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$3$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$3$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$D$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$3$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$E$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$3$$/수식$$(개)\n"
            comment2 = "$$수식$$5 TIMES 2 + 3 TIMES 4 = 22$$/수식$$(개)"
            
            ans = 22
        elif side == "AG":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$D$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$E$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$F$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$2$$/수식$$(개)\n"
            comment2 = "$$수식$$5 TIMES 2 + 2 TIMES 5 = 20$$/수식$$(개)"
            
            ans = 20
        elif side == "AH":
            comment1_1 = "꼭짓점 $$수식$$B$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$C$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$D$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$E$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$F$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n" \
                "꼭짓점 $$수식$$G$$/수식$$에서 그을 수 있는 대각선의 개수는 $$수식$$1$$/수식$$(개)\n"
            comment2 = "$$수식$$5 TIMES 2 + 1 TIMES 6 = 16$$/수식$$(개)"
            
            ans = 16
        
    endpoint = side.split("A")[1]
        
    comment1 = "$$수식$$({n}-3)-1={nn}$$/수식$$(개)\n" \
              "꼭짓점 $$수식$${endpoint}$$/수식$$에서 그을 수 있는 대각선의 개수는\n" \
              "$$수식$$({n}-3)-1={nn}$$/수식$$(개)\n"
              
    comment1 = comment1.format(n=n, nn=n-4, endpoint=endpoint)
    
    comment1 = comment1 + comment1_1
        
    if endpoint == "C":
        drawLine(ax=ax, p1=a, p2=c)
    elif endpoint == "D":
        drawLine(ax=ax, p1=a, p2=d)
    elif endpoint == "E":
        drawLine(ax=ax, p1=a, p2=e)
    elif endpoint == "F":
        drawLine(ax=ax, p1=a, p2=f)
    elif endpoint == "G":
        drawLine(ax=ax, p1=a, p2=g)
    elif endpoint == "H":
        drawLine(ax=ax, p1=a, p2=h)

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

    stem = stem.format(angle=angle, side=side, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(side=side, comment1=comment1, comment2=comment2)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_044():
    stem = "내각의 크기의 합이 $$수식$${ag}DEG $$/수식$$인 다각형의 꼭짓점의 개수는?\n" \
            "① $$수식$${a1}$$/수식$$    ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$    ⑤ $$수식$${a5}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 주어진 다각형을 $$수식$$n$$/수식$$각형이라 하면\n" \
              "$$수식$$180 DEG  TIMES (n-2)={ag}DEG $$/수식$$\n" \
              "$$수식$$n-2={s1}$$/수식$$    $$수식$$THEREFORE n={ans}$$/수식$$\n" \
              "따라서 {p}의 꼭짓점의 개수는 $$수식$${ans}$$/수식$$이다.\n" 

    ans = random.randint(8,12)
    
    if ans == 8 :
      p = "팔각형"
    elif ans == 9 :
      p = "구각형"
    elif ans == 10 :
      p = "십각형"
    elif ans == 11 :
      p = "십일각형"
    elif ans == 12 :
      p = "십이각형"

    s1 = ans-2
    ag = 180*s1

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


    stem = stem.format(ag=ag, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ag=ag, s1=s1, p=p, ans=ans)

    return stem, answer, comment



def planefigure122_Stem_046():
    stem = "대각선의 개수가 $$수식$${n}$$/수식$$개인 다각형의 내각의 크기의 합을 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n 주어진 다각형을 $$수식$$n$$/수식$$각형이라 하면\n" \
              "$$수식$${f}={n}$$/수식$$에서\n" \
              "$$수식$$n(n-3)={s1}$$/수식$$, $$수식$$n(n-3)={s2} TIMES {s3}$$/수식$$\n" \
              "$$수식$$THEREFORE n={s4}$$/수식$$\n" \
              "따라서 {p}의 내각의 크기의 합은\n" \
              "$$수식$$180 DEG  TIMES  ({s4}-2)={result}DEG $$/수식$$"

    f = "\\frac{n(n-3)}{2}"

    s4 = random.randint(10,14)
    s2 = s4
    s3 = s4-3
    s1 = s2*s3
    n = int(s1/2)
    result = (s4-2)*180

    if s4 == 10 :
      p = "십각형"
    elif s4 == 11 :
      p = "십일각형"
    elif s4 == 12 :
      p = "십이각형"
    elif s4 == 13 :
      p = "십삼각형"
    elif s4 == 14 :
      p = "십사각형"

    
    stem = stem.format(n=n)
    answer = answer.format(result=result)
    comment = comment.format(p=p, f=f, n=n, s1=s1, s2=s2, s3=s3, s4=s4, result=result)

    return stem, answer, comment



def planefigure122_Stem_048():
    stem = "내각의 크기의 합이 $$수식$${ag1}DEG $$/수식$$보다 크고 $$수식$${ag2}DEG $$/수식$$보다 작은 다각형은?\n" \
            "① {a1}    ② {a2}     ③ {a3}\n" \
            "④ {a4}    ⑤ {a5}\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n (i) {p1}의 내각의 크기의 합은\n" \
              "\t$$수식$$180 DEG  TIMES  ({s1}-2)={s2}DEG $$/수식$$\n" \
              "(ii) {p2}의 내각의 크기의 합은\n" \
              "\t$$수식$$180 DEG ({s3}-2)={s4}DEG $$/수식$$\n" \
              "(iii) {p3}의 내각의 크기의 합은\n" \
              "\t$$수식$$180 DEG  TIMES ({s5}-2)={s6}DEG $$/수식$$\n" \
              "따라서 내각의 크기의 합이 $$수식$${ag1}DEG $$/수식$$보다 크고\n" \
              "$$수식$${ag2}DEG $$/수식$$보다 작은 다각형은 {ans}이다.\n" \
    
    p_list = ["십일각형","십이각형","십삼각형","십사각형","십오각형"]
    ans = random.choice(p_list)

    if ans == "십일각형" :
      p1 = "십각형"
      p3 = "십이각형"
      s3 = 11
      ag1 = 1600
      ag2 = 1800
    elif ans == "십이각형" :
      p1 = "십일각형"
      p3 = "십삼각형"
      s3 = 12
      ag1 = 1700
      ag2 = 1900
    elif ans == "십삼각형" :
      p1 = "십이각형"
      p3 = "십사각형"
      s3 = 13
      ag1 = 1800
      ag2 = 2000
    elif ans == "십사각형" :
      p1 = "십삼각형"
      p3 = "십오각형"
      s3 = 14
      ag1 = 2000
      ag2 = 2200
    elif ans == "십오각형" :
      p1 = "십사각형"
      p3 = "십육각형"
      s3 = 15
      ag1 = 2200
      ag2 = 2400
    
    p2 = ans
    s1 = s3-1
    s2 = 180*(s1-2)
    s4 = 180*(s3-2)
    s5 = s3+1
    s6 = 180*(s5-2)

    aa_list = ["십각형","십일각형","십이각형","십삼각형","십사각형","십오각형","십육각형"]
    a_list = []
    
    if s3 <= 12 :
      idx = random.randint(0,1)
    elif s4 > 12 :
      idx = random.randint(1,2)

    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break
  
    stem = stem.format(ag1=ag1, ag2=ag2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, ag1=ag1, ag2=ag2, ans=ans)

    return stem, answer, comment



def planefigure122_Stem_049():
    stem = "다음 그림에서 $$수식$$\\angle x$$/수식$$의 크기를 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n 오각형의 내각의 크기 합은\n" \
              "$$수식$$180 DEG  TIMES (5-2)=540 DEG $$/수식$$이므로\n" \
              "$$수식$$(\\angle x+{n1}DEG )+{ag1}DEG +{ag2}DEG +\\angle x+{ag3}DEG = 540 DEG$$/수식$$\n" \
              "$$수식$$2\\angle x={s1}DEG $$/수식$$     $$수식$$THEREFORE \\angle x={result}$$/수식$$"

    while True :    
      n1 = random.choice([10,15,20])
      ag1 = random.choice([125,130,135])
      ag2 = random.choice([95,100,105])
      ag3 = random.choice([95,100,105])
      s1 = 540-(n1+ag1+ag2+ag3)
      if s1 % 2 == 0 :
        break

    p1 = (0.6,1.8)
    p2 = (-0.15,0.9)
    p3 = (0,0)
    p4 = (1.4,0)
    p5 = (1.7,1.4)
       
    
    #ax = setChart(points=[p1,p2,p3,p4,p5])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawPolygon(ax=ax, verts=[p1,p2,p3,p4,p5])
   
    a1 = AngleAnnotation(xy=p1, p1=p2, p2=p5, text=r"$x+{n1}°$".format(n1=n1),
                    textposition="outside", ax=ax, size=30)    
    a2 = AngleAnnotation(xy=p2, p1=p3, p2=p1, text=r"${ag1}°$".format(ag1=ag1),
                         textposition="outside", ax=ax, size=30)
    a3 = AngleAnnotation(xy=p3, p1=p4, p2=p2, text=r"${ag2}°$".format(ag2=ag2),
                         textposition="outside", ax=ax, size=30)
    a4 = AngleAnnotation(xy=p4, p1=p5, p2=p3, text=r"$x$",
                         textposition="outside", ax=ax, size=30)
    a5 = AngleAnnotation(xy=p5, p1=p1, p2=p4, text=r"${ag3}°$".format(ag3=ag3),
                         textposition="outside", ax=ax, size=30)
    
    result = int(s1/2)

    stem = stem.format()
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, ag1=ag1, ag2=ag2, ag3=ag3, s1=s1, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_051():
    stem = "다음 그림에서 $$수식$$\\angle x$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$\n" \
            "③ $$수식$${a3}DEG $$/수식$$    ④ $$수식$${a4}DEG $$/수식$$   ⑤ $$수식$${a5}DEG $$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 사각형의 내각의 크기의 합은 $$수식$$360 DEG $$/수식$$이므로\n" \
              "$$수식$${ag1}DEG +{ag2}DEG +\\angle a+{ag3}DEG = 360 DEG $$/수식$$\n" \
              "$$수식$$THEREFORE \\angle a={s1}DEG $$/수식$$\n" \
              "또, 오각형의 내각의 크기의 합은 $$수식$$540 DEG $$/수식$$이므로\n" \
              "$$수식$${s1}DEG +{ag4}DEG +\\angle x+{ag5}DEG +{ag6}DEG =540 DEG $$/수식$$\n" \
              "$$수식$$THEREFORE \\angle x={ans}DEG $$/수식$$\n" 

    ag1 = random.choice([105,110,115])
    ag2 = random.choice([50,55])
    ag3 = 60

    ag4 = random.choice([65,70,75])
    ag5 = 80
    
    if ag2 == 55 :
      if ag4 == 70 or ag4 == 65 :
        p4 = (0.62,1.03)
      elif ag4 == 75 :
        p4 = (0.64,1.01)
    elif ag2 == 50 :
      if ag4 == 70 or ag4 == 75 :
        p4 = (0.6,1.01)
      elif ag4 == 65 :
        p4 = (0.59,1.03)


    if ag4 == 70 :
      p5 = (-0.5,0.7)
    elif ag4 == 75 :
      p5 = (-0.4,0.7)
    elif ag4 == 65 :
      p5 = (-0.6,0.7)

    if ag2 == 50 :
      p2 = (-0.45,1.6)
      ag6 = 125
      if ag1 == 110 :
        p1 = (0.9,2.2)
      elif ag1 == 115 :
        p1 = (0.9,2.15)
      elif ag1 == 105 :
        p1 = (0.9,2.25)
    elif ag2 == 55 :  
      p2 = (-0.35,1.6)
      ag6 = 130
      if ag1 == 110 :
        p1 = (0.9,2.15)
      elif ag1 == 115 :
        p1 = (0.9,2.1)
      elif ag1 == 105 :
        p1 = (0.9,2.2)

    p3 = (1.75,1.35)
    p6 = (1.35,0.6)
    p7 = (0,0)
    p8 = (1.5,0)

    s1 = 360-(ag1+ag2+ag3)
    ans = 540-(s1+ag4+ag5+ag6)
       
    
    #ax = setChart(points=[p1,p2,p3,p4,p5,p6,p7,p8])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawLine(ax=ax, p1=p1, p2=p2)
    drawLine(ax=ax, p1=p1, p2=p3)
    drawLine(ax=ax, p1=p2, p2=p6)
    drawLine(ax=ax, p1=p3, p2=p5)
    drawLine(ax=ax, p1=p5, p2=p7)
    drawLine(ax=ax, p1=p7, p2=p8)
    drawLine(ax=ax, p1=p8, p2=p6)
   
    a1 = AngleAnnotation(xy=p1, p1=p2, p2=p3, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax, size=26)    
    a2 = AngleAnnotation(xy=p2, p1=p4, p2=p1, text=r"${ag2}°$".format(ag2=ag2),
                         textposition="outside", ax=ax, size=30)
    a3 = AngleAnnotation(xy=p3, p1=p1, p2=p4, text=r"${ag3}°$".format(ag3=ag3),
                         textposition="outside", ax=ax, size=30)
    a4 = AngleAnnotation(xy=p5, p1=p7, p2=p4, text=r"${ag4}°$".format(ag4=ag4),
                         textposition="outside", ax=ax, size=30)
    a5 = AngleAnnotation(xy=p7, p1=p8, p2=p5, text=r"$x$",
                         textposition="outside", ax=ax, size=26)                   
    a6 = AngleAnnotation(xy=p8, p1=p6, p2=p7, text=r"${ag5}°$".format(ag5=ag5),
                         textposition="outside", ax=ax, size=30)
    a7 = AngleAnnotation(xy=p6, p1=p2, p2=p8, text=r"${ag6}°$".format(ag6=ag6),
                         textposition="outside", ax=ax, size=26)
    
    svg1 = saveSvg()

    ax2 = setChart(points=[p1,p2,p3,p4,p5,p6,p7,p8])
    
    drawLine(ax=ax2, p1=p1, p2=p2)
    drawLine(ax=ax2, p1=p1, p2=p3)
    drawLine(ax=ax2, p1=p2, p2=p6)
    drawLine(ax=ax2, p1=p3, p2=p5)
    drawLine(ax=ax2, p1=p5, p2=p7)
    drawLine(ax=ax2, p1=p7, p2=p8)
    drawLine(ax=ax2, p1=p8, p2=p6)
   
    a1 = AngleAnnotation(xy=p1, p1=p2, p2=p3, text=r"${ag1}°$".format(ag1=ag1),
                    textposition="outside", ax=ax2, size=26)    
    a2 = AngleAnnotation(xy=p2, p1=p4, p2=p1, text=r"${ag2}°$".format(ag2=ag2),
                         textposition="outside", ax=ax2, size=30)
    a3 = AngleAnnotation(xy=p3, p1=p1, p2=p4, text=r"${ag3}°$".format(ag3=ag3),
                         textposition="outside", ax=ax2, size=30)
    a4 = AngleAnnotation(xy=p5, p1=p7, p2=p4, text=r"${ag4}°$".format(ag4=ag4),
                         textposition="outside", ax=ax2, size=30)
    a5 = AngleAnnotation(xy=p7, p1=p8, p2=p5, text=r"$x$",
                         textposition="outside", ax=ax2, size=26)                   
    a6 = AngleAnnotation(xy=p8, p1=p6, p2=p7, text=r"${ag5}°$".format(ag5=ag5),
                         textposition="outside", ax=ax2, size=30)
    a7 = AngleAnnotation(xy=p6, p1=p2, p2=p8, text=r"${ag6}°$".format(ag6=ag6),
                         textposition="outside", ax=ax2, size=26)
    a8 = AngleAnnotation(xy=p4, p1=p3, p2=p2, text=r"$a$",
                         textposition="outside", ax=ax2, size=24) 
    a9 = AngleAnnotation(xy=p4, p1=p5, p2=p6, text=r"$a$",
                         textposition="outside", ax=ax2, size=24) 

    svg2 = saveSvg()
    
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
    comment = comment.format(ag1=ag1, ag2=ag2, ag3=ag3, ag4=ag4, ag5=ag5, ag6=ag6, s1=s1, ans=ans)
    svg = [svg1,svg2]
    return stem, answer, comment, svg 



def planefigure122_Stem_061():
    stem = "{p1}의 한 외각의 크기를 $$수식$$a DEG $$/수식$$, {p2}의 한 내각의 크기를 $$수식$$b DEG $$/수식$$라 할 때, " \
            "$$수식$$a+b$$/수식$$의 값을 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n {p1}의 한 외각의 크기는\n" \
              "$$수식$${f1}={s1}DEG $$/수식$$       $$수식$$THEREFORE a={s1}$$/수식$$\n" \
              "{p2}의 한 내각의 크기는\n" \
              "$$수식$${f2}={s2}DEG $$/수식$$       $$수식$$THEREFORE b={s2}$$/수식$$\n" \
              "$$수식$$THEREFORE a+b={result}$$/수식$$\n"
    
    n_list = [(5,"정오각형"),(6,"정육각형"),(8,"정팔각형"),(9,"정구각형"),(10,"정십각형")]

    while True :
      nn1 = random.choice(n_list)
      nn2 = random.choice(n_list)
      if nn1 != nn2 :
        break
    
    n1 = nn1[0]
    p1 = nn1[1]
    n2 = nn2[0]
    p2 = nn2[1]

    f1 = "\\frac{360 DEG}{"+str(n1)+"}"
    f2 = "\\frac{180 DEG  TIMES  ("+str(n2)+"-2)}{"+str(n2)+"}"

    s1 = int(360/n1)
    s2 = int((180*(n2-2))/n2)
    result = s1+s2
    
    stem = stem.format(p1=p1, p2=p2)
    answer = answer.format(result=result)
    comment = comment.format(p1=p1, p2=p2, f1=f1, f2=f2, s1=s1, s2=s2, result=result)

    return stem, answer, comment



def planefigure122_Stem_065():
    stem = "내각과 외각의 크기의 총합이 $$수식$${ag}DEG $$/수식$$인 정다각형의 한 내각의 크기를 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n 주어진 정다각형을 정$$수식$$n$$/수식$$각형이라 하면\n" \
              "$$수식$$180 DEG  TIMES  (n-2)+360={ag}DEG $$/수식$$\n" \
              "$$수식$$180 DEG  TIMES  n={ag}DEG $$/수식$$\n" \
              "$$수식$$THEREFORE n={n}$$/수식$$\n" \
              "따라서 {p}의 한 내각의 크기는\n" \
              "$$수식$${f}={result}DEG $$/수식$$\n"

    p_list = [(6,"정육각형"),(8,"정팔각형"),(9,"정구각형"),(10,"정십각형")]

    nn = random.choice(p_list)
    n = nn[0]
    p = nn[1]

    ag = 180*n
    result = int((180*(n-2))/n)

    f = "\\frac{180 DEG  TIMES  ("+str(n)+"-2)}{"+str(n)+"}"


    stem = stem.format(ag=ag)
    answer = answer.format(result=result)
    comment = comment.format(ag=ag, n=n, p=p, f=f, result=result)

    return stem, answer, comment


def planefigure122_Stem_078():
    stem = "반지름의 길이가 $$수식$${n}```rm {{cm}}$$/수식$$인 원에서 가장 긴 현의길이를 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n 원에서 길이가 가장 긴 현은 지름이므로 반지름의\n" \
              "길이가 $$수식$${n}``rm {{cm}}$$/수식$$인 원에서 가장 긴 현의 길이는\n" \
              "$$수식$${n} TIMES  2 = {result}(rm {{cm}})$$/수식$$\n"

    n = random.randint(12,18)
    result = n*2

    stem = stem.format(n=n)
    answer = answer.format(result=result)
    comment = comment.format(n=n, result=result)

    return stem, answer, comment



def planefigure122_Stem_080():
    stem = "다음 그림의 원 $$수식$$O$$/수식$$에서 $$수식$$\\angle AOB={ag1}DEG $$/수식$$, $$수식$$\\angle COD={ag2}DEG $$/수식$$" \
            "이고 부채꼴 $$수식$$AOB$$/수식$$의 넓이가 $$수식$${n}``rm {{cm^2}}$$/수식$$일 때, 부채꼴 $$수식$$COD$$/수식$$의 넓이를 구하시오."
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n 부채꼴 $$수식$$COD$$/수식$$의 넓이를 $$수식$$x ``rm {{cm^2}}$$/수식$$라 하면\n" \
              "$$수식$${ag1}DEG :{ag2}DEG = {n}:x$$/수식$$이므로\n" \
              "$$수식$${s1}:{s2}={n}:x$$/수식$$     $$수식$$THEREFORE x={result}$$/수식$$\n" \
              "따라서 부채꼴 $$수식$$COD$$/수식$$의 넓이는 $$수식$${result}``rm {{cm^2}}$$/수식$$이다.\n"

    while True :
      ag1 = random.choice([25,30,40])
      ag2 = random.choice([100,120,150])
      if ag2 % ag1 == 0 :
        break

    n = random.randint(10,15)
    s1 = 1
    s2 = int(ag2/ag1)
    result = n*s2

    p = (0,0)
    a = (-2,0)
    b = (2*math.cos(math.radians(180+ag1)),2*math.sin(math.radians(180+ag1)))
    c = (2*math.cos(math.radians(360-(ag2*4/10))),2*math.sin(math.radians(360-(ag2*4/10))))
    d = (2*math.cos(math.radians(ag2*6/10)),2*math.sin(math.radians(ag2*6/10)))

    
    #ax = setChart(points=[p,a,b,c,d])

    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawCircle(ax=ax, center=p, radius=2)

    drawLine(ax=ax, p1=p, p2=a)
    drawLine(ax=ax, p1=p, p2=b)
    drawLine(ax=ax, p1=p, p2=c)
    drawLine(ax=ax, p1=p, p2=d)

    ax.scatter(0,0, c='black', edgecolor='black', s=20)

    a1 = AngleAnnotation(xy=p, p1=a, p2=b, text=r"${ag1}°$".format(ag1=ag1),
              textposition="outside", ax=ax, size=45)    
    a2 = AngleAnnotation(xy=p, p1=c, p2=d, text=r"${ag2}°$".format(ag2=ag2),
              textposition="outside", ax=ax, size=40)    

    ax.text(-0.25,0.05, "O", size = 18)
    ax.text(-2-0.3,-0.1, "A", size = 18)
    ax.text(b[0]-0.3,b[1]-0.15, "B", size = 18)
    if ag2 == 150 :
      ax.text(c[0]-0.05,c[1]-0.28, "C", size = 18)
      ax.text(d[0]-0.05,d[1]+0.06, "D", size = 18)
    else :
      ax.text(c[0]+0.05,c[1]-0.2, "C", size = 18)
      ax.text(d[0]+0.05,d[1]+0.05, "D", size = 18)      

    ax.annotate('',ha = 'center', va = 'bottom',
        xytext = (-1.3,-0.45), xy = (-1,-1.2),
        arrowprops = {
                  'color':'black',
                  'connectionstyle':"arc3,rad=0.4",
                  'edgecolor':'b', 
                  'arrowstyle':'<-'
                  })
    ax.text(-1,-1.2, '${n} cm^2$'.format(n=n), size = 10)

    pp = mpatches.Wedge(p, r=2, theta1=360-(ag2*4/10),
                                theta2=ag2*6/10, fc='yellowgreen', fill=True, alpha=0.5)
    ax.add_patch(pp)

    pp2 = mpatches.Wedge(p, r=2, theta1=180,
                                theta2=180+ag1, fc='yellowgreen', fill=True, alpha=0.5)
    ax.add_patch(pp2)

    stem = stem.format(ag1=ag1, ag2=ag2, n=n)
    answer = answer.format(result=result)
    comment = comment.format(ag1=ag1, ag2=ag2, n=n, s1=s1, s2=s2, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 


def planefigure122_Stem_081():
    stem = "다음 그림의 원 $$수식$$O$$/수식$$에서 $$수식$${ab}={cd}={de}$$/수식$$, $$수식$$\\angle AOB={ag}DEG $$/수식$$일 때, $$수식$$\\angle EOC$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$     ③ $$수식$${a3}DEG $$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$    ⑤ $$수식$${a5}DEG $$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$${ab}={cd}={de}$$/수식$$이므로\n" \
              "$$수식$$\\angle AOB=\\angle COD=\\angle DOE={ag}DEG $$/수식$$\n" \
              "$$수식$$THEREFORE \\angle EOC={ag}DEG +{ag}DEG = {ans}DEG $$/수식$$\n"
    
    ag = random.choice([25,30,35,40])
    ans = ag+ag

    o = (0,0)
    a = (2*math.cos(math.radians(180-ag/2)),2*math.sin(math.radians(180-ag/2)))
    b = (2*math.cos(math.radians(180+ag/2)),2*math.sin(math.radians(180+ag/2)))
    c = (2*math.cos(math.radians(360-ag)),2*math.sin(math.radians(360-ag)))
    d = (2,0)
    e = (2*math.cos(math.radians(ag)),2*math.sin(math.radians(ag)))

    
    #ax = setChart(points=[o,a,b,c,d,e])
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawCircle(ax=ax, center=o, radius=2)

    drawLine(ax=ax, p1=o, p2=a)
    drawLine(ax=ax, p1=o, p2=b)
    drawLine(ax=ax, p1=o, p2=c)
    drawLine(ax=ax, p1=o, p2=d)
    drawLine(ax=ax, p1=o, p2=e)

    drawLine(ax=ax, p1=a, p2=b)
    drawLine(ax=ax, p1=d, p2=e)
    drawLine(ax=ax, p1=d, p2=c)

    ax.scatter(0,0, c='black', edgecolor='black', s=20)

    a1 = AngleAnnotation(xy=o, p1=a, p2=b, text=r"${ag}°$".format(ag=ag),
                  textposition="edge",  text_kw=dict(xytext=(-20, -40), arrowprops=dict(arrowstyle="->",
                              connectionstyle="arc3,rad=-0.4")), ax=ax, size=45)     

    ax.text(-0.1,0.07, "O", size = 18)
    ax.text(a[0]-0.3,a[1]-0.05, "A", size = 18)
    ax.text(b[0]-0.3,b[1]-0.15, "B", size = 18)
    ax.text(c[0]+0.05,c[1]-0.2, "C", size = 18)
    ax.text(d[0]+0.05,d[1]-0.1, "D", size = 18)
    ax.text(e[0],e[1], "E", size = 18)

    x = [a[0]-0.06,a[0]+0.06]
    y = [0.028,0.028]
    ax.plot(x,y, c="black", linewidth = 0.7)

    x2 = [a[0]-0.06,a[0]+0.06]
    y2 = [-0.028,-0.028]
    ax.plot(x2,y2, c="black", linewidth = 0.7)

    ed = ((e[0]+d[0])/2,(e[1]+d[1])/2)

    x3 = [ed[0]-0.08,ed[0]+0.04]
    y3 = [ed[1]+0.02,ed[1]+0.06]
    ax.plot(x3,y3, c="black", linewidth = 0.7)

    x4 = [ed[0]-0.065,ed[0]+0.05]
    y4 = [ed[1]-0.03,ed[1]+0.005]
    ax.plot(x4,y4, c="black", linewidth = 0.7)

    dc = ((d[0]+c[0])/2,(d[1]+c[1])/2)

    x5 = [dc[0]-0.06,dc[0]+0.06]
    y5 = [dc[1]+0.06,dc[1]+0.02]
    ax.plot(x5,y5, c="black", linewidth = 0.7)

    x6 = [dc[0]-0.075,dc[0]+0.045]
    y6 = [dc[1]+0.005,dc[1]-0.035]
    ax.plot(x6,y6, c="black", linewidth = 0.7)

    ab = "\\overline{AB}"
    cd = "\\overline{CD}"
    de = "\\overline{DE}"

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

    stem = stem.format(ab=ab, cd=cd, de=de, ag=ag, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ab=ab, cd=cd, de=de, ag=ag, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_083():
    stem = "다음 그림의 반원 $$수식$$O$$/수식$$에서 $$수식$${n1}\\angle AOC=\\angle BOC$$/수식$$, $$수식$${bc}={n2}``rm {{cm}}$$/수식$$일 때, $$수식$${ac}$$/수식$$의 길이를 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n $$수식$${n1}\\angle AOC=\\angle BOC$$/수식$$에서\n" \
              "$$수식$$\\angle AOC:\\angle BOC=1:{n1}$$/수식$$\n" \
              "$$수식$${ac}:{n2}=1:{n1}$$/수식$$\n" \
              "$$수식$$THEREFORE {ac}={result}(rm {{cm}})$$/수식$$\n"

    n1 = random.choice([2,3,5])
    while True :
      n2 = random.randint(24,36)
      if n2% n1 == 0 :
        break

    if n1 == 2 :
      ag = 60
    elif n1 == 3 :
      ag = 45
    elif n1 == 5 :
      ag = 30

    ag2 = ((180-ag)/2)+10
    ag3 = ((180-ag)/2)-5
    result = int(n2/n1)

    o = (0,0)
    c = (2.3*math.cos(math.radians(180-ag)),2.3*math.sin(math.radians(180-ag)))
    p = (2.2*math.cos(math.radians(180-ag)),2.2*math.sin(math.radians(180-ag)))
    b = (2,0.005)
    p2 = (2.3,0.005)
    p3 = (2.2,0.005)
    p4 = (2.2*math.cos(math.radians(ag2)),2.2*math.sin(math.radians(ag2)))
    p5 = (2.2*math.cos(math.radians(ag3)),2.2*math.sin(math.radians(ag3)))

    
    #ax = setChart(points=[o,b,c,p,p2,p3,p4,p5])

    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawSector(ax=ax, center=o, radius=2, theta1=0, theta2=180)

    drawLine(ax=ax, p1=o, p2=c)
    drawLine(ax=ax, p1=b, p2=p2)

    ax.scatter(-0.01,0.01, c='black', edgecolor='black', s=20)

    ax.text(-0.14,-0.35, "O", size = 18)
    ax.text(-2-0.28,-0.15, "A", size = 18)
    ax.text(b[0]-0.1,b[1]-0.3, "B", size = 18)
    ax.text(c[0]-0.2,c[1]-0.3, "C", size = 18)

    ax.annotate('',ha = 'center', va = 'bottom',
        xytext = (p[0],p[1]), xy = (p4[0],p4[1]),
        arrowprops = {
                  'color':'black',
                  'connectionstyle':"arc3,rad=-0.25",
                  'edgecolor':'b', 
                  'arrowstyle':'<-'
                  })
    ax.annotate('',ha = 'center', va = 'bottom',
        xytext = (p3[0],p3[1]), xy = (p5[0],p5[1]),
        arrowprops = {
                  'color':'black',
                  'connectionstyle':"arc3,rad=0.28",
                  'edgecolor':'b', 
                  'arrowstyle':'<-'
                  })
    ax.text(p4[0]+0.1,p4[1]-0.1, '${n2}cm$'.format(n2=n2), size = 10)

    bc = "\\overset{\\frown}{BC}"
    ac = "\\overset{\\frown}{AC}"

    stem = stem.format(bc=bc, n1=n1, n2=n2, ac=ac)
    answer = answer.format(result=result)
    comment = comment.format(ac=ac, n1=n1, n2=n2, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_088():
    stem = "다음 그림에서 $$수식$${ab}$$/수식$$는 원 $$수식$$O$$/수식$$의 지름이고 " \
            "$$수식$${ad}//{oc}$$/수식$$, $$수식$$\\angle COB={ag}DEG $$/수식$$, $$수식$${bc}={n}``rm {{cm}}$$/수식$$일 때, " \
            "$$수식$${ads}$$/수식$$의 길이는?\n" \
            "① $$수식$${a1}``rm {{cm}}$$/수식$$     ② $$수식$${a2}``rm {{cm}}$$/수식$$       ③ $$수식$${a3}``rm {{cm}}$$/수식$$\n" \
            "④ $$수식$${a4}``rm {{cm}}$$/수식$$     ⑤ $$수식$${a5}``rm {{cm}}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$${ad}//{oc}$$/수식$$이므로\n" \
              "$$수식$$\\angle DAO=\\angle COB={ag}DEG $$/수식$$(동위각)\n" \
              "다음 그림과 같이 $$수식$${oc}$$/수식$$를\n" \
              "그으면 $$수식$$\\triangle ODA$$/수식$$에서\n" \
              "$$수식$${oa}={od}$$/수식$$이므로\n" \
              "$$수식$$\\angle ODA=\\angle DAO={ag}DEG $$/수식$$\n" \
              "$$수식$$THEREFORE \\angle AOD=180 DEG - ({ag}DEG +{ag}DEG )={s1}DEG $$/수식$$\n" \
              "따라서 $$수식$${bc}:{ads}=\\angle COB:\\angle AOD$$/수식$$이므로\n" \
              "$$수식$${n}:$$/수식$$$$수식$${ads} ={ag}DEG :{s1}DEG , {n}:$$/수식$$$$수식$${ads} ={s2}:{s3}$$/수식$$\n" \
              "$$수식$$THEREFORE {ads}={ans}(rm {{cm}})$$/수식$$\n"
    while True :
        ag = random.choice([30,40,45])
        n = random.randint(5,9)
        s1 = 180-(ag+ag)
        s2 = int(ag/math.gcd(ag,s1))
        s3 = int(s1/math.gcd(ag,s1))
        if (s3*n)%s2 == 0:
            break

    ans = int((s3*n)/s2)

    o = (0,0)
    a = (-4,0)
    b = (4,0)
    c = (4*math.cos(math.radians(ag)),4*math.sin(math.radians(ag)))
    d = (4*math.cos(math.radians(ag+ag)),4*math.sin(math.radians(ag+ag)))
    c2 = (4.5*math.cos(math.radians(ag)),4.5*math.sin(math.radians(ag)))
    b2 = (4.5,0)
    c3 = (4.3*math.cos(math.radians(ag)),4.3*math.sin(math.radians(ag)))
    b3 = (4.3,0)
    p = (4.3*math.cos(math.radians(ag/2+3)),4.3*math.sin(math.radians(ag/2+3)))
    p2 = (4.3*math.cos(math.radians(ag/2-3)),4.3*math.sin(math.radians(ag/2-3)))

    
    #ax = setChart(points=[o,a,b,c,d,c2,c3,b2,b3,p,p2])

    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawCircle(ax=ax, center=o, radius=4)

    drawLine(ax=ax, p1=o, p2=a)
    drawLine(ax=ax, p1=o, p2=b2)
    drawLine(ax=ax, p1=o, p2=c2, decoration=">")
    drawLine(ax=ax, p1=a, p2=d, decoration=">")

    ax.scatter(0,0, c='black', edgecolor='black', s=20)

    a1 = AngleAnnotation(xy=o, p1=b, p2=c, text=r"${ag}°$".format(ag=ag),
              textposition="outside", ax=ax, size=45)    


    ax.text(-0.23,-0.65, "O", size = 18)
    ax.text(-4-0.55,-0.1, "A", size = 18)
    ax.text(b[0]+0.05,b[1]-0.6, "B", size = 18)
    ax.text(c[0]-0.2,c[1]+0.25, "C", size = 18)
    ax.text(d[0],d[1]+0.05, "D", size = 18)

    ax.annotate('',ha = 'center', va = 'bottom',
        xytext = (c3[0],c3[1]), xy = (p[0],p[1]),
        arrowprops = {
                  'color':'black',
                  'connectionstyle':"arc3,rad=-0.1",
                  'edgecolor':'b', 
                  'arrowstyle':'<-'
                  })

    ax.annotate('',ha = 'center', va = 'bottom',
        xytext = (b3[0],b3[1]), xy = (p2[0],p2[1]),
        arrowprops = {
                  'color':'black',
                  'connectionstyle':"arc3,rad=0.1",
                  'edgecolor':'b', 
                  'arrowstyle':'<-'
                  })
    ax.text(p[0]-0.1,p[1]-0.3, '${n}cm$'.format(n=n), size = 11)

    ab = "\\overline{AB}"
    ad = "\\overline{AD}"
    oc = "\\overline{OC}"
    oa = "\\overline{OA}"
    od = "\\overline{OD}"

    bc = "\\overset{\\frown}{BC}"
    ads = "\\overset{\\frown}{AD}"

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

    stem = stem.format(ab=ab, ad=ad, oc=oc, bc=bc, ads=ads, ag=ag, n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ad=ad, oc=oc, oa=oa, od=od, bc=bc, ads=ads, ag=ag, n=n, s1=s1, s2=s2, s3=s3, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_096():
    stem = "다음 그림과 같이 반지름의 길이가 $$수식$${n1}``rm {{cm}}$$/수식$$인 원 $$수식$$O$$/수식$$에서 " \
            "$$수식$${pq}={pr}$$/수식$$, $$수식$${pql}={n2}``rm {{cm}}$$/수식$$일 때, 색칠한 부분의 둘레의 길이는?\n" \
            "① $$수식$${a1}``rm {{cm}}$$/수식$$     ② $$수식$${a2}``rm {{cm}}$$/수식$$       ③ $$수식$${a3}``rm {{cm}}$$/수식$$\n" \
            "④ $$수식$${a4}``rm {{cm}}$$/수식$$     ⑤ $$수식$${a5}``rm {{cm}}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n $$수식$${pq}={pr}$$/수식$$이므로 $$수식$$\\angle POQ=\\angle POR$$/수식$$\n" \
              "한 원에서 크기가 같은 중심각에 대한 현의 길이는 같으므로\n" \
              "$$수식$${prl}={pql}={n2}``rm {{cm}}$$/수식$$\n" \
              "한 원에서 반지름의 길이는 같으므로\n" \
              "$$수식$${orl}={oql}={n1}``rm {{cm}}$$/수식$$\n" \
              "따라서 색칠한 부분의 둘레의 길이는\n" \
              "$$수식$${pql}+{prl}+{oql}+{orl}={n2}+{n2}+{n1}+{n1}$$/수식$$\n" \
              "$$수식$$={ans}(rm {{cm}})$$/수식$$\n"

    n1 = random.randint(4,6)
    n2 = (n1*2)-1
    ans = n1+n1+n2+n2

    o = (0,0)
    q = (4*math.cos(math.radians(50)),4*math.sin(math.radians(50)))
    p = (4*math.cos(math.radians(180)),4*math.sin(math.radians(180)))
    r = (4*math.cos(math.radians(310)),4*math.sin(math.radians(310)))


    
    #ax = setChart(points=[o,p,q,r])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawCircle(ax=ax, center=o, radius=4)

    drawPolygon(ax, verts=[p,q,o,r])
    drawPolygon(ax, verts=[p,q,o,r])

    x = [p[0],r[0],o[0],q[0],p[0]]
    y = [p[1],r[1],o[1],q[1],p[1]]
    ax.fill(x, y, color="yellowgreen",alpha = 0.5)

    ax.scatter(0,0, c='black', s=20)

    ax.text(-0.6,-0.2, "O", size = 18)
    ax.text(-4-0.55,-0.15, "P", size = 18)
    ax.text(r[0]-0.05,r[1]-0.5, "R", size = 18)
    ax.text(q[0]-0.15,q[1]+0.15, "Q", size = 18)

    x = [p[0],q[0],o[0],r[0],p[0]]
    y = [p[1],q[1],o[1],r[1],p[1]]

    pp1 = mpatches.PathPatch(
    Path([(p[0],p[1]), ((p[0]+q[0])/2-0.6, 3), (q[0], q[1])],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    pp2 = mpatches.PathPatch(
    Path([(o[0],o[1]), (q[0]/2+0.8, 0.8), (q[0], q[1])],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp1)
    ax.add_patch(pp2)

    ax.text(q[0]/2+0.5, 0.9, '${n1}cm$'.format(n1=n1), size = 12)
    ax.text((p[0]+q[0])/2-0.8, 2.5, '${n2}cm$'.format(n2=n2), size = 12)          

    pql = "\\overline{PQ}"
    prl = "\\overline{PR}"
    orl = "\\overline{OR}"
    oql = "\\overline{OQ}"

    pr = "\\overset{\\frown}{PR}"
    pq = "\\overset{\\frown}{PQ}"

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

    stem = stem.format(pq=pq, pr=pr, pql=pql, n1=n1, n2=n2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(pq=pq, pr=pr, pql=pql, prl=prl, orl=orl, oql=oql, n1=n1, n2=n2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_099():
    stem = "원 $$수식$$O$$/수식$$에서 중심각의 크기가 $$수식$${ag}DEG $$/수식$$인 부채꼴의 호의 " \
            "길이가 $$수식$${n}``rm {{cm}}$$/수식$$일 때, 원 $$수식$$O$$/수식$$의 둘레의 길이를 구하시오.\n"
    answer = "(정답)\n$$수식$${result}``rm {{cm}}$$/수식$$"
    comment = "(해설)\n 원 $$수식$$O$$/수식$$의 둘레의 길이를 $$수식$$x``rm {{cm}}$$/수식$$라 하면\n" \
              "$$수식$${ag}:360={n}:x, {s1}:{s2}={n}:x$$/수식$$\n" \
              "$$수식$$THEREFORE x={result}$$/수식$$\n" \
              "따라서 구하는 둘레의 길이는 $$수식$${result}``rm {{cm}}$$/수식$$이다."
    
    ag_list = [30,45,60,90]
    ag = random.choice(ag_list)

    n = random.randint(10,14)
    
    s1 = 1
    s2 = int(360/ag)

    result = n*s2


    stem = stem.format(ag=ag, n=n)
    answer = answer.format(result=result)
    comment = comment.format(ag=ag, n=n, s1=s1, s2=s2, result=result)

    return stem, answer, comment



def planefigure122_Stem_104():
    stem = "다음 그림에서 원 $$수식$$O$$/수식$$의 넓이는 $$수식$${n1}\\pi ``rm {{cm^2}}$$/수식$$이고 " \
            "부채꼴 $$수식$$OAB$$/수식$$의 넓이는 $$수식$${n2}\\pi ``rm {{cm^2}}$$/수식$$일 때, " \
            "$$수식$$\\triangle OPQ$$/수식$$에서 $$수식$$\\angle x+\\angle y$$/수식$$의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$     ③ $$수식$${a3}DEG $$/수식$$ \n" \
            "④ $$수식$${a4}DEG $$/수식$$    ⑤ $$수식$${a5}DEG $$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 부채꼴의 넓이는 중심각의 크기에 정비례하므로\n" \
              "$$수식$$\\angle AOB:360 DEG =$$/수식$$(부채꼴 AOB의 넓이):(원 $$수식$$O$$/수식$$의 넓이)\n$$수식$$={n2}\\pi:{n1}\\pi={s1}:{s2}$$/수식$$" \
              "\n" \
              "$$수식$${s2}\\angle AOB=360 DEG $$/수식$$        $$수식$$THEREFORE \\angle AOB={s3}$$/수식$$\n" \
              "따라서 $$수식$$\\triangle OPQ$$/수식$$에서\n" \
              "$$수식$$\\angle x+\\angle y=180 DEG - \\angle AOB=180 DEG - {s3}DEG $$/수식$$\n" \
              "$$수식$$={ans}DEG $$/수식$$\n"

    n2 = random.randint(4,9)
    n1 = n2*random.randint(4,5)
    
    s1 = 1
    s2 = int(n1/n2)
    s3 = int(360/s2)
    ans = 180-s3

    o = (0,0)
    a = (2*math.cos(math.radians(180+40)),2*math.sin(math.radians(180+40)))
    b = (2*math.cos(math.radians(360-50)),2*math.sin(math.radians(360-50)))
    p = (4.1712*math.cos(math.radians(180+40)),4.1712*math.sin(math.radians(180+40)))
    q = (3.5*math.cos(math.radians(360-50)),3.5*math.sin(math.radians(360-50)))

    
    #ax = setChart(points=[p,a,b])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.set_ylim(-3.5, 0)
    #ax.autoscale()

    drawCircle(ax=ax, center=o, radius=2, fill=True, alpha=0.3)
    drawCircle(ax=ax, center=o, radius=2)

    drawLine(ax=ax, p1=o, p2=p)
    drawLine(ax=ax, p1=o, p2=q)
    drawLine(ax=ax, p1=p, p2=q)

    a1 = AngleAnnotation(xy=p, p1=q, p2=o, text=r'$x$',
              textposition="outside", ax=ax, size=40) 
    a2 = AngleAnnotation(xy=q, p1=o, p2=p, text=r'$y$',
              textposition="outside", ax=ax, size=40) 

    ax.scatter(0,0, c='black', edgecolor='black', s=20)


    ax.text(-0.15,0.1, "O", size = 18)
    ax.text(a[0]-0.43,a[1]-0.07, "A", size = 18)
    ax.text(b[0]+0.2,b[1]-0.15, "B", size = 18)
    ax.text(p[0]-0.3,p[1]-0.1, "P", size = 18)
    ax.text(q[0]+0.08,q[1]-0.1, "Q", size = 18)        

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

    stem = stem.format(n1=n1, n2=n2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, s1=s1, s2=s2, s3=s3, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 


def planefigure122_Stem_107():
    stem = "다음 그림과 같이 지름의 길이가 $$수식$${n}``rm {{cm}}$$/수식$$인 원에서 색칠한 부분의 둘레의 길이와 넓이를 바르게 구한 것은?\n" \
            "① $$수식$${a1}\\pi ``rm {{cm}}$$/수식$$, $$수식$${a2}\\pi ``rm {{cm^2}}$$/수식$$   ② $$수식$${a3}\\pi ``rm {{cm}}$$/수식$$, $$수식$${a4}\\pi ``rm {{cm^2}}$$/수식$$\n" \
            "③ $$수식$${a5}\\pi ``rm {{cm}}$$/수식$$, $$수식$${a6}\\pi ``rm {{cm^2}}$$/수식$$   ④ $$수식$${a7}\\pi ``rm {{cm}}$$/수식$$, $$수식$${a8}\\pi ``rm {{cm^2}}$$/수식$$\n" \
            "⑤ $$수식$${a9}\\pi ``rm {{cm}}$$/수식$$, $$수식$${a10}\\pi ``rm {{cm^2}}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n (색칠한 부분의 둘레의 길이)\n" \
              "$$수식$$=2\\pi TIMES {s1} TIMES {f} + 2\\pi TIMES {s2} TIMES {f} + 2\\pi TIMES {s3} TIMES {f}$$/수식$$\n" \
              "$$수식$$={s1}\\pi + {s2}\\pi + {s3}\\pi = {ans1}\\pi (cm)$$/수식$$\n" \
              "(색칠한 부분의 넓이)" \
              "$$수식$$=\\pi TIMES {s1}^2 TIMES {f} + \\pi TIMES {s3}^2 TIMES {f} - \\pi TIMES {s2}^2 TIMES {f}$$/수식$$\n" \
              "$$수식$$={f1}\\pi + {f2}\\pi - {f3}\\pi = {ans2}\\pi(rm {{cm^2}})$$/수식$$"

    n1 = random.choice([6,8,10])
    n2 = n1*2
    n = n1+n2

    s1 = int(n/2)
    s2 = int(n2/2)
    s3 = int(n1/2)
    ans1 = s1+s2+s3

    ff1 = fractions.Fraction(fractions.Fraction(s1*s1)/fractions.Fraction(2))
    ff2 = fractions.Fraction(fractions.Fraction(s3*s3)/fractions.Fraction(2))
    ff3 = fractions.Fraction(fractions.Fraction(s2*s2)/fractions.Fraction(2))

    if ff1.denominator == 1 :
        f1 = int(ff1)
    else :
        f1 = "\\frac{"+str(ff1.numerator)+"}{"+str(ff1.denominator)+"}"

    if ff2.denominator == 1 :
        f2 = int(ff2)
    else :
        f2 = "\\frac{"+str(ff2.numerator)+"}{"+str(ff2.denominator)+"}"

    if ff3.denominator == 1 :
        f3 = int(ff3)
    else :
        f3 = "\\frac{"+str(ff3.numerator)+"}{"+str(ff3.denominator)+"}"
    
    an = fractions.Fraction(ff1+ff2-ff3)

    if an.denominator == 1 :
        ans2 = int(an)
    else :
        ans2 = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    center = (0,0)
    p = (-15,0)
    radius = 9

    
    #ax = setChart(points=[center,p])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

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

    pp = mpatches.Circle(center, radius=radius, ec='black',fill=False)
    pp2 = mpatches.Wedge(center, r=radius, theta1=0,
                                theta2=180, ec="black", fc='orange', fill=True, alpha=0.4)
    pp3 = mpatches.Wedge(center=(-6,0), r=3, theta1=180,
                                theta2=360, ec="black", fc='orange', fill=True, alpha=0.4)
    pp4 = mpatches.Wedge(center=(3,0), r=6, theta1=0,
                                theta2=180, ec="black", fc='white', fill=True, alpha=1)
    pp5 = mpatches.Wedge(center=(-6,0), r=3, theta1=180,
                                theta2=360, ec="black",fill=False)
    pp6 = mpatches.Circle(center, radius=0.15, ec='black',fill=True, fc='black')
    pp7 = mpatches.Circle((3,0), radius=0.15, ec='black',fill=True, fc='black')
    pp8 = mpatches.Circle((-6,0), radius=0.15, ec='black',fill=True, fc='black')
    pp9 = mpatches.PathPatch(
    Path([(-9,0), (-6, 3.2), (-3,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    pp10 = mpatches.PathPatch(
    Path([(-3,0), (3, -3.5), (9,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp)
    ax.add_patch(pp2)
    ax.add_patch(pp3)
    ax.add_patch(pp4)
    ax.add_patch(pp5)
    ax.add_patch(pp6)
    ax.add_patch(pp7)
    ax.add_patch(pp8)
    ax.add_patch(pp9)
    ax.add_patch(pp10)

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (-6, 1.6), xy = (-9,4),
    arrowprops = {
              'color':'black',
              'connectionstyle':"arc3,rad=0.4",
              'edgecolor':'b', 
              'arrowstyle':'<-'
              })
    
    ax.text(-11.5,3.7, '${n1}$cm'.format(n1=n1), size = 12)
    ax.text(1.9,-3, '${n2}$cm'.format(n2=n2), size = 12)
    
    f = "\\frac{1}{2}"
    
    x = int(ans1/2)

    aa_list = [(x,fractions.Fraction(an-fractions.Fraction(x))),(x,an),(x,fractions.Fraction(an+fractions.Fraction(x))),
               (ans1,an),(ans1,fractions.Fraction(an+fractions.Fraction(x))),(ans1,fractions.Fraction(an+fractions.Fraction(x)+fractions.Fraction(x)))]
    idx = random.randint(0,1)
    a_list = []
    
    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    aa1, aa2, aa3, aa4, aa5 = a_list

    a1 = aa1[0]
    a_2 = aa1[1]

    if a_2.denominator == 1 :
        a2 = int(a_2)
    else :
        a2 = "\\frac{"+str(a_2.numerator)+"}{"+str(a_2.denominator)+"}"

    a3 = aa2[0]
    a_4 = aa2[1]

    if a_4.denominator == 1 :
        a4 = int(a_4)
    else :
        a4 = "\\frac{"+str(a_4.numerator)+"}{"+str(a_4.denominator)+"}"

    a5 = aa3[0]
    a_6 = aa3[1]

    if a_6.denominator == 1 :
        a6 = int(a_6)
    else :
        a6 = "\\frac{"+str(a_6.numerator)+"}{"+str(a_6.denominator)+"}"

    a7 = aa4[0]
    a_8 = aa4[1]

    if a_8.denominator == 1 :
        a8 = int(a_8)
    else :
        a8 = "\\frac{"+str(a_8.numerator)+"}{"+str(a_8.denominator)+"}"

    a9 = aa5[0]
    a_10 = aa5[1]

    if a_10.denominator == 1 :
        a10 = int(a_10)
    else :
        a10 = "\\frac{"+str(a_10.numerator)+"}{"+str(a_10.denominator)+"}"

    ans = (ans1,an)

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break
   

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, a8=a8, a9=a9, a10=a10)
    answer = answer.format(result=result)
    comment = comment.format(s1=s1, s2=s2, s3=s3, f=f, f1=f1, f2=f2, f3=f3, ans1=ans1, ans2=ans2)
    svg = saveSvg()
    return stem, answer, comment, svg 


def planefigure122_Stem_108():
    stem = "다음 그림과 같이 폭이 $$수식$${n}``rm m$$/수식$$로 일정한 육상 트랙을 만들려고 한다. 이 트랙의 넓이는?\n" \
            "① $$수식$$({a1})m^2$$/수식$$   ② $$수식$$({a2})m^2$$/수식$$\n" \
            "③ $$수식$$({a3})m^2$$/수식$$   ④ $$수식$$({a4})m^2$$/수식$$\n⑤ $$수식$$({a5})m^2$$/수식$$\n"

    answer = "(정답)\n{result}"
    comment = "(해설)\n (트랙의 넓이)$$수식$$=(\\pi TIMES {s1}^2 - \\pi TIMES {s2}^2)+({n} TIMES {n3}) TIMES  2$$/수식$$\n" \
              "$$수식$$={ans}(m^2)$$/수식$$\n"

    while True :
      n = random.randint(3,12)
      n2 = n*3
      n3 = n+n2+n
      if n3%2 == 0 and n2%2==0:
        break
    
    s1 = int(n3/2)
    s2 = int(n2/2)

    ans1 = (s1*s1)-(s2*s2)
    ans2 = n*n3*2

    center = (0,0)
    center2 = (20,0)
    radius = 10

    
    #ax = setChart(points=[center,center2])
    
    fig, ax = plt.subplots(figsize=(3.5,2.5))
    plt.axis("off")
    ax.autoscale()

    #ax.set_xlim(-10,40)
    #ax.set_ylim(-35,20)

    pp = mpatches.Wedge(center, r=radius, theta1=90,
                                theta2=270, ec="black", fc='orange', fill=True, alpha=0.4)
    pp2 = mpatches.Wedge(center, r=6, theta1=90,
                                theta2=270, ec="black", fc='white', fill=True, alpha=1)
    pp3 = mpatches.Wedge(center, r=radius, theta1=90,
                                theta2=270, ec="black", fill=False)
    pp4 = mpatches.Wedge(center2, r=radius, theta1=270,
                                theta2=90, ec="black", fc='orange', fill=True, alpha=0.4)
    pp5 = mpatches.Wedge(center2, r=6, theta1=270,
                                theta2=90, ec="black", fc='white', fill=True, alpha=1)
    pp6 = mpatches.Wedge(center2, r=radius, theta1=270,
                                theta2=90, ec="black",  fill=False)
    
    verts = [(0,10),(20,10),(20,-10),(0,-10)]
    vert = verts
    vert.append(verts[0])
    codes = [Path.MOVETO]

    for i in range(0,len(vert)-2):
        codes.append(Path.LINETO)

    codes.append(Path.CLOSEPOLY)

    path = Path(vert,codes)

    verts2 = [(0,6),(20,6),(20,-6),(0,-6)]
    vert2 = verts2
    vert2.append(verts2[0])
    codes2 = [Path.MOVETO]

    for i in range(0,len(vert2)-2):
        codes2.append(Path.LINETO)

    codes2.append(Path.CLOSEPOLY)

    path2 = Path(vert2,codes2)

    pp7 = mpatches.PathPatch(path, fc='orange', fill=True, alpha=0.4)
    pp8 = mpatches.PathPatch(path, ec="black", fill=False)
    pp9 = mpatches.PathPatch(path2, fc='white', fill=True, alpha=1)
    pp10 = mpatches.Circle(center, radius=0.25, ec='black',fill=True, fc='black')
    pp11 = mpatches.Circle(center2, radius=0.25, ec='black',fill=True, fc='black')
    pp12 = mpatches.PathPatch(
    Path([(0,10), (3, 8), (0,6)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    pp13 = mpatches.PathPatch(
    Path([(0,6), (5, 0), (0,-6)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    pp14 = mpatches.PathPatch(
    Path([(0,-10), (3, -8), (0,-6)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    pp15 = mpatches.PathPatch(
    Path([(0,-10), (10, -15), (20,-10)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")


    ax.add_patch(pp)
    ax.add_patch(pp2)
    ax.add_patch(pp3)
    ax.add_patch(pp4)
    ax.add_patch(pp5)
    ax.add_patch(pp6)
    ax.add_patch(pp7)
    ax.add_patch(pp8)
    ax.add_patch(pp9)
    ax.add_patch(pp10)
    ax.add_patch(pp11)
    ax.add_patch(pp12)
    ax.add_patch(pp13)
    ax.add_patch(pp14)
    ax.add_patch(pp15)

    x = [1.2,1.2,0]
    y = [6,4.8,4.8]

    ax.plot(x,y, c="black", linewidth = 0.4)

    x2 = [0,1.2,1.2]
    y2 = [-4.8,-4.8,-6]

    ax.plot(x2,y2, c="black", linewidth = 0.4)

    x3 = [18.8,18.8,20]
    y3 = [-6,-4.8,-4.8]

    ax.plot(x3,y3, c="black", linewidth = 0.4)

    x4 = [18.8,18.8,20]
    y4 = [6,4.8,4.8]

    ax.plot(x4,y4, c="black", linewidth = 0.4)


    ax.text(1.8,7.1, '${n}$cm'.format(n=n), size = 9)
    ax.text(2.6,-0.8, '${n2}$cm'.format(n2=n2), size = 9)
    ax.text(1.8,-8.9, '${n}$cm'.format(n=n), size = 9)
    ax.text(6.4,-15, '${n3}$cm'.format(n3=n3), size = 9)

    ans = str(ans1)+"\\pi+"+str(ans2)
    
    x = int(ans1/n)
    x2 = int(ans2/n)

    a1 = str(ans1-x)+"\\pi+"+str(int(ans2/2))
    a2 = str(ans1-x)+"\\pi+"+str(ans2)
    a3 = str(ans1)+"\\pi+"+str(int(ans2/2))
    a4 = str(ans1)+"\\pi+"+str(ans2-x2)
    a5 = str(ans1)+"\\pi+"+str(ans2)
    
    #ax.figure.set_size_inches(7, 5)
    #ax.autoscale()

    result = answer_dict[4]

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(s1=s1, s2=s2, n=n, n3=n3, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 




def planefigure122_Stem_109():
    stem = "다음 그림의 반원에서 색칠한 부분의 둘레의 길이는?\n" \
            "① $$수식$$({a1}\\pi+{a2})``rm {{cm}}$$/수식$$     ② $$수식$$({a3}\\pi+{a4})``rm {{cm}}$$/수식$$\n" \
            "③ $$수식$$({a5}\\pi+{a6})``rm {{cm}}$$/수식$$     ④ $$수식$$({a7}\\pi+{a8})``rm {{cm}}$$/수식$$\n⑤ $$수식$$({a9}\\pi+{a10})``rm {{cm}}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n (색칠한 부분의 둘레의 길이)\n" \
              "$$수식$$=(2\\pi TIMES {s1}) TIMES {f}+(2\\pi TIMES {s2}) TIMES {f}+({s1}-{s2}) TIMES  2$$/수식$$\n" \
              "$$수식$${ans1}\\pi+{ans2}(rm {{cm}})$$/수식$$\n"
    while True :
      n = random.randint(4,8)
      n1 = n*2
      n2 = n*3
      if n1 % 2 == 0 and n2 % 2 == 0 :
        break      
    
    s1 = int(n2/2)
    s2 = int(n1/2)
    ans1 = s1+s2
    ans2 = (s1-s2)*2
    ans = (ans1,ans2)

    f = "\\frac{1}{2}"

    aa_list = [(int(ans1/2),int(ans2/4)),(int(ans1/2),int(ans2/2)),(int(ans1/2),ans2),(ans1,int(ans2/2)),(ans1,ans2),(ans1,ans2*2)]
    idx = random.randint(0,1)
    a_list = []
    
    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    aa1, aa2, aa3, aa4, aa5 = a_list    

    a1 = aa1[0]
    a2 = aa1[1]
    a3 = aa2[0]
    a4 = aa2[1]
    a5 = aa3[0]
    a6 = aa3[1]
    a7 = aa4[0]
    a8 = aa4[1]
    a9 = aa5[0]
    a10 = aa5[1]

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    center = (0,0)
    radius = 6

    
    #ax = setChart(points=[center])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
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

    pp = mpatches.Wedge(center, r=radius, theta1=0,
                                theta2=180, ec="black", fc='skyblue', fill=True, alpha=0.5)
    pp2 = mpatches.Wedge(center, r=4, theta1=0,
                                theta2=180, ec="black", fc='white', fill=True, alpha=1)
    pp3 = mpatches.Wedge(center, r=radius, theta1=0,
                                theta2=180, ec="black", fill=False)
    pp4 = mpatches.Circle(center, radius=0.13, ec='black',fill=True, fc='black')

    pp5 = mpatches.PathPatch(
    Path([(-6,0), (0, -2), (6,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    pp6 = mpatches.PathPatch(
    Path([(-4,0), (0, 2), (4,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp)
    ax.add_patch(pp2)
    ax.add_patch(pp3)
    ax.add_patch(pp4)
    ax.add_patch(pp5)
    ax.add_patch(pp6)
    
    ax.text(-0.82,1.4, '${n1}$cm'.format(n1=n1), size = 12)
    ax.text(-0.85,-1.8, '${n2}$cm'.format(n2=n2), size = 12)


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, a8=a8, a9=a9, a10=a10)
    answer = answer.format(result=result)
    comment = comment.format(s1=s1, s2=s2, f=f, ans1=ans1, ans2=ans2)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_111():
    stem = "다음 그림과 같이 반지름의 길이가 $$수식$${n1}``rm {{cm}}$$/수식$$, 호의 길이가 $$수식$${n2}\\pi``rm {{cm}}$$/수식$$인 부채꼴의 중심각의 크기는?\n" \
            "① $$수식$${a1}DEG $$/수식$$    ② $$수식$${a2}DEG $$/수식$$   ③ $$수식$${a3}DEG ``rm {{cm}}$$/수식$$\n" \
            "④ $$수식$${a4}DEG $$/수식$$    ⑤ $$수식$${a5}DEG $$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 중심각의 크기를 $$수식$$x DEG $$/수식$$라 하면\n" \
              "$$수식$$2\\pi TIMES {n1} TIMES {f}={n2}\\pi$$/수식$$   $$수식$$THEREFORE x={ans}$$/수식$$\n" \
              "따라서 구하는 중심각의 크기는 $$수식$${ans}DEG $$/수식$$\n" 

    f = "\\frac{x}{360}"

    while True :
      ans = random.choice([120,130,140,150])
      n1 = random.randint(4,12)
      if (ans*2*n1)%360 == 0:
        break

    n2 = int((2*n1*ans)/360)   

    aa_list = [ans-30, ans-20, ans-10, ans, ans+10, ans+20, ans+30]
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

    center = (0,0)
    p = (6*math.cos(math.radians(ans)),6*math.sin(math.radians(ans)))
    p2 = (7*math.cos(math.radians(ans)),7*math.sin(math.radians(ans)))
    p3 = (6,0)
    p4 = (7,0)

    p5 = (6.5*math.cos(math.radians(ans)),6.5*math.sin(math.radians(ans)))
    p6 = (6.5*math.cos(math.radians(ans/2+5)),6.5*math.sin(math.radians(ans/2+5)))

    p7 = (6.5,0)
    p8 = (6.5*math.cos(math.radians(ans/2-5)),6.5*math.sin(math.radians(ans/2-5)))

    
    ax = setChart(points=[center,p,p2,p3,p4,p5,p6,p7,p8])

    drawSector(ax=ax, center=center, radius=6, theta1=0, theta2=ans)
    drawLine(ax=ax, p1=p, p2=p2)
    drawLine(ax=ax, p1=p3, p2=p4)

    ax.scatter(0,0, c='black', edgecolor='black', s=20)

    if ans == 120 or ans == 130 :
      rad = 0.24
    elif ans == 140 or ans == 150 :
      rad = 0.3
    else :
      rad = 0.32

    ax.annotate('',ha = 'center', va = 'bottom',
    xytext = (p5[0],p5[1]), xy = (p6[0],p6[1]),
    arrowprops = {
              'color':'black',
              'connectionstyle':"arc3,rad=-{rad}".format(rad=rad),
              'edgecolor':'b', 
              'arrowstyle':'<-'
              })
    ax.annotate('',ha = 'center', va = 'bottom',
        xytext = (p7[0],p7[1]), xy = (p8[0],p8[1]),
        arrowprops = {
                  'color':'black',
                  'connectionstyle':"arc3,rad={rad}".format(rad=rad),
                  'edgecolor':'b', 
                  'arrowstyle':'<-'
                  })

    ag1 = AngleAnnotation(xy=center, p1=p3, p2=p, text=r"",
                    textposition="outside", ax=ax, size=25)       
    
    pp = mpatches.PathPatch(
    Path([(0,0), (3, -1.5), (6,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp)
    
    ax.text(p6[0]+0.1,p6[1]-0.1, '${n2}\pi cm$'.format(n2=n2), size = 12)
    ax.text(2.5,-1.4, '${n1}cm$'.format(n1=n1), size = 12)

    stem = stem.format(n1=n1, n2=n2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, f=f, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 





def planefigure122_Stem_112():
    stem = "반지름의 길이가 $$수식$${n1}``rm {{cm}}$$/수식$$이고 넓이가 $$수식$${n2}\\pi ``rm {{cm^2}}$$/수식$$인 부채꼴의 호의 길이는?\n" \
            "① $$수식$${a1}\\pi``rm {{cm}}$$/수식$$    ② $$수식$${a2}\\pi``rm {{cm}}$$/수식$$   ③ $$수식$${a3}\\pi``rm {{cm}}$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm {{cm}}$$/수식$$    ⑤ $$수식$${a5}\\pi``rm {{cm}}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 부채꼴의 중심각의 크기를 $$수식$$x DEG $$/수식$$라 하면\n" \
              "$$수식$$\\pi TIMES {n1}^2 TIMES {f1}={n2}\\pi$$/수식$$\n" \
              "$$수식$${f2}\\pi x={n2}\\pi$$/수식$$     $$수식$$THEREFORE x={ag}$$/수식$$\n" \
              "즉, 부채꼴의 중심각의 크기는 $$수식$${ag}DEG $$/수식$$이다.\n" \
              "따라서 부채꼴의 호의 길이는\n" \
              "$$수식$$2\\pi TIMES {n1} TIMES {f3}={ans}\\pi(rm {{cm}})$$/수식$$\n"

    while True :
        ag = random.choice([120,130,140,150,160])
        n1 = random.randint(8,16)
        if n1*n1*ag%360 == 0 :
            break
    
    n2 = int(n1*n1*ag/360)

    f1 = "\\frac{x}{360}"

    ff2 = fractions.Fraction(fractions.Fraction(n1*n1)/fractions.Fraction(360))
    f2 = "\\frac{"+str(ff2.numerator)+"}{"+str(ff2.denominator)+"}"

    f3 = "\\frac{"+str(ag)+"}{360}"
        
    an = fractions.Fraction(fractions.Fraction(2*n1*ag)/fractions.Fraction(360))
    
    aa_list = [fractions.Fraction(an-3), fractions.Fraction(an-2), fractions.Fraction(an-1), an, fractions.Fraction(an+1), fractions.Fraction(an+2), fractions.Fraction(an+3)]
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

    if an.denominator == 1 :
        ans = int(an)
    else :
        ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    if aa1.denominator == 1 :
        a1 = int(aa1)
    else :
        a1 = "\\frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"

    if aa2.denominator == 1 :
        a2 = int(aa2)
    else :
        a2 = "\\frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = int(aa3)
    else :
        a3 = "\\frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    if aa4.denominator == 1:
        a4 = int(aa4)
    else :
        a4 = "\\frac{"+str(aa4.numerator)+"}{"+str(aa4.denominator)+"}"

    if aa5.denominator == 1:
        a5 = int(aa5)
    else :
        a5 = "\\frac{"+str(aa5.numerator)+"}{"+str(aa5.denominator)+"}"
    


    stem = stem.format(n1=n1, n2=n2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, ag=ag, f1=f1, f2=f2, f3=f3, ans=ans)

    return stem, answer, comment



def planefigure122_Stem_113():
    stem = "다음 그림과 같이 한 변의 길이가 $$수식$${n}``rm {{cm}}$$/수식$$인 정팔각형에서 색칠한 부채꼴의 넓이는?\n" \
            "① $$수식$${a1}\\pi ``rm {{cm^2}}$$/수식$$      ② $$수식$${a2}\\pi ``rm {{cm^2}}$$/수식$$      ③ $$수식$${a3}\\pi ``rm {{cm^2}}$$/수식$$\n" \
            "④ $$수식$${a4}\\pi ``rm {{cm^2}}$$/수식$$      ⑤ $$수식$${a5}\\pi ``rm {{cm^2}}$$/수식$$\n"

    answer = "(정답)\n{result}"
    comment = "(해설)\n 정팔각형의 한 내각의 크기는 $$수식$$135 DEG $$/수식$$이므로 구하는 넓이는\n" \
              "$$수식$$\\pi TIMES {n}^2 TIMES {f1}={ans}\\pi(rm {{cm^2}})$$/수식$$\n"

    while True :
      n = random.randint(4,18)
      if (n*n*135)%360 == 0 :
        break 
        
    ans = int(n*n*135/360)
    f1 = "\\frac{135}{360}"

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

    a = (0.5,0.5)
    b = (0,0)
    c = (0,-0.7)
    d = (0.5,-1.2)
    e = (1.2,-1.2)
    f = (1.7,-0.7)
    g = (1.7,0)
    h = (1.2,0.5)

    
    #ax = setChart(points=[a,b,c,d,e,f,g,h])

    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    drawPolygon(ax=ax, verts=[a,b,c,d,e,f,g,h])

    drawSector(ax=ax, center=c, radius=0.7, theta1=-45, theta2=90, fill=False)
    pp = mpatches.Wedge(c, r=0.7, theta1=-45,
                                theta2=90, fc='greenyellow', fill=True, alpha=0.5)    
    ax.add_patch(pp)

    pp2 = mpatches.PathPatch(
    Path([(0,-0.7), (0,-1.2), (0.5,-1.2)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp2)

    ax.text(-0.1,-1.2, '${n}cm$'.format(n=n), size = 11)
    
    ax.autoscale()

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, f1=f1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_116():
    stem = "다음 그림에서 색칠한 부분의 둘레의 길이는?\n" \
            "① $$수식$${a1}\\pi``rm {{cm}}$$/수식$$     ② $$수식$${a2}\\pi``rm {{cm}}$$/수식$$       ③ $$수식$${a3}\\pi``rm {{cm}}$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm {{cm}}$$/수식$$     ⑤ $$수식$${a5}\\pi``rm {{cm}}$$/수식$$\n"
 
    answer = "(정답)\n{result}"
    comment = "(해설)\n (색칠한 부분의 둘레의 길이)\n" \
              "=(반지름의 길이가 $$수식$${r}``rm {{cm}}$$/수식$$인 사분원의 호의 길이)$$수식$$ TIMES  4$$/수식$$\n" \
              "$$수식$$\\left(2\\pi  TIMES  {r}  TIMES  {f}\\right) TIMES  4$$/수식$$" \
              "$$수식$$={ans}\\pi(rm {{cm}})$$/수식$$\n"

    while True :
      n = random.randint(8,16)
      if n % 2 == 0:
        break

    ans = n
    r = int(n/2)

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

    a = (0,8)
    b = (0,0)
    c = (8,0)
    d = (8,8)
    p1 = (-1.8,4)
    p2 = (4,-1.8)

    
    #ax = setChart(points=[a,b,c,d,p1,p2])

    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()

    x = [0,0,8,8,0]
    y = [8,0,0,8,8]
    #plt.plot(x,y,c="black")
    #plt.fill(x, y, alpha=0.3, color="purple")
    
    
    verts = [a,d,c,b]
    drawPolygon(ax=ax, verts=verts, fill=True, alpha=0.4)
    
    pp1 = mpatches.Wedge(a, r=4, theta1=270,
                                theta2=360, ec="black", fc='white', fill=True, alpha=1, zorder=4)
    pp2 = mpatches.Wedge(b, r=4, theta1=0,
                                theta2=90, ec="black", fc='white', fill=True, alpha=1, zorder=4)
    pp3 = mpatches.Wedge(c, r=4, theta1=90,
                                theta2=180, ec="black", fc='white', fill=True, alpha=1, zorder=4)
    pp4 = mpatches.Wedge(d, r=4, theta1=180,
                         theta2=270, ec="black", fc='white', fill=True, alpha=1, zorder=4)

    pp5 = mpatches.PathPatch(
    Path([(0,0), (-1.8,4), (0,8)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")
    pp6 = mpatches.PathPatch(
    Path([(0,0), (4,-1.8), (8,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    #ax.add_patch(pp_)
    ax.add_patch(pp1)
    ax.add_patch(pp2)
    ax.add_patch(pp3)
    ax.add_patch(pp4)
    ax.add_patch(pp5)
    ax.add_patch(pp6)

    x2 = [0,0.4,0.4]
    y2 = [7.6,7.6,8]

    ax.plot(x2,y2, c="black", linewidth = 0.4)

    x3 = [0,0.4,0.4]
    y3 = [0.4,0.4,0]

    ax.plot(x3,y3, c="black", linewidth = 0.4)

    x4 = [7.6,7.6,8]
    y4 = [0,0.4,0.4]

    ax.plot(x4,y4, c="black", linewidth = 0.4)

    x5 = [7.6,7.6,8]
    y5 = [8,7.6,7.6]

    ax.plot(x5,y5, c="black", linewidth = 0.4)

    if n<10 :
      t=-2.35
    else :
      t=-2.5

    ax.text(t,3.9, '${n}cm$'.format(n=n), size = 12)
    ax.text(3.4,-1.5, '${n}cm$'.format(n=n), size = 12)

    f = "\\frac{1}{4}"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(r=r, f=f, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def planefigure122_Stem_118():
    stem = "다음 그림과 같이 한 변의 길이가 $$수식$${n}``rm {{cm}}$$/수식$$인 정사각형에서 색칠한 부분의 넓이는?\n" \
            "① $$수식$$({a1}\\pi-{a2})``rm {{cm^2}}$$/수식$$        ② $$수식$$({a3}\\pi-{a4})``rm {{cm^2}}$$/수식$$\n" \
            "③ $$수식$$({a5}\\pi-{a6})``rm {{cm^2}}$$/수식$$        ④ $$수식$$({a7}\\pi-{a8})``rm {{cm^2}}$$/수식$$\n" \
            "⑤ $$수식$$({a9}\\pi-{a10})``rm {{cm^2}}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n (색칠한 부분의 넓이)\n" \
              "$$수식$$=\\left(\\pi  TIMES  {n}^2  TIMES  {f1} - {f2} TIMES {n} TIMES {n} \\right) TIMES  2$$/수식$$\n" \
              "$$수식$$={ans1}\\pi-{ans2}(rm {{cm^2}})$$/수식$$\n"

    while True :
      n = random.randint(16,28)
      if n % 2 == 0:
        break

    f1 = "\\frac{90}{360}"
    f2 = "\\frac{1}{2}"
    ans1 = int(n*n*90/360)*2
    ans2 = int(n*n/2)*2
    k = int(ans1/2)
    ans = (ans1,ans2)

    aa_list = [(ans1-k,int(ans2/4)),(ans1-k,int(ans2/2)),(ans1,int(ans2/2)),(ans1,ans2),(ans1*2,ans2),(ans1*2,ans2+int(ans2/2))]
    idx = random.randint(0,1)
    a_list = []
    
    for i in range(5):
      a_list.append(aa_list[idx])
      idx += 1
    
    aa1, aa2, aa3, aa4, aa5 = a_list    

    a1 = aa1[0]
    a2 = aa1[1]
    a3 = aa2[0]
    a4 = aa2[1]
    a5 = aa3[0]
    a6 = aa3[1]
    a7 = aa4[0]
    a8 = aa4[1]
    a9 = aa5[0]
    a10 = aa5[1]

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    a = (0,20)
    b = (0,0)
    c = (20,0)
    d = (20,20)
    p1 = (-1.8,4)
    p2 = (4,-1.8)

    
    #ax = setChart(points=[a,b,c,d,p1,p2])

    fig, ax = plt.subplots(figsize=(4, 4.5))
    plt.axis("off")
    ax.autoscale()

    x = []
    y = []

    for i in range(135,181) :
      x.append(20+20*math.cos(math.radians(i)))
      y.append(20*math.sin(math.radians(i)))

    for i in range(270,316) :
      x.append(20*math.cos(math.radians(i)))
      y.append(20+20*math.sin(math.radians(i)))

    x.append(x[0])
    y.append(y[0])
    ax.fill(x, y, color="pink",alpha = 0.5)

    x2 = []
    y2 = []

    for i in range(0,91) :
      x2.append(20*math.cos(math.radians(i)))
      y2.append(20*math.sin(math.radians(i)))

    x2.append(x2[0])
    y2.append(y2[0])
    ax.fill(x2, y2, color="pink",alpha = 0.5)

    drawPolygon(ax=ax, verts=[a,b,c,d])
    drawLine(ax=ax, p1=a, p2=c)

    pp = mpatches.Wedge(b, r=20, theta1=0,
                                theta2=90, fc='pink', fill=False)
    pp2 = mpatches.Wedge(b, r=20, theta1=0,
                                theta2=90, ec='black', fill=False)
    pp3 = mpatches.Wedge(c, r=20, theta1=90,
                                theta2=180, ec='black', fill=False)
    pp4 = mpatches.Wedge(a, r=20, theta1=270,
                                theta2=360, ec='black', fill=False)
    pp5 = mpatches.PathPatch(
    Path([(0,0), (10,-3), (20,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")


    ax.add_patch(pp)
    ax.add_patch(pp2)
    ax.add_patch(pp3)
    ax.add_patch(pp4)
    ax.add_patch(pp5)

    ax.text(8.2,-2.8, '${n}$cm'.format(n=n), size = 12)

    svg1 = saveSvg()

    ax2 = setChart(points=[a,b,c,d,p1,p2])

    x3 = []
    y3 = []

    for i in range(90,181) :
      x3.append(20+20*math.cos(math.radians(i)))
      y3.append(20*math.sin(math.radians(i)))

    x3.append(x3[0])
    y3.append(y3[0])
    ax2.fill(x3, y3, color="pink",alpha = 0.5)

    x4 = []
    y4 = []

    for i in range(270,361) :
      x4.append(20*math.cos(math.radians(i)))
      y4.append(20+20*math.sin(math.radians(i)))

    x4.append(x4[0])
    y4.append(y4[0])
    ax2.fill(x4, y4, color="pink",alpha = 0.5)

    drawPolygon(ax=ax2, verts=[a,b,c,d])
    drawLine(ax=ax2, p1=a, p2=c)
    drawLine(ax=ax2, p1=b, p2=d)

    pp = mpatches.Wedge(b, r=20, theta1=0,
                                theta2=90, fc='pink', fill=False)
    pp2 = mpatches.Wedge(b, r=20, theta1=0,
                                theta2=90, ec='black', fill=False)
    pp3 = mpatches.Wedge(c, r=20, theta1=90,
                                theta2=180, ec='black', fill=False)
    pp4 = mpatches.Wedge(a, r=20, theta1=270,
                                theta2=360, ec='black', fill=False)
    pp5 = mpatches.PathPatch(
    Path([(0,0), (10,-3), (20,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")


    ax2.add_patch(pp)
    ax2.add_patch(pp2)
    ax2.add_patch(pp3)
    ax2.add_patch(pp4)
    ax2.add_patch(pp5)

    ax2.text(8.2,-2.8, '${n}$cm'.format(n=n), size = 12)

    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (17.5,14.5), xy = (17,6),
    arrowprops = {
              'color':'black',
              'connectionstyle':"arc3,rad=-0.3",
              'edgecolor':'b', 
              'arrowstyle':'<-'
              })
    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (14.5,17.5), xy = (6,17),
    arrowprops = {
              'color':'black',
              'connectionstyle':"arc3,rad=0.3",
              'edgecolor':'b', 
              'arrowstyle':'<-'
              })
   
    svg2 = saveSvg()

    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, a8=a8, a9=a9, a10=a10)
    answer = answer.format(result=result)
    comment = comment.format(f1=f1, f2=f2, n=n, ans1=ans1, ans2=ans2)
    svg = [svg1,svg2]
    return stem, answer, comment, svg 



def planefigure122_Stem_121():
    stem = "다음 그림과 같이 직각삼각형 $$수식$$ABC$$/수식$$를 점 $$수식$$C$$/수식$$를 중심으로 점 $$수식$$A$$/수식$$가 " \
            "변 $$수식$$BC$$/수식$$의 연장선 위의 점 $$수식$$A'$$/수식$$에 오도록 회전시켰다 " \
            "$$수식$$\\angle ABC=60 DEG $$/수식$$이고 $$수식$${ac}={n}``rm {{cm}}$$/수식$$일 때, 점 $$수식$$A$$/수식$$가 움직인 거리는?\n" \
            "① $$수식$${a1}\\pi``rm {{cm}}$$/수식$$    ② $$수식$${a2}\\pi``rm {{cm}}$$/수식$$   ③ $$수식$${a3}\\pi``rm {{cm}}$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm {{cm}}$$/수식$$    ⑤ $$수식$${a5}\\pi``rm {{cm}}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 그림에서 점 " \
              "$$수식$$A$$/수식$$가 움직인 거리는\n" \
              "중심각의 크기가 " \
              "$$수식$$150 DEG $$/수식$$이고\n반지름의 " \
              "길이가 $$수식$${n}``rm {{cm}}$$/수식$$인 부채꼴의 호의 길이와 같으므로\n" \
              "$$수식$$2\\pi TIMES {n} TIMES {f}={ans}\\pi(rm {{cm}})$$/수식$$\n"

    while True :
      n = random.randint(4,18)
      if n % 6 == 0 :
        break 
    
    f = "\\frac{150}{360}"
    ans = int(2*n*(150/360))
    ac = "\\overline{AC}"

    a = (6*math.cos(math.radians(150)),6*math.sin(math.radians(150)))
    a_2 = (6,0)
    c = (0,0)
    b = (-math.sqrt(45),0)
    b_2 = (6,3)
    p1 = (-8,0)
    p2 = (8,0)

    
    #ax = setChart(points=[a,b,c,p1,p2])

    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    ax.set_xlim(-7, 0)

    drawSector(ax=ax, center=c, radius=6, theta1=0, theta2=180, fill=False)
    drawPolygon(ax=ax, verts=[a_2,b_2,c])
    drawPolygon(ax=ax, verts=[a,b,c])
    drawLine(ax=ax, p1=p1, p2=b)
    drawLine(ax=ax, p1=a_2, p2=p2)

    x = [a[0],b[0],c[0],a[0]]
    y = [a[1],b[1],c[1],a[1]]
    ax.fill(x, y, color="white")

    pp = mpatches.PathPatch(
    Path([a, (-2,3.2), c],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp)

    ax.text(-2.4,2.6, '${n}$cm'.format(n=n), size = 11)

    ax.text(a[0]-0.7,a[1], 'A', size = 16)
    ax.text(b[0]-0.5,b[1]-1, 'B', size = 16)
    ax.text(c[0]-0.4,c[1]-1, 'C', size = 16)
    ax.text(a_2[0]-0.4,a_2[1]-1, "A'", size = 16)
    ax.text(b_2[0]-0.2,b_2[1]+0.2, "B'", size = 16)

    a1 = AngleAnnotation(xy=b, p1=c, p2=a, text=r'$60°$',
                    textposition="outside", ax=ax, size=25)  

    x2 = [-5.4,-5,-4.8]
    y2 = [2.6,2.38,2.75]
    ax.plot(x2,y2, c="black", linewidth = 0.7)

    x3 = [5.5,5.5,6]
    y3 = [0,0.5,0.5]
    ax.plot(x3,y3, c="black", linewidth = 0.7)

    svg1 = saveSvg()
    
    ax2 = setChart(points=[a,b,c,p1,p2])

    drawSector(ax=ax2, center=c, radius=6, theta1=0, theta2=180, fill=False)
    drawPolygon(ax=ax2, verts=[a_2,b_2,c])
    drawPolygon(ax=ax2, verts=[a,b,c])
    drawLine(ax=ax2, p1=p1, p2=b)
    drawLine(ax=ax2, p1=a_2, p2=p2)

    ax2.fill(x, y, color="white")

    pp = mpatches.PathPatch(
    Path([a, (-2,3.2), c],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp)

    ax2.text(-2.4,2.6, '${n}$cm'.format(n=n), size = 11)

    ax2.text(a[0]-0.7,a[1], 'A', size = 16)
    ax2.text(b[0]-0.5,b[1]-1, 'B', size = 16)
    ax2.text(c[0]-0.4,c[1]-1, 'C', size = 16)
    ax2.text(a_2[0]-0.4,a_2[1]-1, "A'", size = 16)
    ax2.text(b_2[0]-0.2,b_2[1]+0.2, "B'", size = 16)

    a2 = AngleAnnotation(xy=b, p1=c, p2=a, text=r'$60°$',
                    textposition="outside", ax=ax2, size=25)  
    a3 = AngleAnnotation(xy=c, p1=a, p2=b, text=r'$30°$',
                    textposition="outside", ax=ax2, size=40)
    a4 = AngleAnnotation(xy=c, p1=b_2, p2=a, text=r'$120°$',
                    textposition="outside", ax=ax2, size=22)    
    a5 = AngleAnnotation(xy=c, p1=a_2, p2=b_2, text=r'$30°$',
                    textposition="outside", ax=ax2, size=45)        

    ax2.plot(x2,y2, c="black", linewidth = 0.7)
    ax2.plot(x3,y3, c="black", linewidth = 0.7)
    
    svg2 = saveSvg()
    
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


    stem = stem.format(ac=ac, n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, f=f, ans=ans)
    svg = [svg1,svg2]
    return stem, answer, comment, svg 



def planefigure122_Stem_123():
    stem = "다음 그림과 같이 반지름의 길이가 $$수식$${n}``rm {{cm}}$$/수식$$인 두 원 $$수식$$O$$/수식$$와 $$수식$$O'$$/수식$$" \
            "이 서로의 중심을 지날 때, 색칠한 부분의 둘레의 길이는?\n" \
            "① $$수식$${a1}\\pi``rm {{cm}}$$/수식$$    ② $$수식$${a2}\\pi``rm {{cm}}$$/수식$$   ③ $$수식$${a3}\\pi``rm {{cm}}$$/수식$$\n" \
            "④ $$수식$${a4}\\pi``rm {{cm}}$$/수식$$    ⑤ $$수식$${a5}\\pi``rm {{cm}}$$/수식$$\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n 그림에서 색칠한 부분의 둘레의 길이는\n" \
              "반지름의 길이가 $$수식$${n}``rm {{cm}}$$/수식$$이고\n" \
              "중심각의 크기가 $$수식$$60 DEG $$/수식$$인 부채꼴의 호의 길이의\n" \
              "$$수식$$4$$/수식$$배와 같으므로 구하는 둘레의 길이는\n" \
              "$$수식$$\\left(2\\pi TIMES {n} TIMES {f}\\right) TIMES  4 = {ans}\\pi(rm {{cm}})$$/수식$$\n"

    while True :
      n = random.randint(6,18)
      if n % 3 == 0 :
        break

    f = "\\frac{60}{360}"
    ans = int(2*n*(60/360)*4)

    o = (0,0)
    o_2 = (6,0)
 
    p1 = (6*math.cos(math.radians(60)),6*math.sin(math.radians(60)))
    p2 = (6*math.cos(math.radians(300)),6*math.sin(math.radians(300)))

    
    #ax = setChart(points=[o,o_2])

    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax.autoscale()
    
    drawCircle(ax=ax, center=o, radius=6)
    drawCircle(ax=ax, center=o_2, radius=6)
    drawLine(ax=ax, p1=o, p2=o_2)
    
    ax.scatter(0,0, c='black', edgecolor='black', s=30)
    ax.scatter(6,0, c='black', edgecolor='black', s=30)

    ax.text(-1.2,-0.4, "$O$", size = 15)
    ax.text(6.3,-0.4, "$O'$", size = 15)

    x = []
    y = []

    for i in range(0,61) :
      x.append(6*math.cos(math.radians(i)))
      y.append(6*math.sin(math.radians(i)))

    for i in range(120,181) :
      x.append(6+6*math.cos(math.radians(i)))
      y.append(6*math.sin(math.radians(i)))

    for i in range(180,241) :
      x.append(6+6*math.cos(math.radians(i)))
      y.append(6*math.sin(math.radians(i)))
    
    for i in range(300,361) :
      x.append(6*math.cos(math.radians(i)))
      y.append(6*math.sin(math.radians(i)))

    ax.fill(x, y, color="lightblue", alpha=0.5)

    pp = mpatches.PathPatch(
    Path([(0,0), (3,-2), (6,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp)

    ax.text(2,-1.8, '${n}cm$'.format(n=n), size = 12)
    
    svg1 = saveSvg()

    #ax2 = setChart(points=[o,o_2])
    
    fig, ax2 = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    ax2.autoscale()

    drawCircle(ax=ax2, center=o, radius=6)
    drawCircle(ax=ax2, center=o_2, radius=6)
    drawLine(ax=ax2, p1=o, p2=o_2)
    drawLine(ax=ax2, p1=o, p2=p1)
    drawLine(ax=ax2, p1=o, p2=p2)
    drawLine(ax=ax2, p1=o_2, p2=p1)
    drawLine(ax=ax2, p1=o_2, p2=p2)
  
    ax2.text(-1.2,-0.4, "$O$", size = 15)
    ax2.text(6.3,-0.4, "$O'$", size = 15)

    ax2.fill(x, y, color="lightblue", alpha=0.7)

    pp = mpatches.PathPatch(
    Path([(0,0), (3,-2), (6,0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax2.transData,linestyle="--")

    ax2.add_patch(pp)

    an1 = AngleAnnotation(xy=o, p1=o_2, p2=p1, text=r"$60°$",
                    textposition="outside", ax=ax2, size=35)  
    
    c1 = ((o[0]+p1[0])/2,(o[1]+p1[1])/2)
    c2 = ((o_2[0]+p1[0])/2,(o_2[1]+p1[1])/2)
    c3 = ((o_2[0]+p2[0])/2,(o_2[1]+p2[1])/2)
    c4 = ((o[0]+p2[0])/2,(o[1]+p2[1])/2)

    x2 = [c1[0]-0.2,c1[0]+0.2]
    y2 = [c1[1]+0.1,c1[1]-0.2]
    ax2.plot(x2,y2, c="black", linewidth = 0.7)

    x3 = [c1[0]-0.1,c1[0]+0.3]
    y3 = [c1[1]+0.3,c1[1]]
    ax2.plot(x3,y3, c="black", linewidth = 0.7)

    x4 = [c2[0]-0.2,c2[0]+0.2]
    y4 = [c2[1]-0.2,c2[1]+0.1]
    ax2.plot(x4,y4, c="black", linewidth = 0.7)

    x5 = [c2[0]-0.3,c2[0]+0.1]
    y5 = [c2[1],c2[1]+0.3]
    ax2.plot(x5,y5, c="black", linewidth = 0.7)

    x6 = [c3[0]-0.2,c3[0]+0.2]
    y6 = [c3[1]+0.1,c3[1]-0.2]
    ax2.plot(x6,y6, c="black", linewidth = 0.7)

    x7 = [c3[0]-0.1,c3[0]+0.3]
    y7 = [c3[1]+0.3,c3[1]]
    ax2.plot(x7,y7, c="black", linewidth = 0.7)

    x8 = [c4[0]-0.2,c4[0]+0.2]
    y8 = [c4[1]-0.2,c4[1]+0.1]
    ax2.plot(x8,y8, c="black", linewidth = 0.7)

    x9 = [c4[0]-0.3,c4[0]+0.1]
    y9 = [c4[1],c4[1]+0.3]
    ax2.plot(x9,y9, c="black", linewidth = 0.7)

    ax2.scatter(0,0, c='black', edgecolor='black', s=30)
    ax2.scatter(6,0, c='black', edgecolor='black', s=30)

    ax2.annotate('',ha = 'center', va = 'bottom',
    xytext = (3.8,-0.7), xy = (6.5,-2),
    arrowprops = {
              'color':'black',
              'connectionstyle':"arc3,rad=0.3",
              'edgecolor':'b', 
              'arrowstyle':'<-'
              })
    ax2.text(6.4,-2.4, '${n}cm$'.format(n=n), size = 12)

    svg2 = saveSvg()

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


    stem = stem.format(n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, f=f, ans=ans)
    svg = [svg1,svg2]
    return stem, answer, comment, svg 



def planefigure122_Stem_125():
    stem = "다음 그림은 $$수식$$\\angle A=90 DEG $$/수식$$인 직각삼각형 $$수식$$ABC$$/수식$$의 각 변을 지름으로 하는 반원을 그린 것이다. " \
            "$$수식$${ab}={n1}``rm {{cm}}$$/수식$$, $$수식$${bc}={n2}cm, {ac}={n3}``rm {{cm}}$$/수식$$일 때, 색칠한 부분의 넓이는?\n" \
            "① $$수식$${a1}``rm {{cm^2}}$$/수식$$    ② $$수식$${a2}``rm {{cm^2}}$$/수식$$   ③ $$수식$${a3}``rm {{cm^2}}$$/수식$$\n" \
            "④ $$수식$${a4}\\pi ``rm {{cm^2}}$$/수식$$   ⑤ $$수식$${a5}\\pi ``rm {{cm^2}}$$/수식$$\n" 
    answer = "(정답)\n {result}"
    comment = "(해설)\n 구하는 넓이는\n" \
              "(지름이 $$수식$${ab}$$/수식$$인 반원의 넓이)\n" \
              "$$수식$$+$$/수식$$(지름이 $$수식$${ac}$$/수식$$인 반원의 넓이)\n" \
              "$$수식$$+\\triangle ABC-$$/수식$$(지름이 $$수식$${bc}$$/수식$$인 반원의 넓이)\n" \
              "$$수식$$=\\pi TIMES {r1}^2 TIMES {f}+\\pi TIMES {r2}^2 TIMES {f}+{f} TIMES {n1} TIMES {n3}$$/수식$$\n" \
              "$$수식$$-\\pi TIMES {r3}^2 TIMES {f}$$/수식$$\n" \
              "$$수식$$={s1}\\pi+{s2}\\pi+{s3}-{s4}\\pi$$/수식$$\n" \
              "$$수식$$={ans}(rm {{cm^2}})$$/수식$$" 

    while True :
        k = random.randint(2,6)
        if k%2 == 0 :
            break

    n1 = 4*k
    n2 = 5*k
    n3 = 3*k 

    r1 = int(n1/2)
    r2 = int(n3/2)
    r3 = int(n2/2)

    ss1 = fractions.Fraction(fractions.Fraction(r1*r1)/fractions.Fraction(2))
    ss2 = fractions.Fraction(fractions.Fraction(r2*r2)/fractions.Fraction(2))
    ss3 = fractions.Fraction(fractions.Fraction(n1*n3)/fractions.Fraction(2))
    ss4 = fractions.Fraction(fractions.Fraction(r3*r3)/fractions.Fraction(2))


    if ss1.denominator == 1 :
        s1 = int(ss1)
    else :
        s1 = "\\frac{"+str(ss1.numerator)+"}{"+str(ss1.denominator)+"}"

    if ss2.denominator == 1 :
        s2 = int(ss2)
    else :
        s2 = "\\frac{"+str(ss2.numerator)+"}{"+str(ss2.denominator)+"}"

    if ss3.denominator == 1 :
        s3 = int(ss3)
    else :
        s3 = "\\frac{"+str(ss3.numerator)+"}{"+str(ss3.denominator)+"}"

    if ss4.denominator == 1 :
        s4 = int(ss4)
    else :
        s4 = "\\frac{"+str(ss4.numerator)+"}{"+str(ss4.denominator)+"}"


    ab = "\\overline{AB}"
    bc = "\\overline{BC}"
    ac = "\\overline{AC}"
    f = "\\frac{1}{2}"

    an = fractions.Fraction(ss1+ss2+ss3-ss4)

    kk = fractions.Fraction(an/fractions.Fraction(2))

    aa1 = an-kk
    aa2 = an
    aa3 = an+kk

    if an.denominator == 1 :
        ans = int(an)
    else :
        ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    if aa1.denominator == 1 :
        a1 = int(aa1)
    else :
        a1 = "\\frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"

    if aa2.denominator == 1 :
        a2 = int(aa2)
    else :
        a2 = "\\frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = int(aa3)
    else :
        a3 = "\\frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    a4 = random.choice([a1,a2])

    if a4 == a1 :
        a5 = a2
    elif a4 == a2:
        a5 = a3
    

    a = (8*math.cos(math.radians(36.5))-5,8*math.sin(math.radians(36.5)))
    c = (5,0)
    b = (-5,0)
    o = (0,0)
    a_b = ((a[0]+b[0])/2,(a[1]+b[1])/2)
    a_c = ((a[0]+c[0])/2,(a[1]+c[1])/2)

    
    #ax = setChart(points=[a,b,c,o,a_b,a_c])
    
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    plt.axis("off")
    #ax.set_xlim(0, 10)
    ax.autoscale()

    pp = mpatches.Wedge(a_b, r=4, theta1=36.5,
                                theta2=216.5, fc='pink', fill=True, alpha=0.4)    
    ax.add_patch(pp)

    pp2 = mpatches.Wedge(a_c, r=3, theta1=-53.5,
                                theta2=126.5, fc='pink', fill=True, alpha=0.4)    
    ax.add_patch(pp2)

    pp3 = mpatches.Wedge(o, r=5, theta1=0,
                                theta2=180, fc='white', fill=True, alpha=1)    
    ax.add_patch(pp3)

    drawSector(ax=ax, center=o, radius=5, theta1=0, theta2=180, fill=False)
    drawSector(ax=ax, center=a_b, radius=4, theta1=36.5, theta2=216.5, fill=False)
    drawSector(ax=ax, center=a_c, radius=3, theta1=-53.5, theta2=126.5, fill=False)
    drawPolygon(ax=ax, verts=[a,b,c])

    pp4 = mpatches.PathPatch(
    Path([(-5,0), (-0.6,1), (a[0],a[1])],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp4)
    
    pp5 = mpatches.PathPatch(
    Path([(-5,0), (0,-1.8), (c[0],c[1])],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp5)

    pp6 = mpatches.PathPatch(
    Path([(a[0],a[1]), (2.4,1), (c[0],c[1])],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
    fc="none", transform=ax.transData,linestyle="--")

    ax.add_patch(pp6)

    ax.text(-1.3,1.2, '${n1}cm$'.format(n1=n1), size = 11)
    ax.text(-0.5,-1.7, '${n2}cm$'.format(n2=n2), size = 11)
    ax.text(0.8,1.8, '${n3}cm$'.format(n3=n3), size = 11)

    ax.text(a[0]-0.25,a[1]+0.4, 'A', size = 15)
    ax.text(b[0]-0.7,b[1]-0.7, 'B', size = 15)
    ax.text(c[0],c[1]-0.7, 'C', size = 15)

    result = answer_dict[1]

    stem = stem.format(ab=ab, bc=bc, ac=ac, n1=n1, n2=n2, n3=n3, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ab=ab, ac=ac, bc=bc, f=f, s1=s1, s2=s2, s3=s3, s4=s4, n1=n1, n3=n3, r1=r1, r2=r2, r3=r3, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg
