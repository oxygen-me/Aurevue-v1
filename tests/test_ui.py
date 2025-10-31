# -----------------------------
# Aurevue Board Test Harness
# -----------------------------
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from ui.tileboard.tileboard import BoardWidget

from ui.tiles.presets.weather_tile import WeatherTile
from ui.tiles.presets.notes_tile import NotesTile
from ui.tiles.presets.music_tile import MusicTile

from ui.topbar.topbar import TopBar
from ui.sidebar.sidebar import SideBar

from ui.tileboard.tile_manager import TileManager
from ui.tileboard.metrics import *
import sys


def main():
    app = QApplication(sys.argv)

    # ----- Create window -----
    win = QWidget()
    win.setWindowTitle("Aurevue TileManager Test — Phase 1")
    win.resize(1200, 900)
    layout = QVBoxLayout(win)
    win.setLayout(layout)

    # ----- Initialize Board -----
    board = BoardWidget(win)
    layout.addWidget(board)

    # ----- Setup grid metrics -----
    metrics = TileMetrics(
        win_w=1200,
        win_h=900,
        cols=12,
        rows=8,
        margin_x=10,
        margin_y=10
    )

    # ----- Initialize Manager -----
    manager = TileManager(board=board, metrics=metrics)

    # ----- Create tiles -----
    note = NotesTile(grid_x=0, grid_y=0, grid_w=3, grid_h=2, metrics=metrics)
    weather = WeatherTile(grid_x=3, grid_y=0, grid_w=3, grid_h=2, metrics=metrics)
    music = MusicTile(grid_x=0, grid_y=2, grid_w=6, grid_h=3, metrics=metrics)
    topbar

    # ----- Register tiles with manager -----
    manager.add_tile(note)
    manager.add_tile(weather)
    manager.add_tile(music)

    # ----- Render -----
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()