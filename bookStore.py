class Customer:
    shopping_cart = []

    def __init__(self):
        self.shopping_cart.clear()

    def buy(self, version):
        self.shopping_cart.append(version)

    def buyList(self, shoppingList):
        self.shopping_cart = shoppingList

    def checkout(self):
        price = 8 * len(self.shopping_cart)
        self.shopping_cart.clear()
        return price
