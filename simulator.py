from threading import Thread, Lock, Event
import time, random, concurrent.futures

mutex = Lock()


class Simulator:

    def __init__(self, tank_oil, tank_naoh_etoh, reactor, tank_glycerin=None, tank_etoh=None, tank_biodiesel=None,
                 filter=None, decanter=None, washer_1=None, washer_2=None, washer_3=None, dryer_1=None, dryer_2=None):
        self.filter = filter
        self.reactor = reactor
        self.decanter = decanter

        #Tanks, washers, dryers
        self.tanks = dict([ ('Oil', tank_oil), ('NaOH/EtOH', tank_naoh_etoh), ('Glycerin', tank_glycerin), ('EtOH', tank_etoh), ('BioDiesel', tank_biodiesel)  ])
        self.washers = dict([('Washer 1', washer_1), ('Washer 2', washer_2), ('Washer 3', washer_3)])
        self.dryers = dict([('Dryer 1', dryer_1), ('Dryer 2', dryer_2)])


    def run(self):
        print('..: Simulator is running :..')

        # Start the thread to add Oil every 10 seconds
        adding_oil = Thread(target=self._fill_oil)
        adding_oil.start()

        # Start the thread to add NaOH/EtOH every 1 second
        adding_naoh_etoh = Thread(target=self._fill_naoh_etoh)
        adding_naoh_etoh.start()

        # Start the thread to activate the reactor
        reactor_active = Thread(target=self._active_reactor())
        reactor_active.start()

        # Start the thread to launch to the decanter
        launch_reactor = Thread(target=self._launch_reactor())
        launch_reactor.start()

    def _fill_oil(self):
        while True:
            volume = random.uniform(1.0, 2.0)
            print('\n>> Adding {:.1f}L of residual oil...'.format(float(volume)))
            self.tanks['Oil'].add_volume(float(volume))
            print('{} tank with {:.1f}L of residual oil\n'.format(self.tanks['Oil'].get_substance(), float(self.tanks['Oil'].get_volume())))
            time.sleep(9.9)

    def _fill_naoh_etoh(self):
        while True:
            volume_EtOH = 0.125
            volume_NaOH = 0.25

            # Adds NaOH and EtOH to the NaOH/EthOH tank
            print('>> Adding {:.3f}L of EtOH and {:.2f}L of NaOH...'.format(float(volume_EtOH), float(volume_NaOH)))
            self.tanks['NaOH/EtOH'].add_naoh_volume(float(volume_NaOH))
            self.tanks['NaOH/EtOH'].add_etoh_volume(float(volume_EtOH))

            print('{} tank with {:.3f}L NaOH and {:.3f}L EtOH volumes'.format(self.tanks['NaOH/EtOH'].get_substance(),
                                                                              self.tanks['NaOH/EtOH'].get_naoh_volume(),
                                                                              self.tanks['NaOH/EtOH'].get_etoh_volume()))
            time.sleep(0.9)

    def _active_reactor(self):
        exhaust_volume = 0
        while True:
            mutex.acquire()

            if self.tanks['Oil'].get_volume() >= 1.25 and self.tanks['NaOH/EtOH'].get_naoh_volume() >= 1.25 and self.tanks['NaOH/EtOH'].get_etoh_volume() >= 2.500:
                time.sleep(1)
                mutex.release()

                # Now, the volume is filtered from NaOH/EtOH and Oil tank and passed it to Reactor
                oil = self.tanks['Oil'].filter_volume(1.25)         # Getting 1.25L of Oil from oil tank
                naoh = self.tanks['NaOH/EtOH'].filter_naoh(1.25)     # Getting 1.25L of NaOH from NaOH/EtOH tank
                etoh = self.tanks['NaOH/EtOH'].filter_etoh(2.50)     # Getting 2.50L of EtOH from NaOH/EtOH tank

                # Pass NaOH/EthOH and Oil to the reactor
                self.reactor.add_oil(float(oil))
                self.reactor.add_naoh(float(naoh))
                self.reactor.add_etoh(float(etoh))


                print('\n <<>> Reactor with: {:.2f} of Oil - {} of NaOH - {} of EtOH <<>>'.format(
                                                                        self.reactor.get_oil_volume(),
                                                                        self.reactor.get_naoh_volume(),
                                                                        self.reactor.get_etoh_volume()))
                self.reactor.process()
            else:
                mutex.release()

    def _launch_reactor(self):
        print('abriu launch')
        while True:
            mutex.acquire()

            if not self.reactor.is_resting():
                mutex.release()

                exhausted_volume = self.reactor.launch()

            else:
                mutex.release()













    '''def _launch_decanter(self):
        while True:
            mutex.acquire()

            # If the decanter is not in rest time, launchs the volume in it
            if not self.decanter.is_in_rest():
                mutex.release()
                # Captures the volume launched from the decanter
                glycerin, etoh, washing_solution = self.decanter.launch()
                self.decanter.rest(5)
            # If the decanter is in rest time, waits for it ends
            else:
                mutex.release()'''