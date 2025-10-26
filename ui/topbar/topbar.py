from PySide6.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QLabel
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt


class TopBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # -------------------------
        # TOPBAR INITIALIZATION
        # -------------------------

        self.setFixedHeight(50)
        self.setStyleSheet("background-color: #ffffff; border-radius: 8px;")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # -------------------------
        # TOPBAR LAYOUT STUFF
        # -------------------------

        barlayout = QHBoxLayout()
        barlayout.setContentsMargins(10, 10, 10, 10)


        # -------------------------
        # TITlE
        # -------------------------

        self.title = QLabel(self)
        self.title.setText("AUREVUE")
        self.title.setStyleSheet("background-color: transparent; color: #000000; font-family: Segoe UI; font-size: 24px; font-weight: 600;")
        barlayout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(barlayout)


