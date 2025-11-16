from .manager import ThemeManager
from .light import THEME_LIGHT
from .dark import THEME_DARK
from .qqftfz import THEME_QQFTFZ

theme_manager = ThemeManager()
theme_manager.register("light", THEME_LIGHT)
theme_manager.register("dark", THEME_DARK)
theme_manager.register("qqftfz", THEME_QQFTFZ)

# Set default theme
theme_manager.active = "light"