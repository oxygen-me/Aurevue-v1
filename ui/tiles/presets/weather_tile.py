from ui.tileboard.tile import TileWidget  # adjust path as needed
from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class WeatherTile(TileWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="weather", tile_type="weather", **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ----- Layout -----
        layout = self.inner_layout
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # ----- Style -----
        self.setStyleSheet("""
            WeatherTile {
                background-color: #ffffff;
                border-radius: 12px;
            }
            QLabel {
                background: transparent;
                border: none;
                color: #202020;
            }
        """)

        # ----- Content -----
        self.title = QLabel("Weather")
        self.title.setStyleSheet("font-family:'Segoe UI Semibold'; font-size:14px;")

        self.temp = QLabel("72° • Sunny")
        self.temp.setStyleSheet("font-family:'Segoe UI Semibold'; font-size:28px;")

        self.loc = QLabel("Seattle, WA")
        self.loc.setStyleSheet("font-family:'Segoe UI'; font-size:12px; color:#5A5A5A;")

        layout.addWidget(self.title)
        layout.addWidget(self.temp)
        layout.addWidget(self.loc)
        layout.addStretch(1)