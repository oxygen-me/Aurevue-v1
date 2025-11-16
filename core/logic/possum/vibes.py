class VibeSystem:

    ENERGY_MAP = {
        str: "gentle",
        int: "aggressive",
        float: "liquid",
        list: "liquid",
        dict: "confused",
        type(None): "sleepy",
        bool: "assertive",
    }

    def detect(self, value):
        return self.ENERGY_MAP.get(type(value), "unknown")

    def resolve(self, functions, arg):
        arg_vibe = self.detect(arg)

        for fn in functions:
            if fn.vibe == arg_vibe:
                return fn

        print("politely panic")
        return functions[0]
