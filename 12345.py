class onetwothreefourfive(Scene):
    def construct(self):
        # Build combinations
        nums = [1, 2, 3, 4, 5]
        comb_list = []
        for r in range(1, len(nums) + 1):
            comb_list.extend(list(combinations(nums, r)))
        # comb_list example: (1,), (2,), (3,), (4,), (5,), (1,2), (1,3), ...

        # Layout parameters (tweak as needed)
        rows = 5
        col_spacing = 2.2
        row_spacing = 0.95
        start_pos = LEFT * 5.5 + UP * 2.5

        # Timing: split into a single run-time so morph+move happen visibly together
        transform_move_time = 1.0
        pause = 0.06

        # Helper: create MathTex where each digit is a submobject (helps glyph morph)
        def comb_to_mobject(comb, color=mocha.blue.hex):
            s = "".join(str(n) for n in comb)
            return MathTex(*list(s), color=color)

        # --- Pin the first tile at top-left ---
        first = comb_list[0]
        pinned_first = comb_to_mobject(first)
        pinned_first.move_to(start_pos)
        self.add(pinned_first)
        self.play(FadeIn(pinned_first, scale=0.92))
        self.wait(pause)

        static_last = pinned_first  # last pinned (stays)

        # --- Iterate combinations: spawn mover, morph-while-moving into target (ReplacementTransform) ---
        for i, comb in enumerate(comb_list[1:], start=1):
            prev_comb = comb_list[i - 1]
            next_comb = comb

            # 1) Create a fresh mover that *looks like* the previous pinned tile (fresh object)
            mover = comb_to_mobject(prev_comb)
            mover.move_to(static_last.get_center())
            self.add(mover)

            # 2) Create the target object (what the mover should become); place it at mover's location
            target = comb_to_mobject(next_comb)
            target.move_to(mover.get_center())
            # Ensure target is in the scene so ReplacementTransform has something to morph into.
            # Start with low opacity so morph visually grows the target; ReplacementTransform will handle replacement.
            target.set_opacity(0.0)
            self.add(target)

            # 3) Compute destination grid position
            col = i // rows
            row = i % rows
            dest = start_pos + RIGHT * col * col_spacing + DOWN * row * row_spacing

            # 4) Animate: ReplacementTransform(mover -> target) AND move the target to dest simult.
            # ReplacementTransform morphs mover into target; moving target at the same time makes morph happen during motion.
            anim = AnimationGroup(
                ReplacementTransform(mover, target),
                target.animate.move_to(dest).set_opacity(1.0),  # move + make visible
                lag_ratio=0,
            )
            self.play(anim, run_time=transform_move_time, rate_func=linear)

            # At this point:
            # - target sits at dest and is visible (it replaced mover)
            # - previous pinned tiles are still present
            # - we use target as the new pinned tile for next iteration
            static_last = target

            # tiny pause
            self.wait(pause)

        # Optional: show total count on top
        total_tex = MathTex(f"Total = {len(comb_list)}", color=mocha.text.hex).to_edge(UP)
        self.play(Write(total_tex))
        self.wait(1.25)