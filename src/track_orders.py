class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        foods = {}
        for customer, comida, _ in self.data:
            if customer == customer:
                if comida not in foods:
                    foods[comida] = 0
                foods[comida] += 1
        response = max(foods, key=foods.get)
        return response
    
    def get_never_ordered_per_customer(self, customer):
        total = set()
        food = set()
        for customer, food, _ in self.data:
            total.add(food)
            if customer == customer:
                food.add(food)
                reponse = total.difference(food)
                return reponse
    
    def get_busiest_day(self):
        dias = {}
        for _cust, _order, days in self.data:
            if days not in dias:
                dias[days] = 0
            dias[days] += 1
        response = max(dias, key=dias.get)
        return response


   