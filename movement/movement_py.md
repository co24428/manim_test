### /manim/manimlib/animation/movement.py

<hr>

#### MoveAlongPath
~~~
class MoveAlongPath(Animation):
    CONFIG = {
        "suspend_mobject_updating": False,
    }

    def __init__(self, mobject, path, **kwargs):
        self.path = path
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        point = self.path.point_from_proportion(alpha)
        self.mobject.move_to(point)
~~~
Line이나 도형의 궤도를 따라 움직인다.  
시작과 끝에서 느리고 중간에서 빠르게 움직인다.  
run_time=n을 주어서 시간을 조절할 수 있다.  
각각을 run_time을 다르게 주려했으나 그 부분은 실패를 했다.

<hr>
### 객체에 대한 이해가 필요하다..
### 나중에 다시 해보자

#### Homotopy
~~~
class Homotopy(Animation):
    CONFIG = {
        "run_time": 3,
        "apply_function_kwargs": {},
    }

    def __init__(self, homotopy, mobject, **kwargs):
        """
        Homotopy is a function from
        (x, y, z, t) to (x', y', z')
        """
        self.homotopy = homotopy
        super().__init__(mobject, **kwargs)

    def function_at_time_t(self, t):
        return lambda p: self.homotopy(*p, t)

    def interpolate_submobject(self, submob, start, alpha):
        submob.points = start.points
        submob.apply_function(
            self.function_at_time_t(alpha),
            **self.apply_function_kwargs
        )
~~~

#### SmoothedVectorizedHomotopy
~~~
class SmoothedVectorizedHomotopy(Homotopy):
    def interpolate_submobject(self, submob, start, alpha):
        Homotopy.interpolate_submobject(self, submob, start, alpha)
        submob.make_smooth()
~~~

#### ComplexHomotopy
~~~
class ComplexHomotopy(Homotopy):
    def __init__(self, complex_homotopy, mobject, **kwargs):
        """
        Complex Hootopy a function Cx[0, 1] to C
        """
        def homotopy(x, y, z, t):
            c = complex_homotopy(complex(x, y), t)
            return (c.real, c.imag, z)
        Homotopy.__init__(self, homotopy, mobject, **kwargs)
~~~

#### PhaseFlow
~~~
class PhaseFlow(Animation):
    CONFIG = {
        "virtual_time": 1,
        "rate_func": linear,
        "suspend_mobject_updating": False,
    }

    def __init__(self, function, mobject, **kwargs):
        self.function = function
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        if hasattr(self, "last_alpha"):
            dt = self.virtual_time * (alpha - self.last_alpha)
            self.mobject.apply_function(
                lambda p: p + dt * self.function(p)
            )
        self.last_alpha = alpha
~~~




