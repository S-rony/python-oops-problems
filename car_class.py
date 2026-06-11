class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self,amount):
        self.speed += amount
        return self.speed


    def brake(self,amount):
        self.speed -= amount


c_1 = Car("Maruti", "A2")
print(c_1.accelerate(200))
