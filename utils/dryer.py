import time


class Dryer:
    def __init__(self, id):
        self._name = id
        self._volume = 0
        self._ready_to_dry = False

    def add_volume(self, value):
        """Add volume in.

        :parameter:
        value (float): Quantity of volume."""

        self._volume += value
        self._ready_to_dry = True
        print('>> {} Volume Received '.format(self._name))

    def ready(self):
        """Returns a flag (bool) to know if the Dryer can dry the volume.

        :returns:
        ready_to_dry (bool): Flag to know if the Dryer is ready.
        """

        return self._ready_to_dry

    def dry(self, tank):
        """Dry the volume in it. In each 5 seconds the dried volume is equal to 1L.

        :parameter:
        tank (Tank): The Tank to send the dried volume.
        """

        # Dry 1L in each 5 seconds
        while self._volume > 0.0:
            dry_volume = 1
            print('\n>> ({}) Drying solution..'.format(self._name))

            # Checks if there is any volume to dry
            if self._volume - dry_volume < 0.0:
                dry_volume = self._volume

            # Lost of 3% of the volume dryed
            lost_value = (3 * dry_volume) / 100
            tank.add_volume(dry_volume - lost_value)

            # 1L separated to dry
            self._volume -= dry_volume

            print('<< ({}) Solution dryed.\n'.format(self._name))
            # Waits 5 second to dry again
            time.sleep(5)

        # After all volume is dried, set flag to False
        self._ready_to_dry = False