from PySide6.QtCore import QTimer
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
        """Safely applies a theme to the given widget and updates active state."""
        # ---- Validate theme ----
        if theme_name not in self.themes:
            raise ValueError(f"Theme '{theme_name}' not found.")

        # Lock active theme *before* painting
        self.active = theme_name
        tokens = self.themes[theme_name]

        # ---- Extract core colors ----
        bg = self.token("tile", "background") or self.token("base", "background") or "#ffffff"
        text = self.token("text", "primary") or "#000000"
        border = self.token("tile", "border") or "#d0d0d0"
        shadow = self.token("tile", "shadow") or "rgba(0,0,0,0.25)"

        # ---- Reset previous styles before applying new ones ----
        widget.setStyleSheet("")  # clears old paint layers

        # ---- Apply base styling ----
        widget.setStyleSheet(f"""
            QWidget {{
                background-color: {bg};
                color: {text};
                border: none;  /* prevent over-layering borders */
                border-radius: 12px;
            }}
        """)

        # ---- Mark current theme ----
        widget.active_theme = tokens

        print(f"[ThemeManager] Applied theme '{theme_name}' to {widget.__class__.__name__}")

    def apply_to_children(self, widget, theme_name=None):
        print(f"[DEBUG] Applying theme '{theme_name}' starting from {widget.__class__.__name__}")
        if not widget:
            return

        if theme_name:
            if theme_name not in self.themes:
                raise ValueError(f"Theme '{theme_name}' not found.")
            self.active = theme_name  # <-- lock state *before* painting
            tokens = self.themes[theme_name]
        else:
            tokens = self.themes.get(self.active, {})

        # apply theme to the widget itself
        self.apply(widget, theme_name or self.active)

        # recursively apply to all children
        for child in widget.findChildren(QWidget):
            if hasattr(child, "apply_theme"):
                child.apply_theme(tokens)
                widget.style().unpolish(widget)
                widget.style().polish(widget)
                widget.update()
        widget.update()