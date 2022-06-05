import items, enemies, actions, world

class MapTile:
    """we call this a abstract base class """
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def intro_text(self):
        raise NotImplementedError()

    def Modify_player(self, player):
        raise NotImplementedError()
    
    def adjacent_moves(self):
        """Returns all moves actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the avaliable actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

class EmptyCavePath(MapTile):
    def intro_text(self):
        return"""
        you find yourself in a cave with a flickering torch on the wall. 
        you can make out four paths, each equally as dark and forboding.
        """
    def modify_player(self, player):
        #room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self,x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damge. You have {} hp remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile = self), actions.Attack(enemy = self.enemy)]
        else:
            return self.adjacent_moves()

class Ruined_Castle(MapTile):
    def intro_text(self):
        return """
        you find yourself in the runied castle spoken in myths as the realm of the most evil Demon Lord D 
        """
    def Modify_player(self, player):
        #castle has no action on player 
        pass  
 
class Lost_DruidRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Lost_Druid())
    
    def intro_text(self):
        if self.enemy.is_alive():
           return"""
           The lost druid appears from the shadows of the throne room
           """
        else:
            return"""
            The druid fades away leaving behind the swords of the druids "Ranga"
            """

class FindRangaRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Ranga())

    def intro_text(self):
        return"""
        you notice a pulsating sword with a heavy aura left standing where the Druid stood.
        and you reach for it and pick it up and now have become bonded with your soul.
        """

class FindCoinRoom(LootRoom):
    def __init__(self, x, y, ):
        super().__init__(x, y, items.Gold())


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return"""
        You see a bright light in the distance...
        ... it grows as you get closer! It's the sunlight!
        
        victory is yours!
        """

    def modify_player(self, player):
        player.victory = True