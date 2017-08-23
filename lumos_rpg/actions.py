import Player

#Kwargs allows for a slot of additional parameters.
class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
    def __init__(self):
        super().__init__(method = Player.move_north, name = "Move north", hotkey = "w")

class MoveSout(Action):
    def __init__(self):
        super().__init__(method = Player.move_south, name = "Move south", hotkey = "s")

class MoveEast(Action):
    def __init__(self):
        super().__init__(method = Player.move_east, name = "Move east", hotkey = "d")

class MoveWest(Action):
    def __init__(self):
        super().__init__(method = Player.move_west, name = "Move west", hotkey = "a")

class ViewInventory(Action):
    def __init__(self):
        super().__init__(method = Player.print_inventory, name = "View inventory", hotkey = "i")

class Attack(Action):
    def __init__(self):
        super().__init__(method = Player.attack, name = "Attack", hotkey = "k", enemy = enemy)
