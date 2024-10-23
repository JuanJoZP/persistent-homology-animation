from manim import *
from math import pi, sin, cos
from numpy import linspace


class CreateCircle(Scene):

    def construct(self):
        points = [(cos(tetha), sin(tetha), 0) for tetha in linspace(0, 2 * pi, 20)]
        points = points + [(y, 0, 0) for y in linspace(-0.9, 0.9, 6)]
        self.add(*[Point(location=point, color=WHITE) for point in points])
