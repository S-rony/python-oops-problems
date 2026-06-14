class Bird:
    def fly(self):
        print("Bird fly")

class Parrot(Bird):
    def speak(self):
        print("Parrot do speak")



parrot = Parrot()
parrot.speak()
parrot.fly()