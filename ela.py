from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha.colors

class ela(Scene):
    def construct(self):
        t0 = Text("The House on Mango Street", color=mocha.text.hex).to_edge(UP)
        p0 = Paragraph(
            "An example of onomatopoeia is \"Banging\".",
            "It is used in the second paragraph on page 3.",
            "An example of personification is",
            "\"windows so small you'd think they were holding their breath,\"",
            "which is used in the third paragraph on page 4.",
            "An example of alliteration is \"paint peeling\"",
            "which is used in the first full paragraph on page 5.",
            color=mocha.text.hex,
            t2c={
                "\"Banging\"": mocha.blue.hex,
                "\"windows so small you'd think they were holding their breath,\"": mocha.blue.hex,
                "\"paint peeling\"": mocha.blue.hex,
                "page 3": mocha.red.hex,
                "page 4": mocha.red.hex,
                "page 5": mocha.red.hex,
            },
            alignment="LEFT"
        ).scale(0.625).next_to(t0, DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT, buff=0.6)

        self.play(Write(t0), Write(p0))
        self.wait(2.5)

        t1 = Text("Hairs", color=mocha.text.hex).to_edge(UP)
        p1 = Paragraph(
            "Three similes include \"My Papa's hair is like a broom\",",
            "\"has hair like fur\",",
            "and \"my mother's hair, like little rosettes\".",
            "\"It never obeys barrettes or bands\"",
            "is an example of personification.",
            "An example of alliteration is \"barrettes or bands.\"",
            "Both of these are used in the first paragraph on page 6.",
            color=mocha.text.hex,
            t2c={
                "\"My Papa's hair is like a broom\"": mocha.blue.hex,
                "\"has hair like fur\"": mocha.blue.hex, 
                "\"my mother's hair, like little rosettes\"": mocha.blue.hex, 
                "\"It never obeys barrettes or bands\"": mocha.blue.hex,
                "\"barrettes or bands,\"": mocha.blue.hex,
                "page 6": mocha.red.hex,
            },
            alignment="LEFT"
        ).scale(0.625).next_to(t1, DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT, buff=0.6)

        self.play(Transform(t0, t1), Transform(p0, p1))
        self.wait(2.5)
        t2 = Text("Boys & Girls", color=mocha.text.hex).to_edge(UP)
        p2 = Paragraph(
            "\"Until then I am a red balloon, a balloon tied to an anchor\"",
            "is an example of a metaphor.",
            "It is used on page 9 in the first paragraph.",
            color=mocha.text.hex,
            t2c={
                "\"Until then I am a red balloon, a balloon tied to an anchor\"": mocha.blue.hex,
                "page 9": mocha.red.hex,
            },
            alignment="LEFT"
        ).scale(0.625).next_to(t2, DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT, buff=0.6)

        self.play(Transform(t0, t1), Transform(p0, p1))
        self.wait(2.5)

        t3 = Text("My Name", color=mocha.text.hex).to_edge(UP)
        p3 = Paragraph(
            "\"Songs like sobbing\" is an example of hyperbole, alliteration,",
            "and a simile.",
            "\"A wild horse of a woman\" is an example of a metaphor.",
            "An example of allusion on page 11 is",
            "\"she looked out the window her whole life,",
            "the way so many women sit their sadness on an elbow.\"",
            color=mocha.text.hex,
            t2c={
                "\"Songs like sobbing\"": mocha.blue.hex,
                "\"A wild horse of a woman\"": mocha.blue.hex,
                "\"she looked out the window her whole life,": mocha.blue.hex,
                "the way so many women sit their sadness on an elbow.\"": mocha.blue.hex,
                "page 11": mocha.red.hex,
            },
            alignment="LEFT"
        ).scale(0.625).next_to(t2, DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT, buff=0.6)

        self.play(Transform(t0, t3), Transform(p0, p3))
        self.wait(2.5)
        
        t4 = Text("Cathy, Queen of Cats", color=mocha.text.hex).to_edge(UP)
        p4 = Paragraph(
            "\"Raggedy as rats\" and \"big as a whale\"",
            "are examples of similes.",
            "\"Raggedy as rats\" and \"sold…sold…sell it\"",
            "are both examples of alliteration.",
            "The previous four quotes are on page 12.",
            "An example of a simile is \"cats asleep like little doughnuts,\"",
            "which is on page 13.",
            color=mocha.text.hex,
            t2c={
                "\"Raggedy as rats\"": mocha.blue.hex,
                "\"big as a whale\"": mocha.blue.hex,
                "\"Raggedy as rats\"": mocha.blue.hex,
                "\"sold…sold…sell it\"": mocha.blue.hex,
                "\"cats asleep like little doughnuts,\"": mocha.blue.hex,
                "page 12": mocha.red.hex,
                "page 13": mocha.red.hex,
            },
            alignment="LEFT"
        ).scale(0.625).next_to(t2, DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT, buff=0.6)

        self.play(Transform(t0, t4), Transform(p0, p4))
        self.wait(2.5)
        
        t5 = Text("Our Good Day", color=mocha.text.hex).to_edge(UP)
        p5 = Paragraph(
            "\"They smell like a broom\" is an example of a simile.",
            "\"Five dollars, five dollars\" is an example of alliteration.",
            "Another example of alliteration that is on the top of page 15",
            "is \"shiny Sunday shoes\". A simile used on page 16 is",
            "\"wobbly as if the wheels are spaghetti\".",
            color=mocha.text.hex,
            t2c={
                "\"They smell like a broom\"": mocha.blue.hex,
                "\"Five dollars, five dollars\"": mocha.blue.hex,
                "\"shiny Sunday shoes\"": mocha.blue.hex,
                "\"wobbly as if the wheels are spaghetti\"": mocha.blue.hex,
                "page 15": mocha.red.hex,
                "page 16": mocha.red.hex,
            },
            alignment="LEFT"
        ).scale(0.625).next_to(t2, DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT, buff=0.6)

        self.play(Transform(t0, t5), Transform(p0, p5))
        self.wait(2.5)

        self.play(Unwrite(t0), Unwrite(p0))
        self.wait()