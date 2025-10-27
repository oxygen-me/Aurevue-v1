from PySide6.QtGui import QColor

class ThemeManager:
    def __init__(self):
        self.themes = {}
        self.active = None

    def register(self, name: str, tokens: dict):
        self.themes[name] = tokens

    def apply(self, widget, theme_name: str):
        if theme_name not in self.themes:
            raise ValueError(f"Theme '{theme_name}' not found.")
        self.active = theme_name
        tokens = self.themes[theme_name]

        widget.setStyleSheet(f"""
            background-color: {tokens['background']};
            color: {tokens['text']};
        """)

        widget.active_theme = tokens

    def get(self):
        return self.themes.get(self.active, {})