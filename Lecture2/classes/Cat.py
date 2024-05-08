# Importing Animal from Animal.py.
from Animal import Animal

# class cat extends Animal
class Cat(Animal):
    def __init__(self, name, sound, status):
        Animal.__init__(self, name, sound)
        self.status = status
        
    def __str__(self):
        #return "hello"
        return Animal.__str__(self) + ", status: " + self.status