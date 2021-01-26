

class SelectingEnergySharingForSupplier:
    def __init__(self, house, broadcast):
        self.house = house
        self.broadcast = broadcast
        self.dict_of_consumers = self.broadcast.dict_of_consumers
        self.energy_sharing_instructions = []



