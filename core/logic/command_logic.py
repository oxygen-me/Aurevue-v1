from PySide6.QtCore import QObject, Signal

class CommandInterpreter(QObject):

    sig_output = Signal(str)
    sig_exit_requested = Signal()

    def __init__(self, theme_manager=None, root_widget=None):
        super().__init__()
        self.theme_manager = theme_manager
        self.root_widget = root_widget

        self.commands = {
            "mood": self._cmd_mood,
            "launch": self._cmd_launch,
            "help": self._cmd_help,
            "exit": self._cmd_exit,
            "theme": self._cmd_theme,
        }

    def process(self, raw_input: str):

        if not raw_input.strip():
            return

        parts = raw_input.strip().split()
        cmd, args = parts[0].lower(), parts[1:]

        if cmd in self.commands:
            try:
                response = self.commands[cmd](args)
            except Exception as e:
                response = f"Error: {e}"
        else:
            response = f"Unknown command: {cmd}. Type 'help' for a list."

        self.sig_output.emit(response)

    # ---------- Command Functions ----------

    def _cmd_mood(self, args):
        if not args:
            return "Usage: mood <name>"
        mood_name = args[0].capitalize()
        # Calls mood system here later
        return f"Mood changed to {mood_name}."

    def _cmd_launch(self, args):
        return "Launching app..."

    def _cmd_help(self, args):
        cmds = ", ".join(self.commands.keys())
        return f"Available commands: {cmds}."

    def _cmd_exit(self, args):
        self.sig_output.emit("Shutting down Aurevue...")
        self.sig_exit_requested.emit()
        return "Exiting..."

    def _cmd_theme(self, args):
        if not args:
            return "Usage: theme <light|dark>"

        theme_name = args[0].lower()
        if theme_name not in ("light", "dark"):
            return "Unknown theme. Try 'light' or 'dark'."

        if not self.theme_manager:
            return "Error: No theme manager connected."

        self.theme_manager.apply_to_children(self.root_widget)
        self.theme_manager.apply(self.root_widget, theme_name)
        return f"Theme switched to {theme_name.capitalize()}."