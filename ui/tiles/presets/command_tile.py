from PySide6.QtGui import QFont

from ui.tileboard.tile import TileWidget  # adjust path as needed
from PySide6.QtWidgets import QLabel, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Qt, Signal
from core.logic.command_logic import CommandInterpreter


class CommandTile(TileWidget):
    sig_exit_requested = Signal()

    sig_command = Signal(str)

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="command", tile_type="command", **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ----- Layout -----
        layout = self.inner_layout
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)


        # ----- Content -----
        self.title = QLabel("Command Center")
        self.title.setStyleSheet("font-family:'Segoe UI Semibold'; font-size:14px;")

        self.input = QLineEdit(self)
        self.input.setFont(QFont("Segoe UI", 12))
        self.input.setPlaceholderText("> Enter command.")
        self.input.returnPressed.connect(self._on_enter)

        self.output = QLabel("Ready.")
        self.output.setWordWrap(True)
        self.output.setFont(QFont("Segoe UI", 12))
        self.output.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(self.title)
        layout.addWidget(self.input, 1)
        layout.addWidget(self.output, 1)
        layout.setStretch(0, 0)
        layout.setStretch(1, 1)
        layout.setStretch(2, 1)

        self._connect_interpreter()

    def _on_enter(self):
        cmd = self.input.text().strip()
        if not cmd:
            return
        self.sig_command.emit(cmd)
        self.input.clear()

    def _update_output(self, text: str):
        self.output.setText(text)

    # ----- Interpreter Wiring -----
    def _connect_interpreter(self):
        from core.themes import theme_manager
        self.interpreter = CommandInterpreter(
            theme_manager=theme_manager,
            root_widget=self.window(),
        )
        self.sig_command.connect(self.interpreter.process)
        self.interpreter.sig_output.connect(self._update_output)
        self.interpreter.sig_exit_requested.connect(self.sig_exit_requested)

    def apply_output_theme(self, tokens: dict | None = None):
        while not tokens:
            pass

        output = tokens.get("output", {})
        text = tokens.get("text", {})

        bg = output.get("background", "#F4F4F6")
        fg = text.get("primary", "#000000")

        self.output.setProperty("theme-bg", bg)
        self.output.setProperty("theme-fg", fg)

        self.output.setStyleSheet(f"""
        QLabel {{
        background-color: {bg};
        color: {fg};
        border-radius: 6px;
        padding: 8px 10px;
        }}
    """)

        self.output.style().unpolish(self.output)
        self.output.style().polish(self.output)
        self.output.update()