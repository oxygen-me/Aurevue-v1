from ui.pages import page_manager
from ui.tileboard.tile import TileWidget  # adjust path as needed
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QSizePolicy
from PySide6.QtCore import Qt
from core.themes import theme_manager
from eventbus import bus

class SideBar(TileWidget):
    def __init__(self, parent=None, **kwargs):


        super().__init__(parent, tile_id="sidebar", tile_type="sidebar", **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.theme_manager = theme_manager
        self.root_widget = self.window()
        # ----- Layout -----
        layout = self.inner_layout
        layout.setSpacing(8)

        # ----- Style -----
        self.setStyleSheet("border-radius: 12px;")

        # ----- Content -----
        title = QLabel("AureBar")
        title.setStyleSheet("font-family: Segoe UI; font-size: 24px; font-weight: light;")
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        blayout = QHBoxLayout()
        blayout.setSpacing(8)
        blayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        settings_btn = QPushButton("⚙️")
        settings_btn.setStyleSheet("border-radius: 4px; padding: 0px; margin: 0px; font-size: 24px;")
        settings_btn.setFixedSize(32, 32)
        settings_btn.clicked.connect(self.on_settings)
        blayout.addWidget(settings_btn, alignment=Qt.AlignmentFlag.AlignLeft)

        status_icon = QLabel("☀️")
        status_icon.setStyleSheet("font-size: 24px; padding: 0px; margin: 0px;")
        status_icon.setFixedSize(32, 32)
        blayout.addWidget(status_icon, alignment=Qt.AlignmentFlag.AlignHCenter)

        theme_btn = QPushButton("💡")
        theme_btn.setStyleSheet("border-radius: 4px; padding: 0px; margin: 0px; font-size: 24px;")
        theme_btn.setFixedSize(32, 32)
        theme_btn.clicked.connect(self.change_theme)
        blayout.addWidget(theme_btn, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addStretch(1)
        layout.addLayout(blayout)

    def change_theme(self):

        if theme_manager.active == "light":
            theme_name = "dark"
        else:
            theme_name = "light"

        # Apply global theme
        self.theme_manager.apply_to_children(self.root_widget, theme_name)

        # Apply Specific Styles
        try:
            from ui.tiles.presets.command_tile import CommandTile
            for tile in self.root_widget.findChildren(CommandTile):
                tile.apply_output_theme(self.theme_manager.get())

        except Exception as e:
            print(f"[CommandInterpreter] Failed to apply a specialized theme: {e}")

        return f"Theme switched to {theme_name.capitalize()}."

    def on_settings(self):
        bus.configRequested.emit(1)

