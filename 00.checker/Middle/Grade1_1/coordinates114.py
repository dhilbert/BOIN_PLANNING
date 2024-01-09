#from  draw2svg import *
import matplotlib.pyplot as plt
import numpy as np
import random
import fractions
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

    fig, ax = plt.subplots(figsize=(5, 5))

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

def coordinates114_Stem_001():
    stem = "다음 중좌표평면 위의 점 $$수식$$A,``B,``C,``D,``E$$/수식$$의 좌표를 나타낸 것으로 옳지 않은 것은?\n" \
           "① $$수식$$A({x1}, {y1})$$/수식$$\n" \
           "② $$수식$$B({x2}, {y2})$$/수식$$\n" \
           "③ $$수식$$C({x3}, {y3})$$/수식$$\n" \
           "④ $$수식$$D({x4}, {y4})$$/수식$$\n" \
           "⑤ $$수식$$E({x5}, {y5})$$/수식$$\n" 

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.set_xticks([-4,-3,-2,-1,1,2,3,4])
    ax.set_yticks([-4,-3,-2,-1,1,2,3,4])

    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-0.5, 4.6, "y", size = 15)
    plt.text(4.6, -0.5, "x", size = 15)
    plt.text(-0.6,-0.6, "O", size = 12)

    x_list=[random.randint(-4,4),random.randint(-4,4),random.randint(-4,4),random.randint(-4,4),random.randint(-4,4)]
    y_list=[random.randint(-4,4),random.randint(-4,4),random.randint(-4,4),random.randint(-4,4),random.randint(-4,4)]

    plt.scatter(x_list, y_list, c='black', edgecolor='black', s=10)
    plt.text(x_list[0]+0.1, y_list[0]+0.1, "A", size = 14)
    plt.text(x_list[1]+0.1, y_list[1]+0.1, "B", size = 14)
    plt.text(x_list[2]+0.1, y_list[2]+0.1, "C", size = 14)
    plt.text(x_list[3]+0.1, y_list[3]+0.1, "D", size = 14)
    plt.text(x_list[4]+0.1, y_list[4]+0.1, "E", size = 14)

    plt.grid(True)

    idx = random.randint(0,4)
    c1 = x_list[idx]
    c2 = y_list[idx]
    x_list[idx],y_list[idx] = y_list[idx], x_list[idx]

    result = answer_dict[idx]

    ans_list = ['A','B','C','D','E']
    ans = ans_list[idx]

    answer = "(정답)\n {result}" 
    comment = "(해설)\n$$수식$${result} {ans}({c1},{c2})$$/수식$$\n"
    stem = stem.format(x1=x_list[0], x2=x_list[1], x3=x_list[2], x4=x_list[3], x5=x_list[4], y1=y_list[0], y2=y_list[1], y3=y_list[2], y4=y_list[3], y5=y_list[4])
    answer = answer.format(result=result)
    comment = comment.format(result=result, ans=ans, c1=c1, c2=c2)
    svg = saveSvg()
    return stem, answer, comment, svg


def coordinates114_Stem_002():
    stem = "두 수 $$수식$$a, b$$/수식$$에 대하여 $$수식$$|a|={c1}, |b|={c2}$$/수식$$일 때, 순서쌍 $$수식$$(a, b)$$/수식$$를 모두 구하시오.\n" \
           "(    ①    ,    ②    )\n" \
           "(    ③    ,    ④    )\n" \
           "(    ⑤    ,    ⑥    )\n" \
           "(    ⑦    ,    ⑧    )\n" 
    answer = "(정답)\n $$수식$$(-{c1}, -{c2}), (-{c1}, {c2}), ({c1}, -{c2}), ({c1}, {c2})$$/수식$$\n"
    comment = "(해설)\n$$수식$$|a|={c1}$$/수식$$이므로 $$수식$$a=-{c1}$$/수식$$ 또는 $$수식$$a={c1}$$/수식$$\n"\
        "$$수식$$|b|={c2}$$/수식$$이므로 $$수식$$b=-{c2}$$/수식$$ 또는 $$수식$$b={c2}$$/수식$$\n"\
        "따라서 구하는 순서쌍은\n"\
        "$$수식$$(-{c1}, -{c2}), (-{c1}, {c2}), ({c1}, -{c2}), ({c1}, {c2})$$/수식$$ \n"

    c1=random.randint(1, 6)
    c2=random.randint(1, 6)

    stem = stem.format(c1=c1, c2=c2)
    answer = answer.format(c1=c1, c2=c2)
    comment = comment.format(c1=c1, c2=c2)
    
    return stem, answer, comment


def coordinates114_Stem_003():
    stem = "점 $$수식$$(a{op1}{c1},b{op2}{c2})$$/수식$$은 $$수식$$x$$/수식$$축 위의 점이고 점 $$수식$$(a{op3}{c3},b{op4}{c4})$$/수식$$는 $$수식$$y$$/수식$$축 위의 점일 때, 점 $$수식$$(a,b)$$/수식$$는?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n점 $$수식$$(a{op1}{c1},b{op2}{c2})$$/수식$$은 $$수식$$x$$/수식$$축 위의 점이므로\n"\
        "$$수식$$b{op2}{c2}=0``````THEREFORE b={s1}$$/수식$$ \n"\
        "$$수식$$(a{op3}{c3},b{op4}{c4})$$/수식$$은 $$수식$$y$$/수식$$축 위의 점이므로\n"\
        "$$수식$$a{op3}{c3}=0``````THEREFORE a={s2}$$/수식$$ \n"\
        "따라서 구하는 점의 좌표는 $$수식$$({s1},{s2})$$/수식$$이다."

    while True:
      c1=random.randint(1, 6)
      c2=random.randint(1, 6)
      c3=random.randint(1, 6)
      c4=random.randint(1, 6)
      if c2 != c3:
        break

    op_list = ['+', '-']
    op1 = random.choice(op_list)
    op2 = random.choice(op_list)
    op3 = random.choice(op_list)
    op4 = random.choice(op_list)

    if op2 == '+' :
      s1 = -c2
    else :
      s1 = c2

    if op3 == '+' :
      s2 = -c3
    else :
      s2 = c3 

    ab1 = abs(s1)
    ab2 = abs(s2)

    result_list = [(ab1,ab2), (-ab1,ab2), (ab1,-ab2), (-ab1,-ab2), (ab2,ab1)]
    a_list = random.sample(result_list, 5)

    a1, a2, a3, a4, a5 = a_list
    aa = (s1,s2)

    for i in range(0, len(a_list)):
      if a_list[i] == aa:
        result = answer_dict[i]
        break


    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, op1=op1, op2=op2, op3=op3, op4=op4, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, op1=op1, op2=op2, op3=op3, op4=op4, s1=s1, s2=s2)
    return stem, answer, comment


def coordinates114_Stem_004():
    stem = "두 순서쌍 $$수식$$({c1}a{op1}{c2},{c3}b{op2}{c4}), ({c5}a{op3}{c6}, {c7}b{op4}{c8})$$/수식$$가 같을 때, $$수식$$a+b$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$${c1}a{op1}{c2}={c5}a{op3}{c6}$$/수식$$에서\n"\
        "$$수식$${s1}a={s2}``````THEREFORE a={s3}$$/수식$$ \n"\
        "$$수식$${c3}b{op2}{c4}={c7}b{op4}{c8}$$/수식$$에서\n"\
        "$$수식$${s4}b={s5}``````THEREFORE b={s6}$$/수식$$ \n"\
        "$$수식$$THEREFORE a+b={ans}$$/수식$$"

    num_list = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

    while True:
      n1 = random.choice(num_list)
      n2 = random.choice(num_list)
      n3 = random.choice(num_list)
      n4 = random.choice(num_list)
      n5 = random.choice(num_list)
      n6 = random.choice(num_list)
      n7 = random.choice(num_list)
      n8 = random.choice(num_list)
      if n1 != n5 and n2 != n6 and n3 != n7 and n4 != n8 :
        break     

    if n1 == 1 : 
        c1 = ""
    elif n1 == -1 :
        c1 = "-"
    else :
        c1 = n1

    if n3 == 1 : 
        c3 = ""
    elif n3 == -1 :
        c3 = "-"
    else :
        c3 = n3

    if n5 == 1 : 
        c5 = ""
    elif n5 == -1 :
        c5 = "-"
    else :
        c5 = n5

    if n7 == 1 : 
        c7 = ""
    elif n7 == -1 :
        c7 = "-"
    else :
        c7 = n7


    if n2 > 0 :
      op1 = '+'
      c2 = n2
    else :
      op1 = '-'
      c2 = abs(n2)
    
    if n4 > 0 :
      op2 = '+'
      c4 = n4
    else :
      op2 = '-'
      c4 = abs(n4)
    
    if n6 > 0 :
      op3 = '+'
      c6 = n6
    else :
      op3 = '-'
      c6 = abs(n6)

    if n8 > 0 :
      op4 = '+'
      c8 = n8
    else :
      op4 = '-'
      c8 = abs(n8)

    if n1 > n5 :
      if n5 > 0 :
        ss1 = n1 - n5
      else :
        ss1 = n1 + abs(n5)
      if n2 > 0 :
        s2 = n6 - n2
      else : 
        s2 = n6 + abs(n2)
    else :
      if n1 > 0 :
        ss1 = n5 - n1
      else :
        ss1 = n5 + abs(n1)
      if n6 > 0 :
        s2 = n2 - n6
      else :
        s2 = n2 + abs(n6)

    if ss1 == -1 : 
        s1 = "-"
    elif ss1 == 1 :
        s1 = ""
    else :
        s1 = ss1

    if n3 > n7 :
      if n7 > 0 :
        ss4 = n3 - n7
      else :
        ss4 = n3 + abs(n7)
      if n4 > 0 :
        s5 = n8 - n4
      else :
        s5 = n8 + abs(n4)
    else : 
      if n3 > 0 :
        ss4 = n7 - n3
      else :
        ss4 = n7 + abs(n3)
      if n8 > 0 :
        s5 = n4 - n8
      else :
        s5 = n4 + abs(n8)


    if ss4 == -1 : 
        s4 = "-"
    elif ss4 == 1 :
        s4 = ""
    else :
        s4 = ss4


    ss3 = fractions.Fraction(fractions.Fraction(s2)/fractions.Fraction(ss1))
    ss6 = fractions.Fraction(fractions.Fraction(s5)/fractions.Fraction(ss4))

    an = fractions.Fraction(ss3+ss6)

    result_list = [an, fractions.Fraction(an-1), fractions.Fraction(an-2), fractions.Fraction(an+1), fractions.Fraction(an+2)]
    a_list = random.sample(result_list, 5)
    a_list.sort()

    aa1, aa2, aa3, aa4, aa5 = a_list

    if ss3.denominator == 1 :
        s3 = int(ss3)
    else :
        if ss3.numerator < 0 :
            s3 = "-\\frac{"+str(abs(ss3.numerator))+"}{"+str(ss3.denominator)+"}"
        else :
            s3 = "\\frac{"+str(ss3.numerator)+"}{"+str(ss3.denominator)+"}"

    if ss6.denominator == 1 :
        s6 = int(ss6)
    else :
        if ss6.numerator < 0 :
            s6 = "-\\frac{"+str(abs(ss6.numerator))+"}{"+str(ss6.denominator)+"}"
        else :
            s6 = "\\frac{"+str(ss6.numerator)+"}{"+str(ss6.denominator)+"}"

    if an.denominator == 1 :
        ans = int(an)
    else :
        if an.numerator < 0 :
            ans = "-\\frac{"+str(abs(an.numerator))+"}{"+str(an.denominator)+"}"
        else :
            ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    if aa1.denominator == 1 :
        a1 = int(aa1)
    else :
        if aa1.numerator < 0 :
            a1 = "-\\frac{"+str(abs(aa1.numerator))+"}{"+str(aa1.denominator)+"}"
        else :
            a1 = "\\frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"

    if aa2.denominator == 1 :
        a2 = int(aa2)
    else :
        if aa2.numerator < 0 :
            a2 = "-\\frac{"+str(abs(aa2.numerator))+"}{"+str(aa2.denominator)+"}"
        else :
            a2 = "\\frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = int(aa3)
    else :
        if aa3.numerator < 0 :
            a3 = "-\\frac{"+str(abs(aa3.numerator))+"}{"+str(aa3.denominator)+"}"
        else :
            a3 = "\\frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    if aa4.denominator == 1:
        a4 = int(aa4)
    else :
        if aa4.numerator < 0 :
            a4 = "-\\frac{"+str(abs(aa4.numerator))+"}{"+str(aa4.denominator)+"}"
        else :
            a4 = "\\frac{"+str(aa4.numerator)+"}{"+str(aa4.denominator)+"}"

    if aa5.denominator == 1:
        a5 = int(aa5)
    else :
        if aa5.numerator < 0 :
            a5 = "-\\frac{"+str(abs(aa5.numerator))+"}{"+str(aa5.denominator)+"}"
        else :
            a5 = "\\frac{"+str(aa5.numerator)+"}{"+str(aa5.denominator)+"}"

    for i in range(0, len(a_list)):
      if a_list[i] == an:
        result = answer_dict[i]
        break


    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, op1=op1, op2=op2, op3=op3, op4=op4, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, op1=op1, op2=op2, op3=op3, op4=op4, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, ans=ans)

    return stem, answer, comment


def coordinates114_Stem_007():
    sum = random.randint(3,12)
    
    if sum == 3 :
      result = "(1,2), (2,1)"
    elif sum == 4:
      result = "(1,3), (2,2), (3,1)"
    elif sum == 5:
      result = "(1,4), (2,3), (3,2), (4,1)"
    elif sum == 6:
      result = "(1,5), (2,4), (3,3), (4,2), (5,1)"
    elif sum == 7:
      result = "(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)"
    elif sum == 8:
      result = "(2,6), (3,5), (4,4), (5,3), (6,2)"
    elif sum == 9:
      result = "(3,6), (4,5), (5,4), (6,3)"
    elif sum == 10:
      result = "(4,6), (5,5), (6,4)"
    elif sum == 11:
      result = "(5,6), (6,5)"
    else:
        result = "(6,6)"

    stem = "두 개의 주사위 $$수식$$A, B$$/수식$$를 던져서 나온 눈의 수에 대하여 " \
           "(주사위 $$수식$$A$$/수식$$의 눈의 수, 주사위 $$수식$$B$$/수식$$의 눈의 수)로 하는 순서쌍 중에서 " \
           "눈의 수의 합이 $$수식$${sum}$$/수식$$가 되는 순서쌍을 모두 구하시오.\n" 
    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n(주사위 $$수식$$A$$/수식$$의 눈의 수, 주사위 $$수식$$B$$/수식$$의 눈의 수)로 하는\n"\
        "순서쌍 중에서 눈의 수의 합이 $$수식$${sum}$$/수식$$가 되는 경우는 $$수식$${result}$$/수식$$이다.\n"\

    stem = stem.format(sum=sum)
    answer = answer.format(result=result)
    comment = comment.format(sum=sum, result=result)

    return stem, answer, comment


