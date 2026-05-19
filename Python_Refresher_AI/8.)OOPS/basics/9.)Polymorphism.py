class Car:
    def move(self):
        return "The car drives on the road"


class Bike:
    def move(self):
        return "The bike pedals on the road"


class Plane:
    def move(self):
        return "The plane flies in the sky"


vehicles = Car(), Bike(), Plane()

for vehicle in vehicles:
    print(vehicle.move())