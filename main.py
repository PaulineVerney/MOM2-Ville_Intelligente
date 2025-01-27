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

class Neighborhood:
    def __init__(self, size, remaining_energy_list, full_battery):
        self.broadcast = Broadcast()
        #self.time = Time(windows)
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
            self.neighborhood[id] = House(house_id=id, has_token=has_token, remaining_battery=self.remaining_energy_list[id],
                                         full_battery=self.full_battery)
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

        #for item in self.broadcast.dict_of_suppliers:
        #    print("Key : {} , Value : {}".format(item, self.broadcast.dict_of_suppliers[item]))
        #for item in self.broadcast.dict_of_consumers:
        #    print("Key : {} , Value : {}".format(item, self.broadcast.dict_of_consumers[item]))

        # Multicasting Energy Price
        count = len(self.broadcast.dict_of_consumers)
        if count!=0:
            Ys = len(self.broadcast.dict_of_suppliers)/len(self.broadcast.dict_of_consumers)
            for id in self.broadcast.dict_of_suppliers:
                self.neighborhood[id].Ys = Ys
                self.neighborhood[id].set_Yb()
                self.neighborhood[id].Ya = 110
                self.neighborhood[id].set_price_of_energy()
                self.broadcast.dict_of_suppliers[id] = [self.broadcast.dict_of_suppliers[id], self.neighborhood[id].price]
                #print(self.neighborhood[id].price)
            # Selecting Energy Suppliers
            exchange_in_progress = True
            consumer_selection = {}
            supplier_selection = {}
            for id in self.broadcast.dict_of_consumers:
                consumer_selection[id] = SelectingEnergySharingForConsumer(self.neighborhood[id],self.broadcast)
            for id in self.broadcast.dict_of_suppliers:
                supplier_selection[id] = SelectingEnergySharingForSupplier(self.neighborhood[id],self.broadcast)
            count2 = 0
            answers_of_suppliers = []
            while count2<1:
                consumers_still_asking = 0
                suppliers_still_offering = 0
                for id in consumer_selection:
                    if abs(consumer_selection[id].house.delta) > 0 :
                        consumers_still_asking = consumers_still_asking + 1
                        #self.broadcast.dict_of_consumers[id] = (consumer_selection[id].request())
                        self.broadcast.dict_of_consumers[id] = (consumer_selection[id].request())
                    else:
                        del self.broadcast.dict_of_consumers[id]

                #Update Broadcast
                for id in consumer_selection:
                    consumer_selection[id].update_broadcast(self.broadcast)
                for id in supplier_selection:
                    supplier_selection[id].update_broadcast(self.broadcast)

                for id in supplier_selection:
                    if abs(supplier_selection[id].house.delta) > 0:
                        suppliers_still_offering = suppliers_still_offering + 1
                        #self.broadcast.dict_of_suppliers[id].append(supplier_selection[id].response())
                        #print(self.broadcast.dict_of_suppliers[id])
                        #self.broadcast.dict_of_suppliers
                        self.broadcast.dict_of_suppliers[id] = [self.broadcast.dict_of_suppliers[id][0], self.broadcast.dict_of_suppliers[id][1], supplier_selection[id].response()]
                        #self.broadcast.dict_of_suppliers[id] = supplier_selection[id].response()
                    else:
                        #print(abs(supplier_selection[id].house.delta))
                        try:
                            del self.broadcast.dict_of_suppliers[id]
                        except KeyError:
                            print(".")

                # Update Broadcast
                for id in consumer_selection:
                    consumer_selection[id].update_broadcast(self.broadcast)
                for id in supplier_selection:
                    supplier_selection[id].update_broadcast(self.broadcast)

                for id in consumer_selection:
                    for id2 in supplier_selection:
                        if supplier_selection[id2].current_request_granted == consumer_selection[id].current_request:
                            consumer_selection[id].add_instruction()

                count2 = count2 + 1
                if (consumers_still_asking==0) or (suppliers_still_offering==0):
                    exchange_in_progress = False

            #for id in consumer_selection:
            #    print(id)
            #    print(consumer_selection[id].energy_sharing_instructions)
            #for id in supplier_selection:
            #    print(id)
            #    print(supplier_selection[id].energy_sharing_instructions)


if __name__ == '__main__':
    #maxWindows = 9071
    maxWindows = 24
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    Ya = 110.0 #$/kWh
    x = np.arange(0, maxWindows, 1)
    delta = np.zeros(maxWindows)

    consumption = pd.read_csv("consumption.csv",header=0)
    production = pd.read_csv("production.csv", header=0)

    #print(consumption.head(30))
    #print(production.head(30))

    house1Consumption = consumption["residential1_consumption"].iloc[1:]
    house1Production = production["DE_KN_residential1_pv"].iloc[1:]
    house1Delta =  house1Consumption - house1Production

    house2Delta = consumption["residential2_consumption"].iloc[1:]

    house3Consumption = consumption["residential3_consumption"].iloc[1:]
    house3Production = production["DE_KN_residential3_pv"].iloc[1:]
    house3Delta = house3Consumption - house3Production

    house4Consumption = consumption["residential4_consumption"].iloc[1:]
    house4Production = production["DE_KN_residential4_pv"].iloc[1:]
    house4Delta = house4Consumption - house4Production

    house5Delta = consumption["residential5_consumption"].iloc[1:]

    house6Consumption = consumption["residential6_consumption"].iloc[1:]
    house6Production = production["DE_KN_residential6_pv"].iloc[1:]
    house6Delta = house6Consumption - house6Production

    numberHouses = 6
    remaining_energy_list = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    full_battery = 100.0
    newNeighborhood = Neighborhood (numberHouses, remaining_energy_list, full_battery)
    newNeighborhood.create_neighborhood()
    i = 0
    for i in range(6,maxWindows+6):
        print("Window #",i-6)
        newNeighborhood.neighborhood[0].delta = house1Delta.iloc[i]
        newNeighborhood.neighborhood[1].delta = house2Delta.iloc[i]
        newNeighborhood.neighborhood[2].delta = house3Delta.iloc[i]
        newNeighborhood.neighborhood[3].delta = house4Delta.iloc[i]
        newNeighborhood.neighborhood[4].delta = house5Delta.iloc[i]
        newNeighborhood.neighborhood[5].delta = house6Delta.iloc[i]
        newNeighborhood.update_neighborhood()
        #delta[i] = newNeighborhood.neighborhood[5].delta

    #plt.plot(x, delta)
    #plt.show()