from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QLayout
from PySide6.QtCore import Qt
from ui.tileboard.tileboard import BoardWidget

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

        self.center_on_screen()

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


        # -------------------------
        # TOPBAR AND SIDEBAR
        # -------------------------

        # -------------------------
        # LAYOUTS GALORE
        # -------------------------
        outer_layout.addWidget(self.board, 1)
        window_layout.addWidget(self.outer)

        self.outer.setLayout(outer_layout)
        self.setLayout(window_layout)

    def center_on_screen(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        screen_center = screen_geometry.center()
        window_geometry.moveCenter(screen_center)
        self.move(window_geometry.topLeft())