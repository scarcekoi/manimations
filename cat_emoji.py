import os
from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha.colors

class cat_emoji(MovingCameraScene):
    def construct(self):
        # Background color
        self.camera.background_color = mocha.crust.hex

        # Load SVGs
        folder = "./cat_emojis"
        files = sorted(f for f in os.listdir(folder) if f.endswith(".svg"))
        emojis = VGroup(*[SVGMobject(os.path.join(folder, f)).scale(1.5) for f in files])
        emojis.arrange(RIGHT, buff=1.0)
        self.add(emojis)

        # Camera frame width
        frame_width = self.camera.frame.width

        # Start just off left edge of first emoji
        start_pos = emojis.get_left() - RIGHT * (frame_width / 2)

        # End past the last emoji so it's offscreen to the left
        end_pos = emojis.get_right() + RIGHT * (frame_width / 2)  # move beyond the rightmost emoji

        # Set camera to start
        self.camera.frame.move_to(start_pos)

        # Animate camera moving across emojis
        self.play(
            self.camera.frame.animate.move_to(end_pos),
            run_time=2.5,  # adjust speed
            rate_func=linear
        )
        self.wait()