from utils.tank import Tank
from utils.tank_naoh_etoh import Tank_NaOHEtOH
from utils.decanter import Decanter
from utils.filter import Filter
from utils.dryer import Dryer
from utils.reactor import Reactor
import simulator
import time, schedule, random, threading
from timer import RepeatedTimer
from simulator import Simulator


def fill_oil(tank):
    volume = random.uniform(1.0, 2.0)
    print('Adding {:.1f}L of residual oil...'.format(float(volume)))
    tank.add_volume(float(volume))
    print('{} tank with {:.1f}L of residual oil'.format(tank.get_substance(), float(tank.get_volume())))

def fill_naoh_etoh(tank):
    volume_EtOH = 0.125
    volume_NaOH = 0.25

    print('Adding {:.3f}L of EtOH and {:.2f}L of NaOH...'.format(float(volume_EtOH), float(volume_NaOH)))
    tank.add_volume(float(volume_EtOH))
    tank.add_volume(float(volume_NaOH))

    print('{} tank with {:.3f}L of volume'.format(tank.get_substance(), float(tank.get_volume())))

if __name__ == '__main__':
    '''print('.....:: Simulator ::.....')

    oil_tank = Tank('Oil', 0.0)
    #etoh_tank = Tank('EtOH', 0.0)
    naoh_etoh_tank = Tank('NaOH/EtOH', 0.0)

    # ------------ Requirement 1
    adding_oil = RepeatedTimer(10, fill_oil, oil_tank)
    # To stop this thread
    # add_oil.stop('Stopping adding Oil.')
    # --------------------------

    # ------------ Requirement 2 EtOH
    adding_naoh_etoh = RepeatedTimer(1, fill_naoh_etoh, naoh_etoh_tank)
    # To stop this thread
    # add_etoh.stop('Stopping adding EtOH.')
    # --------------------------'''

    oil_tank = Tank('Oil', 0.0)
    naoh_etoh_tank = Tank_NaOHEtOH('NaOH/EtOH', 0.0, 0.0)
    reactor = Reactor()
    simulator = Simulator(oil_tank, naoh_etoh_tank, reactor)
    simulator.run()
