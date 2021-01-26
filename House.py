from SelectingEnergySharingForConsumer import SelectingEnergySharingForConsumer
from SelectingEnergySharingForSupplier import SelectingEnergySharingForSupplier


class House:
    def __init__(self, house_id, delta, price,
                 has_token, remaining_battery,
                 energy_produced, pmax,
                 sky_condition, alpha, windows,
                 current_time, predicted_previous_consumption,
                 actual_previous_consumption,
                 Ya, Yb, Ys, ratio_window):
        self.house_id = house_id
        self.delta = delta
        self.price = price
        self.has_token = has_token
        self.remaining_battery = remaining_battery
        self.energy_produced = energy_produced
        self.pmax = pmax
        self.sky_condition = sky_condition
        self.alpha = alpha
        self.windows = windows
        self.current_time = current_time
        self.predicted_previous_consumption= predicted_previous_consumption
        self.actual_previous_consumption = actual_previous_consumption
        self.Ya = Ya
        self.Yb = Yb
        self.Ys = Ys
        self.ratio_window = ratio_window

    def predict_energy(self):
        print("Energy produced by house")
        Pi = self.pmax * (1 - self.sky_condition)
        EH = (self.windows[self.current_time+1] - self.windows[self.current_time]) * Pi
        EC = self.alpha * self.predicted_previous_consumption + (1 - self.alpha) * self.actual_previous_consumption
        self.energy_produced = EH + self.remaining_battery - EC

    def set_price(self):
        print("Price of energy")

    def get_price_of_energy(self):
        Y = self.Ya * (1 + 1/self.Yb) * (1 + 1/self.Ys)
        self.price = Y


