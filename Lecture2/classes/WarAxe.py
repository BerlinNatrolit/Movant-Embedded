#start of our new game WarAxe 400001
class Item:
    #constructor
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def __str__(self):
        return self.name + ": " + self.description

class Destructible:
    def __init__(self, durability):
        self.durability = durability
        
    def get_durability(self):
        return self.durability

# Class weapon extends Item and Destructible.
class Weapon(Item, Destructible):
    # Constructor.
    def __init__(self, name, description, damage):
        Item.__init__(self, name, description) # calling constructor if Item class
        Destructible.__init__(self, 100) # calling constructor if Destructible class.
        self.damage = damage
        self.color = "black"
        
    def get_damage(self):
        return self.damage

    # Lets define __str__ so we can call print(weapon)
    def __str__(self):
        return f"{self.name}: {self.description}: Damage: {self.damage}, Remaining durability: {self.durability}"
    
    # Static method. Does not use anything from an instance of Weapon.
    def does_it_hurt():
        return "YES, a lot!"
    
    # static method that uses a predefined variable.
    def get_color(self):
        return self.color


power_suit = Item("Power suit", "A suit that makes you so powerful that space marines looks like ants")
heavy_bolter = Weapon("Heavy_bolter", "A weapon that looks intimidating, but the damage is even more extreme", 500000)

print(power_suit.get_name() + ": " + power_suit.get_description())
print(heavy_bolter.get_name() + ": " + heavy_bolter.get_description() + ": Damage: " + str(heavy_bolter.get_damage()))

print(power_suit)	# this can be done because we have defined the method __str__()
print(heavy_bolter)	# this can be done because we have defined the method __str__()

print("does it hurt? " + Weapon.does_it_hurt())		# calling static method
print("color: " + heavy_bolter.color())				# calling static method