def coordinates114_Stem_009():
    stem = "점 $$수식$$({c1}a{op1}{c2},{c3}a{op2}{c4})$$/수식$$은 $$수식$$x$$/수식$$축 위의 점이고, 점 $$수식$$({c5}b{op3}{c6},{c7}b{op4}{c8})$$/수식$$은 $$수식$$y$$/수식$$축 위의 점일 때,\n" \
           "$$수식$$ab$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n점 $$수식$$({c1}a{op1}{c2},{c3}a{op2}{c4})$$/수식$$은 $$수식$$x$$/수식$$축 위의 점이므로\n"\
        "$$수식$${c3}a{op2}{c4}=0, {s1}a = {s2}``````THEREFORE a={t1}$$/수식$$ \n"\
        "점 $$수식$$({c5}b{op3}{c6},{c7}b{op4}{c8})$$/수식$$은 $$수식$$y$$/수식$$축 위의 점이므로\n"\
        "$$수식$${c5}b{op3}{c6}=0, {s3}b = {s4}``````THEREFORE b={t2}$$/수식$$ \n"\
        "$$수식$$THEREFORE ab={ans}$$/수식$$"

    
    num_list = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

    while True:
      n1 = random.choice(num_list)
      n2 = random.choice(num_list)
      n3 = random.choice(num_list)
      n4 = random.choice(num_list)
      n5 = random.choice(num_list)
      n6 = random.choice(num_list)
      n7 = random.choice(num_list)
      n8 = random.choice(num_list)
      if n1 != n5 and n2 != n6 and n3 != n7 and n4 != n8 :
        break     

    if n1 == 1 : 
        c1 = ""
    elif n1 == -1 :
        c1 = "-"
    else :
        c1 = n1

    if n3 == 1 : 
        c3 = ""
    elif n3 == -1 :
        c3 = "-"
    else :
        c3 = n3

    if n5 == 1 : 
        c5 = ""
    elif n5 == -1 :
        c5 = "-"
    else :
        c5 = n5

    if n7 == 1 : 
        c7 = ""
    elif n7 == -1 :
        c7 = "-"
    else :
        c7 = n7


    if n2 > 0 :
      op1 = '+'
      c2 = n2
    else :
      op1 = '-'
      c2 = abs(n2)
    
    if n4 > 0 :
      op2 = '+'
      c4 = n4
    else :
      op2 = '-'
      c4 = abs(n4)
    
    if n6 > 0 :
      op3 = '+'
      c6 = n6
    else :
      op3 = '-'
      c6 = abs(n6)

    if n8 > 0 :
      op4 = '+'
      c8 = n8
    else :
      op4 = '-'
      c8 = abs(n8)

    if n3 > 0 :
        if n3 == 1 :
            s1 = ""
            ss1 = 1
            s2 = -n4
            ss2 = -n4
        else :
            s1 = n3
            ss1 = n3
            s2 = -n4
            ss2 = -n4
    else :
        if n3 == -1 :
            s1 = ""
            ss1 = 1
            s2 = n4
            ss2 = n4
        else :
            s1 = -n3
            ss1 = -n3
            s2 = n4
            ss2 = n4


    if n5 > 0 :
        if n5 == 1:
            s3 = ""
            ss3 = 1
            s4 = -n6
            ss4 = -n6
        else :
            s3 = n5
            ss3 = n5
            s4 = -n6
            ss4 = -n6
    else :
        if n5 == -1 :
            s3 = ""
            ss3 = 1
            s4 = n6
            ss4 = n6
        else :
            s3 = -n5
            ss3 = -n5
            s4 = n6
            ss4 = n6

    tt1 = fractions.Fraction(fractions.Fraction(ss2)/fractions.Fraction(ss1))
    tt2 = fractions.Fraction(fractions.Fraction(ss4)/fractions.Fraction(ss3))

    an = fractions.Fraction(tt1 * tt2)


    result_list = [an, fractions.Fraction(an-1), fractions.Fraction(an-2), fractions.Fraction(an+1), fractions.Fraction(an+2)]
    a_list = random.sample(result_list, 5)
    a_list.sort()

    aa1, aa2, aa3, aa4, aa5 = a_list

    if tt1.denominator == 1 :
        t1 = int(tt1)
    else :
        if tt1.numerator < 0 :
            t1 = "-\\frac{"+str(abs(tt1.numerator))+"}{"+str(tt1.denominator)+"}"
        else :
            t1 = "\\frac{"+str(tt1.numerator)+"}{"+str(tt1.denominator)+"}"

    if tt2.denominator == 1 :
        t2 = int(tt2)
    else :
        if tt2.numerator < 0 :
            t2 = "-\\frac{"+str(abs(tt2.numerator))+"}{"+str(tt2.denominator)+"}"
        else :
            t2 = "\\frac{"+str(tt2.numerator)+"}{"+str(tt2.denominator)+"}"


    if an.denominator == 1 :
        ans = int(an)
    else :
        if an.numerator < 0 :
            ans = "-\\frac{"+str(abs(an.numerator))+"}{"+str(an.denominator)+"}"
        else :
            ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"


    if aa1.denominator == 1 :
        a1 = int(aa1)
    else :
        if aa1.numerator < 0 :
            a1 = "-\\frac{"+str(abs(aa1.numerator))+"}{"+str(aa1.denominator)+"}"
        else :
            a1 = "\\frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"

    if aa2.denominator == 1 :
        a2 = int(aa2)
    else :
        if aa2.numerator < 0 :
            a2 = "-\\frac{"+str(abs(aa2.numerator))+"}{"+str(aa2.denominator)+"}"
        else :
            a2 = "\\frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = int(aa3)
    else :
        if aa3.numerator < 0 :
            a3 = "-\\frac{"+str(abs(aa3.numerator))+"}{"+str(aa3.denominator)+"}"
        else :
            a3 = "\\frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    if aa4.denominator == 1:
        a4 = int(aa4)
    else :
        if aa4.numerator < 0 :
            a4 = "-\\frac{"+str(abs(aa4.numerator))+"}{"+str(aa4.denominator)+"}"
        else :
            a4 = "\\frac{"+str(aa4.numerator)+"}{"+str(aa4.denominator)+"}"

    if aa5.denominator == 1:
        a5 = int(aa5)
    else :
        if aa5.numerator < 0 :
            a5 = "-\\frac{"+str(abs(aa5.numerator))+"}{"+str(aa5.denominator)+"}"
        else :
            a5 = "\\frac{"+str(aa5.numerator)+"}{"+str(aa5.denominator)+"}"


    for i in range(0, len(a_list)):
      if a_list[i] == an:
        result = answer_dict[i]
        break
  

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, op1=op1, op2=op2, op3=op3, op4=op4, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, op1=op1, op2=op2, op3=op3, op4=op4, s1=s1, s2=s2, s3=s3, s4=s4, t1=t1, t2=t2, ans=ans)

    return stem, answer, comment


def coordinates114_Stem_010():
    stem = "점 $$수식$$A({c1}a,{c2}{op1}{c3}b)$$/수식$$는 $$수식$$x$$/수식$$축 위의 점이고, 점 $$수식$$B({c4}a{op2}{c5},{c6}b)$$/수식$$는 $$수식$$y$$/수식$$축 위의 점일 때, " \
           "두 점 $$수식$$A, B$$/수식$$의 좌표를 각각 구하시오.\n"
    answer = "(정답)\n $$수식$$A({ax},0),``B(0,{by})$$/수식$$\n"
    comment = "(해설)\n점 $$수식$$A$$/수식$$는 $$수식$$x$$/수식$$축 위의 점이므로\n" \
              "$$수식$${c2}{op1}{c3}b=0, {s1}b={s2}``````THEREFORE b={b}$$/수식$$\n" \
              "점 $$수식$$B$$/수식$$는 $$수식$$y$$/수식$$축 위의 점이므로\n" \
              "$$수식$${c4}a{op2}{c5}=0, {s3}a={s4}``````THEREFORE a={a}$$/수식$$\n" \
              "이때 $$수식$$a={a}$$/수식$$이므로 $$수식$${s5}a={s5}\\times{a}={ax}$$/수식$$\n" \
              "$$수식$$THEREFORE A({ax},0)$$/수식$$\n" \
              "$$수식$$b={b}$$/수식$$이므로 $$수식$${c6}b={c6}\\times{b}={by}$$/수식$$\n" \
              "$$수식$$THEREFORE B(0,{by})$$/수식$$"

    num_list = [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]
    while True :
      n1 = random.choice(num_list)
      n2 = random.choice(num_list)
      n3 = random.choice(num_list)
      n4 = random.choice(num_list)
      n5 = random.choice(num_list)
      n6 = random.choice(num_list)
      n7 = random.choice(num_list)
      n8 = random.choice(num_list)
      if n3 != 1 and n3 != -1 and n6 != 1 and n6 != -1 :
        break

    n3 = fractions.Fraction(fractions.Fraction(1)/fractions.Fraction(n3))
    n6 = fractions.Fraction(fractions.Fraction(1)/fractions.Fraction(n6))


    if n1 == 1 : 
        c1 = ""
        s5 = 1
    elif n1 == -1 :
        c1 = "-"
        s5 = -1
    else :
        c1 = n1
        s5 = n1

    if n4 == 1 : 
        c4 = ""
    elif n4 == -1 :
        c4 = "-"
    else :
        c4 = n4

    if n3 > 0 :
      op1 = '+'
    else :
      op1 = ''
 
    if n5 > 0 :
      op2 = '+'
      c5 = n5
    else :
      op2 = '-'
      c5 = abs(n5)


    if n3 > 0 :
      ss1 = n3
      s2 = -n2
    else :
      ss1 = -n3
      s2 = n2

    if n4 > 0 :
      if n4 == 1 :
        s3 = ""
        ss3 = n4
        s4 = -n5
        ss4 = -n5
      else :
        s3 = n4
        ss3 = n4
        s4 = -n5
        ss4 = -n5
    else :
      if n4 == -1 :
        s3 = ""
        ss3 = -n4
        s4 = n5
        ss4 = n5
      else :
        s3 = -n4
        ss3 = -n4
        s4 = n5
        ss4 = n5

    bb = fractions.Fraction(fractions.Fraction(s2)/fractions.Fraction(ss1))
    aa = fractions.Fraction(fractions.Fraction(ss4)/fractions.Fraction(ss3))

    axx = fractions.Fraction(n1*aa)

    byy = fractions.Fraction(n6*bb)

    if ss1.denominator == 1:
        s1 = int(ss1)
    else :
        if ss1.numerator < 0 :
            s1 = "-\\frac{"+str(abs(ss1.numerator))+"}{"+str(ss1.denominator)+"}"
        else :
           s1 = "\\frac{"+str(ss1.numerator)+"}{"+str(ss1.denominator)+"}"

    if n3.denominator == 1:
        c3 = int(n3)
    else :
        if n3.numerator < 0 :
            c3 = "-\\frac{"+str(abs(n3.numerator))+"}{"+str(n3.denominator)+"}"
        else :
           c3 = "\\frac{"+str(n3.numerator)+"}{"+str(n3.denominator)+"}"

    if n6.denominator == 1:
        c6 = int(n6)
    else :
        if n6.numerator < 0 :
            c6 = "-\\frac{"+str(abs(n6.numerator))+"}{"+str(n6.denominator)+"}"
        else :
           c6 = "\\frac{"+str(n6.numerator)+"}{"+str(n6.denominator)+"}"

    if bb.denominator == 1:
        b = int(bb)
    else :
        if bb.numerator < 0 :
            b = "-\\frac{"+str(abs(bb.numerator))+"}{"+str(bb.denominator)+"}"
        else :
            b = "\\frac{"+str(bb.numerator)+"}{"+str(bb.denominator)+"}"

    if aa.denominator == 1:
        a = int(aa)
    else :
        if aa.numerator < 0 :
            a = "-\\frac{"+str(abs(aa.numerator))+"}{"+str(aa.denominator)+"}"
        else :
            a = "\\frac{"+str(aa.numerator)+"}{"+str(aa.denominator)+"}"

    if axx.denominator == 1:
        ax = int(axx)
    else :
        if axx.numerator < 0 :
            ax = "-\\frac{"+str(abs(axx.numerator))+"}{"+str(axx.denominator)+"}"
        else :
            ax = "\\frac{"+str(axx.numerator)+"}{"+str(axx.denominator)+"}"

    if byy.denominator == 1:
        by = int(byy)
    else :
        if byy.numerator < 0 :
            by = "-\\frac{"+str(abs(byy.numerator))+"}{"+str(byy.denominator)+"}"
        else :
            by = "\\frac{"+str(byy.numerator)+"}{"+str(byy.denominator)+"}"
    


    stem = stem.format(c1=c1, c2=n2, c3=c3, c4=c4, c5=c5, c6=c6, op1=op1, op2=op2)
    answer = answer.format(ax=ax, by=by)
    comment = comment.format(c1=c1, c2=n2, c3=c3, c4=c4, c5=c5, c6=c6, op1=op1, op2=op2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, a=a, b=b, ax=ax, by=by)

    return stem, answer, comment



def coordinates114_Stem_011():
    stem = "좌표평면 위의 세 점 $$수식$$A({x1},{y1}),``B({x2},{y2}),``C({x3},{y3})$$/수식$$를 꼭짓점으로 하는 삼각형 $$수식$$ABC$$/수식$$의 넓이는?\n" \
           "① $$수식$$\\{a1}$$/수식$$       ② $$수식$$\\{a2}$$/수식$$       ③ $$수식$$\\{a3}$$/수식$$\n" \
           "④ $$수식$$\\{a4}$$/수식$$       ⑤ $$수식$$\\{a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n세 점$$수식$$A, B, C$$/수식$$를 좌표평면위에 나타내면 그림과 같다.\n" \
              "따라서 삼각형 $$수식$$ABC$$/수식$$의 넓이는\n" \
              "$$수식$$\\{f}\\times{b}\\times{h}=\\{ans}$$/수식$$\n" 

    fig, ax = plt.subplots(figsize=(0,0))
    svg1 = saveSvg()

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-6,6)
    ax.set_ylim(-6,6)
    ax.set_xticks([-4, -2, 2, 4])
    ax.set_yticks([-4, -2, 2, 4])

    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-0.5, 5.5, "y", size = 15)
    plt.text(5.5, -0.5, "x", size = 15)
    plt.text(+0.1,+0.1, "O", size = 12)

    x1 = random.randint(-5,5)
    x2 = random.randint(-5,-1)
    x3 = random.randint(1,5)
    y1 = random.randint(1,5)
    y2 = random.randint(-5,0)
    y3 = y2

    x=[x1,x2,x3,x1]
    y=[y1,y2,y3,y1]

    plt.scatter(x, y, c='black', edgecolor='black', s=7)
    plt.plot(x,y,c="black")
    plt.text(x[0]+0.1, y[0]+0.1, "A", size = 14)
    plt.text(x[1]-0.6, y[1]+0.1, "B", size = 14)
    plt.text(x[2]+0.3, y[2]+0.1, "C", size = 14)



    b = max(x) - min(x)
    h = max(y) - min(y)

    a = b*h*0.5
    an = fractions.Fraction(a)
    
    h2 = h/2
    
    result_list = [fractions.Fraction(an-h2), fractions.Fraction(an+h2), fractions.Fraction(an+h), fractions.Fraction(an-h)]
    a_list = random.sample(result_list, 4)
    a_list.append(an)
    a_list.sort()
    aa1, aa2, aa3, aa4, aa5 = a_list

    if an.denominator == 1 :
        ans = int(an)
    else :
        ans = "frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    if aa1.denominator == 1 :
        a1 = int(aa1)
    else :
        a1 = "frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"

    if aa2.denominator == 1 :
        a2 = int(aa2)
    else :
        a2 = "frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = int(aa3)
    else :
        a3 = "frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    if aa4.denominator == 1:
        a4 = int(aa4)
    else :
        a4 = "frac{"+str(aa4.numerator)+"}{"+str(aa4.denominator)+"}"

    if aa5.denominator == 1:
        a5 = int(aa5)
    else :
        a5 = "frac{"+str(aa5.numerator)+"}{"+str(aa5.denominator)+"}"
        
    
  

    for i in range(0, len(a_list)):
      if a_list[i] == an:
        result = answer_dict[i]
        break

    f = "frac{1}{2}"
  

    stem = stem.format(x1=x1, x2=x2, x3=x3, y1=y1,y2=y2, y3=y3, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, b=b, h=h, ans=ans)
    svg2 = saveSvg()
    
    svg = [svg1, svg2]
    return stem, answer, comment, svg


