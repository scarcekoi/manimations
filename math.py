from manim import *
from catppuccin import PALETTE
from itertools import combinations

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
<<<<<<< HEAD
    def construct(self):
=======
    def construct(self):
        # Top text
        t = Paragraph(
            "Positions of the armies.",
            "Armies A1 and A2 cannot see one another directly,",
            "so need to communicate by messengers,",
            "but their messengers may be captured by army B.",
            color=mocha.text.hex
        ).scale(0.5).to_edge(UP)

        # Horizontal shift for the whole wave
        x_shift = -4

        # Sine wave (no axes)
        graph = VMobject()
        graph_points = [np.array([x + x_shift, np.sin(2*x), 0]) for x in np.linspace(0, 3*PI, 200)]
        graph.set_points_smoothly(graph_points)
        graph.set_color(mocha.blue.hex)

        # Valleys projected to y=0
        x1 = 3*PI/4 + x_shift
        x2 = 7*PI/4 + x_shift
        x3 = 11*PI/4 + x_shift
        valley_dots = [
            Dot([x1, 0, 0], color=mocha.red.hex),
            Dot([x2, 0, 0], color=mocha.red.hex),
            Dot([x3, 0, 0], color=mocha.red.hex)
        ]
        labels = [
            MathTex("A1").next_to(valley_dots[0], DOWN),
            MathTex("B").next_to(valley_dots[1], DOWN),
            MathTex("A2").next_to(valley_dots[2], DOWN)
        ]

        # Moving dot and label
        moving_dot = Dot([0 + x_shift, 0, 0], color=mocha.peach.hex)
        message_label = always_redraw(
            lambda: MathTex("Message", color=mocha.peach.hex).next_to(moving_dot, DOWN)
        )

        self.add(graph, *valley_dots, *labels, moving_dot, message_label)

        # Dot movement along wave
        speed_factor = 0.1
        def update_dot(dot, dt):
            if not hasattr(dot, "time"):
                dot.time = 0
                dot.direction = 1
                dot.disappeared = False  # Track if dot + label disappeared

            # Stop moving if disappeared
            if dot.disappeared:
                dot.set_opacity(0)
                return

            dot.time += dt * dot.direction * speed_factor

            # Forward direction
            if dot.time >= 1:
                dot.time = 1
                dot.direction = -1

            # Backward direction
            if dot.time <= 0:
                dot.time = 0
                dot.direction = 1

            # Map time to x
            x_val = dot.time * 3*PI + x_shift
            y_val = np.sin(2*(dot.time * 3*PI))
            dot.move_to([x_val, y_val, 0])

            # Disappear dot + label at B on the first trip (going right)
            if dot.direction == 1 and not dot.disappeared and abs(x_val - x2) < 0.05:
                dot.disappeared = True
                dot.set_opacity(0)
                message_label.set_opacity(0)

        moving_dot.add_updater(update_dot)

        # Animate
        self.play(Write(t, run_time=5))
        self.wait(10)
        moving_dot.remove_updater(update_dot)
>>>>>>> 4963ecc (feat(five): 2 generals problem)
