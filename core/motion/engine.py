from PySide6.QtCore import QPropertyAnimation, QEasingCurve

# ------------------------------------------
# Core easing presets
# ------------------------------------------
EASINGS = {
    "OutCubic": QEasingCurve.Type.OutCubic,
    "OutQuint": QEasingCurve.Type.OutQuint,
    "OutBack": QEasingCurve.Type.OutBack,
    "OutExpo": QEasingCurve.Type.OutExpo,
    "InOutCubic": QEasingCurve.Type.InOutCubic,
}

# ------------------------------------------
# Base animation helper
# ------------------------------------------
def animate(widget, prop: bytes, start, end, ms=220, easing="OutCubic"):

    anim = QPropertyAnimation(widget, prop)
    anim.setStartValue(start)
    anim.setEndValue(end)
    anim.setDuration(ms)
    anim.setEasingCurve(EASINGS.get(easing, QEasingCurve.Type.OutCubic))
    anim.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)
    return anim


# ------------------------------------------
# Multi-stage chaining helper
# ------------------------------------------
def timeline(widget, keyframes: list):

    animations = []
    for frame in keyframes:
        prop, start, end, ms, easing = frame
        anim = QPropertyAnimation(widget, prop)
        anim.setStartValue(start)
        anim.setEndValue(end)
        anim.setDuration(ms)
        anim.setEasingCurve(EASINGS.get(easing, QEasingCurve.Type.OutCubic))
        animations.append(anim)

    # Sequential Chaining
    for i in range(len(animations) - 1):
        anim = animations[i].finished.connect(animations[i + 1].start)

    animations[0].start()
    return animations