from manim import *
from MF_Tools import *
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
        e6 = MathTex(r"-1\le\frac{2x}{2}<\frac{6}{2}", color=mocha.text.hex)
        e7 = MathTex(r"-1\le x<\frac{6}{2}", color=mocha.text.hex)
        e8 = MathTex(r"-1\le x<3", color=mocha.text.hex)
        e9 = MathTex(r"x\in[-1,3)", color=mocha.text.hex)
        e10 = MathTex(r"-1\le x<3=x\in[-1,3)", color=mocha.text.hex)

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
        right_dot.set_fill(color=mocha.blue.hex, opacity=0)
        interval_line = Line(l.n2p(-1), l.n2p(3), color=mocha.blue.hex, stroke_width=6*1.5)

        self.play(Write(e0))
        self.play(Transform(e0, e1))
        self.play(Transform(e0, e2))
        self.play(Transform(e0, e3))
        self.play(Transform(e0, e4))
        self.play(Transform(e0, e5))
        self.play(Transform(e0, e6))
        self.play(Transform(e0, e7))
        self.play(Transform(e0, e8))
        self.play(Transform(e0, e9))
        self.play(Transform(e0, e10))
        self.play(e0.animate.shift(UP))
        self.play(Create(l))
        self.play(Create(interval_line), FadeIn(left_dot), FadeIn(right_dot))
        self.wait(2)

        self.play(Uncreate(interval_line), FadeOut(left_dot), FadeOut(right_dot))
        self.play(Uncreate(l))
        self.play(Unwrite(e0))
        self.wait(1)

class four(Scene):
    def construct(self):
        eq = MathTex("1", "+", "1", "=", color=mocha.text.hex).scale(2)
        one_left, plus, one_right, equal = eq

        self.play(Write(eq))
        self.wait(0.6)

        top = MathTex("-", color=mocha.text.hex).scale(4)
        bottom = MathTex("-", color=mocha.text.hex).scale(4)

        top.stretch(1.1, 0)
        bottom.stretch(1.1, 0)

        top.move_to(plus.get_top() + UP * 0.3)
        bottom.move_to(plus.get_bottom() + DOWN * 0.3)

        left_target = MathTex("|", color=mocha.text.hex).scale(3)
        left_target.stretch(0.9, 1)
        right_target = MathTex("|", color=mocha.text.hex).scale(3)
        right_target.stretch(0.9, 1)
        left_target.move_to(plus.get_left() + LEFT * 0.3)
        right_target.move_to(plus.get_right() + RIGHT * 0.3)

        self.play(
            Transform(one_left, left_target),
            Transform(one_right, right_target),
            plus.animate.scale(2),
            Transform(equal, VGroup(top, bottom)),
            run_time=1.2,
            rate_func=smooth,
        )

        self.wait(1.2)

class five(Scene):
    def construct(self):
        e0 = MathTex(r"x\times y=z", color=mocha.text.hex).scale(4)
        e1 = MathTex(r"xy=z", color=mocha.text.hex).scale(4)
        e2 = MathTex(r"\frac{xy}{y}=\frac{z}{y}", color=mocha.text.hex).scale(4)
        e3 = MathTex(r"x=\frac{z}{y}", color=mocha.text.hex).scale(4)
        e4 = MathTex(r"z=xy", color=mocha.text.hex).scale(4)

        self.play(Write(e0))
        self.play(Transform(e0, e1))
        self.play(Transform(e0, e2))
        self.play(Transform(e0, e3))
        self.play(Transform(e0, e4))
        self.play(Write(e3), e0.animate.to_edge(DOWN), e3.animate.to_edge(UP))
        self.wait(1)
        self.play(Unwrite(e0), Unwrite(e3))
        self.wait()

class six(Scene):
    def construct(self):
        e0 = MathTex(r"\frac{45}{3}-27\Big(5\times\big[7\times4\big]\Big)>67", color=mocha.text.hex)
        e1 = MathTex(r"15-27\Big(5\times\big[7\times4\big]\Big)>67", color=mocha.text.hex)
        e2 = MathTex(r"15-27\Big(5\times28\Big)>67", color=mocha.text.hex)
        e3 = MathTex(r"15-27\times140>67", color=mocha.text.hex)
        e4 = MathTex(r"15-3780>67", color=mocha.text.hex)
        e5 = MathTex(r"-3765>67", color=mocha.text.hex)
        e6 = MathTex(r"\frac{45}{3}-27\Big(5\times\big[7\times4\big]\Big)>67", color=mocha.text.hex)
        t = Text("False", color=mocha.text.hex)
        t1 = Text("Is", color=mocha.text.hex)

        self.play(Write(e0))
        self.play(Transform(e0, e1))
        self.play(Transform(e0, e2))
        self.play(TransformByGlyphMap(e0, e3))
        self.play(Transform(e0, e4))
        self.play(Transform(e0, e5))
        self.play(Write(t.shift(UP)), Write(e6.shift(UP*3)), Write(t1.shift(UP*2)))
        self.play(t.animate.set_color(mocha.red.hex))
        self.wait()
        self.play(Unwrite(e0), Unwrite(t), Unwrite(t1), Unwrite(e6))
        self.wait()

