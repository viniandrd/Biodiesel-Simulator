from threading import Event
import random, time
class Reactor:
    def __init__(self):
        self._active = False
        self.volumes = dict([ ('NaOH', 0.0), ('EtOH', 0.0), ('Oil', 0.0)])
        self._naoh_volume = 0.0
        self._etoh_volume = 0.0
        self._oil_volume = 0.0
        self._total_volume = 0.0
        self._volume_processed = 0.0
        self._is_processing = False
        self._is_resting = False

    # ---- Set's
    def add_volumes(self, naoh, etoh, oil):
        self.volumes['NaOH'] += naoh
        self.volumes['EtOH'] += etoh
        self.volumes['Oil'] += oil

        print('\n <<>> Reactor with: {:.2f} of Oil - {} of NaOH - {} of EtOH <<>>'.format(self.volumes['Oil'],
                                                                                          self.volumes['NaOH'],
                                                                                          self.volumes['EtOH']))

    # ---- Get's
    def get_naoh_volume(self):
        return float(self.volumes['NaOH'])

    def get_etoh_volume(self):
        return float(self.volumes['EtOH'])

    def get_oil_volume(self):
        return float(self.volumes['Oil'])

    def is_resting(self):
        return self._is_resting

    def get_total_volume(self):
        return self._naoh_volume + self._etoh_volume + self._oil_volume

    def update(self):
        self._total_volume = self._naoh_volume + self._etoh_volume + self._oil_volume

    # ---- Filter
    def filter_naoh(self, value):
        if (self.volumes['NaOH'] - value >= 0):
            self.volumes['NaOH'] -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def filter_etoh(self, value):
        if (self.volumes['EtOH'] - value >= 0):
            self.volumes['EtOH'] -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def filter_oil(self, value):
        if (self.volumes['Oil'] - value >= 0):
            self.volumes['Oil'] -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def get_volume_processed(self):
        return self._volume_processed


    def filter_volume_processed(self, value):
        if (self._volume_processed - value >= 0):
            self._volume_processed -= value
            return float(value)
        else:
            print('<<!!>> The tank does not have this volume available <<!!>>')

    def process(self):
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

        print('\n>> Launching volume from Reactor to Decanter..')
        volume_to_launch = 3
        self.filter_volume_processed(volume_to_launch)
        decanter.add_volume(volume_to_launch)
        print('<< Launched.\n')
        # Waits 5 seconds to be able to launch again
        print('   <<!!>> (Reactor) Wait 5 seconds to rest before you can launch again. <<!!>>')

