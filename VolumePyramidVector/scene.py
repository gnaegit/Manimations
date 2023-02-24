from manim import *
import numpy as np

class VectorExample(Scene):
    def construct(self):
        plane = NumberPlane()
        vector_1 = Vector([1,2])
        vector_2 = Vector([-5,-2])
        self.add(plane, vector_1, vector_2)

class ExampleArrow3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        resolution = 10
        self.set_camera_orientation(phi=75 * DEGREES, theta=300 * DEGREES)

        group = VGroup()
        tex_spatVolume = MathTex(r"V_{spat} = |( \vec{a} \times \vec{b}) \cdot \vec{c}|")
        tex_spatVolume[0][0:5].set_color(PURPLE)
        tex_spatVolume[0][8:10].set_color(BLUE)
        tex_spatVolume[0][11:13].set_color(YELLOW)
        tex_spatVolume[0][15:17].set_color(ORANGE)

        tex_toblerone = MathTex(r"V_{tob} = \frac{1}{2}V_{spat}").next_to(tex_spatVolume,direction=DOWN).align_to(tex_spatVolume, LEFT)
        tex_toblerone[0][0:4].set_color(GREEN)
        tex_toblerone[0][8:13].set_color(PURPLE)
        
        tex_pyramid = MathTex(r"V_{pyramid} & = \frac{1}{3}V_{tob} \\ & = \frac{1}{2} \frac{1}{3} V_{spat} \\ & = \frac{1}{6} V_{spat}").next_to(tex_toblerone,direction=DOWN).align_to(tex_toblerone, LEFT)
        tex_pyramid[0][0:8].set_color(RED)
        tex_pyramid[0][12:16].set_color(GREEN)
        tex_pyramid[0][23:28].set_color(PURPLE)
        tex_pyramid[0][32:37].set_color(PURPLE)
        group.add(tex_spatVolume, tex_toblerone, tex_pyramid).to_edge(UL)

        A = np.array([0, 0, 0])
        B = np.array([4, 0, 0])
        D = np.array([1, 3, 0])
        C = B + D - A 
        E = np.array([2, 2, 2])
        F = B + E - A
        G = C + E - A
        H = D + E - A
        
        arrowAE = Arrow3D(
            start=A,
            end=E,
            resolution=resolution,
            color=ORANGE
        )
        arrowBF = Arrow3D(
            start=B,
            end=F,
            resolution=resolution,
            color=ORANGE
        )
        arrowCG = Arrow3D(
            start=C,
            end=G,
            resolution=resolution,
            color=ORANGE
        )
        arrowDH = Arrow3D(
            start=D,
            end=H,
            resolution=resolution,
            color=ORANGE
        )
        arrowAB = Arrow3D(
            start=A,
            end=B,
            resolution=resolution,
            color=BLUE
        )
        arrowDC = Arrow3D(
            start=D,
            end=C,
            resolution=resolution,
            color=BLUE
        )
        arrowEF = Arrow3D(
            start=E,
            end=F,
            resolution=resolution,
            color=BLUE
        )
        arrowHG = Arrow3D(
            start=H,
            end=G,
            resolution=resolution,
            color=BLUE
        )
        arrowAD = Arrow3D(
            start=A,
            end=D,
            resolution=resolution,
            color=YELLOW
        )
        arrowBC = Arrow3D(
            start=B,
            end=C,
            resolution=resolution,
            color=YELLOW
        )
        arrowEH = Arrow3D(
            start=E,
            end=H,
            resolution=resolution,
            color=YELLOW
        )
        arrowFG = Arrow3D(
            start=F,
            end=G,
            resolution=resolution,
            color=YELLOW
        )

        self.add(axes)
        self.play(Create(arrowAB))
        self.wait(1)
        self.play(Create(arrowAD))
        self.wait(1)
        self.play(Create(arrowAE))
        self.move_camera(phi=75 * DEGREES, theta=390 * DEGREES, run_time =3)

        self.play(Create(arrowBC), Create(arrowDC))
        self.wait(1)
        self.play(Create(arrowBF), Create(arrowCG), Create(arrowDH))
        self.wait(1)
        self.play(Create(arrowEF), Create(arrowFG), Create(arrowEH), Create(arrowHG))

        parallelepiped = VGroup()
        parallelepiped1 = Polygon(A, B, C, D, color=PURPLE_E)
        parallelepiped2 = Polygon(A, B, F, E, color=PURPLE_E)
        parallelepiped3 = Polygon(A, D, H, E, color=PURPLE_E)
        parallelepiped4 = Polygon(B, C, G, F, color=PURPLE_E)
        parallelepiped5 = Polygon(D, C, G, H, color=PURPLE_E)
        parallelepiped6 = Polygon(E, F, G, H, color=PURPLE_E)
        parallelepiped.add(parallelepiped1, parallelepiped2, parallelepiped3,
        parallelepiped4, parallelepiped5, parallelepiped6)

        self.play(Create(parallelepiped1))
        self.wait(0.2)
        parallelepiped1.set_fill(color = PURPLE, opacity=0.2)
        self.wait(0.2)
        self.play(Create(parallelepiped2))
        self.wait(0.2)
        parallelepiped2.set_fill(color = PURPLE, opacity=0.2)
        self.wait(0.2)
        self.play(Create(parallelepiped3))
        self.wait(0.2)
        parallelepiped3.set_fill(color = PURPLE, opacity=0.2)
        self.wait(0.2)
        self.play(Create(parallelepiped4))
        self.wait(0.2)
        parallelepiped4.set_fill(color = PURPLE, opacity=0.2)
        self.wait(0.2)
        self.play(Create(parallelepiped5))
        self.wait(0.2)
        parallelepiped5.set_fill(color = PURPLE, opacity=0.2)
        self.wait(0.2)
        self.play(Create(parallelepiped6))
        self.wait(0.2)
        parallelepiped6.set_fill(color = PURPLE, opacity=0.2)
        self.wait(0.2)
        self.add_fixed_in_frame_mobjects(tex_spatVolume)
        self.wait(0.2)
        self.move_camera(phi=75 * DEGREES, theta=300 * DEGREES, run_time =3)


        toblerone = VGroup()
        area1 = Polygon(B, D, H, F, color=GREEN_E)
        area2 = Polygon(A, B, D, color=GREEN_E)
        area3 = Polygon(E, F, H, color=GREEN_E)
        area4 = Polygon(A, D, H, E, color=GREEN_E)
        area5 = Polygon(A, B, F, E, color=GREEN_E)
        toblerone.add(area1, area2, area3, area4, area5)

        self.wait(3)
        self.play(Create(area1))
        self.wait(0.2)
        area1.set_fill(color = GREEN, opacity=0.3)
        self.wait(0.2)
        self.play(Create(area2))
        self.wait(0.2)
        area2.set_fill(color = GREEN, opacity=0.3)
        self.wait(0.2)
        self.play(Create(area3))
        self.wait(0.2)
        area3.set_fill(color = GREEN, opacity=0.3)
        self.wait(0.2)        
        self.play(Create(area4))
        self.wait(0.2)
        area4.set_fill(color = GREEN, opacity=0.3)
        self.wait(0.2)  
        self.play(Create(area5))
        self.wait(0.2)
        area5.set_fill(color = GREEN, opacity=0.3)
        self.wait(0.2)
        self.add_fixed_in_frame_mobjects(tex_toblerone)
        self.wait(3)  

        pyramid = VGroup()
        areapyramid1 = Polygon(A, B, D, color=RED_E)
        areapyramid2 = Polygon(B, D, E, color=RED_E)
        areapyramid3 = Polygon(A, D, E, color=RED_E)
        areapyramid4 = Polygon(A, B, E, color=RED_E)
        pyramid.add(areapyramid1, areapyramid2, areapyramid3, areapyramid4)

        self.play(Create(areapyramid1))
        self.wait(0.2)
        areapyramid1.set_fill(color = RED, opacity=0.5)
        self.wait(0.2)

        self.play(Create(areapyramid2))
        self.wait(0.2)
        areapyramid2.set_fill(color = RED, opacity=0.5)
        self.wait(0.2)

        self.play(Create(areapyramid3))
        self.wait(0.2)
        areapyramid3.set_fill(color = RED, opacity=0.5)
        self.wait(0.2)

        self.play(Create(areapyramid4))
        self.wait(0.2)
        areapyramid4.set_fill(color = RED, opacity=0.5)
        self.wait(0.2)

        self.add_fixed_in_frame_mobjects(tex_pyramid)
        self.wait(0.5)

        #self.move_camera(phi=75 * DEGREES, theta=-60 * DEGREES, run_time =10)
        self.begin_ambient_camera_rotation(about="theta", rate=360*DEGREES/20)
        self.wait(40)

