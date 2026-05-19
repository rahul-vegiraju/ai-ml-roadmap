class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    def __str__(self):
        return f"{self.name} is in this major: {self.major}"
    
student1 = Student("Rahul","Computer Science")
print(student1)