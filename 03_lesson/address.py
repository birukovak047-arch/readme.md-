class Address:
    def __init__(self, index, city, street, plane, flat):
        self.index = index
        self.city = city
        self.street = street
        self.plane = plane
        self.flat = flat

    def __str__(self):
        return (
            f"{self.index}, {self.city}, {self.street}, {self.plane} - {self.flat}")