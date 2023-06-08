from Unit import Unit
from Mana import Mana

class Archer(Unit):
    def __init__(self, level: int):
        name = "archer"
        range = 3
        attack_speed = 2 - 0.2 * level
        speed = 30 + 10 * level
        defense = 0 + 3 * level
        critical = 0.07 + 0.05 * level
        hp = 80 + 80 * level
        attack_damage = 10 + 10 * level
        super().__init__(name,
                         range,
                         attack_speed,
                         speed,
                         defense,
                         critical,
                         hp,
                         attack_damage,
                         level)
        