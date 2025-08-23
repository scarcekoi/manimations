from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha
macchiato = PALETTE.macchiato
frappe = PALETTE.frappe
latte = PALETTE.latte

class parts_of_an_equation(Scene):
    def construct(self):
        # Equation parts using LaTeX
        term1 = Tex("3x", color=mocha.colors.text.hex)
        operation = Tex("+", color=mocha.colors.text.hex)
        term2 = Tex("1", color=mocha.colors.text.hex)
        equal = Tex("=", color=mocha.colors.text.hex)
        constant = Tex("7", color=mocha.colors.text.hex)

        equation_parts = VGroup(term1, operation, term2, equal, constant).arrange(RIGHT, buff=0.5)
        equation_parts.move_to(ORIGIN)

        # Term boxes (smallest)
        box_term1 = SurroundingRectangle(term1, color=mocha.colors.blue.hex, buff=0.2, stroke_width=6)
        box_term2 = SurroundingRectangle(term2, color=mocha.colors.peach.hex, buff=0.2, stroke_width=6)

        # Expression box (medium) around 3x + 1
        expr_group = VGroup(term1, operation, term2)
        box_expr = SurroundingRectangle(expr_group, color=mocha.colors.green.hex, buff=0.3, stroke_width=6)

        # Equation box (largest) around entire equation
        box_eq = SurroundingRectangle(equation_parts, color=mocha.colors.red.hex, buff=0.4, stroke_width=6)

        # Set layering (z-index) so bigger boxes are behind smaller ones
        box_eq.set_z_index(0)
        box_expr.set_z_index(1)
        box_term1.set_z_index(2)
        box_term2.set_z_index(2)

        legend_labels = VGroup()

        def spawn_label(label_text, color):
            label = Tex(r"\text{" + label_text + "}", font_size=50).set_color(color)
            label.next_to(equation_parts, UP, buff=0.5)
            self.play(FadeIn(label))
            self.play(label.animate.to_corner(UL).shift(DOWN * len(legend_labels) * 0.6))
            legend_labels.add(label)
            self.wait(0.3)

        # Section 1: Show equation parts
        self.next_section("1")
        self.play(FadeIn(equation_parts))

        # Section 2: Animate term1 box and label
        self.next_section("2")
        self.play(Create(box_term1))
        self.play(term1.animate.set_color(mocha.colors.blue.hex))
        spawn_label("Term", mocha.colors.blue.hex)

        # Section 3: Animate term2 box and label
        self.next_section("3")
        self.play(Create(box_term2))
        self.play(term2.animate.set_color(mocha.colors.peach.hex))
        spawn_label("Term", mocha.colors.peach.hex)

        # Section 4: Animate expression box and label
        self.next_section("4")
        self.play(Create(box_expr))
        self.play(expr_group.animate.set_color(mocha.colors.green.hex))
        spawn_label("Expression", mocha.colors.green.hex)

        # Section 5: Animate equation box and label
        self.next_section("5")
        self.play(Create(box_eq))
        self.play(equation_parts.animate.set_color(mocha.colors.red.hex))
        spawn_label("Equation", mocha.colors.red.hex)

        # Helper invisible texts for arrow targets
        self.next_section("6")
        coeff = Tex("3").move_to(term1.get_left() + RIGHT * 0.15).set_opacity(0)
        variable = Tex("x").move_to(term1.get_right() + LEFT * 0.15).set_opacity(0)
        self.add(coeff, variable)

        # Section 6: Setup and animate labels and arrows at top
        self.next_section("7")
        top_y = equation_parts.get_top()[1] + 2.5

        coeff_label = Tex(r"\text{Coefficient}", font_size=40).set_color(mocha.colors.blue.hex)
        var_label = Tex(r"\text{Variable}", font_size=40).set_color(mocha.colors.blue.hex)
        op_label = Tex(r"\text{Operation}", font_size=40).set_color(mocha.colors.red.hex)
        const_label = Tex(r"\text{Constant}", font_size=40).set_color(mocha.colors.peach.hex)

        labels = VGroup(coeff_label, var_label, op_label, const_label).arrange(RIGHT, buff=0.5)
        labels.move_to(UP * top_y)

        arrow_start_offset = DOWN * 0.1
        start_points = [label.get_bottom() + arrow_start_offset for label in labels]

        targets = [
            coeff.get_top(),
            variable.get_center(),
            operation.get_top(),
            term2.get_center(),
        ]
        constant_targets = [term2.get_top(), constant.get_top()]

        arrows_group = VGroup()  # Collect arrows to remove later

        for i, label in enumerate(labels):
            self.play(FadeIn(label))
            start = start_points[i]

            if label == const_label:
                arrows = [
                    Arrow(start=start, end=constant_targets[0], color=mocha.colors.peach.hex, buff=0.1).set_z_index(99),
                    Arrow(start=start, end=constant_targets[1], color=mocha.colors.peach.hex, buff=0.1).set_z_index(99),
                ]
                arrows_group.add(*arrows)
                self.play(*[GrowArrow(arrow) for arrow in arrows])
            else:
                arrow = Arrow(start=start, end=targets[i], color=label.get_color(), buff=0.1).set_z_index(99)
                arrows_group.add(arrow)
                self.play(GrowArrow(arrow))

            self.wait(0.5)

        pause = Text("Pause Here", color=mocha.colors.text.hex).set_z_index(99).shift(np.array([0, -1, 0]))
        self.play(Write(pause))
        self.wait(2)
        self.play(Unwrite(pause))
        self.wait(10)

        # Remove all boxes, labels, and arrows
        self.play(Unwrite(term1), Unwrite(operation), Unwrite(term2), Unwrite(equal), Unwrite(constant))
        self.wait(0.05)
        self.play(Uncreate(box_term1), Uncreate(box_term2), Uncreate(expr_group), Uncreate(box_expr), Uncreate(box_eq))
        self.play(Uncreate(arrows_group, run_time=2))
        self.play(Unwrite(labels))
        self.play(Unwrite(legend_labels))
        self.wait(5)
