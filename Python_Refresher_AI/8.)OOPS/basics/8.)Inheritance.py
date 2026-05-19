class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "some sound"

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def speak(self):
        return "woof"
    
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def speak(self):
        return "Meow"

dog1 = Dog("max")
cat1 = Cat("Kan")

print(dog1.name)
print(dog1.speak())

print(cat1.name)
print(cat1.speak())