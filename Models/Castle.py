
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
   
   def level_up(self):
      self.level += 1
      self.hp += 500
      