def coordinates114_Stem_012():
    stem = "좌표평면 위의 네 점 $$수식$$A({x1},{y1}),``B({x2},{y2}),``C({x3},{y3}),``D({x4},{y4})$$/수식$$를 꼭짓점으로 하는 사각형 " \
           "$$수식$$ABCD$$/수식$$의 넓이는?\n" \
           "① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$         ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n네 점$$수식$$A, B, C, D$$/수식$$를 좌표평면 위에 나타내면 그림과 같다.\n" \
              "따라서 삼각형 $$수식$$ABCD$$/수식$$의 넓이는\n" \
              "$$수식$${b}\\times{h}=\\{ans}$$/수식$$\n" 

    fig, ax = plt.subplots(figsize=(0,0))
    svg1 = saveSvg()
    
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-6,6)
    ax.set_ylim(-6,6)
    ax.set_xticks([-4,-2, 2, 4])
    ax.set_yticks([-4,-2, 2, 4])

    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-0.5, 5.5, "y", size = 15)
    plt.text(5.5, -0.5, "x", size = 15)
    plt.text(+0.1,+0.1, "O", size = 12)

    x1 = random.randint(-5,-1)
    x2 = x1
    x3 = random.randint(1,5)
    x4 = x3
    y1 = random.randint(1,5)
    y2 = random.randint(-5,-1)
    y3 = y2
    y4 = y1

    x=[x1,x2,x3,x4,x1]
    y=[y1,y2,y3,y4,y1]

    plt.scatter(x, y, c='black', edgecolor='black', s=7)
    plt.plot(x,y,c="black")
    plt.text(x1-0.4, y1+0.15, "A", size = 14)
    plt.text(x2-0.6, y2-0.1, "B", size = 14)
    plt.text(x3+0.1, y3-0.1, "C", size = 14)
    plt.text(x4+0.1, y4+0.1, "D", size = 14)


    b = max(x) - min(x)
    h = max(y) - min(y)

    ans = b*h
    
    result_list = [ans, ans+h, ans+(2*h), ans+(3*h), ans-h, ans-(2*h), ans+(3*h)]
    result_list.sort()
    idx = random.randint(0,2)

    a_list = []
    
    for i in range(0, 5):
        a_list.append(result_list[idx+i])
   
    a1, a2, a3, a4, a5 = a_list


    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, y1=y1,y2=y2, y3=y3, y4=y4, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(b=b, h=h, ans=ans)
    
    svg2 = saveSvg()
    
    svg = [svg1, svg2]
    return stem, answer, comment, svg


def coordinates114_Stem_013():
    stem = "좌표평면 위의 네 점 $$수식$$A({x1},{y1}),``B({x2},{y2}),``C({x3},{y3}),``D({x4},{y4})$$/수식$$를 꼭짓점으로 하는 사각형 $$수식$$ABCD$$/수식$$의 넓이는?\n" \
           "① $$수식$$\\{a1}$$/수식$$       ② $$수식$$\\{a2}$$/수식$$       ③ $$수식$$\\{a3}$$/수식$$\n" \
           "④ $$수식$$\\{a4}$$/수식$$       ⑤ $$수식$$\\{a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n네 점$$수식$$A, B, C, D$$/수식$$를 좌표평면 위에 나타내면 그림과 같다.\n" \
              "따라서 삼각형 $$수식$$ABCD$$/수식$$의 넓이는\n" \
              "$$수식$$\\{f}\\times({a}+{b})\\times{h}=\\{ans}$$/수식$$\n" 

    fig, ax = plt.subplots(figsize=(0,0))
    svg1 = saveSvg()
    
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-6,6)
    ax.set_ylim(-6,6)
    ax.set_xticks([-4,-2,2,4])
    ax.set_yticks([-4,-2,2,4])

    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-0.5, 5.5, "y", size = 15)
    plt.text(5.5, -0.5, "x", size = 15)
    plt.text(+0.1,+0.1, "O", size = 12)

    x1 = random.randint(-5,-1)
    x2 = random.randint(-5,-1)
    x3 = random.randint(1,5)
    x4 = x3
    y1 = random.randint(1,5)
    y2 = random.randint(-5,-1)
    y3 = y2
    y4 = y1

    x=[x1,x2,x3,x4,x1]
    y=[y1,y2,y3,y4,y1]

    plt.scatter(x, y, c='black', edgecolor='black', s=7)
    plt.plot(x,y,c="black")
    plt.text(x1-0.2, y1+0.2, "A", size = 14)
    plt.text(x2-0.5, y2-0.5, "B", size = 14)
    plt.text(x3+0.1, y3-0.1, "C", size = 14)
    plt.text(x4+0.1, y4+0.1, "D", size = 14)


    a = x4 - x1
    b = x3 - x2
    h = max(y) - min(y)

    an = fractions.Fraction((a+b)*h*0.5)

    result_list = [an, an+h, fractions.Fraction(an+(2*h)), fractions.Fraction(an+(3*h)), fractions.Fraction(an-h), fractions.Fraction(an-(2*h)), fractions.Fraction(an+(3*h))]
    result_list.sort()
    idx = random.randint(0,2)

    a_list = []
    
    for i in range(0, 5):
        a_list.append(result_list[idx+i])
    

    aa1, aa2, aa3, aa4, aa5 = a_list

    if an.denominator == 1 :
        ans = int(an)
    else :
        ans = "frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    if aa1.denominator == 1 :
        a1 = int(aa1)
    else :
        a1 = "frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"

    if aa2.denominator == 1 :
        a2 = int(aa2)
    else :
        a2 = "frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = int(aa3)
    else :
        a3 = "frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    if aa4.denominator == 1:
        a4 = int(aa4)
    else :
        a4 = "frac{"+str(aa4.numerator)+"}{"+str(aa4.denominator)+"}"

    if aa5.denominator == 1:
        a5 = int(aa5)
    else :
        a5 = "frac{"+str(aa5.numerator)+"}{"+str(aa5.denominator)+"}"


    for i in range(0, len(a_list)):
      if a_list[i] == an:
        result = answer_dict[i]
        break
  
    f = "frac{1}{2}"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, y1=y1,y2=y2, y3=y3, y4=y4, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, a=a, b=b, h=h, ans=ans)
    svg2 = saveSvg()
    
    svg = [svg1, svg2]
    return stem, answer, comment, svg


def coordinates114_Stem_014():
    stem = "좌표평면 위의 세 점 $$수식$$A({x1},{y1}),``B({x2},{y2}),``C({x3},{y3})$$/수식$$를 꼭짓점으로 하는 삼각형\n$$수식$$ABC$$/수식$$의 넓이가 $$수식$${area}$$/수식$$일 때, 양수 $$수식$$a$$/수식$$의 값은?\n" \
           "① $$수식$$\\{a1}$$/수식$$       ② $$수식$$\\{a2}$$/수식$$       ③ $$수식$$\\{a3}$$/수식$$\n" \
           "④ $$수식$$\\{a4}$$/수식$$       ⑤ $$수식$$\\{a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n세 점 $$수식$$A, B, C$$/수식$$를 좌표평면 위에 나타내면 그림과 같다.\n" \
              "이때 삼각형 $$수식$$ABC$$/수식$$의 밑변을 선분$$수식$$AC$$/수식$$, 높이를 선분$$수식$$BH$$/수식$$라 하면\n" \
              "(선분 $$수식$$AC$$/수식$$의 길이)$$수식$$=a-({x1})=a+{x1_abs}$$/수식$$" \
              "(선분 $$수식$$BH$$/수식$$의 길이)$$수식$$={y1}-({y2})={bh}$$/수식$$\n" \
              "따라서 삼각형 $$수식$$ABC$$/수식$$의 넓이가 $$수식$$\\{area}$$/수식$$이므로\n" \
              "$$수식$$\\{f}\\times (a+{x1_abs})\\times{bh}={area}, a+{x1_abs}=\\{s1}``````THEREFORE a={ans}$$/수식$$\n"
              
    fig, ax = plt.subplots(figsize=(0,0))
    svg1 = saveSvg()

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-6,6)
    ax.set_ylim(-6,6)
    ax.set_xticks([-4, -2, 2, 4])
    ax.set_yticks([-4, -2, 2, 4])

    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    plt.text(-0.5, 5.5, "y", size = 15)
    plt.text(5.5, -0.5, "x", size = 15)
    plt.text(+0.1,+0.1, "O", size = 12)

    while True :
        x1 = random.randint(-4,-1)
        x2 = random.randint(1,4)
        x3 = random.randint(1,4)
        y1 = random.randint(1,4)
        y2 = random.randint(-4,-1)
        y3 = y1
        if x1 < x2 and x2 < x3 :
            break

    x=[x1,x2,x3,x1]
    y=[y1,y2,y3,y1]

    hx = x2
    hy = y1
    

    plt.scatter(x, y, c='black', edgecolor='black', s=7)
    plt.plot(x,y,c="black")
    plt.plot([x2,hx],[y2,hy], c="black", linewidth = 1)

    plt.text(x[0]+0.1, y[0]+0.1, "A", size = 14)
    plt.text(x[1]+0.1, y[1]+0.1, "B", size = 14)
    plt.text(x[2]+0.1, y[2]+0.1, "C", size = 14)
    plt.text(hx-0.1, hy+0.1, "H", size = 14)

    bh = y1 - y2 
    x1_abs = abs(x1)

    area = fractions.Fraction((x3 - x1) * bh * 0.5)
    s1 = fractions.Fraction(area / (bh * 0.5))
    an = fractions.Fraction(s1 - x1_abs)

    if an <= 3 :
        result_list = [fractions.Fraction(an+1), fractions.Fraction(an+2), fractions.Fraction(an+3), fractions.Fraction(an+4)]
    elif an > 3 and an < 6 :
        result_list = [fractions.Fraction(an-2), fractions.Fraction(an+2), fractions.Fraction(an+4), fractions.Fraction(an+6)]
    elif an >= 6 :
        result_list = [fractions.Fraction(an-4), fractions.Fraction(an-2), fractions.Fraction(an+2), fractions.Fraction(an+4)]
    a_list = random.sample(result_list, 4)
    a_list.append(an)
    a_list.sort()
    aa1, aa2, aa3, aa4, aa5 = a_list

    if an.denominator == 1 :
        ans = int(an)
    else :
        ans = "frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    if aa1.denominator == 1 :
        a1 = int(aa1)
    else :
        a1 = "frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"

    if aa2.denominator == 1 :
        a2 = int(aa2)
    else :
        a2 = "frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = int(aa3)
    else :
        a3 = "frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    if aa4.denominator == 1:
        a4 = int(aa4)
    else :
        a4 = "frac{"+str(aa4.numerator)+"}{"+str(aa4.denominator)+"}"

    if aa5.denominator == 1:
        a5 = int(aa5)
    else :
        a5 = "frac{"+str(aa5.numerator)+"}{"+str(aa5.denominator)+"}"

    if area.denominator == 1:
        area = int(area)
    else :
        area = "frac{"+str(area.numerator)+"}{"+str(area.denominator)+"}"

    if s1.denominator == 1:
        s1 = int(s1)
    else :
        s1 = "frac{"+str(s1.numerator)+"}{"+str(s1.denominator)+"}"
        

    for i in range(0, len(a_list)):
      if a_list[i] == an:
        result = answer_dict[i]
        break

    f = "frac{1}{2}"
 

    stem = stem.format(x1=x1, x2=x2, x3=x3, y1=y1,y2=y2, y3=y3, area=area, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(x1=x1, y1=y1, y2=y2, bh=bh, area=area, f=f, s1=s1, ans=ans, x1_abs=x1_abs)
    svg2 = saveSvg()
    
    svg = [svg1, svg2]
    return stem, answer, comment, svg


def coordinates114_Stem_016():
    stem = "그림과 같이 세 점 $$수식$$A({c1},{c2}),``B({c3},{c4}),``C({c5},{c6})$$/수식$$을 꼭짓점으로 하는\n" \
            "삼각형 $$수식$$ABC$$/수식$$의 넓이를 $$수식$$S$$/수식$$라 할 때, $$수식$${n}S$$/수식$$의 값을 구하시오.\n" \
    
    f = "\\frac{1}{2}"

    while True :
        c1 = random.randint(-5,-1)
        c2 = random.randint(1,3)
        c3 = random.randint(1,3)
        c4 = random.randint(-3,-1)
        c5 = random.randint(1,5)
        c6 = random.randint(1,5)
        if c3 < c5 and c2 != c6 :
            break

    c7 = c1
    c8 = c4
    c9 = c5
    c10 = c4

    s1 = (c6-c10)+(c2-c8)
    s2 = c9-c7
    s3 = c3-c1
    s4 = c2-c8
    s5 = c5-c3
    s6 = c6-c10

    ss7 = fractions.Fraction(fractions.Fraction(s1)*fractions.Fraction(s2)*fractions.Fraction(1/2))
    ss8 = fractions.Fraction(fractions.Fraction(s3)*fractions.Fraction(s4)*fractions.Fraction(1/2))
    ss9 = fractions.Fraction(fractions.Fraction(s5)*fractions.Fraction(s6)*fractions.Fraction(1/2))
    ss10 = fractions.Fraction(ss7-ss8-ss9)

    nn = int(ss10.denominator)

    if nn == 1 :
        n = ''
    else :
        n = nn

    ans = int(ss10 * ss10.denominator)

    if ss7.denominator == 1:
        s7 = int(ss7)
    else :
        if ss7.numerator < 0 :
            s7 = "-\\frac{"+str(abs(ss7.numerator))+"}{"+str(ss7.denominator)+"}"
        else :
            s7 = "\\frac{"+str(ss7.numerator)+"}{"+str(ss7.denominator)+"}"

    if ss8.denominator == 1:
        s8 = int(ss8)
    else :
        if ss8.numerator < 0 :
            s8 = "-\\frac{"+str(abs(ss8.numerator))+"}{"+str(ss8.denominator)+"}"
        else :
            s8 = "\\frac{"+str(ss8.numerator)+"}{"+str(ss8.denominator)+"}"

    if ss9.denominator == 1:
        s9 = int(ss9)
    else :
        if ss9.numerator < 0 :
            s9 = "-\\frac{"+str(abs(ss9.numerator))+"}{"+str(ss9.denominator)+"}"
        else :
            s9 = "\\frac{"+str(ss9.numerator)+"}{"+str(ss9.denominator)+"}"

    if ss10.denominator == 1:
        s10 = int(ss10)
    else :
        if ss10.numerator < 0 :
            s10 = "-\\frac{"+str(abs(ss10.numerator))+"}{"+str(ss10.denominator)+"}"
        else :
            s10 = "\\frac{"+str(ss10.numerator)+"}{"+str(ss10.denominator)+"}"


    x=[c1, c3, c5, c1]
    y=[c2, c4, c6, c2]

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
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
    plt.text(-0.5, 5.5, "y", size = 15)
    plt.text(5.5, -0.5, "x", size = 15)
    plt.text(-0.6,-0.6, "O", size = 12)

    plt.scatter(x, y, c='black', edgecolor='black', s=7)
    plt.plot(x,y,c="black")
    plt.text(c1-0.2, c2+0.3, "A", size = 12)
    plt.text(c3, c4-0.5, "B", size = 12)
    plt.text(c5, c6+0.2, "C", size = 12)

    x2 = [c1,c1,0]
    y2 = [0,c2,c2]
    plt.plot(x2,y2, c="black", linestyle='dotted')

    x3 = [c3,c3,0]
    y3 = [0,c4,c4]
    plt.plot(x3,y3, c="black", linestyle='dotted')

    x4 = [c5,c5,0]
    y4 = [0,c6,c6]
    plt.plot(x4,y4, c="black", linestyle='dotted')

    plt.text(c1-0.2, -0.5, "{c1}".format(c1=c1), size = 15)
    plt.text(0.3, c2, "{c2}".format(c2=c2), size = 15)

    plt.text(c3-0.1, +0.2, "{c3}".format(c3=c3), size = 15)
    plt.text(-0.6, c4, "{c4}".format(c4=c4), size = 15)

    plt.text(c5-0.1, -0.5, "{c5}".format(c5=c5), size = 15)
    plt.text(-0.5, c6, "{c6}".format(c6=c6), size = 15)

    plt.fill_between(x, y, alpha=0.5)



    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n그림과 같이\n" \
              "$$수식$$D({c7},{c8}),``E({c9},{c10})$$/수식$$라\n" \
              "하면 삼각형 $$수식$$ABC$$/수식$$의 넓이는\n" \
              "(사다리꼴 $$수식$$ADEC$$/수식$$의 넓이)" \
              "$$수식$$-$$/수식$$(삼각형 $$수식$$ADB$$/수식$$의 넓이)" \
              "$$수식$$-$$/수식$$(삼각형 $$수식$$BEC$$/수식$$의 넓이)\n" \
              "$$수식$${f}\\times[{{{c6}-({c10})}}+{{{c2}-({c8})}}]\\times{{{c9}-({c7})}}$$/수식$$\n" \
              "$$수식$$-{f}\\times{{{c3}-({c1})}}\\times{{{c2}-({c8})}}$$/수식$$\n" \
              "$$수식$$-{f}\\times({c5}-{c3})\\times{{{c6}-({c10})}}$$/수식$$\n" \
              "$$수식$$={f}\\times{s1}\\times{s2}-{f}\\times{s3}\\times{s4}-{f}\\times{s5}\\times{s6}$$/수식$$\n" \
              "$$수식$$={s7}-{s8}-{s9}={s10}$$/수식$$\n" \
              "따라서 $$수식$$S={s10}$$/수식$$이므로 $$수식$${n}S={ans}$$/수식$$\n"



    result = ans


    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, n=n)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, s1=s1, s2=s2, s3=s3, s4=s4,
                             s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10, n=n, ans=ans, f=f)
    svg = saveSvg()
    return stem, answer, comment, svg  



