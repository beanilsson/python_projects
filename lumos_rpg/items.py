class Item():
    #The constructor, called whenever a new object is created
    def _init_(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    #Allow printing of object and displaying useful information
    def _str_(self):
        return "{}\n====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

#Extending Item creating subclass Gold
class Gold(Item):
    def _init_(self, amount):
        self.amount = amount
        #Calling the superclass constructor on line 3
        super()._init_(name="Gold", description="A coin with {} stamped on both sides.".format(str(self.amount)), value=self.amount)

#Extending Item creating subclass Weapon
class Weapon(Item):
    def _init_(self, name, description, value, damage):
        self.damage = damage
        super._init_(name, description, value)

    def _str_(self):
        return "{}\n====\n{}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)

#Extending Weapon creating subclass Stick
class Stick(Weapon):
    def _init_(self):
        super()._init_(name="Stick", description="A regular stick, quite useless but basically better than nothing.", value=0, damage=2)

#Extending Weapon creating subclass TableKnife
class TableKnife(Weapon):
    def _init_(self):
        super()._init_(name="Table Knife", description="A completely ordinary table knife.", value=1, damage=1)
