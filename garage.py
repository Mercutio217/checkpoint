class Garage:
    def __init__(self, size, localisation):
        self.size = size
        self.localisation = localisation
        self.occupancy = 0
        self.status = "Vacate"
