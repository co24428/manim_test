from manimlib.imports import *

class line(Scene):
    #A few simple shapes
    def construct(self):
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        self.play(GrowFromCenter(line))
        self.wait(1)
        self.play(Transform(line,triangle))
        self.wait(1)

class AddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author=TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),
          ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))

        self.play(ApplyMethod(author.scale,1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))



class check_koreanText(Scene):
  def construct(self):
    quote  = TextMobject("manim doesnt support korean")
    quoteB = TextMobject("hwan")
    quoteB.set_color(BLUE)
    quoteB.next_to(quote.get_corner(UP+LEFT),UP)
    quote2 = TextMobject("only can use english")
    quote2.set_color(RED)
    quote3 = TextMobject("hello...")

    self.add(quote)
    self.add(quoteB)
    self.wait(2)
    self.play(Transform(quote, quote2), ApplyMethod(quoteB.move_to, quote2.get_corner(UP+RIGHT)+UP*2))
    self.wait(2)
    self.play(Transform(quote, quote3), ApplyMethod(quoteB.move_to, quote3.get_corner(DOWN+RIGHT)+LEFT*2))
    self.play(FadeOut(quoteB))


class mainPlot(GraphScene):
    CONFIG = {
        "x_min" : -1,
        "x_max" : 5,
        "y_min" : 0,
        "y_max" : 32,
    #    "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : WHITE,
        "x_labeled_nums" :range(0,6,1),
        "y_labeled_nums" :range(0,33,8),
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x: 2**x,
                                color = GREEN,
                                x_min = -1,
                                x_max = 6)
        point1 = self.input_to_graph_point(3,graph)
        point2 = self.input_to_graph_point(4,graph)
        line1  = Line(point1, point2-(0,1.5,0), color=BLUE)
        line2  = Line(point2, point2-(0,1.5,0), color=RED)
        text1  = TextMobject("dx")
        text2  = TextMobject("dy")
        text1.set_color(BLUE)
        text2.set_color(RED)

        text1.next_to(line1, DOWN)
        text2.next_to(line2, RIGHT)

        self.play(ShowCreation(graph), run_time = 1)
        self.wait(1)
        self.play(GrowFromCenter(line1), GrowFromCenter(line2), FadeIn(text1), FadeIn(text2))
#        self.play(ShowCreation(line1), ShowCreation(line2))
        self.wait(2)


class Plot1(GraphScene):
    CONFIG = {
        "y_max" : 32,
        "y_min" : 0,
        "x_max" : 5,
        "x_min" : -1,
        "axes_color" : BLUE,
        "y_labeled_nums": range(0,33,8),
        "x_labeled_nums": range(0,6,1),
        "x_label_decimal":1,
        "y_label_direction": RIGHT,
        "x_label_direction": RIGHT,
        "y_label_decimal":3
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : 2**x,
                                    color = GREEN,
                                    x_min = -1,
                                    x_max = 5.5
                                    )
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()

class Plot2(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        func_graph2=self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)

        self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2),ShowCreation(two_pi))

    def func_to_graph(self,x):
        return np.cos(x)

    def func_to_graph2(self,x):
        return np.sin(x)
