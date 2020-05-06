from manimlib.imports import *

class fade(Scene):
    def construct(self):
        point1 = np.array([-1,-1,0])
        point2 = np.array([2,2,0])
        line = Line(point1, point2)

        self.play(FadeIn(line))
        self.wait(1)
        self.play(FadeOut(line))
        self.wait(1)

class fade2(Scene):
    def construct(self):
        point1 = np.array([-1,-1,0])
        point2 = np.array([1,1,0])
        line1 = Line(point1, point2)
        point3 = np.array([-1,1,0])
        point4 = np.array([1,-1,0])
        line2 = Line(point3, point4)
        point5 = np.array([-2,-1,0])
        point6 = np.array([2,1,0])
        line3 = Line(point5, point6)

        self.play(FadeInFrom(line1))
        self.wait(1)
        self.play(FadeInFrom(line2, LEFT))
        self.wait(1)
        self.play(FadeInFromDown(line3))
        self.wait(1)

        self.play(FadeOutAndShift(line3, RIGHT))
        self.wait(1)
        self.play(FadeOutAndShift(line2, UP))
        self.wait(1)
        self.play(FadeOutAndShiftDown(line1))
        self.wait(1)

class fade3(Scene):
    def construct(self):
        point1 = np.array([-1,-1,0])
        point2 = np.array([1,1,0])
        line = Line(point1, point2)
        circle = Circle()
        square = Square()

        self.play(FadeInFromPoint(line, point1))
        self.wait(1)
        self.play(FadeInFromLarge(circle))
        self.wait(1)
        self.play(FadeInFromLarge(square, 3))
        self.wait(1)
