class Animal():

    def __init__(self):
        print("Animal Constructor")
        self.weight = 1

    def eat(self):
        print("eat")


class Mammal(Animal):

    # here we override the base class method
    def __init__(self):
        self.weight = 20
        print("Mammal Constructor")

    def swim(self):
        print("Swim")


class Fish(Animal):

    def swim(self):
        super.__init__()
        print("fish constructor")

m = Mammal()
f = Fish()
m.eat()
print(m.weight)
print(f.weight)