'''As a developer, I want to create an Order Factory class with a 
static create_order method.

As a developer, I want to utilize a Factory Pattern in the create_order() 
method to instantiate instances of the three different Order child classes.
This method should accept a string as a parameter (ex “Pizza”) and return 
the corresponding type of Order child class instantiation (ex Pizza() )
'''

from order import Pizza
from order import Pasta
from order import Salad

class Order_Factory:
    def __init__(self) -> None:
        pass

    def create_order(dish_name):
        if dish_name == "pizza":
            return Pizza(1)
        elif dish_name == "pasta":
            return Pasta(8)
        elif dish_name == "salad":
            return Salad(5)

        
