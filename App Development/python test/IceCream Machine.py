from itertools import product
class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        scoops = []
        for ingredient in self.ingredients:
            for i in self.toppings:
                intg = []
                intg.append(ingredient)
                intg.append(i)
                scoops.append(intg)
        return scoops


    # return [list(p) for p in product(self.ingredients, self.toppings)]




if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce", "Vanilla sauce"])
    print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]