from PySide6.QtCore import QObject, Property, QPropertyAnimation, QEasingCurve, QRect
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor


class HoverBehavior(QObject):
    """
    MagMotion Phase 0 — Refined tactile hover.
    Smooth, reversible animation that respects original geometry.
    """

    def __init__(self, target: QWidget, scale_factor: float = 1.02, lift: int = 4, duration: int = 180):
        super().__init__(target)
        self.target = target
        self.scale_factor = scale_factor
        self.lift = lift
        self.duration = duration
        self._scale = 1.0
        self._base_geom: QRect | None = None
        self._shadow = self._init_shadow()
        self._anim = self._init_anim()

    # ---------------- Setup ----------------
    def _init_shadow(self):
        shadow = QGraphicsDropShadowEffect(self.target)
        shadow.setBlurRadius(24)
        shadow.setOffset(0, 6)
        shadow.setColor(QColor(0, 0, 0, 64))
        self.target.setGraphicsEffect(shadow)
        return shadow

    def _init_anim(self):
        anim = QPropertyAnimation(self, b"scale")
        anim.setDuration(self.duration)
        anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        return anim

    # ---------------- Property ----------------
    def get_scale(self):
        return self._scale

    def set_scale(self, value: float):
        self._scale = value
        if self._base_geom is None:
            self._base_geom = self.target.geometry()

        base = self._base_geom
        cx, cy = base.center().x(), base.center().y()
        new_w = base.width() * value
        new_h = base.height() * value
        new_x = int(cx - new_w / 2)
        new_y = int(cy - new_h / 2 - (self.lift * (value - 1.0) * 50))  # lift upward subtly
        self.target.setGeometry(new_x, new_y, int(new_w), int(new_h))

        # Shadow follows intensity
        blur = 24 + (value - 1.0) * 12
        offset_y = 6 + (value - 1.0) * 6
        alpha = int(64 + (value - 1.0) * 80)
        color = QColor(0, 0, 0, min(alpha, 120))
        self._shadow.setBlurRadius(blur)
        self._shadow.setOffset(0, offset_y)
        self._shadow.setColor(color)

    scale = Property(float, get_scale, set_scale)

    # ---------------- Hooks ----------------
    def enter(self):
        if self._base_geom is None:
            self._base_geom = self.target.geometry()
        self._animate_to(self.scale_factor)

    def leave(self):
        if self._base_geom:
            self._animate_to(1.0)

    # ---------------- Internals ----------------
    def _animate_to(self, value: float):
        self._anim.stop()
        self._anim.setStartValue(self._scale)
        self._anim.setEndValue(value)
        self._anim.start()