from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QRect
from ui.tileboard.tile import TileWidget
from ui.tileboard.metrics import BoardMetrics
from core.mood.mood_system import MoodSystem


class BoardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Core Systems
        self.metrics = BoardMetrics()
        self.moods = MoodSystem()
        self.setFixedSize(1200, 900)

        # Internal Tile Storage
        self.tiles = []

        # --- Create Grid of Tiles ---
        for r in range(self.metrics.rows):
            for c in range(self.metrics.cols):
                x, y, w, h = self.metrics.cell_rect(c, r)
                tile = TileWidget(self, tile_id=f"{r},{c}", tile_type="generic")
                tile.setGeometry(QRect(x, y, w, h))
                self.tiles.append(tile)

        for tile in self.tiles:
            tile.setStyleSheet("background-color: #ffffff; border-radius: 8px")