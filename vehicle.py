class Vehicle:
    def __init__(self, company, model, year, color):
        self.company = company
        self.model = model
        self.year = year
        self.color = color

    def __repr__(self):
        return "{} {} {} {}".format(self.company, self.model, self.year, self.color)
