

class SelectingEnergySharingForConsumer:
    def __init__(self, house, broadcast):
        self.house = house
        self.broadcast = broadcast
        self.dict_of_suppliers = self.broadcast.dict_of_suppliers
        self.energy_sharing_instructions = []

