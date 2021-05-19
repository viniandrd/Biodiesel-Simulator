import time
class Dryer:
    def __init__(self, id):
        self.name = id
        self._volume = 0
        self._ready_to_dry = False

    def add_volume(self, value):
        self._volume += value
        self._ready_to_dry = True
        print('>> {} Volume Received '.format(self.name))

    def ready(self):
        return self._ready_to_dry

    def dry(self, tank):
        # Dry 1L in each 5 seconds
        while self._volume > 0.0:
            dry_volume = 1
            print('\n>> ({}) Drying solution..'.format(self.name))

            if self._volume - dry_volume < 0.0:
                dry_volume = self._volume

            lost_value = (3 * dry_volume) / 100
            tank.add_volume(dry_volume - lost_value)

            # 1L separated to dry
            self._volume -= dry_volume
            # Lost of 3% of the volume dryed

            print('<< ({}) Solution dryed.\n'.format(self.name))
            time.sleep(5)

        self._ready_to_dry = False