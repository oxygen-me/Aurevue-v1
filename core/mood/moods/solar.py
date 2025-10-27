# mood/moods/solar.py
MOOD_SOLAR = {
    "base_theme": "light",  # primarily warm, bright surfaces
    "gradient": {
        "x1": 0, "y1": 0, "x2": 1, "y2": 1,
        "start": "#ff512f",  # ember red
        "end": "#f09819",    # golden orange
    },
    "accent": "#ffd86f",
    "text": {
        "primary": "#1a1208",
        "secondary": "#5e4a2f",
    },
    "surface": {
        "dark": "#0e0b08",
        "light": "#fff9f2"
    },
    "energy": 1.0,  # highest kinetic bias
    "logo_asset": "assets/logos/AurevueSolar.png",
    # --- Future ---
    "motion_profile": None,  # later: rising flare + bounce-in
    "sound_profile": None,   # later: gentle spark chime / bright synth pad
}