'''As a developer, I want to create a Franchise class with a place_order() method that will:
 ask a user what food they would like to order
call the static OrderFactory.create_order() method to instantiate an order object.
call the logger.log_transaction() method to log the order to the log.txt file
'''
from order_factory import Order_Factory
from logger import logger
class Franchise:
    def __init__(self, store_number) -> None:
        self.name = "Dollar Slice"
        self.store_number = int(store_number)

    def place_order(self):
        print(f"Welcome to {self.name}, location #{self.store_number}!")
        order = input("Would you like pizza, pasta, or salad? > ")
        ordered = Order_Factory.create_order(order)
        logger.log_transaction(ordered, self.store_number)