def coordinates114_Stem_017():

    num_list = [1,2,3,4,2]
    n_list = random.sample(num_list, 5)

    def quadrant_1():
      return (random.randint(1,6),random.randint(1,6))

    def quadrant_2():
      return (random.randint(-5,0),random.randint(1,6))
    
    def quadrant_3():
      return (random.randint(-5,0),random.randint(-5,0))

    def quadrant_4():
      return (random.randint(1,6),random.randint(-5,0))

    c_list = []

    def c_append(num) :
      if num == 1 :
        return quadrant_2()
      elif num == 2 :
        return quadrant_3()
      elif num == 3 :
        return quadrant_4()
      elif num == 4 :
        return quadrant_1()

    for i in range(0, len(n_list)):
      c_list.append(c_append(n_list[i]))
    
    def quadrant(num):
      if num[0] > 0 and num[1] > 0 :
        return 1
      elif num[0] < 0 and num[1] > 0 :
        return 2
      elif num[0] < 0 and num[1] < 0 :
        return 3
      elif num[0] > 0 and num[1] < 0 :
        return 4
      else :
        return 0
    
    while True :
      idx = random.randint(0,4)
      if quadrant(c_list[idx]) != 0 :
        n_list[idx] = quadrant(c_list[idx])
        result = answer_dict[idx]
        break

    q1 = quadrant(c_list[0])
    q2 = quadrant(c_list[1])
    q3 = quadrant(c_list[2])
    q4 = quadrant(c_list[3])
    q5 = quadrant(c_list[4])

    def commentt(n) :
      if n == 1 : 
        return "제$$수식$$1$$/수식$$사분면"
      elif n == 2 : 
        return "제$$수식$$2$$/수식$$사분면"
      elif n == 3 :
        return "제$$수식$$3$$/수식$$사분면"
      elif n == 4 : 
        return "제$$수식$$4$$/수식$$사분면"
      else :
        return "어느 사분면에도 속하지 않는다."
    
    cmt1 = commentt(q1)
    cmt2 = commentt(q2)
    cmt3 = commentt(q3)
    cmt4 = commentt(q4)
    cmt5 = commentt(q5)

    stem = "다음 중 점과 그 점이 속한 사분면이 바르게 짝지어진 것은?\n" \
           "① $$수식$${c1}$$/수식$$ : 제$$수식$${n1}$$/수식$$사분면\n" \
           "② $$수식$${c2}$$/수식$$ : 제$$수식$${n2}$$/수식$$사분면\n" \
           "③ $$수식$${c3}$$/수식$$ : 제$$수식$${n3}$$/수식$$사분면\n" \
           "④ $$수식$${c4}$$/수식$$ : 제$$수식$${n4}$$/수식$$사분면\n" \
           "⑤ $$수식$${c5}$$/수식$$ : 제$$수식$${n5}$$/수식$$사분면\n" 
    answer = "(정답)\n{result}"
    comment = "(해설)\n① {cmt1}\n② {cmt2}\n③ {cmt3}\n"\
              "④ {cmt4}\n⑤ {cmt5}\n"


    stem = stem.format(c1=c_list[0], c2=c_list[1], c3=c_list[2], c4=c_list[3], c5=c_list[4], n1=n_list[0], n2=n_list[1], 
                       n3=n_list[2], n4=n_list[3], n5=n_list[4])
    answer = answer.format(result=result)
    comment = comment.format(cmt1=cmt1, cmt2=cmt2, cmt3=cmt3, cmt4=cmt4, cmt5=cmt5)

    return stem, answer, comment

def coordinates114_Stem_018():
    stem = "다음 중에서 제$$수식$${n}$$/수식$$사분면에 있는 점은 모두 몇 개인가?\n" \
           "$$표$$$$수식$${c1},``{c2},``{c3},``{c4}$$/수식$$\n" \
           "$$수식$${c5},``{c6},``{c7},``{c8}$$/수식$$\n" \
           "$$수식$${c9},``{c10},``{c11},``{c12}$$/수식$$$$/표$$\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n제$$수식$${n}$$/수식$$사분면에 있는 점의 $$수식$$x$$/수식$$ 좌표의 부호는 $$수식$${op1}$$/수식$$, \n"\
              "$$수식$$y$$/수식$$좌표의 부호는 $$수식$${op2}$$/수식$$이다.\n"\
              "따라서 제$$수식$${n}$$/수식$$사분면에 있는 점은\n$$수식$${liststr}$$/수식$$의 $$수식$${count}$$/수식$$개이다.\n"

    n = random.randint(1,4)

    if n == 1 :
      op1 = '+'
      op2 = '+'
    elif n == 2 :
      op1 = '-'
      op2 = '+'
    elif n == 3 :
      op1 = '-'
      op2 = '-'
    elif n == 4 :
      op1 = '-'
      op2 = '-'

    c1 = (random.randint(-10,10),random.randint(-10,10))
    c2 = (random.randint(-10,10),random.randint(-10,10))
    c3 = (random.randint(-10,10),random.randint(-10,10))
    c4 = (random.randint(-10,10),random.randint(-10,10))
    c5 = (random.randint(-10,10),random.randint(-10,10))
    c6 = (random.randint(-10,10),random.randint(-10,10))
    c7 = (random.randint(-10,10),random.randint(-10,10))
    c8 = (random.randint(-10,10),random.randint(-10,10))
    c9 = (random.randint(-10,10),random.randint(-10,10))
    c10 = (random.randint(-10,10),random.randint(-10,10))
    c11 = (random.randint(-10,10),random.randint(-10,10))
    c12 = (random.randint(-10,10),random.randint(-10,10))

    c_list = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]

    def quadrant(num):
      if num[0] > 0 and num[1] > 0 :
        return 1
      elif num[0] < 0 and num[1] > 0 :
        return 2
      elif num[0] < 0 and num[1] < 0 :
        return 3
      elif num[0] > 0 and num[1] < 0 :
        return 4
      else :
        return 0
    
    count = 0

    list = []

    for i in range(0, len(c_list)):
      q = quadrant(c_list[i])
      if q == n :
        list.append(str(c_list[i]))
        count+=1

    liststr = ','.join(list)
    
    if count > 3 :
        a_list = [count-1, count, count+1, count+2, count+3]
    else :
        a_list = [count, count+1, count+2, count+3, count+4]

    a1, a2, a3, a4, a5 = a_list

    for i in range(0, len(a_list)):
      if a_list[i] == count:
        result = answer_dict[i]
        break


    stem = stem.format(n=n, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n=n, op1=op1, op2=op2, liststr=liststr, count=count)

    return stem, answer, comment


def coordinates114_Stem_019():
    stem = "두 순서쌍 $$수식$$({c1}a{op1}{c2},{c3}b{op2}{c4}),``({c5}a{op3}{c6},{c7}b{op4}{c8})$$/수식$$가 같을 때 " \
           "점 $$수식$$(a,b)$$/수식$$는 어느 사분면에 있는가?\n" \
           "① 제$$수식$$1$$/수식$$사분면      ② 제$$수식$$2$$/수식$$사분면      ③ 제$$수식$$3$$/수식$$사분면\n" \
           "④ 제$$수식$$4$$/수식$$사분면      ⑤ 어느 사분면에도 있지 않다.\n"

    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$${c1}a{op1}{c2}={c5}a{op3}{c6}$$/수식$$이므로 $$수식$${s1}a={s2}``````THEREFORE a={r1}$$/수식$$\n " \
              "$$수식$${c3}b{op2}{c4}={c7}b{op4}{c8}$$/수식$$이므로 $$수식$${s3}b={s4}``````THEREFORE b={r2}$$/수식$$\n" \
              "따라서 점 $$수식$$({r1},{r2})$$/수식$$은 제$$수식$${q}$$/수식$$사분면에 있다.\n"

    num_list = [-4, -3, -2, -1, 1, 2, 3, 4]

    while True:
      n1 = random.choice(num_list)
      n2 = random.choice(num_list)
      n3 = random.choice(num_list)
      n4 = random.choice(num_list)
      n5 = random.choice(num_list)
      n6 = random.choice(num_list)
      n7 = random.choice(num_list)
      n8 = random.choice(num_list)
      if n1 != n5 and n2 != n6 and n3 != n7 and n4 != n8 :
        break    

    if n1 == 1 : 
        c1 = ""
    elif n1 == -1 :
        c1 = "-"
    else :
        c1 = n1

    if n3 == 1 : 
        c3 = ""
    elif n3 == -1 :
        c3 = "-"
    else :
        c3 = n3

    if n5 == 1 : 
        c5 = ""
    elif n5 == -1 :
        c5 = "-"
    else :
        c5 = n5

    if n7 == 1 : 
        c7 = ""
    elif n7 == -1 :
        c7 = "-"
    else :
        c7 = n7


    if n2 > 0 :
      op1 = '+'
      c2 = n2
    else :
      op1 = '-'
      c2 = abs(n2)
    
    if n4 > 0 :
      op2 = '+'
      c4 = n4
    else :
      op2 = '-'
      c4 = abs(n4)
    
    if n6 > 0 :
      op3 = '+'
      c6 = n6
    else :
      op3 = '-'
      c6 = abs(n6)

    if n8 > 0 :
      op4 = '+'
      c8 = n8
    else :
      op4 = '-'
      c8 = abs(n8)



    if n1 > n5 :
      if n5 > 0 :
        ss1 = n1 - n5
      else :
        ss1 = n1 + abs(n5)
      if n2 > 0 :
        s2 = n6 - n2
      else : 
        s2 = n6 + abs(n2)
    else :
      if n1 > 0 :
        ss1 = n5 - n1
      else :
        ss1 = n5 + abs(n1)
      if n6 > 0 :
        s2 = n2 - n6
      else :
        s2 = n2 + abs(n6)
    
    if ss1 == -1 : 
        s1 = "-"
    elif ss1 == 1 :
        s1 = ""
    else :
        s1 = ss1
   


    rr1 = fractions.Fraction(fractions.Fraction(s2)/fractions.Fraction(ss1))
    
    if rr1.denominator == 1:
        r1 = int(rr1)
    else :
        if rr1.numerator < 0 :
            r1 = "-\\frac{"+str(abs(rr1.numerator))+"}{"+str(rr1.denominator)+"}"
        else :
            r1 = "\\frac{"+str(rr1.numerator)+"}{"+str(rr1.denominator)+"}"


    if n3 > n7 :
      if n7 > 0 :
        ss3 = n3 - n7
      else :
        ss3 = n3 + abs(n7)
      if n4 > 0 :
        s4 = n8 - n4
      else :
        s4 = n8 + abs(n4)
    else : 
      if n3 > 0 :
        ss3 = n7 - n3
      else :
        ss3 = n7 + abs(n3)
      if n8 > 0 :
        s4 = n4 - n8
      else :
        s4 = n4 + abs(n8)


    if ss3 == -1 : 
        s3 = "-"
    elif ss3 == 1 :
        s3 = ""
    else :
        s3 = ss3     
    


    rr2 = fractions.Fraction(fractions.Fraction(s4)/fractions.Fraction(ss3))
    
    if rr2.denominator == 1:
        r2 = int(rr2)
    else :
        if rr2.numerator < 0 :
            r2 = "-\\frac{"+str(abs(rr2.numerator))+"}{"+str(rr2.denominator)+"}"
        else :
            r2 = "\\frac{"+str(rr2.numerator)+"}{"+str(rr2.denominator)+"}"


    if rr1 > 0 and rr2 > 0 :
      q = 1 
      result = answer_dict[0]
    elif rr1 < 0 and rr2 > 0 :
      q = 2
      result = answer_dict[1]
    elif rr1 < 0 and rr2 < 0 :
      q = 3
      result = answer_dict[2]
    elif rr1 > 0 and rr2 < 0 :
      q = 4
      result = answer_dict[3]

    

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, op1=op1, op2=op2, op3=op3, op4=op4)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, op1=op1, op2=op2, op3=op3, op4=op4, s1=s1, s2=s2, s3=s3, s4=s4, r1=r1, r2=r2, q=q)

    return stem, answer, comment



def coordinates114_Stem_024():
    stem = "점 $$수식$$(a,{c1})$$/수식$$와 $$수식$$y$$/수식$$축에 대하여 대칭인 점의 좌표가 " \
           "$$수식$$({c2},b)$$/수식$$일 때, $$수식$$a-b$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n점 $$수식$$(a,{c1}),({c2},b)$$/수식$$가 $$수식$$y$$/수식$$축에 대하여 대칭이므로\n" \
              "$$수식$$x$$/수식$$좌표는 부호가 반대이고, $$수식$$y$$/수식$$좌표는 같다.\n" \
              "따라서 $$수식$$a={s1},``b={s2}$$/수식$$이므로\n" \
              "$$수식$$a-b={s1}{op}{s3}={s4}$$/수식$$\n"
    
    c1 = random.randint(-4,4)
    c2 = random.randint(-4,4)

    s1 = -c2
    s2 = c1

    if s2 > 0 :
      op = "-"
      s3 = s2
      s4 = s1 - s2
    else :
      op = "+"
      s3 = abs(s2)
      s4 = s1 + abs(s2)

    result_list = [s4-3, s4-2, s4-1, s4, s4+1, s4+2, s4+3]
    idx = random.randint(0,2)

    a_list = []
    
    for i in range(0, 5):
        a_list.append(result_list[idx+i])
   
    a1, a2, a3, a4, a5 = a_list


    for i in range(0, len(a_list)):
      if a_list[i] == s4:
        result = answer_dict[i]
        break
     

    stem = stem.format(c1=c1, c2=c2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, s1=s1, s2=s2, s3=s3, s4=s4, op=op)

    return stem, answer, comment



