from manimlib import *
import numpy as np

class s1(Scene):
    def construct(self):
        center = np.array([0,0,0])
        dot_radius = 0.04
        dot_point1 = np.array([0.4,0,0])
        dot_point2 = np.array([0.8,0,0])
        dot_point3 = np.array([1.2,0,0])
        dot_point4 = np.array([1.8,0,0])
        dot_point5 = np.array([2.5,0,0])

        dot_center = Dot(radius=dot_radius)
        

        dot1 = Dot(radius=dot_radius)
        dot1.move_to(dot_point1)
        dot2 = Dot(radius=dot_radius)
        dot2.move_to(dot_point2)
        dot3 = Dot(radius=dot_radius)
        dot3.move_to(dot_point3)
        dot4 = Dot(radius=dot_radius)
        dot4.move_to(dot_point4)
        dot5 = Dot(radius=dot_radius)
        dot5.move_to(dot_point5)
        dot_group = VGroup(dot_center, dot1, dot2, dot3, dot4, dot5)

        arrow_init = Arrow(center, dot_point5)
        arrow = Arrow(center, dot_point5)
        long_arrow = Arrow(center, np.array([6,0,0]), thickness=0.02)

        # self.play(GrowFromCenter(dot_center))
        # self.play(GrowFromPoint(dot1, dot_point1))
        # self.play(GrowFromPoint(dot2, dot_point2), GrowFromPoint(dot3, dot_point3))
        # self.play(GrowFromPoint(dot4, dot_point4), GrowFromPoint(dot5, dot_point5))
        self.play(FadeIn(dot_group))
        self.play(ReplacementTransform(dot_group, arrow_init))
        self.wait(1)
        self.play(ReplacementTransform(arrow_init, long_arrow))
        self.wait(1)
        self.play(ReplacementTransform(long_arrow, arrow))


class s2(Scene):
    def construct(self):
        center = np.array([0,0,0])
        end_point1 = np.array([2.5,0,0])
        end_point2 = np.array([-2.5,0,0])

        arrow1 = Arrow(center, end_point1)
        arrow2 = Arrow(center + np.array([0.5,0,0]), end_point2)
        self.play(FadeIn(arrow1))
        self.play(GrowArrow(arrow2))
