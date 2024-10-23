from manim import *
from math import pi, sin, cos
from numpy import linspace

# CUADRAR COLORES PUNTOS
# BACKGROUND NEGRO
# colores se estan invirtiendo raro
# GRAN MALPARIDO ME HACE EL FAVOR Y ESCONDE EL EJE Z AXEZ COCK SUCKER


class CreateCircle(ThreeDScene):

    def construct(self):
        #self.camera.background_color = WHITE
        self.set_camera_orientation(phi=0, theta=3 * pi / 2)

        c = ThreeDAxes(x_range=[-1, 10, 1],
                       y_range=[-1, 5, 1],
                       z_range=[-1, 5, 1],
                       x_length=11,
                       y_length=6,
                       z_length=6)

        self.add(c)

        point1 = Dot(color=WHITE).move_to(c.c2p(4, 1, 0))
        point2 = Dot(color=PURPLE).move_to(c.c2p(7, 1, 0))
        self.add(point1, point2)

        circle1 = Circle(radius=1.5, color=WHITE).move_to(point1.get_center())
        circle2 = Circle(radius=1.5, color=PURPLE).move_to(point2.get_center())
        self.add(circle1, circle2)

        self.play([GrowFromCenter(circle1), GrowFromCenter(circle2)], run_time=2)

        self.wait(1)

        self.play([FadeOut(circle1), FadeOut(circle2)])

        self.wait(1)

        line1 = Line(point1, point2)
        self.play(FadeIn(line1))

        self.wait(1)

        point3 = Dot(color=BLUE).move_to(c.c2p(5.5, 4, 0))
        self.play(FadeIn(point3))

        self.wait(1)

        circle3 = Circle(radius=1.5, color=PURPLE).move_to(point3.get_center())
        self.play([FadeIn(circle1), FadeIn(circle2), GrowFromCenter(circle3)])

        self.wait()

        circle1_1 = Circle(radius=1.925, color=WHITE).move_to(point1.get_center())
        circle2_1 = Circle(radius=1.925, color=PURPLE).move_to(point2.get_center())
        circle3_1 = Circle(radius=1.925, color=PURPLE).move_to(point3.get_center())

        self.play([
            Transform(circle1, circle1_1),
            Transform(circle2, circle2_1),
            Transform(circle3, circle3_1)
        ])

        self.wait(1)

        self.play([FadeOut(circle1), FadeOut(circle2), FadeOut(circle3)])

        self.wait(1)

        line2 = Line(point2, point3)
        line3 = Line(point1, point3)
        self.play(FadeIn(line2), FadeIn(line3))

        self.wait(1)

        surface = Polygon(point1.get_center(),
                          point2.get_center(),
                          point3.get_center(),
                          color=RED,
                          fill_color=RED,
                          fill_opacity=0.7)

        self.play(FadeIn(surface))

        self.wait(2)

        self.begin_ambient_camera_rotation(pi / 6, about='phi')
        self.wait(2)
        self.stop_ambient_camera_rotation(about='phi')

        point4 = Dot(color=RED_A).move_to(c.c2p(5.5, 2.5, 2.5))
        self.begin_ambient_camera_rotation(pi / 2, about='theta')
        self.play(FadeIn(point4))
        self.stop_ambient_camera_rotation(about='phi')

        self.wait(1)

        bolas_rad = 2
        bola1 = Sphere(point1.get_center(),
                       bolas_rad,
                       color=RED,
                       fill_color=RED,
                       fill_opacity=0.7)
        bola2 = Sphere(point2.get_center(),
                       bolas_rad,
                       color=RED,
                       fill_color=RED,
                       fill_opacity=0.7)
        bola3 = Sphere(point3.get_center(),
                       bolas_rad,
                       color=RED,
                       fill_color=RED,
                       fill_opacity=0.7)
        bola4 = Sphere(point4.get_center(),
                       bolas_rad,
                       color=RED,
                       fill_color=RED,
                       fill_opacity=0.7)

        self.play([
            GrowFromCenter(bola1),
            GrowFromCenter(bola2),
            GrowFromCenter(bola3),
            GrowFromCenter(bola4)
        ],
                  run_time=5)

        self.wait(2)


# muestra ejes 3 d, monta otro punto

# crece bolas

# conecta

# muestra tetraedro
