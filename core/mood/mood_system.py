from core.themes.manager import ThemeManager
from core.themes.light import THEME_LIGHT
from core.themes.dark import THEME_DARK
from core.mood.moods import MOOD_REGISTRY

class MoodSystem:
    """
        Aurevue Mood System (Phase 1)
        ----------------------------------
        Handles registration, activation, and visual styling of moods.

        Phase 1:
            - Visual only (color & gradient layers)
            - Moods subclass themes
        Future Phases:
            - Each mood gains individualized motion & sound profiles
        """

    def __init__(self):
        self.theme_manager = ThemeManager()
        self.register_base_themes()
        self.moods = MOOD_REGISTRY
        self.active_mood = None

        # -------------------------------
        # Theme Registration
        # -------------------------------

    def register_base_themes(self):
        """Register the base themes that moods can inherit from."""
        self.theme_manager.register("light", THEME_LIGHT)
        self.theme_manager.register("dark", THEME_DARK)

        # -------------------------------
        # Mood Activation
        # -------------------------------

    def set_mood(self, name: str, widget):
        if name not in self.moods:
            raise ValueError(f"Mood '{name}' not defined.")
        mood = self.moods[name]

        # Apply base theme
        self.theme_manager.apply(widget, mood["base_theme"])

        # Gradient overlay
        gradient = mood.get("gradient")
        if gradient:
            widget.setStyleSheet(
                widget.styleSheet()
                + f"""
                background: qlineargradient(
                    x1:{gradient['x1']}, y1:{gradient['y1']},
                    x2:{gradient['x2']}, y2:{gradient['y2']},
                    stop:0 {gradient['start']},
                    stop:1 {gradient['end']}
                );
                """
            )

            # Assign high-res logo
            if "logo_asset" in mood:
                widget.logo_path = mood["logo_asset"]

            self.active_mood = name
            widget.active_mood = mood

        # --- Future extensions ---
        # self._apply_motion_profile(mood)
        # self._apply_sound_profile(mood)

        # -------------------------------
        # Future Hooks (no-ops)
        # -------------------------------

    def _apply_motion_profile(self, mood):
        """Reserved for per-mood motion behavior (Phase 2)."""
        pass

    def _apply_sound_profile(self, mood):
        """Reserved for per-mood ambient sound behavior (Phase 2)."""
        pass

        # -------------------------------
        # Utilities
        # -------------------------------

    def get_active_tokens(self):
        """Return currently active theme + mood tokens."""
        return self.theme_manager.get() | {"mood": self.active_mood}

    def list_moods(self):
        """List all registered moods."""
        return list(self.moods.keys())