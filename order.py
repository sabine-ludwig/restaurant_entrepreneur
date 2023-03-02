'''As a developer, I want to create an Order parent class 
and 3 child classes to represent menu items of my choosing'''

class Order:
    def __init__(self, dish_name, price) -> None:
        self.dish_name = dish_name
        self.price = price

class Pizza(Order):
    def __init__(self, price) -> None:
        super().__init__("pizza", price)
        

class Pasta(Order):
    def __init__(self, price) -> None:
        super().__init__("pasta", price)
        
    
class Salad(Order):
    def __init__(self, price) -> None:
        super().__init__("salad", price)
        

