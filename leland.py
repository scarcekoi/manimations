from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha
macchiato = PALETTE.macchiato
frappe = PALETTE.frappe
latte = PALETTE.latte

# Direct SMuFL codepoint mapping for Leland
LELAND_CODEPOINTS = {
    "gClef": "\uE050",    # Treble clef
    "timeSig4": "\uE084"  # Number 4 in time signatures
}

def leland_symbol(name):
    return LELAND_CODEPOINTS[name]

class leland(Scene):
    def construct(self):
        # Staff parameters
        staff_spacing = 0.3  # vertical gap between lines
        staff_width = 8      # total width of staff

        # Draw the staff lines
        staff_lines = VGroup(*[
            Line(LEFT * staff_width / 2, RIGHT * staff_width / 2)
            .shift(UP * staff_spacing * i)
            for i in range(5)
        ])
        staff_lines.set_stroke(width=3, color=WHITE)

        # Treble clef (Leland font)
        treble = Text(
            leland_symbol("gClef"),
            font="Leland",
            font_size=160
        )
        treble.next_to(staff_lines, LEFT, buff=0.5).shift(DOWN * staff_spacing * 1.5)

        # 4/4 time signature (Leland font)
        four = Text(
            leland_symbol("timeSig4"),
            font="Leland",
            font_size=96
        )
        time_signature = VGroup(four.copy(), four)
        time_signature.arrange(DOWN, buff=0.05)
        time_signature.next_to(treble, RIGHT, buff=0.3).shift(UP * staff_spacing * 0.5)

        # First barline
        first_bar = Line(
            UP * (staff_spacing * 4),
            DOWN * (staff_spacing * 0),
            stroke_width=3,
            color=WHITE
        )
        first_bar.next_to(time_signature, RIGHT, buff=0.3)

        # Example text in Edwin Italic
        composer = Text(
            "Johann Sebastian Bach",
            font="Edwin-Italic",  # Edwin Italic for default text
            font_size=36
        )
        composer.next_to(staff_lines, UP, buff=1)

        # Animate
        self.play(Create(staff_lines))
        self.play(Write(treble))
        self.play(Write(time_signature))
        self.play(Create(first_bar))
        self.play(FadeIn(composer))
        self.wait()
