from PySide6.QtWidgets import QLabel

from ui.pages.page import BasePage

class SettingsPage(BasePage):
    page_id = 1
    page_type = "settings"
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = self.inner_layout
        self.setLayout(layout)

        test_label = QLabel("Test Page For SETTINGS BUTTON")
        test_label.setStyleSheet("font-family: Segoe UI; font-weight: bold; font-size: 24px;")
        layout.addWidget(test_label, 0, 0)