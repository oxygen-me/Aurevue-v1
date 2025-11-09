from PySide6.QtWidgets import QWidget
from ui.tileboard.tileboard import BoardWidget
class BasePage(QWidget):

    BUFFER = 40 # 20px inward offset per edge in sets

    def __init__(self, parent=None, page_id=None, page_type='generic'):
        super(BasePage, self).__init__(parent)

        self.page_id = page_id
        self.page_type = page_type

        # ------------------------------
        # Geometry
        # ------------------------------

        w = h = 120
