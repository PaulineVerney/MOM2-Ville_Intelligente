from House import House


class Broadcast:
    def __init__(self, efficiency, ring, windows,
                 current_time, dict_of_suppliers,
                 dict_of_consumers, token):
        self.efficiency = efficiency
        self.ring = ring
        self.windows = windows
        self.current_time = current_time
        self.dict_of_suppliers = dict_of_suppliers
        self.dict_of_consumers = dict_of_consumers
        self.token = token


if __name__ == '__main__':
    print('Hello world!')
