from manim import *
from catppuccin import PALETTE

mocha = PALETTE.mocha

class StatesOfMatter(Scene):
    def construct(self):
        # Colors
        solid_color = mocha.colors.blue.hex
        liquid_color = mocha.colors.teal.hex
        gas_color = mocha.colors.yellow.hex
        plasma_color = mocha.colors.red.hex
        sublimation_color = mocha.colors.flamingo.hex

        # Particle creation helper
        def create_particles(state, color, num=16):
            particles = VGroup()
            if state == "solid":
                for i in range(4):
                    for j in range(4):
                        dot = Dot(point=np.array([i*0.3, j*0.3, 0]), radius=0.07, color=color)
                        particles.add(dot)
                particles.move_to(ORIGIN)
            elif state == "liquid":
                for _ in range(num):
                    pos = np.array([np.random.uniform(-0.6, 0.6),
                                    np.random.uniform(-0.3, 0.3), 0])
                    dot = Dot(point=pos, radius=0.07, color=color)
                    particles.add(dot)
                particles.move_to(ORIGIN)
            elif state == "gas":
                for _ in range(num):
                    pos = np.array([np.random.uniform(-1.5, 1.5),
                                    np.random.uniform(-1, 1), 0])
                    dot = Dot(point=pos, radius=0.07, color=color)
                    particles.add(dot)
            elif state == "plasma":
                for _ in range(num):
                    pos = np.array([np.random.uniform(-1.5, 1.5),
                                    np.random.uniform(-1, 1), 0])
                    dot = Dot(point=pos, radius=0.07, color=color)
                    dot.set_glow_factor(0.8)
                    particles.add(dot)
            return particles

        # Create states
        solid_state = create_particles("solid", solid_color)
        liquid_state = create_particles("liquid", liquid_color)
        gas_state = create_particles("gas", gas_color)
        plasma_state = create_particles("plasma", plasma_color)

        # Labels
        label_scale = 0.7
        solid_label = Text("Solid", color=solid_color).scale(label_scale)
        liquid_label = Text("Liquid", color=liquid_color).scale(label_scale)
        gas_label = Text("Gas", color=gas_color).scale(label_scale)
        plasma_label = Text("Plasma", color=plasma_color).scale(label_scale)

        # Position states: spread across the width with margin
        frame_width = config.frame_width
        left_x = -frame_width / 2 + 1
        right_x = frame_width / 2 - 1
        # Intermediate positions evenly spaced
        pos_solid = np.array([left_x, 0, 0])
        pos_plasma = np.array([right_x, 0, 0])
        pos_liquid = np.array([left_x + (right_x - left_x) / 3, 0, 0])
        pos_gas = np.array([left_x + 2 * (right_x - left_x) / 3, 0, 0])

        solid_state.move_to(pos_solid)
        liquid_state.move_to(pos_liquid)
        gas_state.move_to(pos_gas)
        plasma_state.move_to(pos_plasma)

        # Labels below states
        solid_label.next_to(solid_state, DOWN, buff=0.3)
        liquid_label.next_to(liquid_state, DOWN, buff=0.3)
        gas_label.next_to(gas_state, DOWN, buff=0.3)
        plasma_label.next_to(plasma_state, DOWN, buff=0.3)

        # Fade in states and labels one by one
        for state, label in [(solid_state, solid_label), (liquid_state, liquid_label), (gas_state, gas_label), (plasma_state, plasma_label)]:
            self.play(FadeIn(state), Write(label))
            self.wait(0.3)

        # Process labels and arrow parameters
        process_scale = 0.6
        arrow_stroke = 3
        vertical_offset = 0.7  # vertical offset for arrows
        arrow_trim = 0.5  # reduce arrows by this amount at each end

        # Helper for creating arrow pairs (forward above, reverse below) with trimmed length
        def create_arrow_pair(start_pos, end_pos, forward_label_text, backward_label_text, forward_color, backward_color):
            # Calculate vector for arrow
            direction = end_pos - start_pos
            length = np.linalg.norm(direction)
            unit_dir = direction / length

            # Adjust start and end to make arrows shorter
            start_forward = start_pos + unit_dir * arrow_trim + UP * vertical_offset
            end_forward = end_pos - unit_dir * arrow_trim + UP * vertical_offset
            start_backward = end_pos - unit_dir * arrow_trim + DOWN * vertical_offset
            end_backward = start_pos + unit_dir * arrow_trim + DOWN * vertical_offset

            forward_arrow = Arrow(
                start=start_forward, end=end_forward,
                color=forward_color, buff=0,
                stroke_width=arrow_stroke,
                max_tip_length_to_length_ratio=0.15
            )
            forward_label = Text(forward_label_text, font_size=24, color=forward_color).next_to(forward_arrow, UP, buff=0.15)

            backward_arrow = Arrow(
                start=start_backward, end=end_backward,
                color=backward_color, buff=0,
                stroke_width=arrow_stroke,
                max_tip_length_to_length_ratio=0.15
            )
            backward_label = Text(backward_label_text, font_size=24, color=backward_color).next_to(backward_arrow, DOWN, buff=0.15)

            return VGroup(forward_arrow, forward_label, backward_arrow, backward_label)

        # Thermal energy arrows up/down next to a state group
        def thermal_energy_arrows(state_group, adding=True):
            color = mocha.colors.flamingo.hex
            direction = UP if adding else DOWN
            # Create 3 small arrows spaced vertically
            arrows = VGroup()
            for i in range(3):
                arr = Arrow(
                    start=state_group.get_right() + RIGHT * 0.1 + direction * (i * 0.15),
                    end=state_group.get_right() + RIGHT * 0.3 + direction * (i * 0.15),
                    color=color,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.2,
                    buff=0
                )
                arrows.add(arr)
            label_text = "Adding thermal energy" if adding else "Removing thermal energy"
            label = Text(label_text, font_size=18, color=color).next_to(arrows, RIGHT, buff=0.1)
            return arrows, label

        # Create all arrows pairs
        arrows = VGroup(
            create_arrow_pair(pos_solid, pos_liquid, "Melting", "Freezing", liquid_color, solid_color),
            create_arrow_pair(pos_liquid, pos_gas, "Evaporation", "Condensation", gas_color, liquid_color),
            create_arrow_pair(pos_gas, pos_plasma, "Ionization", "Deionization", plasma_color, gas_color),
        )

        # Sublimation and deposition curved arrows below solid and gas (curved downward)
        arc_height = 1.5
        sublimation_arrow = ArcBetweenPoints(
            pos_solid + DOWN * arc_height,
            pos_gas + DOWN * arc_height,
            angle=-PI / 2,
            color=sublimation_color,
            stroke_width=arrow_stroke,
        )
        sublimation_label = Text("Sublimation", font_size=24, color=sublimation_color).next_to(sublimation_arrow, DOWN, buff=0.15)

        deposition_arrow = ArcBetweenPoints(
            pos_gas + DOWN * (arc_height + 0.3),
            pos_solid + DOWN * (arc_height + 0.3),
            angle=PI / 2,
            color=sublimation_color,
            stroke_width=arrow_stroke,
        )
        deposition_label = Text("Deposition", font_size=24, color=sublimation_color).next_to(deposition_arrow, DOWN, buff=0.15)

        # Animate arrows and labels with thermal energy arrows and text
        for i, (start_pos, end_pos, forward_label_text, backward_label_text, forward_color, backward_color, start_state, end_state) in enumerate([
            (pos_solid, pos_liquid, "Melting", "Freezing", liquid_color, solid_color, solid_state, liquid_state),
            (pos_liquid, pos_gas, "Evaporation", "Condensation", gas_color, liquid_color, liquid_state, gas_state),
            (pos_gas, pos_plasma, "Ionization", "Deionization", plasma_color, gas_color, gas_state, plasma_state),
        ]):
            # Draw forward arrow and label
            fg_arrow_group = create_arrow_pair(start_pos, end_pos, forward_label_text, backward_label_text, forward_color, backward_color)
            forward_arrow, forward_label, backward_arrow, backward_label = fg_arrow_group

            self.play(Create(forward_arrow), Write(forward_label))
            thermal_arrows, thermal_label = thermal_energy_arrows(start_state, adding=True)
            self.play(FadeIn(thermal_arrows), Write(thermal_label))
            self.wait(1.5)
            self.play(FadeOut(thermal_arrows), FadeOut(thermal_label))
            self.play(FadeOut(forward_arrow), FadeOut(forward_label))

            # Draw backward arrow and label
            self.play(Create(backward_arrow), Write(backward_label))
            thermal_arrows_b, thermal_label_b = thermal_energy_arrows(end_state, adding=False)
            self.play(FadeIn(thermal_arrows_b), Write(thermal_label_b))
            self.wait(1.5)
            self.play(FadeOut(thermal_arrows_b), FadeOut(thermal_label_b))
            self.play(FadeOut(backward_arrow), FadeOut(backward_label))

        # Sublimation forward (solid to gas)
        self.play(Create(sublimation_arrow), Write(sublimation_label))
        thermal_arrows_sub, thermal_label_sub = thermal_energy_arrows(solid_state, adding=True)
        self.play(FadeIn(thermal_arrows_sub), Write(thermal_label_sub))
        self.wait(1.5)
        self.play(FadeOut(thermal_arrows_sub), FadeOut(thermal_label_sub))

        # Deposition backward (gas to solid)
        self.play(Create(deposition_arrow), Write(deposition_label))
        thermal_arrows_dep, thermal_label_dep = thermal_energy_arrows(gas_state, adding=False)
        self.play(FadeIn(thermal_arrows_dep), Write(thermal_label_dep))
        self.wait(1.5)
        self.play(FadeOut(thermal_arrows_dep), FadeOut(thermal_label_dep))

        self.wait(5)

        # Fade everything out nicely at the end
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(5)
