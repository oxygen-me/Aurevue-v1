from PySide6.QtCore import QObject, Signal


class AurevueBus(QObject):

    mainHandshake = Signal()
    quitRequested = Signal()
    configRequested = Signal(int)

bus = AurevueBus()