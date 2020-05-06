from manimlib.imports import *

class create1(Scene):
    def construct(self):
        point1 = np.array([-1,-2,0])
        point2 = np.array([1,2,0])
        line = Line(point1, point2)
        circle = Circle()

        self.play(ShowCreation(line))
        self.wait(1)
        self.play(Uncreate(line))
        self.wait(1)
        self.play(ShowCreation(circle))
        self.wait(1)
        self.play(Uncreate(circle))
        self.wait(1)

class write1(Scene):
    def construct(self):
        text1 = TextMobject("Writing with manim is fun")
        text2 = TextMobject("Growing method")
        text2.next_to(text1, DOWN)
        circle = Circle()

        self.play(Write(text1))
        self.wait(1)
        self.play(Write(circle))
        self.wait(1)
        self.play(GrowFromEdge(text2, LEFT))
        self.wait(1)

class write2(Scene):
    def construct(self):
        text1 = TextMobject("Writing with manim is fun")
        text2 = TextMobject("Growing method")
        text2.next_to(text1, DOWN)

        self.play(AddTextWordByWord(text1))
        self.wait(1)
        self.play(AddTextWordByWord(text2))
        self.wait(1)
