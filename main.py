from House import House

class Broadcast:
    def __init__(self):
        self.efficiency = []
        self.ring = []
        self.dict_of_suppliers = {}
        self.dict_of_consumers = {}
        self.token = 0
        self.Ya = 0
        self.Ys = 0

class Time:
    def __init__(self, windows):
        self.windows = windows
        self.current_window_index = 0
        self.current_window = self.windows[self.current_window_index]
        self.current_time = 0

    def update_window(self):
        self.current_window_index = self.current_window_index + 1
        self.current_window = self.windows[self.current_window_index]

class Neighborhood:
    def __init__(self, broadcast, size, remaining_energy_list, full_battery):
        self.broadcast = broadcast
        self.size = size
        self.remaining_energy_list = remaining_energy_list
        self.full_battery = full_battery
        self.neighborhood = {}

        self.set_Ya()
        self.create_neighborhood()
        self.set_efficiency()
        self.set_ring()

    def create_neighborhood(self):
        for id in range(self.size):
            has_token = False
            if id==0:
                # Give token to first house only
                has_token = True
            # Add all the houses to the neighborhood
            self.neighborhood[id] = House(house_id=id, has_token=has_token, remaining_battery=self.remaining_energy_list[i],
                                         full_battery=self.full_battery, windows=self.broadcast.windows,
                                         current_time=self.broadcast.current_time,
                                         Ya=self.broadcast.Ya, Ys=self.broadcast.Yb)
    def set_efficiency(self):
        for i in range(self.size):
            efficiency_i = []
            for j in range(self.size):
                efficiency_i.append(1) # On fixe l'efficacité à 1 entre toutes les maisons pour l'instant
            self.broadcast.efficiency.append(efficiency_i)

    def set_ring(self):
        for id in range(self.size):
            self.broadcast.ring.append(id)

    def set_Ya(self):
        self.broadcast.Ya = 110 # Nombre aléatoire pour l'instant

    def update_neighborhood(self):
        # Broadcasting Energy Difference
        self.broadcast.dict_of_suppliers = {}
        self.broadcast.dict_of_consumers = {}
        for id in range(self.size):
            if self.neighborhood[id].delta > 0:
                self.broadcast.dict_of_suppliers[id] = self.neighborhood[id].delta
            if self.neighborhood[id].delta < 0:
                self.broadcast.dict_of_consumers[id] = self.neighborhood[id].delta
        # Multicasting Energy Price
        Ys = len(self.broadcast.dict_of_suppliers)/len(self.broadcast.dict_of_consumers)
        for id in self.broadcast.dict_of_suppliers:
            self.neighborhood[id].Ys = Ys
            self.neighborhood[id].set_Yb()
            self.neighborhood[id].set_price_of_energy()
            


def _test_values():
    print("Test values")

if __name__ == '__main__':
    print('Hello world!')
