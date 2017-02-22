from sportscar import *
import csv

class Garage:

    def __init__(self, size, localisation):
        self.size = size
        self.localisation = localisation
        self.occupation = 0
        self.vehicles = []

    def show_my_cars(self):
        for car in self.vehicles:
            print(car)

    def add_car(self, car):
        if self.occupation + car.size <= self.size:
            self.occupation += car.size
            self.vehicles.append(car)
        else:
            print("There's not enough room in you garage!")

    def space_left(self):
        room = self.size - self.occupation
        print(room)

    # # def add_many_cars(self, csv):
    #     with open(csv, "r") as f:
    #         car_reader = csv.reader(f, delimiter=",")
    #         for car in car_reader:
    #             if car[0] == "name":
    #                 pass
    #             else:
