from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class SideBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # -------------------------
        # SIDEBAR INIT
        # -------------------------

        self.setFixedWidth(200)
        self.setStyleSheet("background-color: #ffffff; border-radius: 8px")
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        barlayout = QVBoxLayout()
        barlayout.setContentsMargins(10, 10, 10, 10)

        # -------------------------
        # SIDEBAR TITLE
        # -------------------------

        self.title = QLabel(self)
        self.title.setStyleSheet("background-color: transparent; color: #000000; font-family: Segoe UI; font-size: 24px; font-weight: 600;")
        self.title.setText("SideBar")
        barlayout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(barlayout)

        self.layout = QVBoxLayout()