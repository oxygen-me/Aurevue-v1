# mood/moods/twilight.py
MOOD_TWILIGHT = {
    "base_theme": "dark",
    "gradient": {
        "x1": 0, "y1": 0, "x2": 1, "y2": 1,
        "start": "#ff82d2",  # warm pink
        "end": "#6273ff",    # cool violet-blue
    },
    "accent": "#d68aff",
    "text": {
        "primary": "#f2e9f8",
        "secondary": "#b9a6c9",
    },
    "surface": {
        "dark": "#18141f",
        "light": "#f3ebfa"
    },
    "energy": 0.6,  # moderate motion bias
    "logo_asset": "assets/logos/AurevueTwilight.png",
    # --- Future Phase ---
    "motion_profile": None,  # later: fade-and-rise wave motion
    "sound_profile": None,   # later: ambient synth swell / soft strings
}