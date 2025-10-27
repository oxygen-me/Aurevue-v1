from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from ui.tileboard.tileboard import BoardWidget
from ui.tileboard.tile import TileWidget

class AppShell(QWidget):
    def __init__(self):
        super().__init__()

        # -------------------------
        # INITIAL WINDOW CREATION
        # -------------------------

        self.setWindowTitle("Aurevue")
        self.resize(1260, 960)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        window_layout = QVBoxLayout()

        # -------------------------
        # OUTER SHELL CREATION
        # -------------------------

        self.outer = QWidget(self)
        self.outer.setStyleSheet("background-color: #ffffff; border-radius: 16px")
        outer_layout = QVBoxLayout()
        outer_layout.setContentsMargins(10, 10, 10, 10)

        # -------------------------
        # CONTENT AREA CREATION
        # -------------------------

        self.board = BoardWidget()  # lives inside the layout, not manually positioned
        self.board.setObjectName("board_area")
        self.board.setStyleSheet("""
            #board_area {
                background-color: #d0d3d5;
                border-radius: 12px;
            }
        """)

        self.board.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # -------------------------
        # TOPBAR AND SIDEBAR
        # -------------------------

        # -------------------------
        # LAYOUTS GALORE
        # -------------------------
        outer_layout.addWidget(self.board, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        window_layout.addWidget(self.outer)

        self.outer.setLayout(outer_layout)
        self.setLayout(window_layout)