from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


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

    # -----------------------------
    # Theme / Mood Integration
    # -----------------------------
    def apply_theme(self, tokens: dict):
        bg = tokens.get("tile", "#ffffff")
        text = tokens.get("text", "#000000")
        border = tokens.get("border", "#d0d0d0")
        self.inner.setStyleSheet(f"""
            QWidget#inner {{
                background-color: {bg};
                color: {text};
                border: 1px solid {border};
                border-radius: 12px;
            }}
        """)

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
    def enterEvent(self, event):  # hover placeholder
        event.accept()

    def leaveEvent(self, event):
        event.accept()

    def mousePressEvent(self, event):
        event.accept()