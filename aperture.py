from manim import *
from catppuccin import PALETTE
import re
import html

mocha = PALETTE.mocha.colors

class aperture(Scene):
    def construct(self):
        s = SVGMobject("./icons/aperture-profile-mocha-blue.svg").scale(7.115)

        self.play(Write(s, run_time=2.5))