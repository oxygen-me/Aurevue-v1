from PySide6.QtCore import QObject, Signal
from eventbus import bus


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
            "print": self._print_text,
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
        bus.quitRequested.emit()
        return "Exiting..."

    def _cmd_theme(self, args):
        if not args:
            return "Usage: theme <light|dark>"

        theme_name = args[0].lower()
        if theme_name not in ("light", "dark", "qqftfz"):
            return "Unknown theme. Try 'light' or 'dark'."

        if not self.theme_manager:
            return "Error: No theme manager connected."

        # Apply global theme
        self.theme_manager.apply_to_children(self.root_widget, theme_name)

        # Apply Specific Styles
        try:
            from ui.tiles.presets.command_tile import CommandTile
            for tile in self.root_widget.findChildren(CommandTile):
                tile.apply_output_theme(self.theme_manager.get())

        except Exception as e:
            print(f"[CommandInterpreter] Failed to apply a specialized theme: {e}")

        return f"Theme switched to {theme_name.capitalize()}."

    def _print_text(self, args):
        if not args:
            return "Usage: print <message>"
        message = " ".join(args)
        print(f"[AUREVUE PRINT] {message}")
        return message