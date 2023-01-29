class Animal:
    def __init__(self, name):
        self.name = name
        self.__animal_kind = "placeholder"

    def speak(self): # method
        print("Hi " + self.name)

    def set_animal_kind(self, kind):
    # control flow
        self.__animal_kind = kind

    def get_animal_kind(self):
        return self.__animal_kind


class Dog(Animal):

        def __init__(self, name, best_trick):
            super().__init__(name)
            self.best_trick = best_trick


        def speak(self):
            return "woof!"