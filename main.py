from sportscar import *
from truck import *
from garage import *

def main():
    garage = Garage(5, "Kraków")
    truck = Truck("Mercedes", "M45", 1997, "black", 8000, 8)
    print(truck)
    garage.space_left()
    garage.add_car(truck)
    garage.space_left()
    garage.show_my_cars()


main()
