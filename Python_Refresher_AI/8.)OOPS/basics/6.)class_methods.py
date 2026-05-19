class Pizza:
    def __init__(self, topping, size):
        self.topping = topping
        self.size = size
    
    @classmethod
    def from_string(cls, pizza_string):
        topping, size = pizza_string.split(",")
        return cls(topping, int(size))
    


pizza1 = Pizza.from_string("pepperoni,12")

print(pizza1.topping)
print(pizza1.size)