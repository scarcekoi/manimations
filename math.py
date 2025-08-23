from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha.colors

class MathScene(Scene):
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
