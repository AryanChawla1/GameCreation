import random

class Unit:
    count = 0
    # Uses primitive data types, but it will be changed
    def __init__(self,
                 name: str,
                 range: int,
                 attack_speed: float,
                 speed: int,
                 defense: int,
                 critical: float,
                 hp: float,
                 attack_damage: int,
                 level: int) -> None:
        Unit.count += 1
        self.name: str = name
        self.range: int = range
        self.attack_speed: float = attack_speed
        self.speed: int = speed
        self.defense: int = defense
        self.critical: float = critical
        self.hp: float = hp   
        self.attack_damage: int = attack_damage
        self.level: int = level
    
    def __del__(self) -> None:
        pass

    def __str__(self) -> str:
        return "{id: " + str(Unit.count)\
        + ", name: " + self.name + \
        ", range: " + str(self.range) + \
        ", attack_speed: " + str(self.attack_speed) + \
        ", speed: " + str(self.speed) + \
        ", defense: " + str(self.defense) + \
        ", critical: " + str(self.critical) + \
        ", hp: " + str(self.hp) + \
        ", attack damage: " + str(self.attack_damage) + \
        ", level: " + str(self.level) + "}"

    def attack(self) -> int:
        if random.randint(0, 100) <= self.critical:
            return self.attack_damage * 3
        return self.attack_damage
    
    def lose_hp(self, damage) -> int | None:
        # damage is negated by defense
        # 100 damage with 10 defense is 90 damage
        self.hp -= damage * (100 - self.defense) / 100
        if self.hp < 0:
            self.hp = 0
        return self.hp
    