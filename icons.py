from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha
macchiato = PALETTE.macchiato
frappe = PALETTE.frappe
latte = PALETTE.latte

class archlinux(Scene):
    def construct(self):
        m = SVGMobject("./icons/archlinux", color=mocha.colors.text.hex).shift(UP)
        t = Text("Arch Linux", color=mocha.colors.text.hex).next_to(m, DOWN)
        self.play(DrawBorderThenFill(m, run_time=5), Write(t))