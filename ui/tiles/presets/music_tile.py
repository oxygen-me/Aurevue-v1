from PySide6.QtCore import Qt, Signal, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy

from ui.tileboard.tile import TileWidget  # your base TileWidget

class MusicTile(TileWidget):
    """Aurevue Music Tile (visual shell). No external APIs yet.
       Shows album art, track/artist, and basic controls.
       Emits play/pause/next/prev signals for integration later.
    """

    # Signals you can connect to Spotify/AureAux later
    sig_play_pause = Signal()
    sig_next = Signal()
    sig_prev = Signal()

    def __init__(self, parent=None):
        super().__init__(parent, tile_id="music", tile_type="music")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # --- Layout from base TileWidget ---
        root = self.layout()
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(10)
        root.setAlignment(Qt.AlignmentFlag.AlignTop)

        # --- Styles (light mode; moods can override later) ---
        self.setStyleSheet("""
            MusicTile {
                background-color: #ffffff;
                border: 1px solid #E3E3E3;
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

        # Album Art
        self.cover = QLabel()
        self.cover.setFixedSize(88, 88)  # fits nicely in a 2x2 cell tile
        self.cover.setScaledContents(True)
        self.cover.setPixmap(self._placeholder_pixmap(88, 88))

        # Title/Artist block
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
        meta_col.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        top.addWidget(self.cover)
        top.addLayout(meta_col)
        top.addStretch(1)

        # --- Controls Row ---
        controls = QHBoxLayout()
        controls.setSpacing(8)

        self.btn_prev = QPushButton("Prev")
        self.btn_play = QPushButton("Play")
        self.btn_next = QPushButton("Next")

        # Hook signals for later integration
        self.btn_prev.clicked.connect(self.sig_prev.emit)
        self.btn_play.clicked.connect(self.sig_play_pause.emit)
        self.btn_next.clicked.connect(self.sig_next.emit)

        controls.addWidget(self.btn_prev)
        controls.addWidget(self.btn_play)
        controls.addWidget(self.btn_next)
        controls.addStretch(1)

        # --- Progress (placeholder) ---
        self.progress = QLabel("")  # can be replaced by a proper bar later
        self.progress.setStyleSheet("color:#7a7a7a; font-size:11px;")
        self.progress.setText("00:00 — 00:00")

        # --- Assemble ---
        root.addLayout(top)
        root.addLayout(controls)
        root.addWidget(self.progress)

        # --- Album art fade animation (for future track changes) ---
        self._cover_fade = QPropertyAnimation(self.cover, b"windowOpacity", self)
        self._cover_fade.setDuration(200)
        self._cover_fade.setEasingCurve(QEasingCurve.Type.InOutQuad)

    # ---------- Public API (no external deps) ----------

    def set_track(self, title: str, artist: str):
        """Update text labels."""
        self.title.setText(title or "Unknown Track")
        self.artist.setText(artist or "Unknown Artist")

    def set_cover(self, pixmap: QPixmap | None):
        """Fade to a new album cover (pixmap)."""
        if pixmap is None or pixmap.isNull():
            pixmap = self._placeholder_pixmap(88, 88)

        # simple fade
        self._cover_fade.stop()
        self.cover.setWindowOpacity(0.0)
        self.cover.setPixmap(pixmap)
        self._cover_fade.setStartValue(0.0)
        self._cover_fade.setEndValue(1.0)
        self._cover_fade.start()

    def set_playing(self, playing: bool):
        """Toggle play/pause button label to reflect state."""
        self.btn_play.setText("Pause" if playing else "Play")

    def set_progress_text(self, text: str):
        """Set simple time text until we wire a real progress bar."""
        self.progress.setText(text)

    # ---------- Helpers ----------

    def _placeholder_pixmap(self, w: int, h: int) -> QPixmap:
        pm = QPixmap(w, h)
        pm.fill(Qt.lightGray)
        return pm