def coordinates114_Stem_025():
    stem = "다음 중 점 $$수식$$({c1},{c2})$$/수식$$와 $$수식$$x$$/수식$$축에 대하여 대칭인 점의 좌표는?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$x$$/수식$$축에 대하여 대칭인 점은 $$수식$$y$$/수식$$좌표의 부호가 반대이고, \n" \
              "$$수식$$x$$/수식$$좌표는 같으므로 $$수식$${ans}$$/수식$$이다.\n" 
    
    c1 = random.randint(-5,5)
    c2 = random.randint(-5,5)

    ans = (c1,-c2)

    a_list = [(-c1,-c2), (c1,-c2), (-c1,c2), (-c2,-c1), (c2,-c1)]
    a_list.sort()
    a1, a2, a3, a4, a5 = a_list


    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    
    stem = stem.format(c1=c1, c2=c2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(ans=ans)

    return stem, answer, comment


def coordinates114_Stem_026():
    stem = "점 $$수식$$(a,{c1})$$/수식$$와 $$수식$$x$$/수식$$축에 대하여 대칭인 점의 좌표와 " \
           "점 $$수식$$({c2},b)$$/수식$$와 $$수식$$y$$/수식$$축에 대하여 대칭인 점의 좌표가 같을 때, " \
           "$$수식$$a+b$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n점 $$수식$$(a,{c1})$$/수식$$와 $$수식$$x$$/수식$$축에 대하여 대칭인 점의 좌표는\n" \
              "$$수식$$(a,{s1})$$/수식$$\n" \
              "점 $$수식$$({c2},b)$$/수식$$와 $$수식$$y$$/수식$$축에 대하여 대칭인 점의 좌표는\n" \
              "$$수식$$({s2},b)$$/수식$$" \
              "두 점의 좌표가 같으므로\n" \
              "$$수식$$a={s2}, b={s1}``````THEREFORE a+b = {ans}$$/수식$$\n"

    c1 = random.randint(-6,6)
    c2 = random.randint(-6,6)

    s1 = -c1
    s2 = -c2

    ans = s1 + s2

    result_list = [ans-3, ans-2, ans-1, ans, ans+1, ans+2, ans+3]
    idx = random.randint(0,2)

    a_list = []
    
    for i in range(0, 5):
        a_list.append(result_list[idx+i])
   
    a1, a2, a3, a4, a5 = a_list


    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break
    

    stem = stem.format(c1=c1, c2=c2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, s1=s1, s2=s2, ans=ans)

    return stem, answer, comment


def coordinates114_Stem_027():
    stem = "점 $$수식$$A({c1},{c2})$$/수식$$과 $$수식$$x$$/수식$$축에 대하여 대칭인 점을 $$수식$$P$$/수식$$, $$수식$$y$$/수식$$축에 대하여 " \
           "대칭인 점을 $$수식$$Q$$/수식$$, 원점에 대하여 대칭인 점을 $$수식$$R$$/수식$$이라 할 때, " \
           "삼각형 $$수식$$PQR$$/수식$$의 넓이는?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n점 $$수식$$A({c1},{c2})$$/수식$$과 $$수식$$x$$/수식$$축에 대하여 대칭인 점의 좌표는 $$수식$$P({s1},{s2})$$/수식$$\n" \
              "$$수식$$y$$/수식$$축에 대하여 대칭인 점의 좌표는 $$수식$$Q({s3},{s4})$$/수식$$\n" \
              "따라서 세 점 $$수식$$P,Q,R$$/수식$$를 좌표평면 위에 나타내면 그림과 같으므로\n" \
              "(삼각형 $$수식$$PQR$$/수식$$의 넓이)\n" \
              "$$수식$$={f}\\times[{s7}-({s8})]\\times[{s9}-({s10})]$$/수식$$\n" \
              "$$수식$$={f}\\times{b}\\times{h}={ans}$$/수식$$"     

    fig, ax = plt.subplots(figsize=(0,0))
    svg1 = saveSvg()
    
    while True :
      c1 = random.randint(-3,3)
      c2 = random.randint(-3,3)
      if c1 != 0 and c2 != 0 :
        break

    
    s1 = c1
    s2 = -c2

    s3 = -c1
    s4 = c2

    s5 = -c1
    s6 = -c2

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    x=[s1, s3, s5, s1]
    y=[s2, s4, s6, s2]

    ax.set_xlim(-6,6)
    ax.set_ylim(-6,6)
    ax.set_xticks([-max(x), max(x)])
    ax.set_yticks([-max(y), max(y)])

    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-0.5, 5.5, "y", size = 15)
    plt.text(5.5, -0.5, "x", size = 15)
    plt.text(+0.1,+0.1, "O", size = 12)

    plt.scatter(x, y, c='black', edgecolor='black', s=7)
    plt.plot(x,y,c="black")
    plt.text(s1+0.1, s2+0.1, "P", size = 14)
    plt.text(s3+0.1, s4+0.1, "Q", size = 14)
    plt.text(s5+0.1, s6+0.1, "R", size = 14)

    s7 = max(x)
    s8 = min(x)

    s9 = max(y)
    s10 = min(y)

    f = "\\frac{1}{2}"

    b = max(x) - min(x)
    h = max(y) - min(y)

    ans = fractions.Fraction(b * h * 0.5)

    result_list = [ans-4, ans-2, ans, ans+2, ans+4, ans+6, ans+8]

    if ans < 5 :
        idx = 2
    else :
        idx = random.randint(0,2)
    

    a_list = []
    
    for i in range(0, 5):
        a_list.append(result_list[idx+i])
   
    a1, a2, a3, a4, a5 = a_list


    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break


    stem = stem.format(c1=c1, c2=c2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10, f=f, b=b, h=h, ans=ans)
    svg2 = saveSvg()
    
    svg = [svg1, svg2]
    return stem, answer, comment, svg


def coordinates114_Stem_032():
    stem = "정비례 관계 $$수식$$y=ax$$/수식$$의 그래프가 두 점 $$수식$$({c1},{c2}),``({c3},b)$$/수식$$를 지날 때, $$수식$$b$$/수식$$의 값은?\n" \
           "(단, $$수식$$a$$/수식$$는 상수이다.)\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$y=ax$$/수식$$에 $$수식$$x={c1}, y={c2}$$/수식$$를 대입하면\n" \
              "$$수식$${c2}={s1}a``````THEREFORE a={s2}$$/수식$$\n" \
              "따라서 $$수식$$y={s2}x$$/수식$$이므로 $$수식$$x={c3}, y=b$$/수식$$를 대입하면\n" \
              "$$수식$$b={s2}\\times{c3}={ans}$$/수식$$\n"

    while True :
        c1 = random.randint(-5,5)
        c2 = c1 * random.randint(-5,5)
        c3 = random.randint(-5,5)
        if c1 != 0 and c2 != 0 and c3 != 0 :
            break

    s2 = int(c2/c1)
    ans = s2 * c3

    if c1 == 1:
        s1 = ""
    elif c1 == -1 :
        s1 = "-"
    else :
        s1 = c1

    result_list = [ans-6, ans-4, ans-2, ans, ans+2, ans+4, ans+6]
    idx = random.randint(0,2)

    a_list = []
    
    for i in range(0, 5):
        a_list.append(result_list[idx+i])
   
    a1, a2, a3, a4, a5 = a_list


    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    stem = stem.format(c1=c1, c2=c2, c3=c3, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, c3=c3, s1=s1, s2=s2, ans=ans)

    return stem, answer, comment


def coordinates114_Stem_034():
    stem = "다음 중 $$수식$$y$$/수식$$가 $$수식$$x$$/수식$$에 정비례하는 것은?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$y$$/수식$$가 $$수식$$x$$/수식$$에 정비례하는 것은 {result}이다.\n"

    aa1 = "$$수식$$y=-\\frac{x}{"+str(random.randint(2,9))+"}$$/수식$$"
    aa2 = "$$수식$$y=\\frac{"+str(random.randint(2,9))+"}{x}$$/수식$$"
    aa3 = "$$수식$$y=x+"+str(random.randint(1,9))+"$$/수식$$"
    aa4 = "$$수식$$xy="+str(random.randint(8,20))+"$$/수식$$"
    aa5 = "$$수식$$y=\\frac{x}{"+str(random.randint(2,9))+"}+"+str(random.randint(1,9))+"$$/수식$$"

    a_list = [aa1,aa2,aa3,aa4,aa5]
    a_list.sort()

    a1, a2, a3, a4, a5 = a_list
    
    for i in range(0, len(a_list)):
      if a_list[i] == aa1:
        result = answer_dict[i]
        break

    

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(result=result)

    return stem, answer, comment


def coordinates114_Stem_035():
    stem = "$$수식$$y$$/수식$$가 $$수식$$x$$/수식$$에 정비례하고 $$수식$$x={n1}$$/수식$$일 때 $$수식$$y={n2}$$/수식$$이다. " \
           "이때 $$수식$$y$$/수식$$를 $$수식$$x$$/수식$$에 대한 식으로 나타내면?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$y=ax(a\\neq0)$$/수식$$로 놓고 $$수식$$x={n1}, y={n2}$$/수식$$를 대입하면\n" \
              "$$수식$${n2}={s1}a``````THEREFORE a={s2}$$/수식$$\n" \
              "$$수식$$THEREFORE y={s2}x$$/수식$$\n"

    while True :
      n1 = random.randint(-9,9)
      n2 = random.randint(-9,9)
      if n1 != 0 and n2 != 0 and n1 != n2 and abs(n1) != abs(n2) :
        break

    if  n1 == 1 :
      s1 = ""
    elif n1 == -1 :
      s1 = "-"
    else :
      s1 = n1
    
    ss2 = fractions.Fraction(fractions.Fraction(n2)/fractions.Fraction(n1))

    if ss2.denominator == 1:
        s2 = int(ss2)
    elif ss2.denominator == -1:
        s2 = int(ss2)
    else :
        if ss2.numerator < 0 :
            s2 = "-\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"}"
        else :
            s2 = "\\frac{"+str(ss2.numerator)+"}{"+str(ss2.denominator)+"}"


    if ss2.denominator == 1 :
        aa1 = "$$수식$$y=-"+str(abs(ss2.numerator))+"x$$/수식$$"
        aa2 = "$$수식$$y=\\frac{x}{"+str(abs(ss2.numerator))+"}$$/수식$$"
        aa3 = "$$수식$$y=-\\frac{x}{"+str(abs(ss2.numerator))+"}$$/수식$$"
        aa4 = "$$수식$$y="+str(abs(ss2.numerator))+"x$$/수식$$"
        aa5 = "$$수식$$y="+str(n2)+"x$$/수식$$"
    else :
        if ss2.numerator == 1:
            aa1 = "$$수식$$y=-\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"}x$$/수식$$"
            aa2 = "$$수식$$y=-\\frac{x}{"+str(ss2.denominator)+"}$$/수식$$"
            aa3 = "$$수식$$y="+str(abs(ss2.numerator))+"x$$/수식$$"
            aa4 = "$$수식$$y=\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"}x$$/수식$$"
            aa5 = "$$수식$$y=x$$/수식$$"
        else :
            aa1 = "$$수식$$y=-\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"}x$$/수식$$"
            aa2 = "$$수식$$y=-\\frac{x}{"+str(ss2.denominator)+"}$$/수식$$"
            aa3 = "$$수식$$y=\\frac{"+str(ss2.denominator)+"}{"+str(abs(ss2.numerator))+"}x$$/수식$$"
            aa4 = "$$수식$$y=\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"}x$$/수식$$"
            aa5 = "$$수식$$y="+str(n2)+"x$$/수식$$"

                

    a_list = [aa1,aa2,aa3,aa4,aa5]
    a_list.sort()

    a1, a2, a3, a4, a5 = a_list

    if ss2 < 0 :
      ans = aa1
    else : 
      ans = aa4
    
    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break
    
  

    stem = stem.format(n1=n1, n2=n2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, s1=s1, s2=s2)

    return stem, answer, comment



def coordinates114_Stem_041():
    stem = "정비례 관계 $$수식$$y=ax$$/수식$$의 그래프가 두 점 $$수식$$({c1},{c2})$$/수식$$, $$수식$$(b,{c3})$$/수식$$를\n지날 때 $$수식$${t}a+b$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$y=ax$$/수식$$ $$수식$$x={c1}, y={c2}$$/수식$$를 대입하면\n" \
              "$$수식$${c2}={s1}a``````THEREFORE a={s2}$$/수식$$\n" \
              "즉, $$수식$$y={s1}x$$/수식$$이므로 이 식에 $$수식$$x=b, y={c3}$$/수식$$를 대입하면\n" \
              "$$수식$${c3}={s2}b``````THEREFORE b={s3}$$/수식$$\n" \
              "$$수식$$THEREFORE {t}a+b={t}\\times{s4}+{s5}={ans}$$/수식$$\n"

    num_list = [-4, -3, -2, -1, 1, 2, 3, 4]

    c1 = random.choice(num_list)
    c2 = random.choice(num_list)
    c3 = random.choice(num_list)
    
    if  c1 == 1 :
      s1 = ""
    elif c1 == -1 :
      s1 = "-"
    else :
      s1 = c1
    
    ss2 = fractions.Fraction(fractions.Fraction(c2)/fractions.Fraction(c1))

    if ss2.denominator == 1:
        s2 = int(ss2)
    elif ss2.denominator == -1:
        s2 = int(ss2)
    else :
        if ss2.numerator < 0 :
            s2 = "-\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"}"
        else :
            s2 = "\\frac{"+str(ss2.numerator)+"}{"+str(ss2.denominator)+"}"

    
    ss3 = fractions.Fraction(fractions.Fraction(c3)/ss2)

    if ss3.denominator == 1:
        s3 = int(ss3)
    elif ss3.denominator == -1:
        s3 = int(ss3)
    else :
        if ss3.numerator < 0 :
            s3 = "-\\frac{"+str(abs(ss3.numerator))+"}{"+str(ss3.denominator)+"}"
        else :
            s3 = "\\frac{"+str(ss3.numerator)+"}{"+str(ss3.denominator)+"}"


    if ss2.denominator == 1:
        s4 = int(ss2)
    elif ss2.denominator == -1:
        s4 = int(ss2)
    else :
        if ss2.numerator < 0 :
            s4 = "(-\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"})"
        else :
            s4 = "\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"}"


    if ss3.denominator == 1:
        s5 = int(ss3)
    elif ss3.denominator == -1:
        s5 = int(ss3)
    else :
        if ss3.numerator < 0 :
            s5 = "(-\\frac{"+str(abs(ss3.numerator))+"}{"+str(ss3.denominator)+"})"
        else :
            s5 = "\\frac{"+str(abs(ss3.numerator))+"}{"+str(ss3.denominator)+"}"



    tt = ss2.denominator
    t_list = [2,3,4]

    t = tt * random.choice(t_list)

    ans = t * ss2 + ss3 
    ans = int(ans)

    

    result_list = [ans-3, ans-2, ans-1, ans, ans+1, ans+2, ans+3]
    idx = random.randint(0,2)

    a_list = []
    
    for i in range(0, 5):
        a_list.append(result_list[idx+i])
   
    a1, a2, a3, a4, a5 = a_list


    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break
    

    

    stem = stem.format(c1=c1, c2=c2, c3=c3, t=t, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, c3=c3, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, t=t, ans=ans)

    return stem, answer, comment


