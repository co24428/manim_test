### /manim/manimlib/animation/growing.py

<hr>

#### GrowFromPoint
~~~
class GrowFromPoint(Transform):
    CONFIG = {
        "point_color": None,
    }

    def __init__(self, mobject, point, **kwargs):
        self.point = point
        super().__init__(mobject, **kwargs)

    def create_target(self):
        return self.mobject

    def create_starting_mobject(self):
        start = super().create_starting_mobject()
        start.scale(0)
        start.move_to(self.point)
        if self.point_color:
            start.set_color(self.point_color)
        return start
~~~
특정 포인트로부터 객체를 그린다  
line의 경우, 가까운 좌표에서 시작되게 그려진다.  
도형의 경우, 포인트에서 날아와서 그려진다.
<br>

point_color는 RED를 줘도 눈에 보이진 않는다.

- example
~~~
# line
self.play(GrowFromPoint(line,point1))
# circle
self.play(GrowFromPoint(circle1,point3))
~~~

#### GrowFromCenter
~~~
class GrowFromCenter(GrowFromPoint):
    def __init__(self, mobject, **kwargs):
        point = mobject.get_center()
        super().__init__(mobject, point, **kwargs)
~~~
객체의 가운데를 구한 후에  
그 포인트에서 객체를 그린다.

- example
~~~
self.play(GrowFromCenter(circle)
~~~

#### GrowFromEdge
~~~
class GrowFromEdge(GrowFromPoint):
    def __init__(self, mobject, edge, **kwargs):
        point = mobject.get_critical_point(edge)
        super().__init__(mobject, point, **kwargs)
~~~
edge : LEFT, RIGHT, UP, DOWN  
객체의 edge에서 시작해서 그려진다.  
방향 조합(대각선)도 가능하다.

- example
~~~
self.play(GrowFromEdge(square, DOWN))
self.play(GrowFromEdge(circle, UP))
self.play(GrowFromEdge(line, UP+RIGHT))
~~~

#### GrowArrow
~~~
class GrowArrow(GrowFromPoint):
    def __init__(self, arrow, **kwargs):
        point = arrow.get_start()
        super().__init__(arrow, point, **kwargs)
~~~
Arrow()객체만을 위한 함수이다.  
화살표 방향으로 그려진다.

- example
~~~
self.play(GrowArrow(arrow1))
~~~

#### SpinInFromNothing
~~~
class SpinInFromNothing(GrowFromCenter):
    CONFIG = {
        "path_arc": PI,
    }
~~~
GrowFromCenter 동작에서 CONFIG를 통해서 회전시키면서 등장한다.  
path_arc를 조정해주면 바꿔줄 수 있을 것이다.

- example
~~~
self.play(SpinInFromNothing(circle))
self.play(SpinInFromNothing(square))
self.play(SpinInFromNothing(line))
~~~