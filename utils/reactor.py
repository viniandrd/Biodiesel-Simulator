from threading import Event
import random, time
class Reactor:
    reactorEvent = Event()
    def __init__(self):
        self._active = False
        self._naoh_volume = 0.0
        self._etoh_volume = 0.0
        self._oil_volume = 0.0
        self._total_volume = 0.0
        self._volume_processed = 0.0
        self._is_processing = False
        self._is_resting = False

    # ---- Set's
    def add_naoh(self, value):
        self._naoh_volume += value

    def add_etoh(self, value):
        self._etoh_volume += value

    def add_oil(self, value):
        self._oil_volume += value

    # ---- Get's
    def get_naoh_volume(self):
        return float(self._naoh_volume)

    def get_etoh_volume(self):
        return float(self._etoh_volume)

    def get_oil_volume(self):
        return float(self._oil_volume)

    def is_resting(self):
        return self._is_resting

    def get_total_volume(self):
        return self._naoh_volume + self._etoh_volume + self._oil_volume

    def update(self):
        self._total_volume = self._naoh_volume + self._etoh_volume + self._oil_volume

    # ---- Filter
    def filter_naoh(self, value):
        if (self._naoh_volume - value >= 0):
            self._naoh_volume -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def filter_etoh(self, value):
        if (self._etoh_volume - value >= 0):
            self._etoh_volume -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def filter_oil(self, value):
        if (self._oil_volume - value >= 0):
            self._oil_volume -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def filter_volume_processed(self, value):
        if (self._volume_processed - value >= 0):
            self._volume_processed -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')
    # ---- Events

    def process(self):
        self._is_processing = True
        self.reactorEvent.clear()

        print('\n>> Processing Reactor..')
        self.filter_naoh(1.25)
        self.filter_etoh(2.50)
        self.filter_oil(1.25)
        self._volume_processed += 1.25 + 2.50 + 1.25
        print('<< Reactor processed.\n')

        time.sleep(1)
        self._is_processing = False

    def launch(self):

        print('\n>> Launching volume from Reactor..')
        volume_to_launch = 3
        self.filter_volume_processed(volume_to_launch)
        self._is_resting = True
        print('<< Launched.\n')
        # Waits 5 seconds to be able to launch again
        time.sleep(5)

        return volume_to_launch