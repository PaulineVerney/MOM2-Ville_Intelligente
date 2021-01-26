from SelectingEnergySharingForConsumer import SelectingEnergySharingForConsumer
from SelectingEnergySharingForSupplier import SelectingEnergySharingForSupplier


class House:
    def __init__(self, house_id, has_token, remaining_battery, full_battery, pmax,
                 sky_condition, alpha, windows, current_time, predicted_previous_consumption,
                 actual_previous_consumption, Ya, Ys):
        self.house_id = house_id
        self.delta = 0
        self.price = 0
        self.has_token = has_token
        self.remaining_battery = remaining_battery
        self.full_battery = full_battery
        #self.energy_produced = energy_produced
        self.pmax = pmax
        self.sky_condition = sky_condition
        self.alpha = alpha
        self.windows = windows
        self.current_time = current_time
        self.predicted_previous_consumption= predicted_previous_consumption
        self.actual_previous_consumption = actual_previous_consumption
        self.Ya = Ya
        self.Yb = 0
        self.Ys = Ys
        #self.ratio_window = ratio_window
        self.set_Yb()
        self.set_price_of_energy()
        self.predict_energy()

    def set_Yb(self):
        self.Yb = self.remaining_battery / self.full_battery

    def predict_energy(self):
        print("Energy produced by house")
        Pi = self.pmax * (1 - self.sky_condition)
        EH = (self.windows[self.current_time+1] - self.windows[self.current_time]) * Pi
        EC = self.alpha * self.predicted_previous_consumption + (1 - self.alpha) * self.actual_previous_consumption
        self.delta = EH + self.remaining_battery - EC

    def set_price_of_energy(self):
        Y = self.Ya * (1 + 1/self.Yb) * (1 + 1/self.Ys)
        self.price = Y


