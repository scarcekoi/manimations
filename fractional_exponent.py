from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha.colors
macchiato = PALETTE.macchiato.colors
frappe = PALETTE.frappe.colors
latte = PALETTE.latte.colors

class five_shortcut(Scene):
    def construct(self):
        a = MathTex(r"\text{If }a^{\frac{3}{2}}=64\text{, what is value of }\sqrt{a}",  color = mocha.text.hex)
        self.wait(1)