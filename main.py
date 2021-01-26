from House import House
from SelectingEnergySharingForSupplier import SelectingEnergySharingForSupplier
from SelectingEnergySharingForConsumer import SelectingEnergySharingForConsumer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime

class Broadcast:
    def __init__(self):
        self.efficiency = []
        self.ring = []
        self.dict_of_suppliers = {}
        self.dict_of_consumers = {}
        self.token = 0

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
    def __init__(self, size, remaining_energy_list, full_battery, windows):
        self.broadcast = Broadcast()
        self.time = Time(windows)
        self.size = size
        self.remaining_energy_list = remaining_energy_list
        self.full_battery = full_battery
        self.neighborhood = {}

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
                                         full_battery=self.full_battery, windows=self.time.windows,
                                         current_time=self.time.current_time)
    def set_efficiency(self):
        for i in range(self.size):
            efficiency_i = []
            for j in range(self.size):
                efficiency_i.append(1) # On fixe l'efficacité à 1 entre toutes les maisons pour l'instant
            self.broadcast.efficiency.append(efficiency_i)

    def set_ring(self):
        for id in range(self.size):
            self.broadcast.ring.append(id)

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
            self.neighborhood[id].Ya = 110
            self.neighborhood[id].set_price_of_energy()
            self.broadcast.dict_of_suppliers[id].append(self.neighborhood[id].price)

        # Selecting Energy Suppliers
        exchange_in_progress = True
        consumer_selection = {}
        supplier_selection = {}
        for id in self.broadcast.dict_of_consumers:
            consumer_selection[id] = SelectingEnergySharingForConsumer(self.neighborhood[id],self.broadcast)

        consumer_selection = SelectingEnergySharingForConsumer()
        supplier_selection = SelectingEnergySharingForSupplier()
        #while exchange_in_progress:





def _test_values():
    print("Test values")

if __name__ == '__main__':
    print('Hello world!')
    maxWindows = 9071
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    Ya = 110.0 #$/kWh
    x = np.arange(0, maxWindows, 1)
    delta = np.zeros(maxWindows )
    house1 = House(1, True, remaining_battery=0.1, full_battery=100.0, windows=0, current_time=0, Ya=Ya, Ys=3.0)
    #house2 = House(2, False, remaining_battery=0, full_battery=100, windows=0, current_time=0, Ya=Ya, Ys=3)
    #house3 = House(3, False, remaining_battery=0, full_battery=100, windows=0, current_time=0, Ya=Ya, Ys=3)
    #house4 = House(4, False, remaining_battery=0, full_battery=100, windows=0, current_time=0, Ya=Ya, Ys=3)
    #house5 = House(5, False, remaining_battery=0, full_battery=100, windows=0, current_time=0, Ya=Ya, Ys=3)
    #house6 = House(6, False, remaining_battery=0, full_battery=100, windows=0, current_time=0, Ya=Ya, Ys=3)

    consumption = pd.read_csv("consumption.csv",header=0)
    production = pd.read_csv("production.csv", header=0)

    house1Consumption = consumption["residential1_consumption"].iloc[1:]
    house1Production = production["DE_KN_residential1_pv"].iloc[1:]
    house1Delta =  house1Consumption - house1Production
    for i in range(maxWindows) :
        house1.delta = house1Delta.iloc[i]
        delta[i] = house1.delta

    plt.plot(x,delta)
    plt.show()


    #for i in range()