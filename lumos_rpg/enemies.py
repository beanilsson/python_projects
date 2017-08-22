class Enemy:
    def _init_(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

#Extending Enemy creating subclass Beetle
class Beetle(Enemy):
    def _init_(self):
        super()._init_(name="Beetle", hp=3, damage=5)

class Spider(Enemy):
    def _init_(self):
        super()._init_(name="Spider", hp=10, damage=3)
