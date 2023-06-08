from Unit import Unit
from Mana import Mana

class Knight(Unit):
    def __init__(self, level: int):
        name = "knight"
        range = 1
        attack_speed = 0.25 + 0.1 * level
        speed = 25 + 10 * level
        defense = 5 + 5 * level
        critical = 0.05 + 0.05 * level
        hp = 100 + 100 * level
        attack_damage = 20 + 10 * level
        cost = Mana(10)
        super().__init__(name,
                         range,
                         attack_speed,
                         speed,
                         defense,
                         critical,
                         hp,
                         attack_damage,
                         cost,
                         level)