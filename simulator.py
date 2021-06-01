from threading import Thread, Lock
import time, random

mutex1 = Lock()
mutex2 = Lock()
mutex3 = Lock()
mutex4 = Lock()
mutex5 = Lock()
mutex6 = Lock()
mutex7 = Lock()
mutex8 = Lock()

flag_run = True
activate_washers = False
activate_etoh_tank = False

reactor_cycles = 0

class Simulator:

    def __init__(self, tank_oil, tank_naoh_etoh, reactor, washer_1, washer_2, washer_3, tank_glycerin, tank_etoh,
                 tank_biodiesel,decanter, dryer_1, dryer_2):
        self.reactor = reactor
        self.decanter = decanter

        #Tanks, washers, dryers
        self.tanks = dict([ ('Oil', tank_oil), ('NaOH/EtOH', tank_naoh_etoh), ('Glycerin', tank_glycerin),
                            ('EtOH', tank_etoh), ('Biodiesel', tank_biodiesel)])
        self.washers = dict([('Washer 1', washer_1), ('Washer 2', washer_2), ('Washer 3', washer_3)])
        self.dryers = dict([('Dryer 1', dryer_1), ('Dryer 2', dryer_2)])
        self._run = False

        self._running_threads = []

    def run(self):
        """ Run the simulator.
        Creates all necessary Threads"""
        global reactor_cycles
        self._run = True
        print('..: Simulator is running :..')

        # Start the thread to add Oil every 10 seconds
        adding_oil = Thread(target=self._fill_oil)
        adding_oil.start()
        self._running_threads.append(adding_oil)

        # Start the thread to add NaOH/EtOH every 1 second
        adding_naoh_etoh = Thread(target=self._fill_naoh_etoh)
        adding_naoh_etoh.start()
        self._running_threads.append(adding_naoh_etoh)

        # Start the thread to activate the reactor
        reactor_active = Thread(target=self._active_reactor)
        reactor_active.start()
        self._running_threads.append(reactor_active)

        # Start the thread to launch to the decanter
        launch_reactor = Thread(target=self._launch_reactor)
        launch_reactor.start()
        self._running_threads.append(launch_reactor)

        # Start the thread to decant to the washers
        exhaust_decanter = Thread(target=self._exhaust_decanter)
        exhaust_decanter.start()
        self._running_threads.append(exhaust_decanter)

        # Start the thread to activate dryer 1
        dry = Thread(target=self._dry)
        dry.start()
        self._running_threads.append(dry)

        # Start the thread to activate washers
        wash = Thread(target=self._washers)
        wash.start()
        self._running_threads.append(wash)

        # Start the thread to activate final dryer
        dry_2 = Thread(target=self._final_dry)
        dry_2.start()
        self._running_threads.append(dry_2)

        time.sleep(3600)
        etoh_remaning = self.tanks['NaOH/EtOH'].get_etoh_volume() + self.tanks['EtOH'].get_volume()
        naoh_remaining = self.tanks['NaOH/EtOH'].get_naoh_volume()
        oil_remaining = self.tanks['Oil'].get_volume()
        self.stop()
        print('-----------------------------------------------------------------')
        print('| Biodiesel produced: {}                                        |'.format(self.tanks['Biodiesel'].get_volume()))
        print('| Glycerin produced: {}                                         |'.format(self.tanks['Glycerin'].get_volume()))
        print('| Oil, NaOH and EtOH remaining: {} | {} | {}                    |'.format(oil_remaining,naoh_remaining, etoh_remaning))
        print('| Reactor Cycles: {}                                        |'.format(reactor_cycles))



    def _fill_oil(self):
        """Fill Oil tank in each 10 seconds (Thread 1)."""
        while self._run:
            mutex1.acquire()
            volume = random.uniform(1.0, 2.0)
            print('\n>> Adding {:.1f}L of residual oil...'.format(float(volume)))
            self.tanks['Oil'].add_volume(float(volume))
            print('{} tank with {:.1f}L of residual oil\n'.format(self.tanks['Oil'].get_substance(),
                                                                  float(self.tanks['Oil'].get_volume())))
            time.sleep(9.9)
            mutex1.release()


    def _fill_naoh_etoh(self):
        """Fill NaOH/EtOH tank in each 1 second (Thread 2)."""
        global next_volume_etoh
        while self._run:
            mutex2.acquire()
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
            mutex2.release()


    def _active_reactor(self):
        """Active reactor when the minimum volumes if reached. (Thread 3)."""
        while self._run:
            mutex3.acquire()

            if self.tanks['Oil'].get_volume() >= 1.25 and self.tanks['NaOH/EtOH'].get_naoh_volume() >= 1.25 and \
                    self.tanks['NaOH/EtOH'].get_etoh_volume() >= 2.500:
                time.sleep(1)
                mutex3.release()

                # Now, the volume is filtered from NaOH/EtOH and Oil tank and passed it to Reactor
                oil = self.tanks['Oil'].filter_volume(1.25)         # Getting 1.25L of Oil from oil tank
                naoh = self.tanks['NaOH/EtOH'].filter_naoh(1.25)     # Getting 1.25L of NaOH from NaOH/EtOH tank
                etoh = self.tanks['NaOH/EtOH'].filter_etoh(2.50)     # Getting 2.50L of EtOH from NaOH/EtOH tank

                # Pass NaOH/EthOH and Oil to the reactor
                self.reactor.add_volumes(float(naoh), float(etoh), float(oil))


                #print('\n <<>> Reactor with: {:.2f} of Oil - {} of NaOH - {} of EtOH <<>>'.format(
                #                                                        self.reactor.get_oil_volume(),
                #                                                        self.reactor.get_naoh_volume(),
                #                                                        self.reactor.get_etoh_volume()))


                self.reactor.process()
            else:
                mutex3.release()

    def _launch_reactor(self):
        """Launch reactor when it's not resting. (Thread 4)."""
        global reactor_cycles
        while self._run:
            mutex4.acquire()
            if not self.reactor.is_resting() and self.reactor.get_volume_processed() >= 3.0:
                mutex4.release()
                self.reactor.launch(self.decanter)
                reactor_cycles += 1
                time.sleep(5)
            else:
                mutex4.release()


    def _exhaust_decanter(self):
        """Exhaust decanter when it's ready. (Thread 4)."""
        global activate_washers
        while self._run:
            mutex5.acquire()
            # Verify if the decanter is ready to exhaust
            if self.decanter.ready():
                mutex5.release()
                # Exhaust 2% of Glycerin 9% of EtOH and 89% of Washing Solution
                self.decanter.exhaust(self.tanks['Glycerin'], self.washers['Washer 1'], self.dryers['Dryer 1'])
                # Activate washers
                activate_washers = True
            else:
                mutex5.release()

    def _dry(self):
        """Dry solution exhausted from Decanter and send to EtOH Tank. (Thread 5)."""
        while self._run:
            mutex6.acquire()
            # Verify if the volume is already in the Dryer 1
            if self.dryers['Dryer 1'].ready():
                mutex6.release()

                # If there is any volume in it, dry and exhaust it to EtOH tank
                self.dryers['Dryer 1'].dry(self.tanks['EtOH'])

                # Get the volume from EtOH tank and passes it to NaOH/EtOH main tank
                etoh_from_etoh_tank = self.tanks['EtOH'].filter_volume(self.tanks['EtOH'].get_volume())
                print(' <<>> Passing volume from EtOH tank to NaOH/EtOH <<>>')
                self.tanks['NaOH/EtOH'].add_etoh_volume(etoh_from_etoh_tank)
            else:
                mutex6.release()

    def _washers(self):
        """Wash solution exhausted from Decanter (3x) (Thread 6)."""
        global activate_washers
        while self._run:
            mutex7.acquire()
            if activate_washers:
                mutex7.release()
                # Wash the volume in the Washer 1
                washed_1 = self.washers['Washer 1'].wash()

                # Pass the volume from Washer 1 to Washer 2
                self.washers['Washer 2'].add_volume(washed_1)
                # Wash the volume in the Washer 2
                washed_2 = self.washers['Washer 2'].wash()

                # Pass the volume from Washer 2 to Washer 3
                self.washers['Washer 3'].add_volume(washed_2)
                # Wash the volume in the Washer 3
                washed_3 = self.washers['Washer 3'].wash()

                # Pass the volume from Washer 3 to Dryer 2
                self.dryers['Dryer 2'].add_volume(washed_3)
                # Desactivate washers until next batch
                activate_washers = False
            else:
                mutex7.release()

    def _final_dry(self):
        """Dry solution exhausted from the Washer 3 (Thread 7)."""
        while self._run:
            mutex8.acquire()
            if self.dryers['Dryer 2'].ready():
                mutex8.release()
                self.dryers['Dryer 2'].dry(self.tanks['Biodiesel'])
                print(' >> Biodiesel tank with {:.2f}L'.format(self.tanks['Biodiesel'].get_volume()))
            else:
                mutex8.release()

    def stop(self):
        """Stop the Simulator"""
        # Stops running simulator.
        self._run = False

        '''# Stop all threads here.
        for thread in self._running_threads:
            thread.stop()'''