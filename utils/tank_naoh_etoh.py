class Tank_NaOHEtOH:
    def __init__(self, substance, naoh_volume, etoh_volume):
        self.substance = substance
        self.naoh_volume = naoh_volume
        self.etoh_volume = etoh_volume
        self.total_volume = self.naoh_volume + self.etoh_volume

    # ---- Get's
    def get_substance(self):
        return self.substance

    def get_naoh_volume(self):
        return self.naoh_volume

    def get_etoh_volume(self):
        return self.etoh_volume

    def get_total_volume(self):
        return self.naoh_volume + self.etoh_volume

    # ---- Add volume
    def add_naoh_volume(self, value):
        self.naoh_volume += value

    def add_etoh_volume(self, value):
        self.etoh_volume += value

    # ---- Filters
    def filter_naoh(self, value):
        if(self.naoh_volume - value >= 0):
            self.naoh_volume -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def filter_etoh(self, value):
        if (self.etoh_volume - value >= 0):
            self.etoh_volume -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')