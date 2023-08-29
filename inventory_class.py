class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_cap_level = 0
        self.inventory_list = []

    #sort by name
    def byName(name):
        return name[0]

    #sort by price
    def byPrice(price):
        return price[1]

    def add_item(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        self.current_cap_level += self.quantity
        if self.current_cap_level > self.max_capacity:
            self.current_cap_level -= self.quantity
            return False

        for i in self.inventory_list:
            if self.name in i:
                return False

        self.inventory_list.append([self.name, self.price, self.quantity])
        return True

    def delete_item(self, name):                #####do poprawy
        for i, j in enumerate(self.inventory_list):
            if self.name in j:
                self.inventory_list.pop(i)
                return True
        
        return False


    def get_items_in_price_range(self, min_price, max_price):
        self.min_price = min_price
        self.max_price = max_price

        self._price_range_list = []
        for i, j in enumerate(self.inventory_list):
            if j[1] >= self.min_price and j[1] <= max_price:
                self._price_range_list.append(j[0])

        return self._price_range_list


    def get_most_stocked_item(self):

            #sort by quantity
        def byQuantity(quantity):
            return quantity[2]

        if len(self.inventory_list) == 0:
            return None

        self.most_stocked = self.inventory_list.copy()
        self.most_stocked.sort(key=byQuantity, reverse = True)
        return self.most_stocked[0][0]
        

inventory = Inventory(4)
inventory.add_item('Chocolate', 4.99, 4)
print(inventory.delete_item('Chocolate'))
print(inventory.delete_item('Chocolate'))
print(inventory.delete_item('Bread'))