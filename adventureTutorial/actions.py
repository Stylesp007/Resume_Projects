import player

class Action():
    def __init__(self,method,name,hotkey, **kwargs):
        self.method = method
        self.method = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=player.move_north, name='Move north', hotkey = 'n')

class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=player.move_south, name='Move south', hotkey = 's')

class MoveEast(Action):
    def __init__(self):
        super().__init__(method=player.move_east, name='Move east', hotkey = 'e')

class MoveWest(Action):
    def __init__(self):
        super().__init__(method=player.move_west, name='Move west', hotkey = 'w')

class ViewInventory(Action):
    def __init__(self):
        super().__init__(method = player.print_inventory, name = 'View inventory', hotkey = 'i')

class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method = player.attack, name = 'Attack', hotkey = 'a', enemy = enemy)

class Flee(Action):
    def __init__(self, tile):
        super().__init__(method = player.Flee, name = 'Flee', hotkey = 'f', tile = tile)