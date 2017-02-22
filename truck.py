from van import Van

class Truck(Van):

    def __init__(self, company, model, year, color, max_space, wheel_count):
        Van.__init__(self, company, model, year, color, max_space)
        self.size = 3
        self.wheel_count = wheel_count

    def __repr__(self):
        return "{} {} {} {} {} {}".format(self.company, self.model, self.year, self.color, self.max_space, self.wheel_count)
