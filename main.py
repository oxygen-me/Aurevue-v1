import sys
from PySide6.QtWidgets import QApplication
from core.appshell import AppShell

app = QApplication(sys.argv)

window = AppShell()
window.show()

sys.exit(app.exec())