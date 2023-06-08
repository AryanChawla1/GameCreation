from __future__ import annotations
from functools import total_ordering

@total_ordering
class Mana:
    def __init__(self, value: int) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __ge__(self, other: Mana):
        return self.value >= other.value
    
    def __eq__(self, other: Mana):
        return self.value == other.value

    def knight_cost() -> int:
        return Mana(10)
    
    def archer_cost() -> int:
        return  Mana(15)
    