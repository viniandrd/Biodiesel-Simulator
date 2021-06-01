class Washer:
    def __init__(self, id):
        self.name = id
        self._volume = 0

    def add_volume(self, value):
        """Add volumes in it.

        :parameter:
        value (float): Amount of volume to add.
        """
        self._volume += value

    def wash(self):
        """Wash solution in the Washer.

        :returns:
        washed (float): Amount of washed solution.
        """

        # 7.5% of the total volume is lost
        lost_value = ( 7.5 * self._volume) / 100
        print('\n>> ({}) Washing solution..'.format(self.name))
        self._volume -= lost_value
        washed = self._volume

        # Solution washed
        self._volume -= washed
        print('<< ({}) Solution washed.\n'.format(self.name))

        return washed