### /manim/manimlib/animation/creation.py

<hr>

#### ShowPartial
~~~
class ShowPartial(Animation):
    """
    Abstract class for ShowCreation and ShowPassingFlash
    """

    def interpolate_submobject(self, submob, start_submob, alpha):
        submob.pointwise_become_partial(
            start_submob, *self.get_bounds(alpha)
        )

    def get_bounds(self, alpha):
        raise Exception("Not Implemented")
~~~
ShowCreation과 ShowPassingFlash를 위한 추상클래스  
직접 부를 일은 없을 것같다.

#### ShowCreation
~~~
class ShowCreation(ShowPartial):
    CONFIG = {
        "lag_ratio": 1,
    }

    def get_bounds(self, alpha):
        return (0, alpha)
~~~
포인트에서 포인트로 등장시킨다.  
GrowFromPoint를 일반화시킨 것과 같다.  
line 나타낼 때 종종 쓰일 것으로 확인.

#### Uncreate
~~~
class Uncreate(ShowCreation):
    CONFIG = {
        "rate_func": lambda t: smooth(1 - t),
        "remover": True
    }
~~~
조립은 해체의 역순  
ShowCreate의 반대로 동작하며 사라지게 한다.

#### DrawBorderThenFill
- \_\_init\_\_ 을 보면 VMobject를 받는다.  
  나중에 다시 온다!
  
~~~
class DrawBorderThenFill(Animation):
    CONFIG = {
        "run_time": 2,
        "rate_func": double_smooth,
        "stroke_width": 2,
        "stroke_color": None,
        "draw_border_animation_config": {},
        "fill_animation_config": {},
    }

    def __init__(self, vmobject, **kwargs):
        self.check_validity_of_input(vmobject)
        super().__init__(vmobject, **kwargs)

    def check_validity_of_input(self, vmobject):
        if not isinstance(vmobject, VMobject):
            raise Exception(
                "DrawBorderThenFill only works for VMobjects"
            )

    def begin(self):
        self.outline = self.get_outline()
        super().begin()

    def get_outline(self):
        outline = self.mobject.copy()
        outline.set_fill(opacity=0)
        for sm in outline.family_members_with_points():
            sm.set_stroke(
                color=self.get_stroke_color(sm),
                width=self.stroke_width
            )
        return outline

    def get_stroke_color(self, vmobject):
        if self.stroke_color:
            return self.stroke_color
        elif vmobject.get_stroke_width() > 0:
            return vmobject.get_stroke_color()
        return vmobject.get_color()

    def get_all_mobjects(self):
        return [*super().get_all_mobjects(), self.outline]

    def interpolate_submobject(self, submob, start, outline, alpha):
        index, subalpha = integer_interpolate(0, 2, alpha)
        if index == 0:
            submob.pointwise_become_partial(
                outline, 0, subalpha
            )
            submob.match_style(outline)
        else:
            submob.interpolate(outline, start, subalpha)
~~~
테두리부터 그리고 채우면서 그려나간다.  
Write를 위해 사용되는 것으로 확인된다.

#### Write
~~~
class Write(DrawBorderThenFill):
    CONFIG = {
        # To be figured out in
        # set_default_config_from_lengths
        "run_time": None,
        "lag_ratio": None,
        "rate_func": linear,
    }

    def __init__(self, mobject, **kwargs):
        digest_config(self, kwargs)
        self.set_default_config_from_length(mobject)
        super().__init__(mobject, **kwargs)

    def set_default_config_from_length(self, mobject):
        length = len(mobject.family_members_with_points())
        if self.run_time is None:
            if length < 15:
                self.run_time = 1
            else:
                self.run_time = 2
        if self.lag_ratio is None:
            self.lag_ratio = min(4.0 / length, 0.2)
~~~
텍스트(TextMobject)는 확실하게 보인다.  
테두리부터 그리고 속을 채워나간다.(좌측 > 우측)  
도형은 잘 감이 안온다. 두께가 있으면 보일 것으로 추측된다.

#### ShowIncreasingSubsets
- group 객체는 무엇인가..?

~~~
class ShowIncreasingSubsets(Animation):
    CONFIG = {
        "suspend_mobject_updating": False,
        "int_func": np.floor,
    }

    def __init__(self, group, **kwargs):
        self.all_submobs = list(group.submobjects)
        super().__init__(group, **kwargs)

    def interpolate_mobject(self, alpha):
        n_submobs = len(self.all_submobs)
        index = int(self.int_func(alpha * n_submobs))
        self.update_submobject_list(index)

    def update_submobject_list(self, index):
        self.mobject.submobjects = self.all_submobs[:index]
~~~

#### ShowSubmobjectsOneByOne
~~~
class ShowSubmobjectsOneByOne(ShowIncreasingSubsets):
    CONFIG = {
        "int_func": np.ceil,
    }

    def __init__(self, group, **kwargs):
        new_group = Group(*group)
        super().__init__(new_group, **kwargs)

    def update_submobject_list(self, index):
        # N = len(self.all_submobs)
        if index == 0:
            self.mobject.submobjects = []
        else:
            self.mobject.submobjects = self.all_submobs[index - 1]
~~~

#### AddTextWordByWord
~~~
# TODO, this is broken...
class AddTextWordByWord(Succession):
    CONFIG = {
        # If given a value for run_time, it will
        # override the time_per_char
        "run_time": None,
        "time_per_char": 0.06,
    }

    def __init__(self, text_mobject, **kwargs):
        digest_config(self, kwargs)
        tpc = self.time_per_char
        anims = it.chain(*[
            [
                ShowIncreasingSubsets(word, run_time=tpc * len(word)),
                Animation(word, run_time=0.005 * len(word)**1.5),
            ]
            for word in text_mobject
        ])
        super().__init__(*anims, **kwargs)
~~~
그냥 좌측부터 우측으로 써지는 느낌이다.  
뭔가 버벅이는 것처럼 보여진다. 
