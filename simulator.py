class Simulator:

    def __init__(self, tank_oil, tank_ethanol_naoh, tank_glycerin, tank_etoh, tank_biodiesel, filter, reactor, decanter, washer_1, washer_2, washer_3, dryer_1, dryer_2):
        self.filter = filter
        self.reator = reactor
        self.decanter = decanter
        self.washers = []
        self.dryers = []
        self.tanks = []

        # Washers
        self.washers.append(washer_1)
        self.washers.append(washer_2)
        self.washers.append(washer_3)

        # Dryers
        self.dryers.append(dryer_1)
        self.dryers.append(dryer_2)

        # Tanks
        self.tanks.append(tank_oil)
        self.tanks.append(tank_ethanol_naoh)
        self.tanks.append(tank_glycerin)
        self.tanks.append(tank_etoh)
        self.tanks.append(tank_biodiesel)