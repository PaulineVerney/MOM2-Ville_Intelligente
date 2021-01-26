from House import House

class Broadcast:
    def __init__(self, efficiency, ring, windows, current_time, dict_of_suppliers, dict_of_consumers, token,
                 pmax, sky_condition, Ya, Ys):
        self.efficiency = efficiency
        self.ring = ring
        self.windows = windows
        self.current_time = current_time
        self.dict_of_suppliers = dict_of_suppliers
        self.dict_of_consumers = dict_of_consumers
        self.token = token
        self.pmax = pmax
        self.sky_condition = sky_condition
        self.alpha = 0.5 # Trouvé dans un article cité dans les sources de notre article
        self.Ya = Ya
        self.Ys = Ys

class Neighborhood:
    def __init__(self, broadcast, size, remaining_energy_list, full_battery, predicted_previous_consumption_list, actual_previous_consumption_list):
        self.broadcast = broadcast
        self.size = size
        self.remaining_energy_list = remaining_energy_list
        self.full_battery = full_battery
        self.predicted_previous_consumption_list = predicted_previous_consumption_list
        self.actual_previous_consumption_list = actual_previous_consumption_list
        self.neighborhood = {}

        self.create_neighborhood()

    def create_neighborhood(self):
        for i in range(self.size):
            has_token = False
            if i==0:
                # Give token to first house only
                has_token = True
            # Add all the houses to the neighborhood
            self.neighborhood[i] = House(house_id=i, has_token=has_token, remaining_battery=self.remaining_energy_list[i],
                                               full_battery=self.full_battery, pmax=self.broadcast.pmax,
                                               sky_condition=self.broadcast.sky_condition, alpha=self.broadcast.alpha,
                                               windows=self.broadcast.windows, current_time=self.broadcast.current_time,
                                               predicted_previous_consumption=self.predicted_previous_consumption_list[i],
                                               actual_previous_consumption=self.actual_previous_consumption_list[i],
                                               Ya=self.broadcast.Ya, Ys=self.broadcast.Yb)

def _test_values():
    print("Test values")

if __name__ == '__main__':
    print('Hello world!')
