class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Animal makes a noise.")

class Dog(Animal):
    def speak(self):
        super().speak()
        print(f"{self.name} says Woof!")

dog1 = Dog("Bud")

dog1.speak()