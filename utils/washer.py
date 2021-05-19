class Washer:
    def __init__(self, id):
        self.name = id
        self._volume = 0

    def add_volume(self, value):
        self._volume += value

    def wash(self):
        lost_value = ( 7.5 * self._volume) / 100
        print('\n>> ({}) Washing solution..'.format(self.name))
        self._volume -= lost_value
        washed = self._volume
        self._volume -= washed
        print('<< ({}) Solution washed.\n'.format(self.name))

        return washed