'''As a developer, I want to create a Simulation class with a run_simulation() 
method to act as a facade pattern. The run_simulation() method should:
Instantiate 3 separate Franchise objects.
Call place_order() on each franchise object multiple times.
'''
from franchise import Franchise

class Simulation:
    def __init__(self) -> None:
        pass

    def run_simulation(self):
        store_one = Franchise(1)
        store_two = Franchise(2)
        store_three = Franchise(3)

        store_one.place_order()
        store_one.place_order()
        store_two.place_order()
        store_two.place_order()
        store_three.place_order()
        store_three.place_order()
