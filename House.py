from SelectingEnergySharingForConsumer import SelectingEnergySharingForConsumer
from SelectingEnergySharingForSupplier import SelectingEnergySharingForSupplier

class House:
    def __init__(self, house_id, has_token, remaining_battery, full_battery):
        #, windows, current_time
        self.house_id = house_id
        self.delta = 0
        self.price = 0
        self.has_token = has_token
        self.remaining_battery = remaining_battery
        self.full_battery = full_battery
        #self.windows = windows
        #self.current_time = current_time
        self.Ya = 110
        self.Yb = 1.0
        self.Ys = 1

        #self.set_Yb()
        #self.set_price_of_energy()
        self.set_delta()

    def set_Yb(self):
        self.Yb = self.remaining_battery / self.full_battery

    def set_delta(self):
        #print("Set delta")
        self.delta = 0 # CHANGER : On doit récupérer la différence entre la consommation et l'énergie produite dans les données

    def set_price_of_energy(self):
        Y = self.Ya * (1.0 + 1.0/self.Yb) * (1.0 + 1.0/self.Ys)
        self.price = Y


