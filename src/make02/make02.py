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
    
    self.play(GrowFromCenter(square))
    self.play(Write(sector1))
    self.play(Write(sector2))