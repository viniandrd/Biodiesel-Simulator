class Tank:
    def __init__(self, substance, volume):
        self.substance = substance
        self.volume = volume

    def get_substance(self):
        return self.substance

    def get_volume(self):
        return self.volume

    def add_volume(self, value):
        self.volume += value

    def filter_volume(self, value):
        if (self.volume - value >= 0):
            self.volume -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')