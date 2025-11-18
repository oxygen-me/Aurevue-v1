import sys
from PySide6.QtWidgets import QApplication
from core.appshell import AppShell
from core.themes import theme_manager
from eventbus import bus
from bootstrap import Bootstrapper

print("[Main] Start Registered")

app = QApplication(sys.argv)

print("[Main] Attempting handshake...")

boot = Bootstrapper()
ready, data = boot.initialize()

if not ready:
    raise RuntimeError("[Main] Bootstrap failed!")

print ("[Main] Handshake finalized")

window = AppShell(theme_manager=theme_manager, reference=data)

bus.quitRequested.connect(app.quit)

window.show()
sys.exit(app.exec())