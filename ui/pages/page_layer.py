from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class PageLayer(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("PageLayer")
        self.hide()

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

    def resizeEvent(self, e):
        self.setGeometry(self.parent().rect())
        super().resizeEvent(e)

