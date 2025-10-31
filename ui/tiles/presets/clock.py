from ui.tileboard.tile import TileWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from datetime import datetime


class ClockTile(TileWidget):
    def __init__(self, parent=None):
        super().__init__(parent, tile_id="weather", tile_type="weather")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ----- Layout -----
        layout = self.layout()
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # ----- Style -----
        self.setStyleSheet("""
                   WeatherTile {
                       background-color: #ffffff;
                       border-radius: 12px;
                       border: 1px solid #E3E3E3;
                   }
                   QLabel {
                       background: transparent;
                       border: none;
                       color: #202020;
                   }
               """)