from vehicle import Vehicle

class Sportscar(Vehicle):

    def __init__(self, company, moder, year, color, max_speed):
        super().__init__(company, model, year, color)
        self.size = 1
        self.max_speed = max_speed
