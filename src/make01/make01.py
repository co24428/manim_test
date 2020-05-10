from manimlib.imports import *

class test_arrow(Scene):
  def construct(self):
    x1 = TextMobject("1").shift(LEFT*2, UP*3)
    x2 = TextMobject("3")
    arrow = Arrow(x1, x2)
    
    self.add(x1, x2)
    self.play(Write(arrow))

class show_table(Scene):
  def construct(self):
    
    ellipse1=Ellipse(width=2, height=4, color=GOLD_B)

    ellipse1.shift(LEFT*5)
    ellipse2=Ellipse(width=2, height=4, color=GOLD_B)
    ellipse2.shift(LEFT*2)
    group1 = VGroup(ellipse1, ellipse2)
    
    ellipse3=Ellipse(width=2, height=4, color=GOLD_B)
    ellipse3.shift(RIGHT*2)
    ellipse4=Ellipse(width=2, height=4, color=GOLD_B)
    ellipse4.shift(RIGHT*5)
    group2 = VGroup(ellipse3, ellipse4)
    
    arrow1 = Arrow(LEFT*1.7)
    x11 = TextMobject("X").next_to(arrow1,LEFT)
    x12 = TextMobject("X").next_to(arrow1,RIGHT)
    f = TextMobject("f").next_to(arrow1,UP)
    group3 = VGroup(arrow1, x11, x12, f).next_to(group1, UP)
    
    arrow2 = Arrow(LEFT*1.7)
    x21 = TextMobject("X").next_to(arrow2,LEFT)
    x22 = TextMobject("X").next_to(arrow2,RIGHT)
    g = TextMobject("g").next_to(arrow2,UP)
    group4 = VGroup(arrow2, x21, x22, g).next_to(group2, UP)

    n11 = TextMobject("1")
    n12 = TextMobject("3")
    n13 = TextMobject("5")
    n14 = TextMobject("7").next_to(n13,DOWN)
    n15 = TextMobject("9").next_to(n14,DOWN)
    n12.next_to(n13,UP)
    n11.next_to(n12,UP)
    n_group1 = VGroup(n11, n12, n13, n14, n15).shift(LEFT*5)
    
    n21 = TextMobject("1")
    n22 = TextMobject("3")
    n23 = TextMobject("5")
    n24 = TextMobject("7").next_to(n23,DOWN)
    n25 = TextMobject("9").next_to(n24,DOWN)
    n22.next_to(n23,UP)
    n21.next_to(n22,UP)
    n_group2 = VGroup(n21, n22, n23, n24, n25).shift(LEFT*2)
    
    n31 = TextMobject("1")
    n32 = TextMobject("3")
    n33 = TextMobject("5")
    n34 = TextMobject("7").next_to(n33,DOWN)
    n35 = TextMobject("9").next_to(n34,DOWN)
    n32.next_to(n33,UP)
    n31.next_to(n32,UP)
    n_group3 = VGroup(n31, n32, n33, n34, n35).shift(RIGHT*2)

    n41 = TextMobject("1")
    n42 = TextMobject("3")
    n43 = TextMobject("5")
    n44 = TextMobject("7").next_to(n43,DOWN)
    n45 = TextMobject("9").next_to(n44,DOWN)
    n42.next_to(n43,UP)
    n41.next_to(n42,UP)
    n_group4 = VGroup(n41, n42, n43, n44, n45).shift(RIGHT*5)

    NtoN11 = Arrow(n11, n23, tip_length=0.2)
    NtoN12 = Arrow(n12, n21, tip_length=0.2)
    NtoN13 = Arrow(n13, n24, tip_length=0.2)
    NtoN14 = Arrow(n14, n25, tip_length=0.2)
    NtoN15 = Arrow(n15, n22, tip_length=0.2)
    NtoN_group1 = VGroup(NtoN11,NtoN12,NtoN13,NtoN14,NtoN15)
    
    NtoN21 = Arrow(n31, n42, tip_length=0.2)
    NtoN22 = Arrow(n32, n43, tip_length=0.2)
    NtoN23 = Arrow(n33, n45, tip_length=0.2)
    NtoN24 = Arrow(n34, n44, tip_length=0.2)
    NtoN25 = Arrow(n35, n41, tip_length=0.2)
    NtoN_group2 = VGroup(NtoN21,NtoN22,NtoN23,NtoN24,NtoN25)

    func1 = TexMobject("(g \circ f)(1)", "=", "g(f(1))")
    func1.to_edge(DOWN)
    func2 = TexMobject("g(f(1))", "=", "9")
    func2.to_edge(DOWN)

    self.play(GrowFromCenter(group1))
    self.play(TransformFromCopy(group1, group2))
    self.play(Write(group3), Write(group4))
    self.play(FadeIn(n_group1, LEFT), 
              FadeIn(n_group2, LEFT), 
              FadeIn(n_group3, LEFT), 
              FadeIn(n_group4, LEFT))
    self.play(Write(NtoN_group1), Write(NtoN_group2))
    self.play(FadeInFrom(func1,DOWN))
    self.wait(1)
    self.play(Transform(func1[0], func2[0]),
              FadeOut(func1[1]),
              FadeOut(func1[2]))
    
    func3 = TexMobject("f(1)", "=", "5")
    func3.next_to(group1,DOWN)
    self.wait(0.5)
    self.play(FadeIn(func3[0]))
    self.play(FadeOut(NtoN12),
              FadeOut(NtoN13),
              FadeOut(NtoN14),
              FadeOut(NtoN15))
    self.play(ApplyMethod(NtoN11.set_color,YELLOW),
              FadeIn(func3[1]),
              FadeIn(func3[2]))
    
    func4 = TexMobject("f(5)", "=", "9")
    func4.next_to(group2,DOWN)
    self.wait(0.5)
    self.play(FadeIn(func4[0]))
    self.play(FadeOut(NtoN21),
              FadeOut(NtoN22),
              FadeOut(NtoN24),
              FadeOut(NtoN25))
    self.play(ApplyMethod(NtoN23.set_color,YELLOW),
              FadeIn(func4[1]),
              FadeIn(func4[2]))
    self.play(FadeInFrom(func2[1]),
              FadeInFrom(func2[2]))

