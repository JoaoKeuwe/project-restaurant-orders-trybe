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
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
