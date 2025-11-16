import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from core.appshell import AppShell
from core.themes import theme_manager

print("[Main] Start Registered")

app = QApplication(sys.argv)

window = AppShell(theme_manager=theme_manager)
window.show()
sys.exit(app.exec())

