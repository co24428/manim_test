### /manim/manimlib/animation/fading.py

<hr>

#### FADE_LAG
~~~
DEFAULT_FADE_LAG_RATIO = 0
~~~

#### FadeOut & FadeIn
~~~
class FadeOut(Transform):
    CONFIG = {
        "remover": True,
        "lag_ratio": DEFAULT_FADE_LAG_RATIO,
    }

    def create_target(self):
        return self.mobject.copy().fade(1)

    def clean_up_from_scene(self, scene=None):
        super().clean_up_from_scene(scene)
        self.interpolate(0)
        
class FadeIn(Transform):
    CONFIG = {
        "lag_ratio": DEFAULT_FADE_LAG_RATIO,
    }

    def create_target(self):
        return self.mobject

    def create_starting_mobject(self):
        start = super().create_starting_mobject()
        start.fade(1)
        if isinstance(start, VMobject):
            start.set_stroke(width=0)
            start.set_fill(opacity=0)
        return start
~~~
스르륵 나오기 & 스르륵 사라지기

- example
~~~
self.play(FadeIn(line))
self.play(FadeOut(line))
~~~

#### FadeInFrom
~~~
class FadeInFrom(Transform):
    CONFIG = {
        "direction": DOWN,
        "lag_ratio": DEFAULT_ANIMATION_LAG_RATIO,
    }

    def __init__(self, mobject, direction=None, **kwargs):
        if direction is not None:
            self.direction = direction
        super().__init__(mobject, **kwargs)

    def create_target(self):
        return self.mobject.copy()

    def begin(self):
        super().begin()
        self.starting_mobject.shift(self.direction)
        self.starting_mobject.fade(1)

class FadeInFromDown(FadeInFrom):
    """
    Identical to FadeInFrom, just with a name that
    communicates the default
    """
    CONFIG = {
        "direction": DOWN,
        "lag_ratio": DEFAULT_ANIMATION_LAG_RATIO,
    }
~~~
해당 방향에서 스르륵 등장한다.  
default값이 DOWN,  
이를 위한 명시적인 함수가 **FadeInFromDown**

- example
~~~
self.play(FadeInFrom(line1))
self.play(FadeInFrom(line2, LEFT))
self.play(FadeInFromDown(line3))
~~~

#### FadeOutAndShift
~~~
class FadeOutAndShift(FadeOut):
    CONFIG = {
        "direction": DOWN,
    }

    def __init__(self, mobject, direction=None, **kwargs):
        if direction is not None:
            self.direction = direction
        super().__init__(mobject, **kwargs)

    def create_target(self):
        target = super().create_target()
        target.shift(self.direction)
        return target

class FadeOutAndShiftDown(FadeOutAndShift):
    """
    Identical to FadeOutAndShift, just with a name that
    communicates the default
    """
    CONFIG = {
        "direction": DOWN,
    }
~~~
해당 방향으로 스르륵 사라진다.  
default값이 DOWN,  
이를 위한 명시적인 함수가 **FadeOutAndShiftDown**

- example
~~~
self.play(FadeOutAndShift(line3, RIGHT))
self.play(FadeOutAndShift(line2, UP))
self.play(FadeOutAndShiftDown(line1))
~~~

#### FadeInFromPoint
~~~
class FadeInFromPoint(FadeIn):
    def __init__(self, mobject, point, **kwargs):
        self.point = point
        super().__init__(mobject, **kwargs)

    def create_starting_mobject(self):
        start = super().create_starting_mobject()
        start.scale(0)
        start.move_to(self.point)
        return start
~~~
특정포인트로부터 스르륵 등장한다.  
크게 의미있는지는 모르것다.

- example
~~~
self.play(FadeInFromPoint(line, point1))
~~~
#### FadeInFromLarge
~~~
class FadeInFromLarge(FadeIn):
    CONFIG = {
        "scale_factor": 2,
    }

    def __init__(self, mobject, scale_factor=2, **kwargs):
        if scale_factor is not None:
            self.scale_factor = scale_factor
        super().__init__(mobject, **kwargs)

    def create_starting_mobject(self):
        start = super().create_starting_mobject()
        start.scale(self.scale_factor)
        return start
~~~
지정한 배수의 사이즈에서 원본사이즈로 줄어들거나 커진다.  
default 값은 2배이고 두번째 파라미터에 넣어주면 된다.

- example
~~~
self.play(FadeInFromLarge(circle)) # default = 2
self.play(FadeInFromLarge(square, 3))
~~~

<hr>
- 아래는 VMobject에 대해서 알고난 후에 진행

#### VFadeIn & VFadeOut
~~~
class VFadeIn(Animation):
    """
    VFadeIn and VFadeOut only work for VMobjects,
    """
    CONFIG = {
        "suspend_mobject_updating": False,
    }

    def interpolate_submobject(self, submob, start, alpha):
        submob.set_stroke(
            opacity=interpolate(0, start.get_stroke_opacity(), alpha)
        )
        submob.set_fill(
            opacity=interpolate(0, start.get_fill_opacity(), alpha)
        )

class VFadeOut(VFadeIn):
    CONFIG = {
        "remover": True
    }

    def interpolate_submobject(self, submob, start, alpha):
        super().interpolate_submobject(submob, start, 1 - alpha)
~~~

#### VFadeInThenOut
~~~
class VFadeInThenOut(VFadeIn):
    CONFIG = {
        "rate_func": there_and_back,
        "remover": True,
    }
~~~






