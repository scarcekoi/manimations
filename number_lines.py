from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha.colors
macchiato = PALETTE.macchiato.colors
frappe = PALETTE.frappe.colors
latte = PALETTE.latte.colors

class number_lines(Scene):
    def construct(self):
        def color_numbers(number_line, color):
            for num in number_line.numbers:
                num.set_color(color)
        
        l0 = NumberLine(
            x_range=[-5, 5, 1],
            length=13,
            color=mocha.text.hex,
            numbers_with_elongated_ticks=[-5, 0, 5],
            include_numbers=True,
            label_direction=DOWN
        )
        color_numbers(l0, mocha.text.hex)

        self.play(Write(l0))