class seven(Scene):
    def construct(self):
        e0 = MathTex(r"73\left(\frac{57}{63}\right)-27=39.0476", color=mocha.text.hex)
        e1 = MathTex(r"73\left(\frac{19}{21}\right)-27=39.0476", color=mocha.text.hex)
        e2 = MathTex(r"\frac{73\times19}{21}-27=39.0476", color=mocha.text.hex)
        e3 = MathTex(r"\frac{1387}{21}-27=39.0476", color=mocha.text.hex)
        e4 = MathTex(r"\frac{1387}{21}-\frac{567}{21}=39.0476", color=mocha.text.hex)
        e5 = MathTex(r"\frac{820}{21}=39.0476", color=mocha.text.hex)
        e6 = MathTex(r"39.0476=39.0476", color=mocha.text.hex)
        t = Text("True", color=mocha.text.hex)

        self.play(Write(e0))
        self.play(Transform(e0, e1))
        self.play(Transform(e0, e2))
        self.play(TransformByGlyphMap(e2, e3,
            ([0,2,4,5], [0,1,2,3]),
            ([3,6], [4]),
            ([7,8], [5,6]),
            ([9], [7]),
            ([10], [8]),
            ([11], [9]),
            ([12], [10]),
            ([13], [11]),
            ([14], [12]),
            ([15], [13]),
            ([5], [4]),
            ([17], [16])
        ), FadeOut(e0, scale=0.5, run_time=0.0001))
        self.play(TransformByGlyphMap(e3, e4,
        ([8,9], [8,9,10,11,12,13]),
        ([10], [14]),
        ([11,12,13,14,15,16,17], [15,16,17,18,19,20,21])
        ))
        self.play(TransformByGlyphMap(e4, e5,
        ([0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5]),
        ([10], [6]),
        ([11,12,13,14,15,16,17], [7,8,9,10,11,12,13])
        ))
        self.play(TransformByGlyphMap(e3, e6))
        self.play(Write(t.shift(UP)))
        self.play(t.animate.set_color(mocha.green.hex))
        self.wait()
        self.play(Unwrite(e3), Unwrite(t))

class eight(MovingCameraScene):
    def construct(self):
        q = Text("Which One Is Greater?", color=mocha.text.hex)
        a0 = MathTex(r"8^{4}\text{ or }4^{8}", color=mocha.text.hex)
        a01 = a0.copy()
        a1 = MathTex(r"8^{4}", color=mocha.text.hex)
        a2 = MathTex(r"4^{8}", color=mocha.text.hex)
        a3 = MathTex(r"4^{8}\text{ Is Greater}", color=mocha.text.hex)

        h = MathTex(r"(x^{a})^{b}=x^{ab}")

        e0 = MathTex(r"8=2\times2\times2", color=mocha.text.hex)
        e1 = MathTex(r"4=2\times2", color=mocha.text.hex)
        e2 = MathTex(r"2^{3}", color=mocha.text.hex)
        e3 = MathTex(r"2^{2}", color=mocha.text.hex)
        e4 = MathTex(r"(2^{3})^{4}", color=mocha.text.hex)
        e5 = MathTex(r"(2^{2})^{8}", color=mocha.text.hex)
        e6 = MathTex(r"2^{3\times4}", color=mocha.text.hex)
        e7 = MathTex(r"2^{2\times8}", color=mocha.text.hex)
        e8 = MathTex(r"2^{12}", color=mocha.text.hex)
        e9 = MathTex(r"2^{16}", color=mocha.text.hex)
        e10 = MathTex(r"12<16", color=mocha.text.hex)

        self.play(Write(q.shift(UP)))
        self.play(Write(a0), Write(a01))
        self.wait(0.1)
        self.play(q.animate.to_edge(UP), Transform(a0, a1.to_edge(UP + LEFT)), Transform(a01, a2.to_edge(UP + RIGHT)))
        self.play(Write(e0), e0.animate.to_edge(UP*2.5 + LEFT))
        self.play(Write(e1), e1.animate.to_edge(UP*2.5 + RIGHT))
        self.play(Write(e2), e2.animate.to_edge(UP*4.5 + LEFT))
        self.play(Write(e3), e3.animate.to_edge(UP*4.5 + RIGHT))
        self.play(Write(h), h.animate.shift(UP))
        self.play(Write(e4), e4.animate.to_edge(UP*6.5 + LEFT))
        self.play(Write(e5), e5.animate.to_edge(UP*6.5 + RIGHT))
        self.play(Write(e6), e6.animate.to_edge(UP*8.5 + LEFT))
        self.play(Write(e7), e7.animate.to_edge(UP*8.5 + RIGHT))
        self.play(Write(e8), e8.animate.to_edge(UP*10.5 + LEFT))
        self.play(Write(e9), e9.animate.to_edge(UP*10.5 + RIGHT))
        self.play(Unwrite(h), Write(e10))
        self.wait()
        self.play(Unwrite(q), Unwrite(a0), Unwrite(a01), Unwrite(e0), Unwrite(e1), Unwrite(e2), Unwrite(e3), Unwrite(e4), Unwrite(e5), Unwrite(e6), Unwrite(e7), Unwrite(e8), Unwrite(e9), Unwrite(e10))
        self.play(Write(a3))
        self.wait()
        self.play(Unwrite(a3))
        self.wait()

class nine(Scene):
    def construct(self):
        e0 = MathTex(r"100\div\frac{1}{10}\times10")

        pemdas = Text("PEMDAS").scale(1.5)

        # Arrow from M → D (upper-left of M to upper-right of D)
        arrow_md = Arrow(
            start=pemdas[2].get_corner(UL) + UP*0.25,
            end  =pemdas[3].get_corner(UR) + UP*0.25,
            buff=0.0
        )

        # Arrow from A → S (upper-left of A to upper-right of S)
        arrow_as = Arrow(
            start=pemdas[4].get_corner(UL) + UP*0.25,
            end  =pemdas[5].get_corner(UR) + UP*0.25,
            buff=0.0
        )

        self.play(Write(e0))
        self.play(e0.animate.to_edge(UP))
        self.play(Write(pemdas))
        self.play(pemdas.animate.to_edge(DOWN))
        self.play(GrowArrow(arrow_md), GrowArrow(arrow_as))
        self.wait()