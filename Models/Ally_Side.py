from units import *
from mana import Mana
from castle import Castle
from player import Player

class Ally_Side:
    def __init__(self, player: Player) -> None:
        self.castle: Castle = Castle(player.castle_level)
        self.mana: Mana = Mana(0)
        self.lanes: int = 3
        self.units = []
        for _ in range(self.lanes):
            self.units.append([])
        self.player = player

    def add_unit(self, unit_name: str, lane: int):
        match unit_name:
            case "knight":
                if self.mana >= Mana.knight_cost():
                    new_unit = Knight(self.player.knight_level)
                    self.add_to_lane(new_unit, lane)
            case "archer":
                if self.mana >= Mana.archer_cost():
                    new_unit = Archer(self.player.archer_level)
                    self.add_to_lane(new_unit, lane)
            case _:
                raise NameError
    
    def add_to_lane(self, unit: Unit, lane: int):
        for i in range(len(self.units[lane])):
            if self.units[lane][i] is None:
                self.units[lane][i] = unit
                return
        self.units[lane].append(unit)
        