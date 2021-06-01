import time


class Reactor:
    def __init__(self):
        self._active = False
        self._volumes = dict([('NaOH', 0.0), ('EtOH', 0.0), ('Oil', 0.0)])
        '''self._naoh_volume = 0.0
        self._etoh_volume = 0.0
        self._oil_volume = 0.0'''
        self._total_volume = 0.0
        self._volume_processed = 0.0
        self._is_processing = False

    # ---- Set's
    def add_volumes(self, naoh, etoh, oil):
        """Add volumes in it.

        :parameter:
        naoh (float): Amount of NaOH volume.
        etoh (float): Amount of EtOH volume.
        oil. (float): Amount of Oil volume.
        """

        self._volumes['NaOH'] += naoh
        self._volumes['EtOH'] += etoh
        self._volumes['Oil'] += oil

        print('\n <<>> Reactor with: {:.2f} of Oil - {} of NaOH - {} of EtOH <<>>'.format(self._volumes['Oil'],
                                                                                          self._volumes['NaOH'],
                                                                                          self._volumes['EtOH']))

    # ---- Get's
    def get_naoh_volume(self):
        """Returns the amount of NaOH volume in it.

        :returns:
        volumes['NaOH'] (float): Amount of NaOH volume.
        """
        return float(self._volumes['NaOH'])

    def get_etoh_volume(self):
        """Returns the amount of EtOH volume in it.

        :returns:
        volumes['EtOH'] (float): Amount of EtOH volume.
        """
        return float(self._volumes['EtOH'])

    def get_oil_volume(self):
        """Returns the amount of Oil volume in it.

        :returns:
        volumes['Oil'] (float): Amount of Oil volume.
        """
        return float(self._volumes['Oil'])

    def get_volume_processed(self):
        """Returns the amount of processed volume.

        :returns:
        volume_processed (float): Amount of processed volume.
        """
        return self._volume_processed

    def get_total_volume(self):
        """Returns the total volume (EtOH + NaOH + Oil).

        :returns:
        volume_processed (float): Amount of NaOH volume.
        """
        return self._volumes['NaOH'] + self._volumes['EtOH'] + self._volumes['Oil']

    # ---- Filter
    def filter_naoh(self, value):
        """Filters an amount of NaOH.

        :parameter:
        value (float): The value to filter.

        :returns:
        value (float): Valuer filtered from solution if available.
        """

        if (self._volumes['NaOH'] - value >= 0):
            self._volumes['NaOH'] -= value
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

        if (self._volumes['EtOH'] - value >= 0):
            self._volumes['EtOH'] -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def filter_oil(self, value):
        """Filters an amount of Oil.

        :parameter:
        value (float): The value to filter.

        :returns:
        value (float): Valuer filtered from solution if available.
        """

        if (self._volumes['Oil'] - value >= 0):
            self._volumes['Oil'] -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def filter_volume_processed(self, value):
        """Filters an amount of volume processed.

        :parameter:
        value (float): The value to filter.

        :returns:
        value (float): Valuer filtered from processed volume if available.
        """

        if (self._volume_processed - value >= 0):
            self._volume_processed -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def process(self):
        """Process the volume to the processed volume."""

        self._is_processing = True

        print('\n>> Processing Reactor..')
        self.filter_naoh(1.25)
        self.filter_etoh(2.50)
        self.filter_oil(1.25)
        self._volume_processed += 1.25 + 2.50 + 1.25
        print('   Volume processed: {}'.format(self._volume_processed))
        print('<< Reactor processed.\n')

        time.sleep(1)
        self._is_processing = False

    def launch(self, decanter):
        """Launch the processed volume to the Decanter.

        :parameter:
        decanter (Decanter): Decanter object
        """

        print('\n>> Launching volume from Reactor to Decanter..')
        volume_to_launch = 3
        self.filter_volume_processed(volume_to_launch)
        decanter.add_volume(volume_to_launch)
        print('<< Launched.\n')
        # Waits 5 seconds to be able to launch again
        print('   <<!!>> (Reactor) Wait 5 seconds to rest before you can launch again. <<!!>>')