from utils.tank import Tank
from utils.tank_naoh_etoh import Tank_NaOHEtOH
from utils.decanter import Decanter
from utils.dryer import Dryer
from utils.reactor import Reactor
from utils.washer import Washer
from utils.logginprinter import LoggingPrinter
from simulator import Simulator

if __name__ == '__main__':

    oil_tank = Tank('Oil', 0.0)
    naoh_etoh_tank = Tank_NaOHEtOH('NaOH/EtOH', 0.0, 0.0)
    reactor = Reactor()
    decanter = Decanter()
    washer_1 = Washer('Washer 1')
    washer_2 = Washer('Washer 2')
    washer_3 = Washer('Washer 3')

    glycerin_tank = Tank('Glycerin', 0.0)
    dryer_1 = Dryer('Dryer 1')
    dryer_2 = Dryer('Dryer 2')
    etoh_tank = Tank('EtOH', 0.0)
    biodiesel_tank = Tank('Biodiesel', 0.0)


    simulator = Simulator(tank_oil=oil_tank, tank_naoh_etoh=naoh_etoh_tank, reactor=reactor, decanter=decanter,
                          tank_glycerin=glycerin_tank, washer_1=washer_1, washer_2=washer_2, washer_3=washer_3,
                          dryer_1=dryer_1, dryer_2=dryer_2, tank_etoh=etoh_tank, tank_biodiesel=biodiesel_tank)
    with LoggingPrinter("log.txt"):
        simulator.run()
    #time.sleep(3600)