def coordinates114_Stem_043():
    stem = "두 정비례 관계 $$수식$$y={a}x$$/수식$$, $$수식$$y={b}x$$/수식$$의 그래프는 그림과 같고 " \
           "한 변의 길이가 $$수식$${n}$$/수식$$인 정사각형 $$수식$$ABCD$$/수식$$와 각각 점 $$수식$$A, C$$/수식$$에서 만난다.\n" \
           "이때 점 $$수식$$D$$/수식$$의 좌표를 구하시오.(단, 두 점 $$수식$$A, B$$/수식$$의 $$수식$$x$$/수식$$좌표는 같다.)\n" \

    while True :          
      n1 = random.randint(2,5)
      n2 = random.randint(2,5)
      if n1 != n2 and n1 > n2 :
        break


    aa = fractions.Fraction(fractions.Fraction(n1)/fractions.Fraction(n2))
    bb = fractions.Fraction(fractions.Fraction(n2)/fractions.Fraction(n1))

    n = int((aa * n2) - (bb * n1))
    lcm = n1 * n2

    s1 = n1 * n1
    s2 = n * lcm
    s3 = n2 * n2
    s4 = s1 - s3
    s5 = (s3 * n) + s2
    ss6 = fractions.Fraction(fractions.Fraction(s5)/fractions.Fraction(s4))

    xx = fractions.Fraction(ss6+fractions.Fraction(n))
    yy = fractions.Fraction(fractions.Fraction(aa*ss6))


    if xx.denominator == 1:
        x = int(xx)
    else :
        if xx.numerator < 0 :
            x = "-\\frac{"+str(abs(xx.numerator))+"}{"+str(xx.denominator)+"}"
        else :
            x = "\\frac{"+str(xx.numerator)+"}{"+str(xx.denominator)+"}"

    if yy.denominator == 1:
        y = int(yy)
    else :
        if yy.numerator < 0 :
            y = "-\\frac{"+str(abs(yy.numerator))+"}{"+str(yy.denominator)+"}"
        else :
            y = "\\frac{"+str(yy.numerator)+"}{"+str(yy.denominator)+"}"

    if ss6.denominator == 1:
        s6 = int(ss6)
    else :
        if ss6.numerator < 0 :
            s6 = "-\\frac{"+str(abs(ss6.numerator))+"}{"+str(ss6.denominator)+"}"
        else :
            s6 = "\\frac{"+str(ss6.numerator)+"}{"+str(ss6.denominator)+"}"

       
    if aa.denominator == 1:
        a = int(aa)
    else :
        if aa.numerator < 0 :
            a = "-\\frac{"+str(abs(aa.numerator))+"}{"+str(aa.denominator)+"}"
        else :
            a = "\\frac{"+str(aa.numerator)+"}{"+str(aa.denominator)+"}"
    
    if bb.denominator == 1:
        b = int(bb)
    else :
        if bb.numerator < 0 :
            b = "-\\frac{"+str(abs(bb.numerator))+"}{"+str(bb.denominator)+"}"
        else :
            b = "\\frac{"+str(bb.numerator)+"}{"+str(bb.denominator)+"}"

    result = "({x},{y})".format(x=x, y=y)

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-8,8)
    ax.set_ylim(-8,8)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-0.5, 7.3, "y", size = 15)
    plt.text(7.3, -0.5, "x", size = 15)
    plt.text(0.1, 0.1, "O", size = 12)

    x = np.linspace(-6, 6, 10)
    y = aa*x
    plt.plot(x,y,'k',c="black")

    x2 = np.linspace(-6, 6, 10)
    y2 = bb*x
    plt.plot(x2,y2,'k',c="black")

    x3 = [n2, n1, n1, n2, n2]
    y3 = [bb*n1, bb*n1, aa*n2, aa*n2, bb*n1]
    plt.plot(x3,y3,'k',c="black", linewidth = 0.7)
      
    plt.text(n2-0.4, aa*n2+0.3, "A", size = 15)
    plt.text(n2-0.6, bb*n1-0.6, "B", size = 15)
    plt.text(n1+0.2, bb*n1-0.6, "C", size = 15)
    plt.text(n1+0.2, aa*n2+0.2, "D", size = 15)

    if aa.denominator == 1:
        f1 = "$y={aa}x$".format(aa=aa)
    else :
        f1 = "$y=-\\frac{"+str(abs(aa.numerator))+"}{"+str(aa.denominator)+"}x$"
    f2 = "$y=-\\frac{"+str(abs(bb.numerator))+"}{"+str(bb.denominator)+"}x$"

    plt.text(5, 6, '{f1}'.format(f1=f1), size = 15)
    plt.text(6, 2, '{f2}'.format(f2=f2), size = 15)

    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n점 $$수식$$A$$/수식$$의 $$수식$$x$$/수식$$좌표를 $$수식$$a$$/수식$$라 하면 점 $$수식$$A$$/수식$$는 $$수식$$y={a}x$$/수식$$의 그래프 위의 점이므로\n" \
              "점 $$수식$$A$$/수식$$의 $$수식$$y$$/수식$$좌표는 $$수식$${a}a$$/수식$$ $$수식$$THEREFORE (a,{a}a)$$/수식$$\n" \
              "(선분 $$수식$$AB$$/수식$$의 길이)$$수식$$={n}$$/수식$$에서 점 $$수식$$B$$/수식$$의 $$수식$$y$$/수식$$좌표는\n" \
              "$$수식$${a}a-{n}$$/수식$$ 이므로 $$수식$$B(a,{a}a-{n})$$/수식$$\n" \
              "(선분 $$수식$$BC$$/수식$$의 길이)$$수식$$={n}$$/수식$$에서 점 $$수식$$C$$/수식$$의 $$수식$$x$$/수식$$좌표는\n" \
              "$$수식$$a+{n}$$/수식$$ 이므로 $$수식$$C(a+{n},{a}a-{n})$$/수식$$\n" \
              "또, $$수식$$D(a+{n},{a}a)$$/수식$$\n" \
              "이때 점 $$수식$$C$$/수식$$는 $$수식$$y={b}x$$/수식$$의 그래프 위의 점이므로\n" \
              "$$수식$$y={b}x$$/수식$$에 $$수식$$x=a+{n}, y={a}a-{n}$$/수식$$을 대입하면\n" \
              "$$수식$${a}a-{n}={b}(a+{n})$$/수식$$" \
              "양변에 $$수식$${lcm}$$/수식$$을 곱하면\n" \
              "$$수식$${s1}a-{s2}={s3}(a+{n})$$/수식$$\n" \
              "$$수식$${s4}a={s5} ``````THEREFORE a={s6}$$/수식$$\n" \
              "따라서 점 $$수식$$D$$/수식$$의 좌표는 $$수식$$D{result}$$/수식$$\n"
    
    stem = stem.format(a=a, b=b, n=n)
    answer = answer.format(result=result)
    comment = comment.format(a=a, b=b, n=n, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, lcm=lcm, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg  


def coordinates114_Stem_045():
    stem = "그래프가 나타내는 식은?\n" \
           "① {a1}       ② {a2}         ③ {a3}\n" \
           "④ {a4}       ⑤ {a5}\n"

    while True :
      c_list = [-5, -4, -3, -2, 2, 3, 4, 5]
      c1 = random.choice(c_list)
      c2 = random.choice(c_list)
      if abs(c1) != abs(c2) :
        break

    aa = fractions.Fraction(fractions.Fraction(c2)/fractions.Fraction(c1))

    if c1 == 1 :
      s1 = ''
    elif c1 == -1 :
      s1 = '-'
    else :
      s1 = c1

    if aa.denominator == 1:
        a = int(aa)
    elif aa.denominator == -1:
        a = int(aa)
    else :
        if aa.numerator < 0 :
            a = "-\\frac{"+str(abs(aa.numerator))+"}{"+str(aa.denominator)+"}"
        else :
            a = "\\frac{"+str(aa.numerator)+"}{"+str(aa.denominator)+"}"


    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-7,7)
    ax.set_ylim(-7,7)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-0.5, 6.2, "y", size = 15)
    plt.text(6.2, -0.5, "x", size = 15)
    plt.text(0.1, 0.1, "O", size = 12)

    x = np.linspace(-5, 5, 10)
    y = aa*x
    plt.plot(x,y,'k',c="black")

    x2 = [c1,c1,0]
    y2 = [0,c2,c2]
    plt.plot(x2,y2,c="black", linestyle='dotted')

    plt.text(c1, -0.5, "{c1}".format(c1=c1), size = 15)
    plt.text(-0.5, c2, "{c2}".format(c2=c2), size = 15)
    
    f1 = "-\\frac{"+str(abs(aa.numerator))+"}{"+str(aa.denominator)+"}"
    f2 = "\\frac{"+str(abs(aa.numerator))+"}{"+str(aa.denominator)+"}"
    f3 = "-\\frac{"+str(aa.denominator)+"}{"+str(abs(aa.numerator))+"}"
    f4 = "\\frac{"+str(aa.denominator)+"}{"+str(abs(aa.numerator))+"}"

    aa1 = "$$수식$$y={c1}x$$/수식$$".format(c1=c1)
    aa2 = "$$수식$$y={f1}x$$/수식$$".format(f1=f1)
    aa3 = "$$수식$$y={f2}x$$/수식$$".format(f2=f2)
    aa4 = "$$수식$$y={f3}x$$/수식$$".format(f3=f3)
    aa5 = "$$수식$$y={f4}x$$/수식$$".format(f4=f4)

    a_list = [aa1,aa2,aa3,aa4,aa5]
    a_list.sort()

    a1, a2, a3, a4, a5 = a_list

    if aa.numerator < 0 :
      ans = aa2
    else :
      ans = aa3

    for i in range(0, len(a_list)):
      if a_list[i] == ans:
        result = answer_dict[i]
        break

    answer = "(정답)\n{result}"
    comment = "(해설)\n그래프가 원점과 점 $$수식$$({c1},{c2})$$/수식$$을 지나는 직선이므로\n" \
              "$$수식$$y=ax(a\\neq0)$$/수식$$라 하고 $$수식$$x={c1}, y={c2}$$/수식$$를 대입하면\n" \
              "$$수식$${c2}={s1}a``````THEREFOREa={a}$$/수식$$\n" \
              "$$수식$$THEREFORE y={a}x$$/수식$$"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(c1=c1, c2=c2, s1=s1, a=a)
    svg = saveSvg()
    return stem, answer, comment, svg  



