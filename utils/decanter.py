import time
class Decanter:
    def __init__(self):
        self._maximum_capacity = 10.0
        self._volume = 0
        self._rest_time = 5
        self._is_in_rest_time = False

    def fill(self, value):
        if self._volume + value > self._maximum_capacity:
            print('\n <!!> Decanter is in full capacity <!!> \n')
        else:
            self._volume += value

    def rest(self, timer):
        self._is_in_rest_time = True
        time.sleep(timer)
        self._is_in_rest_time = False

    def is_in_rest(self):
        return self._is_in_rest_time

    def launch(self):
        volume_to_decant = 3
        self.decant_volume(volume_to_decant)

        glycerin = (2 * volume_to_decant) / 100
        etoh = (9 * volume_to_decant) / 100
        washing_solution = (89 * volume_to_decant) / 100


        return glycerin, etoh, washing_solution

    def decant_volume(self, value):
        self._volume -= value



