from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget

class ThemeManager:
    def __init__(self):
        self.themes = {}
        self.active = None

    # Register a new theme dict
    def register(self, name: str, tokens: dict):
        self.themes[name] = tokens

    # Get the current active theme tokens
    def get(self):
        return self.themes.get(self.active, {})

    # Deep-access helper, e.g. get("text", "primary")
    def token(self, *path, fallback=None):
        theme = self.get()
        node = theme
        for key in path:
            if not isinstance(node, dict):
                return fallback
            node = node.get(key, fallback)
        return node

    # Activate and apply a theme to a specific widget
    def apply(self, widget, theme_name: str):
        if theme_name not in self.themes:
            raise ValueError(f"Theme '{theme_name}' not found.")
        self.active = theme_name
        tokens = self.themes[theme_name]

        # pull common colors
        bg = self.token("tile", "background") or self.token("base", "background")
        text = self.token("text", "primary")
        border = self.token("tile", "border")
        shadow = self.token("tile", "shadow")

        # Apply the theme visually to the root widget
        widget.setStyleSheet(f"""
            QWidget {{
                background-color: {bg};
                color: {text};
                border: 1px solid {border};
                border-radius: 12px;
            }}
        """)

        widget.active_theme = tokens

    def apply_to_children(self, root_widget: QWidget):
        """Apply the active theme recursively to any widget with apply_theme()."""
        if not self.active:
            return
        theme = self.get()
        for child in root_widget.findChildren(QWidget):
            if hasattr(child, "apply_theme"):
                print("[ThemeManager] Applying theme to:", child.objectName(), child.__class__.__name__)
                try:
                    child.apply_theme(theme)
                    child.style().unpolish(child)
                    child.style().polish(child)
                    child.update()
                except Exception as e:
                    print(f"[ThemeManager] Failed to theme {child}: {e}")