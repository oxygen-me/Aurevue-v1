from ui.tileboard.tile import TileWidget  # adjust path as needed
from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class SideBar(TileWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="sidebar", tile_type="sidebar", **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ----- Layout -----
        layout = self.inner_layout
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # ----- Style -----
        self.setStyleSheet("""
            SideBar {
                background-color: #ffffff;
                border-radius: 12px;
            }
        """)

        # ----- Content -----

        layout.addStretch(1)