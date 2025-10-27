import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from ui.tiles.presets.music_tile import MusicTile

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("Test")
win.resize(800, 600)
layout = QVBoxLayout()

tile = MusicTile()
layout.addWidget(tile)
win.setLayout(layout)




win.show()
sys.exit(app.exec())