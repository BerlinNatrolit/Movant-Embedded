# Class Animal.
class Animal:
    # Constructor
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    # Magic or dunder function __str__, defined so we can call print(Animal)
    def __str__(self):
        return self.name + " makes a " + self.sound
    
    # Method get_sound
    def get_sound(self):
        return sound
    
    # Method get_name
    def get_name(self):
        return name
        