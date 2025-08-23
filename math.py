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
        self.wait(1)
        self.play(Transform(e, e2))
        self.wait(1)
        self.play(Transform(e, e3))
        self.wait(1)
        self.play(Transform(e, e4))
        self.wait(1)
        self.play(e.animate.shift(UP))
        self.wait(1)
        self.play(Write(l))
        self.wait(1)
        self.play(l.numbers[2].animate.set_color(mocha.blue.hex))
        self.play(Create(oc), GrowArrow(a))
        self.wait(5)
        self.play(Uncreate(a), Uncreate(oc))
        self.play(l.numbers[2].animate.set_color(mocha.text.hex), Unwrite(l))
        self.play(Unwrite(e))
        self.wait(0.5)