
class Mana:
    def __init__(self, value: int) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)
    
    def knight_cost() -> int:
        return Mana(10)