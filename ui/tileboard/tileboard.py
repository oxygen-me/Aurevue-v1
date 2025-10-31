from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QBrush, QColor
from ui.tileboard.metrics import *
from ui.tileboard.tile_manager import TileManager


class BoardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("board_area")
        self.setMinimumSize(400, 400)
        self.setStyleSheet("""
            #board_area {
                background-color: #d0d3d5;
                border-radius: 12px;
            }
        """)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Core grid configuration
        from ui.tileboard.metrics import GridConfig
        self.cfg = GridConfig(cols=14, rows=9, margin_x=10, margin_y=10)  # ✅ create a real config

        self.gm = None
        self.manager = None
        self.edit_mode = False

        print("BoardWidget initialized, waiting for resizeEvent to create TileManager.")

    # -------------------------------------------------
    # Geometry
    # -------------------------------------------------
    def resizeEvent(self, event):
        super().resizeEvent(event)

        if self.width() <= 0 or self.height() <= 0:
            return  # avoid invalid geometries on startup

        # compute grid AFTER actual dimensions exist
        self.gm = calc_grid(self.width(), self.height(), self.cfg)

        if self.manager is None:
            print("✅ Creating TileManager after grid init...")
            from ui.tileboard.tile_manager import TileManager
            self.manager = TileManager(self, self.gm)
            self.manager.render_default_set()
        else:
            self.manager.metrics = self.gm

    # -------------------------------------------------
    # Edit-mode toggle (Ctrl + E)
    # -------------------------------------------------
    def keyPressEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_E:
            self.edit_mode = not self.edit_mode
            self.update()
            event.accept()
        else:
            super().keyPressEvent(event)

    def paintEvent(self, event):
        if not self.gm:
            self.gm = calc_grid(self.width(), self.height(), self.cfg)

        from PySide6.QtCore import Qt, QPointF
        from PySide6.QtGui import QPainter, QPen, QColor

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        grid_pen = QPen(QColor("#999999"), 1, Qt.PenStyle.DotLine)
        grid_pen.setCosmetic(True)

        # --- Frame bounds ---
        left = self.gm.margin_x
        top = self.gm.margin_y
        right = self.width() - self.gm.margin_x
        bottom = self.height() - self.gm.margin_y

        # --- Draw frame ---

        # --- Draw grid only if edit mode ---
        if self.edit_mode:
            painter.setPen(grid_pen)

            # Calculate evenly spaced line positions (no remainder compression)
            cols, rows = self.gm.cols, self.gm.rows
            step_x = (right - left) / cols
            step_y = (bottom - top) / rows

            # verticals
            for c in range(1, cols):
                x = left + c * step_x
                painter.drawLine(QPointF(x, top), QPointF(x, bottom))

            # horizontals
            for r in range(1, rows):
                y = top + r * step_y
                painter.drawLine(QPointF(left, y), QPointF(right, y))