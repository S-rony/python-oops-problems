#parent
class Animal:
    def make_sound(self):
        print("Animal make sound")


#child
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

dog = Dog()

dog.make_sound()



