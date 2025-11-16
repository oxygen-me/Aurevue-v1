from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from ui.tileboard.metrics import *
from core.themes import theme_manager

from core.themes.light import THEME_LIGHT
from core.themes.dark import THEME_DARK
theme_manager.register("light", THEME_LIGHT)
theme_manager.register("dark", THEME_DARK)

class BasePage(QWidget):

    BUFFER = GridConfig.t_buffer

    def __init__(self, parent=None):
        super().__init__(parent)

        self.theme_manager = theme_manager

        # Inner True Frame
        self.inner = QWidget(self)

        self.inner.setObjectName("area")

        # Layout for page contents (used by presets)
        self.inner_layout = QGridLayout(self.inner)
        self.inner_layout.setContentsMargins(20, 20, 20, 20)
        self.inner_layout.setSpacing(8)

        # Style: light shell; mood overrides later
        self.inner.setStyleSheet("""
                   QWidget#area {
                       background-color: #ffffff;
                       border-radius: 12px;
                       border: 1px solid #d0d0d0;
                   }
               """)

    def apply_theme(self, tokens: dict | None = None):
        """Applies Aurevue theme tokens to this page and all shared UI elements."""
        if tokens is None and self.theme_manager:
            tokens = self.theme_manager.get()
        if not tokens:
            return

        # --- Extract grouped tokens safely ---
        tile = tokens.get("tile", {})
        text = tokens.get("text", {})
        io = tokens.get("io", {})
        accent = tokens.get("accent", {})
        base = tokens.get("base", {})

        # --- Core colors with fallbacks ---
        bg = tile.get("background", "#ffffff")
        fg = text.get("primary", "#000000")
        border = tile.get("border", "#d0d0d0")
        shadow_str = tile.get("shadow", base.get("shadow", "rgba(0,0,0,0.25)"))

        io_bg = io.get("background", "#f0f0f0")
        io_fg = io.get("text", "#202020")
        io_focus = io.get("focus", "#e0e0e0")

        accent_main = accent.get("main", "#0078ff")
        accent_hover = accent.get("hover", "#3399ff")
        accent_press = accent.get("press", "#005fcc")
        accent_text = accent.get("text", "#ffffff")

        # --- Unified Tile Stylesheet ---
        self.inner.setStyleSheet(f"""
            QWidget#area {{
                background-color: {bg};
                color: {fg};
                border: none;                 /* removes hard gray lines */
                border-radius: 12px;
            }}

            QLabel {{
                background: transparent;
                color: {fg};
                font-family: 'Segoe UI';
            }}

            QLineEdit, QTextEdit {{
            background-color: {io_bg};
            color: {io_fg};
            border: none;
            border-radius: 6px;
            padding: 8px 10px;
            box-shadow: inset 0 1px 2px rgba(0,0,0,0.10),
                inset 0 0 0 1px rgba(0,0,0,0.04);
            }}
            QLineEdit:focus, QTextEdit:focus {{
            background-color: {io_focus};
            box-shadow: inset 0 1px 2px rgba(0,0,0,0.12),
            inset 0 0 0 1px rgba(0,0,0,0.06);
            }}

            QPushButton {{
            background-color: {accent_main};
            color: {accent_text};
            border: none;
            border-radius: 6px;
            padding: 6px 12px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.08),
            inset 0 0 0 1px rgba(255,255,255,0.6);
            }}
            QPushButton:hover {{
            background-color: {accent_hover};
            box-shadow: 0 1px 2px rgba(0,0,0,0.10),
            inset 0 0 0 1px rgba(255,255,255,0.8);
            }}
            QPushButton:pressed {{
          background-color: {accent_press};
           box-shadow: inset 0 1px 2px rgba(0,0,0,0.15);
            }}
        """)

        # --- Shadow Reapplication (for depth) ---
        shadow_color = QColor("#000000")
        shadow_color.setAlphaF(0.25)
        self.apply_shadow(color=shadow_color.name(), blur=24, y_offset=6, opacity=0.25)

        print("[DEBUG TILE] Using IO_BG:", io_bg, "Accent Main:", accent_main)

    # -----------------------------
    # Depth / Shadow Handling
    # -----------------------------
    def apply_shadow(self, color="#000000", blur=24, x_offset=0, y_offset=0, opacity=0.25):
        shadow = QGraphicsDropShadowEffect(self)
        qcolor = QColor(color)
        qcolor.setAlphaF(opacity)
        shadow.setColor(qcolor)
        shadow.setBlurRadius(blur)
        shadow.setOffset(x_offset, y_offset)
        self.setGraphicsEffect(shadow)  # apply to visible frame only

    def showEvent(self, event):
        super().showEvent(event)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        parent = self.parent()
        if not parent:
            return

        pg = parent.geometry()

        self.setGeometry(
            0,
            0,
            pg.width(),
            pg.height(),
        )
