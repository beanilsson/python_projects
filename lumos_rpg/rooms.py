import tiles

class EmptyPassage(MapTile):
    def intro_text(self):
        return """
        Just another unremarkable path. Keep on walking.
        """

    def modify_player(self, player):
        #This room has no action on the player
        pass

class BeetleRoom(EnemyRoom):
    def _init_(self, x, y):
        super()._init_(x, y, enemies.Beetle())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An evil beetle is hovering in front of you!
            """
        else:
            return """
            The shell of a dead beetle is lying on the ground.
            """

class SpiderRoom(EnemyRoom):
    def _init_(self, x, y):
        super()._init_(x, y, enemies.Spider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An angry spider crawls out of the corner!
            """
        else:
            return """
            A dead spider is lying on the ground.
            """

class TableKnifeRoom(LootRoom):
    def _init_(self, x, y):
        super()._init_(x, y, items.TableKnife())

    def intro_text(self):
        return """
        There is something shiny on the floor.
        It's a table knife! You pick it up.
        """

class StickRoom(LootRoom):
    def _init_(self, x, y):
        super()._init_(x, y, items.Stick())

    def intro_text(self):
        return """
        You step on something.
        It's a stick! You pick it up.
        """

class GoldRoom(LootRoom):
    def _init_(self, x, y):
        super()._init_(x, y, items.Gold())

    def intro_text(self):
        return """
        Something catches your eye.
        It's a golden coin! You pick it up.
        """
