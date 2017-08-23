class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

#Extending Enemy creating subclass Beetle
class Beetle(Enemy):
    def __init__(self):
        super().__init__(name="Beetle", hp=3, damage=5)

class Spider(Enemy):
    def __init__(self):
        super().__init__(name="Spider", hp=10, damage=3)
