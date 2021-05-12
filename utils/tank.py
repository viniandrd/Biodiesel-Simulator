class Tank:
    def __init__(self, substance, volume):
        self.substance = substance
        self.volume = volume

    def get_substance(self):
        return self.substance

    def get_volume(self):
        return self.substance

    def add_volume(self, value):
        self.volume += value