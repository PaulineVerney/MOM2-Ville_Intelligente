

class SelectingEnergySharingForConsumer:
    def __init__(self, house, broadcast):
        self.house = house
        self.broadcast = broadcast
        self.dict_of_suppliers = self.broadcast.dict_of_suppliers
        self.efficiency = self.broadcast.efficiency
        self.current_request = []
        self.energy_sharing_instructions = []

    def request(self):
        #print("Dealing request")
        # Sorting suppliers by price
        if self.dict_of_suppliers[list(self.dict_of_suppliers.keys())[0]] == None:
            return None
        else:
            cheapest_price = self.dict_of_suppliers[list(self.dict_of_suppliers.keys())[0]][1]
            cheapest_id = list(self.dict_of_suppliers.keys())[0]
            for id in self.dict_of_suppliers:
                #print(self.dict_of_suppliers[id][1])
                #print(cheapest_price)
                if self.dict_of_suppliers[id][1] != None:
                    if self.dict_of_suppliers[id][1] < cheapest_price:
                        cheapest_id = id
                        cheapest_price = self.dict_of_suppliers[id][1]
            """
            suppliers_sorted_by_price = []
            ids_and_prices = []
            for id in self.dict_of_suppliers:
                #ids_and_prices.append([id,self.dict_of_suppliers[id][1]])
                ids_and_prices.append([id, self.dict_of_suppliers[id][1]])
            for iter_num in range(len(ids_and_prices)-1,0,-1):
                for idx in range(iter_num):
                    if ids_and_prices[idx][1] > ids_and_prices[idx+1][1]:
                        temp = ids_and_prices[idx]
                        ids_and_prices[idx] = ids_and_prices[idx+1]
                        ids_and_prices[idx+1] = temp
            for item in ids_and_prices:
                suppliers_sorted_by_price.append(item[0])
            """
            # Going throught suppliers sorted by price
            #cheapest_id = suppliers_sorted_by_price[0]

            #print("ici:",self.dict_of_suppliers[cheapest_id][0])
            #if type(self.dict_of_suppliers[cheapest_id][0])==list:
            #    print(self.dict_of_suppliers[cheapest_id][0])
            #    Ei = 0
            #if type(self.dict_of_suppliers[cheapest_id][0])!=list:
            #    #print("ok:", abs(self.dict_of_suppliers[cheapest_id][0]))
            #    Ei = abs(self.dict_of_suppliers[cheapest_id][0])
            Ei = abs(self.dict_of_suppliers[cheapest_id][0])
            Ej_eff = abs(self.house.delta / self.efficiency[cheapest_id][self.house.house_id])
            if Ei >= Ej_eff:
                self.current_request = [cheapest_id, Ej_eff]
            else:
                self.current_request = [cheapest_id, Ei]
            print("La maison",self.house.house_id,"demande",self.current_request[1],"à la maison",self.current_request[0])
            return self.current_request

    def update_broadcast(self, broadcast):
        self.broadcast = broadcast
        self.dict_of_suppliers = self.broadcast.dict_of_suppliers
        self.efficiency = self.broadcast.efficiency

    def add_instruction(self, instruction):
        self.energy_sharing_instructions.append(instruction)
        self.house.delta = self.house.delta - instruction[1] * self.efficiency[instruction[0]][self.house.house_id]


