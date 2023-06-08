from Ally_Side import Ally_Side

class Player:
    def __init__(self) -> None:
        self.castle_level: int = 1
        self.knight_level: int = 1
    
    def upgrade_castle(self) -> int:
        self.castle_level += 1
        return self.castle_level
    
    def upgrade_knight(self) -> int:
        self.knight_level += 1
        return self.knight_level
    
    def create_side(self):
        Ally_Side(self.castle_level, self.knight_level)