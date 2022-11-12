
class Vehicle:

    def drive_direction(self):
        print("Vehicle: Drive Forward")

class Plane(Vehicle):

    def drive_direction(self):
        print("Plane: Drive Upward")

class SubMarine(Vehicle):

    def drive_direction(self):
        print("SubMarine: Drive Downward")

vehicle = Vehicle()
vehicle.drive_direction()

plane = Plane()
plane.drive_direction()

sub_marine = SubMarine()
sub_marine.drive_direction()