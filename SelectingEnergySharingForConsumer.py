

class SelectingEnergySharingForConsumer:
    def __init__(self, id, delta, dict_of_suppliers, energy_left_to_acquire):
        self.id = id
        self.delta = delta
        self.dict_of_suppliers = dict_of_suppliers
        self.energy_left_to_acquire = energy_left_to_acquire

