from EnergySellingPrice import EnergySellingPrice
from SelectingEnergySharingForConsumer import SelectingEnergySharingForConsumer
from SelectingEnergySharingForSupplier import SelectingEnergySharingForSupplier


class House:
    def __init__(self, house_id, delta, price,
                 has_token, remaining_battery,
                 energy_produced, pmax,
                 sky_condition, alpha):
        self.house_id = house_id
        self.delta = delta
        self.price = price
        self.has_token = has_token
        self.remaining_battery = remaining_battery
        self.energy_produced = energy_produced
        self.pmax = pmax
        self.sky_condition = sky_condition
        self.alpha = alpha

    def predict_energy(self):
        print("Needs to return delta_E(n+1) float")

