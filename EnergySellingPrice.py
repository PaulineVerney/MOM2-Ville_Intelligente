

class EnergySellingPrice:
    def __init__(self, Ya, Yb, Ys, ratio_window):
        self.Ya = Ya
        self.Yb = Yb
        self.Ys = Ys
        self.ratio_window = ratio_window

    def get_price_of_energy(self):
        Y = self.Ya * (1 + 1/self.Yb) * (1 + 1/self.Ys)
        return Y
