class Item():
    #The constructor, called whenever a new object is created
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    #Allow printing of object and displaying useful information
    def __str__(self):
        return "{}\n====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

#Extending Item creating subclass Gold
class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        #Calling the superclass constructor on line 3
        super().__init__(name="Gold", description="A coin with {} stamped on both sides.".format(str(self.amount)), value=self.amount)

#Extending Item creating subclass Weapon
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super.__init__(name, description, value)

    def __str__(self):
        return "{}\n====\n{}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)

#Extending Weapon creating subclass Stick
class Stick(Weapon):
    def __init__(self):
        super().__init__(name="Stick", description="A regular stick, quite useless but basically better than nothing.", value=0, damage=2)

#Extending Weapon creating subclass TableKnife
class TableKnife(Weapon):
    def __init__(self):
        super().__init__(name="Table Knife", description="A completely ordinary table knife.", value=1, damage=1)
