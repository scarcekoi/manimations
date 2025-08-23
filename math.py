from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha.colors

class one(Scene):
    def construct(self):
        max_width = self.camera.frame_width * 0.9
        max_height = self.camera.frame_height * 0.2

        p = Tex("1+1", color=mocha.text.hex)
        scale_factor = min(max_width / p.width, max_height / p.height)
        p.scale(scale_factor)

        s = Tex("2", color=mocha.text.hex)
        scale_factor = min(max_width / s.width, max_height / s.height)
        s.scale(scale_factor)

        e = Tex("1+1=2", color=mocha.text.hex)
        scale_factor = min(max_width / e.width, max_height / e.height)
        e.scale(scale_factor)

        p.move_to(ORIGIN)
        s.move_to(ORIGIN)
        e.move_to(ORIGIN)

        self.play(Write(p))
        self.wait(0.5)
        self.play(Transform(p, s))
        self.wait(0.5)
        self.play(Transform(p, e))
        self.wait(1)

class two(Scene):
    def construct(self):
        def color_numbers(number_line, color):
            for num in number_line.numbers:
                num.set_color(color)
        
        e = MathTex(r"3-1x<-5", color=mocha.text.hex)
        e1 = MathTex(r"3-3-1x<-5-3", color=mocha.text.hex)
        e2 = MathTex(r"-1x<-8", color=mocha.text.hex)
        e3 = MathTex(r"\frac{-1x}{-1}<\frac{-8}{-1}", color=mocha.text.hex)
        e4 = MathTex(r"x>8", color=mocha.text.hex)
        l = NumberLine(
            x_range=[0, 20, 4],
            length=8,
            color=mocha.text.hex,
            numbers_with_elongated_ticks=[0, 10],
            include_numbers=True,
            label_direction=DOWN
        )
        color_numbers(l, mocha.text.hex)

        lx = l.n2p(8)

        oc = Circle(radius=0.1, color=mocha.blue.hex)
        oc.move_to(lx)

        a = Arrow(
            start=lx + RIGHT * 0.1,
            end=l.n2p(20),
            buff=0,
            color=mocha.blue.hex
        )

        self.play(Transform(e, e1))
        self.play(Transform(e, e2))
        self.play(Transform(e, e3))
        self.play(Transform(e, e4))
        self.play(e.animate.shift(UP))
        self.play(Write(l), l.numbers[2].animate.set_color(mocha.blue.hex))
        self.play(Create(oc), GrowArrow(a))
        self.wait(5)
        self.play(Uncreate(a), Uncreate(oc))
        self.play(l.numbers[2].animate.set_color(mocha.text.hex), Unwrite(l))
        self.play(Unwrite(e))
        self.wait(0.5)

class three(Scene):
    def construct(self):
        def color_numbers(number_line, color):
            for num in number_line.numbers:
                num.set_color(color)
        
        e0 = MathTex(r"-3\le2x-1<5", color=mocha.text.hex)
        e1 = MathTex(r"-3+1\le2x-1+1<5+1", color=mocha.text.hex)
        e2 = MathTex(r"-2\le2x-1+1<5+1", color=mocha.text.hex)
        e3 = MathTex(r"-2\le2x<5+1", color=mocha.text.hex)
        e4 = MathTex(r"-2\le2x<6", color=mocha.text.hex)
        e5 = MathTex(r"\frac{-2}{2}\le\frac{2x}{2}<\frac{6}{2}", color=mocha.text.hex)
        e6 = MathTex(r"-2\le\frac{2x}{2}<\frac{6}{2}", color=mocha.text.hex)
        e7 = MathTex(r"-2\le x<\frac{6}{2}", color=mocha.text.hex)
        e8 = MathTex(r"-1\le x<3", color=mocha.text.hex)
        e9 = MathTex(r"x\in[-1,3)", color=mocha.text.hex)

        for e in [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9]:
            e.scale(1.5)

        l = NumberLine(
            x_range=[-2, 4, 1],
            length=8 * 1.5,
            color=mocha.text.hex,
            include_numbers=True,
            label_direction=DOWN
        )
        color_numbers(l, mocha.text.hex)
        l.next_to(e0, DOWN, buff=1.5)

        left_dot = Dot(l.n2p(-1), color=mocha.blue.hex).scale(1.5)
        right_dot = Dot(l.n2p(3), color=mocha.blue.hex).scale(1.5)
        right_dot.set_fill(color=mocha.blue.hex, opacity=0)  # open circle
        interval_line = Line(l.n2p(-1), l.n2p(3), color=mocha.blue.hex, stroke_width=6*1.5)

        self.play(Write(e0))
        self.wait(1)
        self.play(Transform(e0, e1))
        self.wait(1)
        self.play(Transform(e0, e2))
        self.wait(1)
        self.play(Transform(e0, e3))
        self.wait(1)
        self.play(Transform(e0, e4))
        self.wait(1)
        self.play(Transform(e0, e5))
        self.wait(1)
        self.play(Transform(e0, e6))
        self.wait(1)
        self.play(Transform(e0, e7))
        self.wait(1)
        self.play(Transform(e0, e8))
        self.wait(1)
        self.play(e0.animate.shift(UP*1.5), Write(e9.shift(UP*2.5)))
        self.wait(0.5)
        self.play(Create(l))
        self.wait(1)
        self.play(Create(interval_line), FadeIn(left_dot), FadeIn(right_dot))
        self.wait(2)

        self.play(Uncreate(interval_line), FadeOut(left_dot), FadeOut(right_dot))
        self.play(Uncreate(l))
        self.play(Unwrite(e0), Unwrite(e9))
        self.wait(1)