from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha
macchiato = PALETTE.macchiato
frappe = PALETTE.frappe
latte = PALETTE.latte

class demo(Scene):
    def construct(self):
        s = Circle(radius=0.5, stroke_width=10, color=mocha.colors.red.hex, fill_opacity=0.3)
        r = SurroundingRectangle(s, color=mocha.colors.blue.hex, corner_radius=0.1)
        t = Text("Manim", color=mocha.colors.text.hex).next_to(r, UP, buff=0.5)

        self.play(Write(s))
        self.play(DrawBorderThenFill(r))
        self.play(Write(t))

        sr = VGroup(s, r)

        self.play(t.animate.move_to([-4, 0, 0]), sr.animate.move_to([4, 0, 0]))
