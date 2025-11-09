from PySide6.QtCore import Qt, Signal, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy
from ui.tileboard.tile import TileWidget


class MusicTile(TileWidget):
    """Aurevue Music Tile (visual shell). No external APIs yet.
       Shows album art, track/artist, and basic controls.
       Emits play/pause/next/prev signals for integration later.
    """

    sig_play_pause = Signal()
    sig_next = Signal()
    sig_prev = Signal()

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="music", tile_type="music", **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ---------- layout fix ----------
        root = self.inner_layout
        root.setSpacing(10)
        root.setAlignment(Qt.AlignmentFlag.AlignTop)

        # --- Styles (light mode; moods can override later) ---
        self.setStyleSheet("""
            MusicTile {
                background-color: #ffffff;
                border-radius: 12px;
            }
            QLabel {
                background: transparent;
                color: #202020;
            }
            QPushButton {
                background-color: #f4f4f4;
                border: 1px solid #d8d8d8;
                border-radius: 8px;
                padding: 6px 10px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #ececec;
            }
        """)

        # --- Top Row: Album Art + Meta ---
        top = QHBoxLayout()
        top.setSpacing(12)

        self.cover = QLabel()
        self.cover.setFixedSize(88, 88)
        self.cover.setScaledContents(True)
        self.cover.setPixmap(self._placeholder_pixmap(88, 88))

        meta_col = QVBoxLayout()
        meta_col.setSpacing(4)

        self.title = QLabel("No Track")
        self.title.setFont(QFont("Segoe UI Semibold", 12))
        self.title.setWordWrap(True)

        self.artist = QLabel("—")
        f = QFont("Segoe UI", 10)
        self.artist.setFont(f)
        self.artist.setStyleSheet("color:#5a5a5a;")
        self.artist.setWordWrap(True)

        meta_col.addWidget(self.title)
        meta_col.addWidget(self.artist)
        meta_col.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        )

        top.addWidget(self.cover)
        top.addLayout(meta_col)
        top.addStretch(1)

        # --- Controls Row ---
        controls = QHBoxLayout()
        controls.setSpacing(8)

        self.btn_prev = QPushButton("Prev")
        self.btn_play = QPushButton("Play")
        self.btn_next = QPushButton("Next")

        self.btn_prev.clicked.connect(self.sig_prev.emit)
        self.btn_play.clicked.connect(self.sig_play_pause.emit)
        self.btn_next.clicked.connect(self.sig_next.emit)

        controls.addWidget(self.btn_prev)
        controls.addWidget(self.btn_play)
        controls.addWidget(self.btn_next)
        controls.addStretch(1)

        # --- Progress (placeholder) ---
        self.progress = QLabel("00:00 — 00:00")
        self.progress.setStyleSheet("color:#7a7a7a; font-size:11px;")

        # --- Assemble ---
        root.addLayout(top)
        root.addLayout(controls)
        root.addWidget(self.progress)

        # --- Album art fade animation ---
        self._cover_fade = QPropertyAnimation(self.cover, b"windowOpacity", self)
        self._cover_fade.setDuration(200)
        self._cover_fade.setEasingCurve(QEasingCurve.Type.InOutQuad)

    # ---------- Public API ----------
    def set_track(self, title: str, artist: str):
        self.title.setText(title or "Unknown Track")
        self.artist.setText(artist or "Unknown Artist")

    def set_cover(self, pixmap: QPixmap | None):
        if pixmap is None or pixmap.isNull():
            pixmap = self._placeholder_pixmap(88, 88)
        self._cover_fade.stop()
        self.cover.setWindowOpacity(0.0)
        self.cover.setPixmap(pixmap)
        self._cover_fade.setStartValue(0.0)
        self._cover_fade.setEndValue(1.0)
        self._cover_fade.start()

    def set_playing(self, playing: bool):
        self.btn_play.setText("Pause" if playing else "Play")

    def set_progress_text(self, text: str):
        self.progress.setText(text)

    # ---------- Helpers ----------
    def _placeholder_pixmap(self, w: int, h: int) -> QPixmap:
        pm = QPixmap(w, h)
        pm.fill(Qt.lightGray)
        return pm
