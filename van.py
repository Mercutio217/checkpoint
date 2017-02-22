from vehicle import Vehicle

class Van(Vehicle):
    def __init__(company, model, year, color, max_space):
        super().__init__(company, model, year, color)
        self.size = 2
        self.max_space = max_space