def coordinates114_Stem_047():
    stem = "다음 그림과 같이 정비례 관계 $$수식$$y={a}x$$/수식$$의 그래프 위의 한 점 $$수식$$P$$/수식$$에서 " \
           "$$수식$$y$$/수식$$축에 수직인 직선을 그었을 때, $$수식$$y$$/수식$$축과 만나는 점을 $$수식$$Q$$/수식$$라 하자. " \
           "점 $$수식$$Q$$/수식$$의 좌표가 $$수식$$(0,{c1})$$/수식$$일 때, 삼각형 $$수식$$POQ$$/수식$$의 넓이는?\n" \
           "① $$수식$${a1}$$/수식$$      ② $$수식$${a2}$$/수식$$        ③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$      ⑤ $$수식$${a5}$$/수식$$\n"

    a = random.randint(2,5)
    c1 = random.randint(2,5)

    ss1 = fractions.Fraction(fractions.Fraction(c1)/fractions.Fraction(a))

    if ss1.denominator == 1:
        s1 = int(ss1)
    elif ss1.denominator == -1:
        s1 = int(ss1)
    else :
        if ss1.numerator < 0 :
            s1 = "-\\frac{"+str(abs(ss1.numerator))+"}{"+str(ss1.denominator)+"}"
        else :
            s1 = "\\frac{"+str(ss1.numerator)+"}{"+str(ss1.denominator)+"}"

    
    an = fractions.Fraction(fractions.Fraction(1/2)*ss1*fractions.Fraction(c1))

    if an.denominator == 1:
        ans = int(an)
    elif an.denominator == -1:
        ans = int(an)
    else :
        if an.numerator < 0 :
            ans = "-\\frac{"+str(abs(an.numerator))+"}{"+str(an.denominator)+"}"
        else :
            ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"


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
    
    f = "\\frac{1}{2}"

    if aa1.denominator == 1 :
        a1 = int(aa1)
    else :
        if aa1.numerator < 0 :
            a1 = "-\\frac{"+str(abs(aa1.numerator))+"}{"+str(aa1.denominator)+"}"
        else :
            a1 = "\\frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"

    if aa2.denominator == 1 :
        a2 = int(aa2)
    else :
        if aa2.numerator < 0 :
            a2 = "-\\frac{"+str(abs(aa2.numerator))+"}{"+str(aa2.denominator)+"}"
        else :
            a2 = "\\frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = int(aa3)
    else :
        if aa3.numerator < 0 :
            a3 = "-\\frac{"+str(abs(aa3.numerator))+"}{"+str(aa3.denominator)+"}"
        else :
            a3 = "\\frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    if aa4.denominator == 1:
        a4 = int(aa4)
    else :
        if aa4.numerator < 0 :
            a4 = "-\\frac{"+str(abs(aa4.numerator))+"}{"+str(aa4.denominator)+"}"
        else :
            a4 = "\\frac{"+str(aa4.numerator)+"}{"+str(aa4.denominator)+"}"

    if aa5.denominator == 1:
        a5 = int(aa5)
    else :
        if aa5.numerator < 0 :
            a5 = "-\\frac{"+str(abs(aa5.numerator))+"}{"+str(aa5.denominator)+"}"
        else :
            a5 = "\\frac{"+str(aa5.numerator)+"}{"+str(aa5.denominator)+"}"


    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
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
    plt.text(-0.5, 5.5, "y", size = 15)
    plt.text(5.5, -0.5, "x", size = 15)
    plt.text(+0.1,+0.1, "O", size = 12)

    x = np.linspace(-5, 5, 10)
    y = a*x
    plt.plot(x,y,'k',c="black")

    x2 = [c1/a, 0]
    y2 = [c1,c1]
    plt.plot(x2,y2,c="black", linestyle='dotted')

    plt.text(c1/a+0.3, c1, "P", size = 12)
    plt.text(-0.5, c1, "Q", size = 12)
    plt.text(5/a+1, 5, "y={a}x".format(a=a), size = 15)

    x3 = [0, c1/a, 0]
    y3 = [0, c1, c1]
    plt.fill_between(x3, y3, alpha=0.5)


    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$Q(0,{c1})$$/수식$$이므로 점 $$수식$$P$$/수식$$의 $$수식$$y$$/수식$$좌표는 $$수식$${c1}$$/수식$$이다.\n" \
              "$$수식$$y={a}x$$/수식$$에 $$수식$$y={c1}$$/수식$$을 대입하면\n" \
              "$$수식$${c1}={a}x``````THEREFORE x={s1}$$/수식$$\n" \
              "따라서 $$수식$$P({s1},{c1})$$/수식$$이므로\n" \
              "(삼각형 $$수식$$POQ$$/수식$$의 넓이)$$수식$$={f}\\times{c1}\\times{s1}={ans}$$/수식$$"


    stem = stem.format(a=a, c1=c1, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f=f, a=a, c1=c1, s1=s1, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg  



def coordinates114_Stem_050():
    stem = "$$수식$${n1}``rm L$$/수식$$의 연료로 $$수식$${n2}``rm {{km}}$$/수식$$를 달리는 하이브리드 자동차가 있다. " \
            "이 자동차가 $$수식$$x``rm L$$/수식$$의 연료로 달릴 수 있는 거리를 $$수식$$y``rm {{km}}$$/수식$$라 할 때, " \
            "$$수식$$x$$/수식$$와 $$수식$$y$$/수식$$ 사이의 관계식을 $$수식$$y=ax$$/수식$$, $$수식$${n3}``rm {{km}}$$/수식$$를 달릴 때 필요한 연료를 " \
            "$$수식$$b``rm L$$/수식$$라 할 때, $$수식$$a+b$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$         ② $$수식$${a2}$$/수식$$            ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$         ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$${n1}``rm L$$/수식$$의 연료로 $$수식$${n2}`` rm {{km}}$$/수식$$를 달릴 수 있으므로 $$수식$$1``rm L$$/수식$$의\n" \
              "연료로 $$수식$${s1}`` rm {{km}}$$/수식$$를 달릴 수 있다.\n" \
              "즉, $$수식$$x``rm L$$/수식$$의 연료로 $$수식$$y`` rm {{km}}$$/수식$$를 달릴 수 있으므로\n" \
              "$$수식$$y={s1}x``````THEREFORE a={s1}$$/수식$$\n" \
              "$$수식$${n3}`` rm {{km}}$$/수식$$를 달릴 때 필요한 연료가 $$수식$$b``rm L$$/수식$$이므로\n" \
              "$$수식$${n3}={s1}\\times b``````THEREFORE b={s2}$$/수식$$\n" \
              "$$수식$$THEREFORE a+b={s1}+{s2}={ans}$$/수식$$"
    

    n1 = random.randint(2,5)
    s1 = random.randint(18,24)
    n2 = n1 * s1

    s2 = random.randint(18,24)
    n3 = s1 * s2
    ans = s1 + s2

  
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


    stem = stem.format(n1=n1, n2=n2, n3=n3, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, ans=ans)

    return stem, answer, comment



def coordinates114_Stem_051():
    stem = "그림은 두 정비례 관계 $$수식$$y=ax, y=bx$$/수식$$의 그래프이다. " \
            "상수 $$수식$$a, b$$/수식$$에 대하여 $$수식$$ab$$/수식$$의값을 구하시오.\n" \

    while True :
        c1 = random.randint(-5,-1)
        c2 = random.randint(1,5)
        c3 = random.randint(1,5)
        c4 = random.randint(1,5)
        if c2 != c4 :
            break


    if c1 == -1 :
      s1 = '-'
    else :
      s1 = c1

    ss2 = fractions.Fraction(fractions.Fraction(c2)/fractions.Fraction(c1))

    if c3 == 1 :
      s3 = ''
    else :
      s3 = c3

    ss4 = fractions.Fraction(fractions.Fraction(c4)/fractions.Fraction(c3))

    an = fractions.Fraction(ss2*ss4)

    if ss2.denominator == 1:
        s2 = int(ss2)
    elif ss2.denominator == -1:
        s2 = int(ss2)
    else :
        if ss2.numerator < 0 :
            s2 = "-\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"}"
        else :
            s2 = "\\frac{"+str(ss2.numerator)+"}{"+str(ss2.denominator)+"}"

    if ss4.denominator == 1:
        s4 = int(ss4)
    elif ss4.denominator == -1:
        s4 = int(ss4)
    else :
        if ss4.numerator < 0 :
            s4 = "-\\frac{"+str(abs(ss4.numerator))+"}{"+str(ss4.denominator)+"}"
        else :
            s4 = "\\frac{"+str(ss4.numerator)+"}{"+str(ss4.denominator)+"}"

    if an.denominator == 1:
        ans = int(an)
    elif an.denominator == -1:
        ans = int(an)
    else :
        if an.numerator < 0 :
            ans = "-\\frac{"+str(abs(an.numerator))+"}{"+str(an.denominator)+"}"
        else :
            ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"


    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-7,7)
    ax.set_ylim(-7,7)
    ax.set_xticks([c1, c3])
    ax.set_yticks([c2, c4])

    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-0.5, 6.3, "y", size = 15)
    plt.text(6.3, -0.5, "x", size = 15)
    plt.text(+0.1,+0.1, "O", size = 12)

    x = np.linspace(-5.5, 5.5, 100)
    y = ss2*x
    plt.plot(x,y,'k',c="black")

    x2 = np.linspace(-5.5, 5.5, 100)
    y2 = ss4*x2
    plt.plot(x2,y2,'k',c="black")

    x3 = [c1,c1,0]
    y3 = [0,c2,c2]
    plt.plot(x3,y3,c="black", linestyle='dotted')

    x4 = [c3,c3,0]
    y4 = [0,c4,c4]
    plt.plot(x4,y4,c="black", linestyle='dotted')

    plt.text(-5.5-0.3,(-5.5*ss2)+0.3, "y=ax", size = 15)
    plt.text(5.5+0.3, (5.5*ss4)+0.3, "y=bx", size = 15)



    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n$$수식$$y=ax$$/수식$$에 $$수식$$x={c1},``y={c2}$$/수식$$를 대입하면\n" \
              "$$수식$${c2}={s1}a``````THEREFORE a={s2}$$/수식$$\n" \
              "$$수식$$y=bx$$/수식$$에 $$수식$$x={c3}, y={c4}$$/수식$$를 대입하면\n" \
              "$$수식$${c4}={s3}b``````THEREFORE b={s4}$$/수식$$\n" \
              "$$수식$$THEREFORE ab={ans}$$/수식$$\n"

     
    answer = answer.format(result=ans)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, s1=s1, s2=s2, s3=s3, s4=s4, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def coordinates114_Stem_052():
    stem = "그림과 같이 정비례 관계 $$수식$$y={a}x$$/수식$$의 그래프 위의 점 $$수식$$A$$/수식$$와 " \
            "정비례관계 $$수식$$y={b}x$$/수식$$의 그래프위의 점 $$수식$$B$$/수식$$에서 $$수식$$x$$/수식$$축에 수직인 " \
            "직선을 그었을 때, $$수식$$x$$/수식$$축과 만나는 점을 각각 $$수식$$C,``D$$/수식$$라 하자. " \
            "선분 $$수식$$AB$$/수식$$의 길이가 $$수식$${n}$$/수식$$일 때, 직사각형 $$수식$$ACDB$$/수식$$의 넓이는?\n" \
            "① $$수식$${a1}$$/수식$$         ② $$수식$${a2}$$/수식$$            ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$         ⑤ $$수식$${a5}$$/수식$$\n"

    while True :
        n1 = random.randint(-6,-1)
        n2 = random.randint(3,5)
        n3 = random.randint(1,6)
        n4 = n2
        if abs(n1) != abs(n2) and n3 != n4 :
            break


    n = n3-n1

    aa = fractions.Fraction(fractions.Fraction(n2)/fractions.Fraction(n1))

    if aa.denominator == 1:
        a = int(aa)
    else :
        a = "-\\frac{"+str(abs(aa.numerator))+"}{"+str(aa.denominator)+"}"

    bb = fractions.Fraction(fractions.Fraction(n4)/fractions.Fraction(n3))

    if bb.denominator == 1:
        b = int(bb)
    else :
        b = "\\frac{"+str(bb.numerator)+"}{"+str(bb.denominator)+"}"

    ss1 = fractions.Fraction(fractions.Fraction(1)/fractions.Fraction(aa))
    ss2 = fractions.Fraction(fractions.Fraction(1)/fractions.Fraction(bb))

    if ss1.denominator == 1 :
        s1 = int(ss1)
    else :
        if ss1.numerator < 0 :
            s1 = "-\\frac{"+str(abs(ss1.numerator))+"}{"+str(ss1.denominator)+"}"
        else :
            s1 = "\\frac{"+str(ss1.numerator)+"}{"+str(ss1.denominator)+"}"

    if ss2.denominator == 1 :
        s2 = int(ss2)
    else :
        if ss2.numerator < 0 :
            s2 = "-\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"}"
        else :
            s2 = "\\frac{"+str(ss2.numerator)+"}{"+str(ss2.denominator)+"}"
              
    ss3 = fractions.Fraction(ss2-ss1)

    if ss3.denominator == 1 :
        s3 = int(ss3)
    else :
        if ss3.numerator < 0 :
            s3 = "-\\frac{"+str(abs(ss3.numerator))+"}{"+str(ss3.denominator)+"}"
        else :
            s3 = "\\frac{"+str(ss3.numerator)+"}{"+str(ss3.denominator)+"}"

    ss4 = fractions.Fraction(n/ss3)

    if ss4.denominator == 1 :
        s4 = int(ss4)
    else :
        if ss4.numerator < 0 :
            s4 = "-\\frac{"+str(abs(ss4.numerator))+"}{"+str(ss4.denominator)+"}"
        else :
            s4 = "\\frac{"+str(ss4.numerator)+"}{"+str(ss4.denominator)+"}"

    cc1 = fractions.Fraction(ss1*ss4)
    cc2 = ss4
    cc3 = fractions.Fraction(ss2*ss4)
    cc4 = ss4

    if cc1.denominator == 1 :
        c1 = int(cc1)
    else :
        if cc1.numerator < 0 :
            c1 = "-\\frac{"+str(abs(cc1.numerator))+"}{"+str(cc1.denominator)+"}"
        else :
            c1 = "\\frac{"+str(cc1.numerator)+"}{"+str(cc1.denominator)+"}"

    if cc2.denominator == 1 :
        c2 = int(cc2)
    else :
        if cc2.numerator < 0 :
            c2 = "-\\frac{"+str(abs(cc2.numerator))+"}{"+str(cc2.denominator)+"}"
        else :
            c2 = "\\frac{"+str(cc2.numerator)+"}{"+str(cc2.denominator)+"}"
    
    if cc3.denominator == 1 :
        c3 = int(cc3)
    else :
        if cc3.numerator < 0 :
            c3 = "-\\frac{"+str(abs(cc3.numerator))+"}{"+str(cc3.denominator)+"}"
        else :
            c3 = "\\frac{"+str(cc3.numerator)+"}{"+str(cc3.denominator)+"}"


    if cc4.denominator == 1 :
        c4 = int(cc4)
    else :
        if cc4.numerator < 0 :
            c4 = "-\\frac{"+str(abs(cc4.numerator))+"}{"+str(cc4.denominator)+"}"
        else :
            c4 = "\\frac{"+str(cc4.numerator)+"}{"+str(cc4.denominator)+"}"

    an = fractions.Fraction(n*ss4)

    aa_list = [fractions.Fraction(an-6), fractions.Fraction(an-4), fractions.Fraction(an-2), an, fractions.Fraction(an+2), fractions.Fraction(an+4), fractions.Fraction(an+6)]
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

    if an.denominator == 1:
        ans = int(an)
    elif an.denominator == -1:
        ans = int(an)
    else :
        if an.numerator < 0 :
            ans = "-\\frac{"+str(abs(an.numerator))+"}{"+str(an.denominator)+"}"
        else :
            ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"


    if aa1.denominator == 1 :
        a1 = int(aa1)
    else :
        if aa1.numerator < 0 :
            a1 = "-\\frac{"+str(abs(aa1.numerator))+"}{"+str(aa1.denominator)+"}"
        else :
            a1 = "\\frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"

    if aa2.denominator == 1 :
        a2 = int(aa2)
    else :
        if aa2.numerator < 0 :
            a2 = "-\\frac{"+str(abs(aa2.numerator))+"}{"+str(aa2.denominator)+"}"
        else :
            a2 = "\\frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = int(aa3)
    else :
        if aa3.numerator < 0 :
            a3 = "-\\frac{"+str(abs(aa3.numerator))+"}{"+str(aa3.denominator)+"}"
        else :
            a3 = "\\frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    if aa4.denominator == 1:
        a4 = int(aa4)
    else :
        if aa4.numerator < 0 :
            a4 = "-\\frac{"+str(abs(aa4.numerator))+"}{"+str(aa4.denominator)+"}"
        else :
            a4 = "\\frac{"+str(aa4.numerator)+"}{"+str(aa4.denominator)+"}"

    if aa5.denominator == 1:
        a5 = int(aa5)
    else :
        if aa5.numerator < 0 :
            a5 = "-\\frac{"+str(abs(aa5.numerator))+"}{"+str(aa5.denominator)+"}"
        else :
            a5 = "\\frac{"+str(aa5.numerator)+"}{"+str(aa5.denominator)+"}"


    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-7,7)
    ax.set_ylim(-7,7)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-0.5, 6.5, "y", size = 15)
    plt.text(6.5, -0.5, "x", size = 15)
    plt.text(+0.1,+0.1, "O", size = 12)

    x = np.linspace(-6, 6, 10)
    y = aa*x
    plt.plot(x,y,'k',c="black")

    x2 = np.linspace(-6, 6, 10)
    y2 = bb*x
    plt.plot(x2,y2,'k',c="black")

    f1 = "$y=-\\frac{"+str(abs(aa.numerator))+"}{"+str(aa.denominator)+"}x$"
    f2 = "$y=\\frac{"+str(bb.numerator)+"}{"+str(bb.denominator)+"}x$"

    plt.text(max(x)-0.5, min(y), '{f1}'.format(f1=f1), size = 12)
    plt.text(max(x2)+0.3, max(y2)+0.3, '{f2}'.format(f2=f2), size = 12)
    plt.text(n1, n2+0.3, "A", size = 12)
    plt.text(n3, n4+0.3, "B", size = 12)
    plt.text(n1, -0.8, "C", size = 12)
    plt.text(n3, -0.8, "D", size = 12)

    x3 = [n1, n3, n3, n1, n1]
    y3 = [n2, n2, 0, 0, n2]
    plt.fill_between(x3, y3, alpha=0.5)
    plt.plot(x3,y3,'k',c="black", linewidth = 0.6)

    answer = "(정답)\n{result}"
    comment = "(해설)\n사각형 $$수식$$ACDB$$/수식$$가 직사각형이므로 두 점 $$수식$$A,B$$/수식$$의\n" \
              "$$수식$$y$$/수식$$좌표를 $$수식$$a$$/수식$$라 하면\n" \
              "$$수식$$A({s1}a,a),``B({s2}a,a),``C({s1}a,0),``D({s2}a,0)$$/수식$$\n" \
              "이때 선분 $$수식$$AB$$/수식$$의 길이가 $$수식$${n}$$/수식$$이므로\n" \
              "$$수식$${s2}a-({s1}a)={n},``{s3}a={n}$$/수식$$\n" \
              "$$수식$$THEREFORE a={s4}$$/수식$$\n" \
              "따라서 $$수식$$A({c1},{c2}),``B({c3},{c4})$$/수식$$이므로 직사각형\n" \
              "$$수식$$ACDB$$/수식$$의 넓이는$$수식$${n}\\times{s4}={ans}$$/수식$$" \

    

    stem = stem.format(a=a, b=b, n=n, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, n=n, c1=c1, c2=c2, c3=c3, c4=c4, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 



def coordinates114_Stem_053():
    stem = "다음 중 $$수식$$y$$/수식$$가 $$수식$$x$$/수식$$에 반비례하는 것은?\n" \
            "① $$수식$$y={a1}-x$$/수식$$         ② $$수식$$xy={a2}$$/수식$$         ③ $$수식$$x+y={a3}$$/수식$$\n" \
            "④ $$수식$${f1}={a4}$$/수식$$        ⑤ $$수식$$y={f2}+{a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n①, ③, ⑤ 정비례도 반비례도 아니다.\n" \
              "② $$수식$$y={f3}$$/수식$$이므로 $$수식$$y$$/수식$$가 $$수식$$x$$/수식$$에 반비례한다.\n" \
              "④ $$수식$$y={f4}x$$/수식$$이므로 $$수식$$y$$/수식$$가 $$수식$$x$$/수식$$에 정비례한다." 
    
    a1 = random.randint(1,9)
    a2 = random.randint(-9,9)
    a3 = random.randint(1,9)
    a4 = random.randint(-9,9)
    a5 = random.randint(1,9)
    
    f1 = "\\frac{x}{y}"
    f2 = "\\frac{" + str(random.randint(1,9)) + "}{x}"

    if a2 < 0 :
      f3 = "-\\frac{" + str(abs(a2)) + "}{x}"
    else :
      f3 = "\\frac{" + str(a2) + "}{x}"

    if a4 < 0 :
      f4 = "-\\frac{1}{" + str(abs(a4)) + "}"
    else :
      f4 = "\\frac{1}{" + str(a4) + "}"


    result = answer_dict[1]


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, f1=f1, f2=f2)
    answer = answer.format(result=result)
    comment = comment.format(f3=f3, f4=f4)

    return stem, answer, comment




