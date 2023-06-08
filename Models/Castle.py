
class Castle:
   def __init__(self, level: int = 1) -> None:
      self.level: int = level
      self.hp: float = 500 * self.level
   
   def __del__(self) -> None:
      pass
      
   def lose_hp(self, damage: int) -> float:
      self.hp -= damage
      if self.hp < 0:
         self.hp = 0
      return self.hp
   
   def level_up(self, new_level):
      self.level = new_level
      self.hp = 500 * self.level
      