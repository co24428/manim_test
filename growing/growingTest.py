from manimlib.imports import *

class Point(Scene):
    #A few simple shapes
    def construct(self):
        CONFIG = {
            "point_color": RED,
        }
        point1 = np.array([-1.2,0,0])
        point2 = np.array([1.2,0,0])
        line=Line(point1,point2)
        circle1 = Circle()
        circle2 = Circle()
        circle3 = Circle()
        circle2.next_to(circle1,RIGHT)
        circle3.next_to(circle1,LEFT)
        point3 = np.array([-2,2,0])
        point4 = np.array([2,2,0])

        self.play(GrowFromPoint(line,point1))
        self.wait(1)
        self.play(GrowFromPoint(circle2,point3))
        self.wait(1)
        self.play(GrowFromPoint(circle3,point4))
        self.wait(1)


class Center(Scene):
    def construct(self):
        circle = Circle()

        self.play(GrowFromCenter(circle))
        self.wait(1)

class edge(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        point1 = np.array([-1,-1,0])
        point2 = np.array([1,1,0])
        line=Line(point1,point2)

#        self.play(GrowFromCenter(square))
#        self.play(GrowFromCenter(circle))
        self.play(GrowFromEdge(square, DOWN))
        self.wait(1)
        self.play(GrowFromEdge(circle, UP))
        self.wait(1)
        self.play(GrowFromEdge(line, UP+RIGHT))
        self.wait(1)

class arrow(Scene):
    def construct(self):
        arrow1 = Arrow(LEFT,UP)
        arrow2 = Arrow(LEFT,UP)
        arrow2.next_to(arrow1,RIGHT+UP)
        arrow3 = Arrow(LEFT,UP)
        arrow3.next_to(arrow2,RIGHT+UP)
        arrow4 = Arrow(LEFT,UP)
        arrow4.next_to(arrow3,RIGHT+UP)

        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.play(GrowArrow(arrow3))
        self.play(GrowArrow(arrow4))

class spin(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        point1 = np.array([-1,-1,0])
        point2 = np.array([1,1,0])
        line=Line(point1,point2)

        self.play(SpinInFromNothing(circle))
        self.wait(1)
        self.play(SpinInFromNothing(square))
        self.wait(1)
        self.play(SpinInFromNothing(line))
        self.wait(1)