class TestEquation(ThreeDScene):
    def construct(self): 
        self.set_camera_orientation(0.8*np.pi/2, -0.45*np.pi)
        axes = ThreeDAxes()
        arrow = Arrow3D(
            start=[0, 0, 0],
            end=[1, 0, 0],
            resolution=8,
            color=ORANGE
        )
        self.add(axes, arrow)

        group = VGroup()
        tex_spatVolume = MathTex(r"V_{spat} = |( \vec{a} \times \vec{b}) \cdot \vec{c}|")
        tex_spatVolume[0][0:5].set_color(PURPLE)
        tex_spatVolume[0][8:10].set_color(BLUE)
        tex_spatVolume[0][11:13].set_color(YELLOW)
        tex_spatVolume[0][15:17].set_color(ORANGE)

        tex_toblerone = MathTex(r"V_{tob} = \frac{1}{2}V_{spat}").next_to(tex_spatVolume,direction=DOWN).align_to(tex_spatVolume, LEFT)
        tex_toblerone[0][0:4].set_color(GREEN)
        tex_toblerone[0][8:13].set_color(PURPLE)
        
        tex_pyramid = MathTex(r"V_{pyramid} & = \frac{1}{3}V_{tob} \\ & = \frac{1}{2} \frac{1}{3} V_{spat} \\ & = \frac{1}{6} V_{spat}").next_to(tex_toblerone,direction=DOWN).align_to(tex_toblerone, LEFT)
        tex_pyramid[0][0:8].set_color(RED)
        tex_pyramid[0][12:16].set_color(GREEN)
        tex_pyramid[0][23:28].set_color(PURPLE)
        tex_pyramid[0][32:37].set_color(PURPLE)
        group.add(tex_spatVolume, tex_toblerone, tex_pyramid)
        group.to_corner(UL)

        self.set_camera_orientation(0.8*np.pi/2, -0.45*np.pi)
        # self.add(index_labels(tex_pyramid[0]))

        self.add_fixed_in_frame_mobjects(tex_spatVolume)
        self.wait()
        self.add_fixed_in_frame_mobjects(tex_toblerone)
        self.wait()
        self.add_fixed_in_frame_mobjects(tex_pyramid)
        self.wait()

        self.play(Transform(tex_spatVolume[0][15:17].copy(), arrow.copy()))
        self.wait()

