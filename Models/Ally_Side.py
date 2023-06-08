from Units import *
from Mana import Mana
from Castle import Castle

class Ally_Side:
    def __init__(self, castle_level: int, knight_level: int) -> None:
        self.castle: Castle = Castle(castle_level)
        self.mana: Mana = Mana(0)
        self.lanes: int = 3
        self.units = []
        for _ in range(self.lanes):
            self.units.append([])
        self.knight_level: int = knight_level
    
    def add_unit(self, unit_name: str, lane):
        match unit_name:
            case "knight":
                if self.mana >= Mana.knight_cost():
                    new_unit = Knight(self.knight_level)
                    for i in range(len(self.units[lane])):
                        if self.units[lane][i] is None:
                            self.units[lane][i] = new_unit
            case _:
                raise NameError
