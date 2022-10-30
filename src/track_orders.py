class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        foods = {}
        for cliente, comida, _ in self.data:
            if cliente == customer:
                if comida not in foods:
                    foods[comida] = 0
                foods[comida] += 1
        response = max(foods, key=foods.get)
        return response
    
    def get_never_ordered_per_customer(self, customer):
        total = set()
        food = set()
        for cliente, food, _ in self.data:
            total.add(food)
            if cliente == customer:
                food.add(food)
                reponse = total.difference(food)
                return reponse

    def get_orders_per_customer(self, customer, order):
        orders = 0
        for client, food, _day in self.data:
            if client == customer and order == food:
                orders += 1
        return orders
    
    
    def get_days_never_visited_per_customer(self, customer):
        totalDias = set()
        dias = set()
        for cliente, _, day in self.data:
            totalDias.add(day)
            if cliente == customer:
                dias.add(day)
        response = totalDias.difference(dias)
        return response
    
    def get_busiest_day(self):
        dias = {}
        for _cust, _order, days in self.data:
            if days not in dias:
                dias[days] = 0
            dias[days] += 1
        response = max(dias, key=dias.get)
        return response

    def get_least_busy_day(self):
        dias = {}
        for _cust, _order, days in self.data:
            if days not in dias:
                dias[days] = 0
            dias[days] += 1

        response = min(dias, key=dias.get)
        return response

    def get_orders_per_customer(self, customer, order):
        pedido = 0
        for cliente, food, _day in self.data:
            if cliente == customer and order == food:
                pedido += 1
        return pedido

   