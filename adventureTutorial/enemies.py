
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Dragon(Enemy):
    def __init__(self):
        super().__init__(name = "Dragon", hp = 75, damage = 125)


class Celestial_avatar(Enemy):
    def __init__(self):
        super().__init__(name = "Celestial_avatar", hp = 50, damage = 75)

class Lost_Druid(Enemy):
    def _init__(self):
        super().__init__(name = "Lost druid", hp = 30, damage = 45)