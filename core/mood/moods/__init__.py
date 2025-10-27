# Aurevue/mood/moods/__init__.py

from .aurora import MOOD_AURORA
from .solar import MOOD_SOLAR
from .twilight import MOOD_TWILIGHT
from .crystal import MOOD_CRYSTAL
from .voidline import MOOD_VOIDLINE

MOOD_REGISTRY = {
    "Aurora": MOOD_AURORA,
    "Solar": MOOD_SOLAR,
    "Twilight": MOOD_TWILIGHT,
    "Crystal": MOOD_CRYSTAL,
    "Voidline": MOOD_VOIDLINE,
}