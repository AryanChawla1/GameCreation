from unit import Unit

class Enemy(Unit):
    def __init__(self, level: int):
        name = "enemy"
        range = 2
        attack_speed = 0.5 - 0.1 * level
        speed = 10 + 10 * level
        defense = 0 + 5 * level
        critical = 0.03 + 0.01 * level
        hp = 120 + 90 * level
        attack_damage = 15 + 8 * level
        super().__init__(name,
                         range,
                         attack_speed,
                         speed,
                         defense,
                         critical,
                         hp,
                         attack_damage,
                         level)
