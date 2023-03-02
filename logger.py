'''As a developer, I want to create a Logger class with a log_transaction() method 
that will accept an Order object and store number and:
Increase the Loggers transaction_count by one
Add the price of the Order object to the Loggers daily_sales
Open the log.txt file
Write a well-formatted message to the log.txt file containing the current 
transaction count, the name of the dish ordered, the store it was ordered from, 
the price of the item, and the combined daily income.
Close the log.txt file.

As a developer, I want to use the Singleton pattern 
(as shown in the Design Patterns Demo repo) to create a single instance of a 
Logger object inside the logger.py file and import this instance into the 
Franchise class to be shared by all instantiations.
'''

class Logger:

    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, order, store_number):
        self.transaction_count += 1
        self.daily_sales += order.price
        file = open("log.txt", "a")
        file.write(f"\n Order #{self.transaction_count}: {order.dish_name} at location #{store_number} - ${order.price}; Total: ${self.daily_sales}\n")
        file.close()

logger = Logger()