from ui.tileboard.tile import TileWidget  # adjust path as needed
from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class LaunchTile(TileWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="launch", tile_type="launch", **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ----- Layout -----
        layout = self.inner_layout
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # ----- Style -----
        self.setStyleSheet("""
                    LaunchTile {
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
        self.title = QLabel("Launch")
        self.title.setStyleSheet("font-family:'Segoe UI Semibold'; font-size:14px;")

        layout.addWidget(self.title)
        layout.addStretch(1)