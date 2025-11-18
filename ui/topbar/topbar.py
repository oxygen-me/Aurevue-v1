from ui.tileboard.tile import TileWidget  # adjust path as needed
from PySide6.QtWidgets import QLabel, QPushButton
from PySide6.QtCore import Qt
from eventbus import bus

class TopBar(TileWidget):

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="topbar", tile_type="topbar", **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ----- Layout -----
        layout = self.inner_layout
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

        # ----- Style -----
        self.setStyleSheet("""
            TopBar {
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
        title = QLabel("Aurevue v0.0.2")
        title.setStyleSheet("font-family: Segoe UI; font-size: 32px; font-weight: light;")
        layout.addWidget(title)

        exit_btn = QPushButton("X")
        exit_btn.setStyleSheet("font-family: Segoe UI; border-radius: 4px;")
        exit_btn.clicked.connect(bus.quitRequested.emit)
        layout.addWidget(exit_btn, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addStretch(1)