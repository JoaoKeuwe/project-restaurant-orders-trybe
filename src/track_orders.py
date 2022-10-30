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
