from manimlib.imports import *

class q1(Scene):
  def construct(self):
    square = Square(side_length=4)
    sector1 = Sector(fill_opacity=1,
                    angle=TAU/4,
                    inner_radius=3.96,
                    outer_radius=4)
    sector1.shift(DOWN*2+LEFT*2)
    sector2 = Sector(fill_opacity=1,
                    angle=TAU/4,
                    inner_radius=3.96,
                    outer_radius=4,
                    start_angle=TAU/4)
    sector2.shift(DOWN*2+RIGHT*2)
    sector3 = Sector(fill_opacity=1,
                    angle=TAU/2,
                    inner_radius=1.96,
                    outer_radius=2,
                    start_angle=TAU)
    sector3.shift(DOWN*2)
    A = TextMobject("A").next_to(square, UP).shift(DOWN*0.7).scale(0.7)
    B = TextMobject("B").next_to(sector3, UP).scale(0.7)
    Qgroup = VGroup(square,sector1,sector2,sector3,A,B)
    Qgroup.save_state()

    Q = TexMobject("A-B =\ ?")


    self.play(GrowFromCenter(square))
    self.play(Write(sector1),Write(sector2), Write(sector3))
    self.play(FadeIn(A), FadeIn(B))
    self.play(Qgroup.to_edge, LEFT,
              Qgroup.scale, 0.8,
              FadeIn(Q, run_time=2))
