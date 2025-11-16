import requests
from datetime import datetime
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QLabel
from ui.tileboard.tile import TileWidget


class WeatherTile(TileWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="weather", tile_type="weather", **kwargs)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # ----- Layout -----
        layout = self.inner_layout
        layout.setSpacing(8)

        # ----- Labels -----
        self.title = QLabel("Weather")
        self.title.setStyleSheet("font-family:'Segoe UI Semibold'; font-size:14px;")

        self.temp = QLabel("—°")
        self.temp.setStyleSheet("font-family:'Segoe UI Semibold'; font-size:28px;")

        self.condition = QLabel("Loading...")
        self.condition.setStyleSheet("font-family:'Segoe UI'; font-size:14px;")

        self.loc = QLabel("")
        self.loc.setStyleSheet("font-family:'Segoe UI'; font-size:12px;")

        layout.addWidget(self.title)
        layout.addWidget(self.temp)
        layout.addWidget(self.condition)
        layout.addWidget(self.loc)
        layout.addStretch(1)

        # ----- Timer -----
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_weather)
        self.timer.start(15 * 60 * 1000)  # every 15 minutes
        self.update_weather()

    # -------------------------------------------------
    # Weather update using Open-Meteo (no API key)
    # -------------------------------------------------
    def update_weather(self):
        try:
            # --- 1️⃣ Get approximate user location ---
            loc_resp = requests.get("https://ipinfo.io/json", timeout=6)
            loc_resp.raise_for_status()
            loc_data = loc_resp.json()
            lat, lon = map(float, loc_data.get("loc", "0,0").split(","))
            city = loc_data.get("city", "Unknown")
            country = loc_data.get("country", "")
            self.loc.setText(f"{city}, {country}")

            # --- 2️⃣ Query Open-Meteo ---
            params = {
                "latitude": lat,
                "longitude": lon,
                "current_weather": True,  # ✅ correct endpoint field
                "timezone": "auto",
                "temperature_unit": "fahrenheit" if country == "US" else "celsius",
            }
            resp = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=8)
            data = resp.json()
            current = data.get("current_weather", {})

            temp = round(current.get("temperature", 0))
            code = current.get("weathercode", -1)
            is_day = current.get("is_day", 1) == 1

            # 🌞/🌙 Emoji Variants
            if is_day:
                weather_map = {
                    0: "☀️ Clear",
                    1: "🌤 Mostly Clear",
                    2: "⛅ Partly Cloudy",
                    3: "☁️ Overcast",
                    45: "🌫 Fog",
                    48: "🌫 Fog",
                    51: "🌦 Drizzle",
                    61: "🌧 Rain",
                    71: "❄️ Snow",
                    95: "⛈ Thunderstorm",
                }
            else:
                weather_map = {
                    0: "🌙 Clear",
                    1: "🌙 Few Clouds",
                    2: "☁️ Partly Cloudy",
                    3: "🌌 Overcast Night",
                    45: "🌫 Fog",
                    48: "🌫 Fog",
                    51: "🌧 Drizzle",
                    61: "🌧 Rain",
                    71: "❄️ Snow",
                    95: "🌩 Stormy",
                }

            desc = weather_map.get(code, "—")
            unit = "°F" if country == "US" else "°C"

            # --- 3️⃣ Update UI ---
            self.temp.setText(f"{temp}{unit}")
            self.condition.setText(desc)

        except Exception as e:
            print("Weather update failed:", e)
            self.temp.setText("—°")
            self.condition.setText("Offline")
            self.loc.setText("—")