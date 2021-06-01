class Tank_NaOHEtOH:
    def __init__(self, id, naoh_volume, etoh_volume):
        self._name = id
        self._naoh_volume = naoh_volume
        self._etoh_volume = etoh_volume
        self._total_volume = self._naoh_volume + self._etoh_volume

    # ---- Get's
    def get_name(self):
        """Get the name of the Tank.

        :returns:
        name (string): The name of the Tank.
        """

        return self._name

    def get_naoh_volume(self):
        """Returns the amount of NaOH volume in it.

        :returns:
        naoh_volume (float): Amount of NaOH volume.
        """

        return self._naoh_volume

    def get_etoh_volume(self):
        """Returns the amount of EtOH volume in it.

        :returns:
        etoh_volume (float): Amount of EtOH volume.
        """

        return self._etoh_volume

    def get_total_volume(self):
        """Returns the total volume (EtOH + NaOH).

        :returns:
        total volume (float): Amount of EtOH + NaOH volume.
        """
        return self._naoh_volume + self._etoh_volume

    # ---- Add volume
    def add_naoh_volume(self, value):
        """Add amount of NaOH in it.

        :parameter:
        value (float): Amount of NaOH volume.
        """

        self._naoh_volume += value

    def add_etoh_volume(self, value):
        """Add amount of EtOH in it.

        :parameter:
        value (float): Amount of EtOH volume.
        """

        self._etoh_volume += value

    # ---- Filters
    def filter_naoh(self, value):
        """Filters an amount of NaOH.

        :parameter:
        value (float): The value to filter.

        :returns:
        value (float): Valuer filtered from solution if available.
        """

        if(self._naoh_volume - value >= 0):
            self._naoh_volume -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def filter_etoh(self, value):
        """Filters an amount of EtOH.

        :parameter:
        value (float): The value to filter.

        :returns:
        value (float): Valuer filtered from solution if available.
        """

        if (self._etoh_volume - value >= 0):
            self._etoh_volume -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')