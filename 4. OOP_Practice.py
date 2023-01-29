# Wednesday 25/01/2023 - Morning Exercises - Create classes based on any objects of your choice
class Vehicle:

    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
        self.__vehicle_movement = False

    def noise(self):
        return "Make a noise"

    def set_vehicle_to_go(self):
        self.__vehicle_movement = True

    def set_vehicle_to_stop(self):
        self.__vehicle_movement = False

    def get_vehicle_movement(self):
        return self.__vehicle_movement


class Car(Vehicle):

    def __init__(self, name, manufacturer, body_type, colour):
        super().__init__(name, manufacturer)
        self.body_type = body_type
        self.colour = colour

    def noise(self):
        return "Beep!"


class Train(Vehicle):

    def __init__(self, name, manufacturer, destination):
        super().__init__(name, manufacturer)
        self.destination = destination

    def noise(self):
        return "Choo Choo!"


vehicle_1 = Car('Fiesta','Ford', 'Hatchback', 'red')
vehicle_2 = Train('Eurostar', 'Alstom', 'Paris')

print(vehicle_1.colour)

Car.set_vehicle_to_go(vehicle_1)

print(vehicle_1.get_vehicle_movement())

print(vehicle_2)
print("The " + vehicle_2.name + " goes " + vehicle_2.noise())
