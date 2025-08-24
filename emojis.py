import os
from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha.colors

class transform_emojis(MovingCameraScene):
    def construct(self):
        self.camera.background_color = mocha.crust.hex

        folder = "./emojis"
        files = sorted(f for f in os.listdir(folder) if f.endswith(".svg"))
        emojis = [SVGMobject(os.path.join(folder, f)).scale(1.5) for f in files]

        # Start with the first emoji in the center
        current = emojis[0]
        self.add(current)
        self.wait(0.5)

        # Transition through the rest using Transform
        for next_emoji in emojis[1:]:
            next_emoji.move_to(current.get_center())
            self.play(Transform(current, next_emoji), run_time=0.5)
            self.wait(0.1)