# -------------------------------------
AUR_VERSION = "0.0.5-prealpha"
# -------------------------------------

class Bootstrapper:
    def __init__(self):
        self.ready = False
        self.data = {}

    def initialize(self):
        print("[Bootstrapper] Starting checks...")

        try:
            self.data["config"] = self.load_config()
        except Exception:
            raise RuntimeError("[Bootstrapper] Failed to load config")
        self.data["version"] = AUR_VERSION
        self.data["UPD"] = 0
        self.data["status"] = "OK"

        print("[Bootstrapper] Checks complete")

        self.ready = True
        return self.ready, self.data

    def load_config(self):
        return {"theme": "light", "clock": "24h"}