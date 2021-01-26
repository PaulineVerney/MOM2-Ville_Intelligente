

class SelectingEnergySharingForSupplier:
    def __init__(self, house, broadcast):
        self.house = house
        self.broadcast = broadcast
        self.dict_of_consumers = self.broadcast.dict_of_consumers
        self.efficiency = self.broadcast.efficiency
        self.current_request_granted = []
        self.energy_sharing_instructions = []

    def response(self):
        most_efficient_id = 'None'
        best_efficiency = 0
        for id in self.dict_of_consumers:
            #print(self.dict_of_consumers[id])
            if self.dict_of_consumers[id][0] == self.house.house_id:
                efficiency_of_consumer = self.efficiency[self.house.house_id][id]
                if efficiency_of_consumer > best_efficiency:
                    best_efficiency = efficiency_of_consumer
                    most_efficient_id = id
        if most_efficient_id == 'None':
            return None

        else:
            Ei = abs(self.house.delta)
            print()
            Er = abs(self.broadcast.dict_of_consumers[most_efficient_id][1])

            if Ei >= Er:
                energy_granted = Er
            else:
                energy_granted = Ei
            self.energy_sharing_instructions.append([most_efficient_id,energy_granted])
            self.house.delta = Ei - energy_granted
            self.current_request_granted = [most_efficient_id, energy_granted]
            return self.current_request_granted

    def update_broadcast(self, broadcast):
        self.broadcast = broadcast
        self.dict_of_consumers = self.broadcast.dict_of_consumers
        self.efficiency = self.broadcast.efficiency

