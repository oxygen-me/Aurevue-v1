from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QLayout
from PySide6.QtCore import Qt, QTimer

from ui.tileboard.tile_manager import TileManager
from ui.tileboard.tileboard import BoardWidget

class AppShell(QWidget):
    def __init__(self, theme_manager=None):
        super().__init__()
        self.theme_manager = theme_manager
        # -------------------------
        # INITIAL WINDOW CREATION
        # -------------------------

        print("[AppShell] Initializing shell...")

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
        self.outer.setStyleSheet("border-radius: 16px")
        self.outer.setObjectName("outer")
        outer_layout = QVBoxLayout()
        outer_layout.setContentsMargins(10, 10, 10, 10)

        # -------------------------
        # CONTENT AREA CREATION
        # -------------------------

        self.board = BoardWidget()  # lives inside the layout, not manually positioned
        self.board.setObjectName("board")


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

        if self.theme_manager:
            QTimer.singleShot(0, self._apply_init_theme)

    def center_on_screen(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        screen_center = screen_geometry.center()
        window_geometry.moveCenter(screen_center)
        self.move(window_geometry.topLeft())

    # ---------- STANDARDIZED THEME HELPER + INIT ----------
    def apply_theme(self, tokens: dict | None = None):
        if not tokens:
            return
        shell = tokens.get("shell", {})
        bg = shell.get("background", "#FDFDFD")

        self.outer.setProperty("background", bg)

        self.setStyleSheet(f"#outer {{ background: {bg} }}")

        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

    def _apply_init_theme(self):
        """Deferred theme initialization once widgets exist."""
        try:
            theme = self.theme_manager.active or "light"
            print(f"[AppShell] Applying initial theme: {theme}")
            self.theme_manager.apply_to_children(self, theme)

            # Special-case application
            from ui.tiles.presets.command_tile import CommandTile
            for tile in self.findChildren(CommandTile):
                tile.apply_output_theme(self.theme_manager.get())
                print(f"[AppShell] Applied output theme to {tile.tile_id}")

            print(f"[AppShell] Theme '{theme}' applied successfully.")
        except Exception as e:
            print("[AppShell] Theme initialization failed:", e)