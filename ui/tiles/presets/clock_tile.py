from ui.tileboard.tile import TileWidget  # adjust path as needed
from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer, QDateTime
from datetime import datetime


class ClockTile(TileWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="clock", tile_type="clock", **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ----- Layout -----
        layout = self.inner_layout
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # ----- Content -----
        self.title = QLabel("Clock")
        self.title.setStyleSheet("font-family:'Segoe UI Semibold'; font-size:14px;")
        layout.addWidget(self.title)

        self.time_label = QLabel()
        self.time_label.setStyleSheet("font-family:'Segoe UI Semibold'; font-size:36px;")
        layout.addWidget(self.time_label)

        self.date_label = QLabel()
        self.date_label.setStyleSheet("font-family:'Segoe UI'; font-size:14px;")
        layout.addWidget(self.date_label)

        layout.addStretch(1)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        now = QDateTime.currentDateTime()
        self.time_label.setText(now.toString("hh:mm:ss"))
        currentdate = datetime.now().strftime("%b %d, %Y")
        self.date_label.setText(currentdate)