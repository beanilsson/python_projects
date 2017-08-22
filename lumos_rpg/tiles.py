import items, enemies, actions, world

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

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory)
        return moves

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

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy = self.enemy)]
        else:
            return self.adjacent_moves()

class LeaveCellarRoom(MapTile):
    def intro_text(self):
        return """
        A door is opening in front of you, a bright light shines through it.
        You survived the cellar!
        """

    def modify_player(self, player):
        player.victory = True
