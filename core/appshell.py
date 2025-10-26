from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from ui.topbar.topbar import TopBar
from ui.sidebar.sidebar import SideBar

class AppShell(QWidget):
    def __init__(self):
        super().__init__()

        # -------------------------
        # INITIAL WINDOW CREATION
        # -------------------------

        self.setWindowTitle("Aurevue")
        self.resize(1220, 920)
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

        self.inner = QWidget(self.outer)
        self.inner.setStyleSheet("background-color: #d1d5d8; border-radius: 12px")
        inner_layout = QGridLayout()
        inner_layout.setContentsMargins(20, 20, 20, 20)
        inner_layout.setSpacing(20)

        # -------------------------
        # TOPBAR AND SIDEBAR
        # -------------------------

        self.topbar = TopBar(self.inner)
        self.topbar.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        inner_layout.addWidget(self.topbar, 0, 0, alignment=Qt.AlignmentFlag.AlignTop)

        self.sidebar = SideBar(self.inner)
        self.sidebar.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        inner_layout.addWidget(self.sidebar, 1, 0)

        # -------------------------
        # LAYOUTS GALORE
        # -------------------------
        outer_layout.addWidget(self.inner)
        window_layout.addWidget(self.outer)

        self.inner.setLayout(inner_layout)
        self.outer.setLayout(outer_layout)
        self.setLayout(window_layout)