import time
class Decanter:
    def __init__(self):
        self._maximum_capacity = 10.0
        self._volume = 0
        self._exhaust_volumes = dict([ ('Glycerin', 0.0), ('EtOH', 0.0), ('Washing', 0.0)])
        self._ready_to_decant = False

    def add_volume(self, value):
        if self._volume + value > self._maximum_capacity:
            print('\n <!!> Decanter is in full capacity <!!> \n')
        else:
            self._volume += value
        print('   <<>> Decanter with {:.2f}/{} of volume <<>>'.format(self._volume, self._maximum_capacity))
        self._ready_to_decant = True

    def ready(self):
        return self._ready_to_decant

    def exhaust(self, glycerin_tank, washer_1, dryer_1):
        # 2% of Glycerin, 9% of EtOH and 89% of Washing solution
        self._exhaust_volumes['Glycerin'] += (2 * self._volume) / 100
        self._exhaust_volumes['EtOH'] += (9 * self._volume) / 100
        self._exhaust_volumes['Washing'] += (89 * self._volume) / 100

        # Clean the total volume of decanter
        self._volume -= self._exhaust_volumes['Glycerin']
        self._volume -= self._exhaust_volumes['EtOH']
        self._volume -= self._exhaust_volumes['Washing']

        # Exhaust the volumes to the Glycerin tank, Dryer 1 and Washer 1
        glycerin_tank.add_volume(self._exhaust_volumes['Glycerin'])
        washer_1.add_volume(self._exhaust_volumes['Washing'])
        dryer_1.add_volume(self._exhaust_volumes['EtOH'])

        # Filter values
        self._exhaust_volumes['Glycerin'] -= self._exhaust_volumes['Glycerin']
        self._exhaust_volumes['Washing'] -= self._exhaust_volumes['Washing']
        self._exhaust_volumes['EtOH'] -= self._exhaust_volumes['EtOH']
        print('<< (Decanter) Exhausted Glycerin, EtOH and Washing Solution <<')

        self._ready_to_decant = False
        print('   <<>> Decanter with {:.2f}/{} of volume <<>>'.format(self._volume, self._maximum_capacity))