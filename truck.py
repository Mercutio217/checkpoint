from van import Van

class Truck(Van):

    def __init__(company, model, year, max_space, wheel_count):
        Van.__init__(company, model, year, color, max_space)
        self.size = 3
        self.wheel_count = wheel_count
