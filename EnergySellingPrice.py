

class EnergySellingPrice:
    def __init__(self, Ya, Yb, Ys, ratio_window):
        self.Ya = Ya
        self.Yb = Yb
        self.Ys = Ys
        self.ratio_window = ratio_window

    def get_price_of_energy(self):
        print("Returns float")
