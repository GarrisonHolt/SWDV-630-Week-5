class Pizza(object):
    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price

class CheesePizza(Pizza):
    def __init__(self):
        self._price = 8.5

class DeluxePizza(Pizza):
    def __init__(self):
        self._price = 10.5

class SupremePizza(Pizza): 
    def __init__(self):
        self._price = 11.5

class PizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == 'Cheese':
            return CheesePizza()
        elif pizza_type == 'Deluxe':
            return DeluxePizza()
        elif pizza_type == 'Supreme':
            return SupremePizza()

if __name__ == '__main__':
    for pizza_type in ('Cheese', 'Deluxe', 'Supreme'):
          print('Price of {0} is {1}'.format(pizza_type, PizzaFactory.create_pizza(pizza_type).get_price()))