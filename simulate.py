from utils.tank import Tank
from utils.decanter import Decanter
from utils.filter import Filter
from utils.dryer import Dryer
from utils.reactor import Reactor
import simulator
import time, schedule, random, threading
from timer import RepeatedTimer


def fill_oil(tank):
    volume = random.uniform(1.0, 2.0)
    print('Adding {:.1f}L of residual oil...'.format(float(volume)))
    tank.add_volume(float(volume))
    print('Oil tank with {:.1f}L of residual oil'.format(float(tank.get_volume())))

def fill_etoh(tank):
    volume = 0.125
    print('Adding {:.1f}L of EtOH...'.format(float(volume)))
    tank.add_volume(float(volume))
    print('EtOH tank with {:.1f}L of volume'.format(float(tank.get_volume())))

def fill_naoh(tank):
    volume = 0.25
    print('Adding {:.1f}L of NaOH...'.format(float(volume)))
    tank.add_volume(float(volume))
    print('NaOH/EtOH tank with {:.1f}L of NaOH volume'.format(float(tank.get_volume())))

if __name__ == '__main__':
    print('.....:: Simulator ::.....')


    oil_tank = Tank('Oil', 0.0)
    etoh_tank = Tank('EtOH', 0.0)
    naoh_etoh_tank = Tank('NaOH/EtOH', 0.0)


    # ------------ Requirement 1
    add_oil = RepeatedTimer(10, fill_oil, oil_tank)
    # To stop this thread
    # add_oil.stop('Stopping adding Oil.')
    # --------------------------

    # ------------ Requirement 2 EtOH
    add_etoh = RepeatedTimer(1, fill_etoh, naoh_etoh_tank)
    # To stop this thread
    # add_etoh.stop('Stopping adding EtOH.')
    # --------------------------

    # ------------ Requirement 2 NaOH
    add_naoh = RepeatedTimer(1, fill_naoh, naoh_etoh_tank)
    # To stop this thread
    # add_etoh.stop('Stopping adding EtOH.')
    # --------------------------