def coordinates114_Stem_058():
    stem = "정비례 관계 $$수식$$y={a}x$$/수식$$의 그래프와 반비례 관계 $$수식$$y={f1}$$/수식$$의 그래프가 " \
           "아래 그림과 같고 점 $$수식$$P$$/수식$$의 $$수식$$x$$/수식$$좌표를 $$수식$$a$$/수식$$, $$수식$$y$$/수식$$좌표를 $$수식$$b$$/수식$$라 할 때, " \
           "$$수식$$ab$$/수식$$의 값을 구하시오.\n" \

    a = random.randint(2,4)
    b = random.randint(-15,-2)


    f1 = "-\\frac{" + str(abs(b)) + "}{x}"
    f2 = "-\\frac{" + str(abs(b)) + "}{p}"
    f = "$y=-\\frac{" + str(abs(b)) + "}{x}$"

    k = random.randint(2,3)
    s1 = a*k

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-16,16)
    ax.set_ylim(-16,16)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-1.5, 15.5, "y", size = 15)
    plt.text(15.5, -1.5, "x", size = 15)
    plt.text(+0.1,+0.1, "O", size = 12)

    x = np.linspace(-14, 14, 200)
    y = a*x
    plt.plot(x,y,'k',c="black")

    x2 = np.linspace(-14, 14, 200)
    y2 = b/x2
    plt.plot(x2,y2,'k',c="black")

    x3 = [k,k,b/(k*a)]
    y3 = [0,k*a,k*a]
    plt.plot(x3,y3,c="black", linestyle='dotted')

    plt.scatter(b/(k*a), k*a, c='black', edgecolor='black', s=7)
    plt.text(b/(k*a)-1.5, k*a+0.5, "P".format(a=a), size = 12)
    plt.text(14/a+1, 14+0.3, "y={a}x".format(a=a), size = 15)
    plt.text(3, -10, '{f}'.format(f=f), size = 12)
    plt.text(k, -1.5, '{k}'.format(k=k), size = 12)

    ss2 = fractions.Fraction(fractions.Fraction(b)/fractions.Fraction(s1))

    if ss2.denominator == 1:
        s2 = int(ss2)
    elif ss2.denominator == -1:
        s2 = int(ss2)
    else :
        if ss2.numerator < 0 :
            s2 = "-\\frac{"+str(abs(ss2.numerator))+"}{"+str(ss2.denominator)+"}"
        else :
            s2 = "\\frac{"+str(ss2.numerator)+"}{"+str(ss2.denominator)+"}"

    an = fractions.Fraction(ss2*fractions.Fraction(s1))

    if an.denominator == 1:
        ans = int(an)
    elif an.denominator == -1:
        ans = int(an)
    else :
        if an.numerator < 0 :
            ans = "-\\frac{"+str(abs(an.numerator))+"}{"+str(an.denominator)+"}"
        else :
            ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n점 $$수식$$P$$/수식$$의 좌표를 $$수식$$(p,q)$$/수식$$라 하면 $$수식$$y={a}x$$/수식$$의 그래프가\n" \
              "점 $$수식$$({k},q)$$/수식$$를 지나므로 $$수식$$q={a}\\times{k}={s1}$$/수식$$\n" \
              "$$수식$$y={f1}$$/수식$$에 $$수식$$x=p, y={s1}$$/수식$$을 대입하면\n" \
              "$$수식$${s1}={f2}``````THEREFORE p={s2}$$/수식$$\n" \
              "$$수식$$THEREFORE P({s2},{s1})$$/수식$$\n" \
              "따라서 $$수식$$a={s2},``b={s1}$$/수식$$이므로\n" \
              "$$수식$$ab={ans}$$/수식$$\n" 

    stem = stem.format(a=a, f1=f1)
    answer = answer.format(result=ans)
    comment = comment.format(a=a, k=k, f1=f1, f2=f2, s1=s1, s2=s2, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 




def coordinates114_Stem_060():
    stem = "점 $$수식$$(a, {n1})$$/수식$$이 반비례 관계 $$수식$$y={f1}$$/수식$$의 그래프 위에 있을 때, $$수식$$a$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$         ② $$수식$${a2}$$/수식$$            ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$         ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$y={f1}$$/수식$$에 $$수식$$x=a,``y={n1}을 대입하면$$/수식$$\n" \
              "$$수식$${n1}={f2}``````THEREFORE a={ans}$$/수식$$\n"

    while True :
        ans = random.randint(-4,4)
        if ans != 0:
            break

    k = random.randint(2,4)
    n2 = ans * k
    n1 = int(n2/ans)

    aa_list = [ans-2*k, ans-k, ans, ans+k, ans+2*k, ans+3*k]
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
    
    if n2 > 0 :
        f1 = "\\frac{"+ str(n2) + "}{x}"
        f2 = "\\frac{"+ str(n2) + "}{a}"
    else :
        f1 = "-\\frac{"+ str(abs(n2)) + "}{x}"
        f2 = "-\\frac{"+ str(abs(n2)) + "}{a}"

              
    stem = stem.format(n1=n1, n2=n2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, f1=f1)
    answer = answer.format(result=result)
    comment = comment.format(n1=n1, n2=n2, ans=ans, f1=f1, f2=f2)

    return stem, answer, comment




def coordinates114_Stem_062():
    stem = "반비례 관계 $$수식$$y={f1}$$/수식$$의 그래프가 두 점 $$수식$$({c1},{c2})$$/수식$$, $$수식$$(b,{c4})$$/수식$$를 지날 때, " \
            "상수 $$수식$$a,``b$$/수식$$를 지날 때, 상수 $$수식$$a,``b$$/수식$$에 대하여 $$수식$$b-a$$/수식$$의 값은?\n" \
            "① $$수식$${a1}$$/수식$$         ② $$수식$${a2}$$/수식$$            ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$         ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n$$수식$$y={f1}$$/수식$$에 $$수식$$x={c1},``y={c2}$$/수식$$를 대입하면\n" \
              "$$수식$${c2}={f2}``````THEREFORE a={s1}$$/수식$$\n" \
              "따라서 $$수식$$y={f3}$$/수식$$이므로 $$수식$$x=b, y={c4}$$/수식$$를 대입하면\n" \
              "$$수식$${c4}={f4}``````THEREFORE b={c3}$$/수식$$\n" \
              "$$수식$$THEREFORE b-a={ans}$$/수식$$"
    
    a_list = [-24, -20, -18, -16]

    s1 = random.choice(a_list)
    
    while True :
      c_list = [-3, -2, -1, 1, 2, 3]
      c1 = random.choice(c_list)
      c3 = random.choice(c_list)
      if s1 % c1 == 0 and s1 % c3 == 0 and c1 != c3 :
        break
    
    c2 = int(s1/c1)
    c4 = int(s1/c3)

    ans = c3-s1


    aa_list = [-ans, -(ans-4), -(ans-8), ans-4, ans, ans+4]
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
   
    
    f1 = "\\frac{a}{x}"
    f2 = "\\frac{a}{" + str(c1) + "}"
    f3 = "-\\frac{" + str(abs(s1)) + "}{x}"
    f4 = "-\\frac{" + str(abs(s1)) + "}{b}"

  

    stem = stem.format(f1=f1, c1=c1, c2=c2, c4=c4, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, c1=c1, c2=c2, c3=c3, c4=c4, s1=s1, ans=ans)

    return stem, answer, comment




def coordinates114_Stem_067():
    stem = "아래 그림은 반비례 관계 $$수식$$y={f1}$$/수식$$의 그래프이고, " \
            "점 $$수식$$C$$/수식$$ 는 이 그래프 위의 점이다. 이때 삼각형 $$수식$$ABC$$/수식$$의 넓이는?\n" \
            "① $$수식$${a1}$$/수식$$         ② $$수식$${a2}$$/수식$$            ③ $$수식$${a3}$$/수식$$\n" \
            "④ $$수식$${a4}$$/수식$$         ⑤ $$수식$${a5}$$/수식$$\n"

    n = random.randint(4,9)
    
    f1 = "\\frac{" + str(n) + "}{x}"
    f2 = "\\frac{" + str(n) + "}{a}"
    f3 = "\\frac{1}{2}"


    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-8,8)
    ax.set_ylim(-8,8)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-1.5, 7.5, "y", size = 15)
    plt.text(7.5, -1.5, "x", size = 15)
    plt.text(-0.8,-0.8, "O", size = 12)

    x = np.linspace(-8, 8, 200)
    y = n/x
    plt.plot(x,y,'k',c="black")

    x2 = [n/2, n/2, 0, n/2]
    y2 = [0, 2, 2, 0]
    plt.plot(x2,y2,c="black")
    plt.fill_between(x2, y2, alpha=0.5)

    #f = "$y=\\frac{" + str(n) + "}{x}$"

    #plt.text(4, 10, '{f}'.format(f=f), size = 14)
    plt.text(-0.8, 2, "A", size = 12)
    plt.text(n/2-0.2, -0.8, "B", size = 12)
    plt.text(n/2, 2.2, "C", size = 12)

    an = fractions.Fraction(fractions.Fraction(n/2))

    if an.denominator == 1:
        ans = int(an)
    else :
        ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    aa_list = [fractions.Fraction(an-3/2), fractions.Fraction(an-1), fractions.Fraction(an-1/2), an, fractions.Fraction(an+1/2), fractions.Fraction(an+1), fractions.Fraction(an+3/2)]
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
        a1 = int(aa1)
    else :
        if aa1.numerator < 0 :
            a1 = "-\\frac{"+str(abs(aa1.numerator))+"}{"+str(aa1.denominator)+"}"
        else :
            a1 = "\\frac{"+str(aa1.numerator)+"}{"+str(aa1.denominator)+"}"

    if aa2.denominator == 1 :
        a2 = int(aa2)
    else :
        if aa2.numerator < 0 :
            a2 = "-\\frac{"+str(abs(aa2.numerator))+"}{"+str(aa2.denominator)+"}"
        else :
            a2 = "\\frac{"+str(aa2.numerator)+"}{"+str(aa2.denominator)+"}"

    if aa3.denominator == 1 :
        a3 = int(aa3)
    else :
        if aa3.numerator < 0 :
            a3 = "-\\frac{"+str(abs(aa3.numerator))+"}{"+str(aa3.denominator)+"}"
        else :
            a3 = "\\frac{"+str(aa3.numerator)+"}{"+str(aa3.denominator)+"}"

    if aa4.denominator == 1:
        a4 = int(aa4)
    else :
        if aa4.numerator < 0 :
            a4 = "-\\frac{"+str(abs(aa4.numerator))+"}{"+str(aa4.denominator)+"}"
        else :
            a4 = "\\frac{"+str(aa4.numerator)+"}{"+str(aa4.denominator)+"}"

    if aa5.denominator == 1:
        a5 = int(aa5)
    else :
        if aa5.numerator < 0 :
            a5 = "-\\frac{"+str(abs(aa5.numerator))+"}{"+str(aa5.denominator)+"}"
        else :
            a5 = "\\frac{"+str(aa5.numerator)+"}{"+str(aa5.denominator)+"}"


    answer = "(정답)\n{result}"
    comment = "(해설)\n점 $$수식$$C$$/수식$$의 좌표를 $$수식$$a(a>0)$$/수식$$라 하면 $$수식$$C(a,{f2})$$/수식$$\n" \
              "따라서 삼각형 $$수식$$ABC$$/수식$$의 넓이는\n" \
              "$$수식$${f3}\\times a\\times{f2}={ans}$$/수식$$"

    stem = stem.format(f1=f1, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(result=result)
    comment = comment.format(f2=f2, f3=f3, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 




def coordinates114_Stem_068():
    stem = "아래 그림은 반비례 관계 $$수식$$y={f1}$$/수식$$의 그래프이고, " \
            "점 $$수식$$C$$/수식$$는 이 그래프 위의 점이다. 이때 직사각형 $$수식$$AOBC$$/수식$$의 넓이를 구하시오.\n" \

    n = random.randint(18,25)

    f1 = "\\frac{" + str(n) + "}{x}"
    f2 = "\\frac{" + str(n) + "}{a}"


    n = random.randint(18,25)

    f1 = "\\frac{" + str(n) + "}{x}"
    f2 = "\\frac{" + str(n) + "}{a}"


    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-3,15)
    ax.set_ylim(-3,15)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-1.5, 14.5, "y", size = 15)
    plt.text(14.5, -1.5, "x", size = 15)
    plt.text(-1,-1, "O", size = 12)

    x = np.linspace(-1, 15, 200)
    y = n/x
    plt.plot(x,y,'k',c="black")

    x2 = [n/4, n/4, 0, 0, n/4]
    y2 = [0, 4, 4, 0, 0]
    plt.plot(x2,y2,c="black")
    plt.fill_between(x2, y2, alpha=0.5)

    f = "$y=\\frac{" + str(n) + "}{x}$"

    plt.text(4, 20, '{f}'.format(f=f), size = 14)
    plt.text(-1, 3.5, "A", size = 12)
    plt.text(n/4-0.4, -1, "B", size = 12)
    plt.text(n/4, 4.2, "C", size = 12)

    result = n

    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n점 $$수식$$C$$/수식$$의 좌표를 $$수식$$(a,b)$$/수식$$라 하면 $$수식$$b={f2}$$/수식$$\n" \
              "따라서 직사각형 $$수식$$AOBC$$/수식$$의 넓이는\n" \
              "$$수식$$ab=a\\times{f2}={result}$$/수식$$"

    stem = stem.format(f1=f1)
    answer = answer.format(result=result)
    comment = comment.format(f2=f2, result=result)
    svg = saveSvg()
    return stem, answer, comment, svg 



def coordinates114_Stem_072():
    stem = "아래 그림은 정비례 관계 $$수식$$y={n1}x$$/수식$$의 그래프와 반비례 관계 $$수식$$y={f1}$$/수식$$의 그래프의 일부이다. " \
            "두 그래프가 만나는 점인 $$수식$$A$$/수식$$의 $$수식$$x$$/수식$$좌표는 $$수식$${a1}$$/수식$$이고, 점 $$수식$$A$$/수식$$에서 $$수식$$x$$/수식$$축에 수직인 직선을 그었을 때,  " \
            "$$수식$$x$$/수식$$축이 만나는 점을 $$수식$$P$$/수식$$라 하자. $$수식$$y={f1}$$/수식$$의 그래프 위의 $$수식$$y$$/수식$$좌표가 $$수식$${a2}$$/수식$$인 점 $$수식$$Q$$/수식$$에서 $$수식$$y$$/수식$$축에 수직인 " \
            "직선을 그었을 때, $$수식$$y$$/수식$$축과 만나는 점을 $$수식$$R$$/수식$$라 하자. 사각형 $$수식$$OPQR$$/수식$$의 넓이를 구하시오. " \
            "(단, $$수식$$a$$/수식$$는 상수이다.)\n" \

    n1 = random.randint(2,4)
    a1 = random.randint(2,3)
    s1 = n1*a1
    a2 = s1+random.randint(2,3)
    s2 = s1*a1
    ss3 = fractions.Fraction(fractions.Fraction(s2)/fractions.Fraction(a2))

    if ss3.denominator == 1 :
        s3 = int(ss3)
    else :
        s3 = "\\frac{"+str(ss3.numerator)+"}{"+str(ss3.denominator)+"}"
    
    an = fractions.Fraction(fractions.Fraction(1/2)*fractions.Fraction(a1+ss3)*fractions.Fraction(a2))

    if an.denominator == 1:
        ans = int(an)
    else :
        ans = "\\frac{"+str(an.numerator)+"}{"+str(an.denominator)+"}"

    f1 = "\\frac{a}{x}"
    f2 = "\\frac{a}{" + str(a1) + "}"
    f3 = "\\frac{" + str(s2) + "}{x}"
    f4 = "\\frac{1}{2}"


    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (3.5,3.5)
    plt.rcParams['font.size'] = 13

    fig, ax = plt.subplots()

    ax.set_xlim(-2,18)
    ax.set_ylim(-2,18)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])


    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    plt.text(-1, 17, "y", size = 15)
    plt.text(17, -1, "x", size = 15)
    plt.text(0.5,-1, "O", size = 12)

    x = np.linspace(-2, 17, 20)
    y = n1*x
    plt.plot(x,y,'k',c="black")

    x2 = np.linspace(-2, 17, 200)
    y2 = s2/x2
    plt.plot(x2,y2,'k',c="black")

    x3 = [0, a1, s2/a2, 0]
    y3 = [0, 0, a2, a2]
    plt.plot(x3,y3,c="black")
    plt.fill_between(x3, y3, alpha=0.5)

    f5 = "$y=\\frac{a}{x}$"

    plt.text(15, 4, '{f5}'.format(f5=f5), size = 14)
    plt.text(6, 18.5, "$y={n1}x$".format(n1=n1), size = 12)
    plt.text(a1, -1, "P", size = 12)
    plt.text(a1+0.3, s1, "A", size = 12)
    plt.text(s2/a2+0.2, a2+0.1, "Q", size = 12)
    plt.text(-1, a2, "R", size = 12)



    answer = "(정답)\n$$수식$${result}$$/수식$$"
    comment = "(해설)\n$$수식$$y={n1}x$$/수식$$에 $$수식$$x={a1}$$/수식$$를 대입하면 $$수식$$y={s1}$$/수식$$\n" \
              "$$수식$$THEREFORE A({a1},{s1}),``P({a1},0)$$/수식$$\n" \
              "$$수식$$y={f1}$$/수식$$에 $$수식$$x={a1},``y={s1}$$/수식$$를 대입하면\n" \
              "$$수식$${s1}={f2}``````THEREFORE a={s2}$$/수식$$\n" \
              "따라서 $$수식$$y={f3}$$/수식$$이므로 $$수식$$y={a2}$$/수식$$를 대입하면\n" \
              "$$수식$${a2}={f3}``````THEREFORE x={s3}$$/수식$$\n" \
              "$$수식$$THEREFORE Q({s3},{a2}),``R(0,{a2})$$/수식$$\n" \
              "따라서 사각형 $$수식$$OPQR$$/수식$$의 넓이는\n" \
              "$$수식$${f4}\\times({a1}+{s3})\\times{a2}={ans}$$/수식$$"

    stem = stem.format(n1=n1, a1=a1, a2=a2, f1=f1)
    answer = answer.format(result=ans)
    comment = comment.format(n1=n1, a1=a1, a2=a2, s1=s1, s2=s2, s3=s3, f1=f1, f2=f2, f3=f3, f4=f4, ans=ans)
    svg = saveSvg()
    return stem, answer, comment, svg 
