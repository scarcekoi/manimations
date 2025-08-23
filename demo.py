from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha.colors
macchiato = PALETTE.macchiato.colors
frappe = PALETTE.frappe.colors
latte = PALETTE.latte.colors

class demo(Scene):
    def construct(self):
        s = Circle(radius=0.5, stroke_width=10, color=mocha.red.hex, fill_opacity=0.3)
        r = SurroundingRectangle(s, color=mocha.blue.hex, corner_radius=0.1)
        t = Text("Manim", color=mocha.text.hex).next_to(r, UP, buff=0.5)

        self.play(Write(s))
        self.play(DrawBorderThenFill(r))
        self.play(Write(t))

        sr = VGroup(s, r)

        self.play(t.animate.move_to([-4, 0, 0]), sr.animate.move_to([4, 0, 0]))
