# Sunday 29/01/2023 Practicing Classes
class Vehicle:
    # Class variable, shared between all class instances. Outside of __init__
    colour = "White"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name  # Instance variables, vary depending on inputs
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)  # super() calls the parent class

    def fare(self):
        amount = super().fare()
        amount *= 1.1  # Same as amount = amount * 1.1
        return f"{amount}"


School_bus = Bus("School Volvo", 180, 12, 50)
print(type(School_bus))
print(isinstance(School_bus, Vehicle))  # checks whether the object/variable is an instance of the specified
# class/data type
print(School_bus.seating_capacity())
print(School_bus.fare())