class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = salary
    
emp1 = Employee("Rahul", 50000)

print(emp1.name)
print(emp1.salary)

emp1.salary = 60000
print(emp1.salary)