class TrackOrders:
    def __init__(self):
        lists = list()
        self.myList = lists
   
    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.myList)

    def add_new_order(self, customer, order, day):
        self.myList.append({day, order, customer})

    def get_most_ordered_dish_per_customer(self, customer):
        list = [orders[1] for orders in self.myList
                if orders[2] == customer]
        return max(list, key=list.count)

    def get_never_ordered_per_customer(self, customer):
        foods = [orders[1] for orders in self.myList]
        customerFoods = [orders[1] for orders in self.myList
                 if customer == orders[2]]
                            
        return set(set(foods) - set(customerFoods ))

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        list = [orders[0] for orders in self.myList]
        return max(list, key=list.count)

    def get_least_busy_day(self):
        list = [orders[0] for orders in self.minha_list]
        return min(list, key=list.count)
