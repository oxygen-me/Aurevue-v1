from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from core.motion.presets.hover import HoverBehavior
from ui.tileboard.expand_behavior import ExpandBehavior
from core.themes.manager import ThemeManager

theme_manager = ThemeManager()

from core.themes.light import THEME_LIGHT
from core.themes.dark import THEME_DARK
theme_manager.register("light", THEME_LIGHT)
theme_manager.register("dark", THEME_DARK)


class TileWidget(QWidget):
    """Aurevue Tile Foundry — Faux-Gutter System.
    The outer widget matches exact grid cell geometry.
    The inner (visible) frame is inset 10px on each edge
    to create optical gutters without breaking grid math.
    """
    BUFFER = 10  # px inward offset per edge

    def __init__(self, parent=None, tile_id=None, tile_type="generic",
                 grid_x=0, grid_y=0, grid_w=1, grid_h=1, metrics=None):
        super().__init__(parent)
        self.tile_id = tile_id
        self.tile_type = tile_type
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.grid_w = grid_w
        self.grid_h = grid_h
        self.metrics = metrics

        # -----------------------------
        # Geometry
        # -----------------------------
        w = h = 120  # default failsafe
        if metrics:
            print(f"{self.tile_type} metrics ok", metrics)
            x, y, w, h = metrics.to_pixels(grid_x, grid_y, grid_w, grid_h)
            self.setGeometry(int(x), int(y), int(w), int(h))
        else:
            print(f"{self.tile_type} missing metrics")
            self.resize(w, h)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # -----------------------------
        # Inner (visible) frame
        # -----------------------------
        self.inner = QWidget(self)
        self.inner.setGeometry(
            self.BUFFER, self.BUFFER,
            w - (2 * self.BUFFER),
            h - (2 * self.BUFFER)
        )
        self.inner.setObjectName("inner")
        self.inner.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # Layout for content widgets (used by presets)
        self.inner_layout = QVBoxLayout(self.inner)
        self.inner_layout.setContentsMargins(10, 10, 10, 10)
        self.inner_layout.setSpacing(8)

        # Style: light shell; mood overrides later
        self.inner.setStyleSheet("""
            QWidget#inner {
                background-color: #ffffff;
                border-radius: 12px;
                border: 1px solid #d0d0d0;
            }
        """)

        # -----------------------------
        # Shadow (depth)
        # -----------------------------
        self.apply_shadow("#000000", blur=24, x_offset=0, y_offset=6, opacity=0.25)
        self.expand_fx = ExpandBehavior(self.inner)
        self.hover_fx = HoverBehavior(self.inner)

    # -----------------------------
    # Theme / Mood Integration
    # -----------------------------
    def apply_theme(self, tokens: dict | None = None):
        """Applies Aurevue theme tokens to this tile."""
        if tokens is None and self.theme_manager:
            tokens = self.theme_manager.get()
        if not tokens:
            return

        # Resolve groups safely
        tile = tokens.get("tile", {})
        text = tokens.get("text", {})
        base = tokens.get("base", {})

        # Extract colors with fallbacks
        bg = tile.get("background", "#ffffff")
        fg = text.get("primary", "#000000")
        border = tile.get("border", "#d0d0d0")
        shadow_str = tile.get("shadow", base.get("shadow", "rgba(0,0,0,0.25)"))

        # Convert shadow string (RGBA or hex) to usable QColor
        shadow_color = QColor()
        shadow_color.setNamedColor(shadow_str.split()[0]) if shadow_str.startswith("#") else shadow_color.setNamedColor(
            "#000000")

        # Apply style
        self.inner.setStyleSheet(f"""
            QWidget#inner {{
                background-color: {bg};
                color: {fg};
                border: 1px solid {border};
                border-radius: 12px;
            }}
        """)

        # Update shadow
        self.apply_shadow(shadow_color.name(), blur=24, y_offset=6, opacity=0.25)

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

    # -----------------------------
    # Event Hooks (Phase 2)
    # -----------------------------
    def enterEvent(self, event):
        if hasattr(self, "hover_fx"):
            self.hover_fx.enter()
        super().enterEvent(event)

    def leaveEvent(self, event):
        if hasattr(self, "hover_fx"):
            self.hover_fx.leave()
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        # if hasattr(self, "expand_fx"):
            # self.expand_fx.click()
        # super().mousePressEvent(event)
        pass