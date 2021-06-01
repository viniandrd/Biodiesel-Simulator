class Tank:
    def __init__(self, substance, volume):
        self._substance = substance
        self._volume = volume

    def get_substance(self):
        """Get the substance in the Tank.

        :returns:
        substance (string): The name of substance used in the Tank.
        """

        return self._substance

    def get_volume(self):
        """Get the total volume.

        :returns:
        volume (float): Quantity of volume.
        """

        return self._volume

    def add_volume(self, value):
        """Add volume in it.

        :parameter:
        value (float): Quantity of volume.
        """

        self._volume += value

    def filter_volume(self, value):
        """Filters an amount of volume.

        :parameter:
        value (float): The value to filter.

        :returns:
        value (float): Valuer filtered from total volume if available.
        """

        if (self._volume - value >= 0):
            self._volume -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')