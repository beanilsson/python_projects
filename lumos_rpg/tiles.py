import items, enemies

#Provide template for all the tiles
#An abstract base class, template for the different types of tiles
#This method shouldn't be instanced
class MapTile:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself in a dark room with a flickering torch on the wall.
        There are four paths leading out of the room, where will you go?
        """

    def modify_player(self, player):
        #This room has no action on the player
        pass

#Template for loot rooms
class LootRoom(MapTile):
    def _init_(self, x, y, item):
        self.item = item
        super()._init_(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

#Template for enemy rooms
class EnemyRoom(MapTile):
    def _init_(self, x, y, enemy):
        self.enemy = enemy
        super()._init_(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("The enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
