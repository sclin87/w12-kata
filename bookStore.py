from typing import Set


class Customer:
    shopping_cart = []

    def __init__(self):
        self.shopping_cart.clear()

    def buy(self, version):
        self.shopping_cart.append(version)

    def buyList(self, shoppingList):
        self.shopping_cart = shoppingList

    def checkout(self):
        sets = self.getSets()
        price = self.getPrice(sets)
        self.shopping_cart.clear()
        return price

    def getSets(self):
        # Divide books into sets of series for best price
        sets = [[]]
        for book in self.shopping_cart:
            checked = False
            for set in sets:
                if book not in set:
                    set.append(book)
                    checked = True
                    break
            # If previous sets contain this version, add a new set
            if not checked:
                sets.append([book])

        # Swap a book from every set of 5 books to every set of 3 books
        for i in range(len(sets)):
            if len(sets[i]) < 5:
                break
            for j in range(i + 1, len(sets)):
                if len(sets[j]) > 3:
                    continue
                elif len(sets[j]) < 3:
                    break
                # Find the book that isn't in the set of 3 books
                for book in sets[i]:
                    if book not in sets[j]:
                        sets[j].append(book)
                        sets[i].remove(book)
                        break
                break

        return sets

    def getPrice(self, sets):
        price = 0
        for set in sets:
            # Check if any discount can be given
            if len(set) > 1:
                match len(set):
                    case 2:
                        price += 8 * len(set) * 0.95
                    case 3:
                        price += 8 * len(set) * 0.9
                    case 4:
                        price += 8 * len(set) * 0.8
                    case 5:
                        price += 8 * len(set) * 0.75
            else:
                price += 8 * len(set)
        return price
