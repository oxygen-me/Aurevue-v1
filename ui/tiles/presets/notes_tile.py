from ui.tileboard.tile import TileWidget
from PySide6.QtWidgets import QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
import markdown2


class NotesTile(TileWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="notes", tile_type="notes", **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ----- Layout -----
        layout = self.inner_layout
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # ----- Styles -----
        self.inner.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 12px;
        """)
        self.setStyleSheet("""
            QLabel {
                background: transparent;
                border: none;
                color: #202020;
                font-family: 'Segoe UI';
                font-size: 13px;
            }
            QTextEdit {
                background-color: #f7f7f7;
                border: 1px solid #dcdcdc;
                border-radius: 8px;
                padding: 8px;
                font-family: 'Segoe UI';
                font-size: 13px;
                color: #333333;
            }
            QPushButton {
                background-color: #f3f3f3;
                color: #202020;
                border-radius: 6px;
                border: 1px solid #202020;
                font-size: 12px;
                padding: 4px 8px;
            }
            QPushButton:hover {
                background-color: #e8e8e8;
            }
        """)

        # ----- Title Bar -----
        self.title_row = QHBoxLayout()
        self.title = QLabel("Notes")
        self.toggle_btn = QPushButton("Preview")
        self.toggle_btn.clicked.connect(self.toggle_preview)
        self.title_row.addWidget(self.title)
        self.title_row.addStretch(1)
        self.title_row.addWidget(self.toggle_btn)
        layout.addLayout(self.title_row)

        # ----- Editor + Preview -----
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Write in Markdown...")
        self.preview = QLabel()
        self.preview.setWordWrap(True)
        self.preview.setTextFormat(Qt.TextFormat.RichText)
        self.preview.hide()  # start in edit mode

        layout.addWidget(self.editor)
        layout.addWidget(self.preview)
        layout.addStretch(1)

        self.previewing = False

    # ----- Toggle between Edit and Preview -----
    def toggle_preview(self):
        if self.previewing:
            self.preview.hide()
            self.editor.show()
            self.toggle_btn.setText("Preview")
        else:
            md_text = self.editor.toPlainText()
            html = markdown2.markdown(md_text)
            self.preview.setText(html)
            self.preview.show()
            self.editor.hide()
            self.toggle_btn.setText("Edit")

        self.previewing = not self.previewing