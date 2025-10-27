from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class TileWidget(QWidget):
    """
    Aurevue Tile Foundry — Phase 1
    Visual-only tile unit with theme / mood compatibility and shadow depth.
    """

    def __init__(self, parent=None, tile_id=None, tile_type="generic"):
        super(TileWidget, self).__init__(parent)
        self.tile_id = tile_id
        self.tile_type = tile_type

        # ----- Layout -----
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        # ----- Placeholder Content -----
        # label = QLabel(f"{self.tile_type.title()} #{self.tile_id or '?'}", self)
        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)                        # EVIL BASTARD BEGONE!
        # layout.addWidget(label)

        # ----- Initial Style -----
        self.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 12px;
            border: 1px solid #d0d0d0;
        """)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ----- Shadow -----
        self.apply_shadow("#000000", blur=24, x_offset=0, y_offset=6, opacity=0.25)

    # -----------------------------
    # Theme / Mood Integration
    # -----------------------------
    def apply_theme(self, tokens):
        bg = tokens.get("tile", "#ffffff")
        text = tokens.get("text", "#000000")
        border = tokens.get("border", "#d0d0d0")
        self.setStyleSheet(f"""
            background-color: {bg};
            color: {text};
            border: 1px solid {border};
            border-radius: 12px;
        """)

    # -----------------------------
    # Depth / Shadow Handling
    # -----------------------------
    def apply_shadow(self, color="#000000", blur=24, x_offset=0, y_offset=6, opacity=0.25):
        shadow = QGraphicsDropShadowEffect(self)
        qcolor = QColor(color)
        qcolor.setAlphaF(opacity)
        shadow.setColor(qcolor)
        shadow.setBlurRadius(blur)
        shadow.setOffset(x_offset, y_offset)
        self.setGraphicsEffect(shadow)

    # -----------------------------
    # Event Placeholders (Phase 2)
    # -----------------------------
    def enterEvent(self, event):
        pass

    def leaveEvent(self, event):
        pass

    def mousePressEvent(self, event):
        pass