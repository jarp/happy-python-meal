class Drink:
  def __init__(self):
    self.syrup = "Water"
    self.water = "plain"
    self.calories = 0
    self.ice_ratio = 0

  def to_s():
    return self.syrup

  def calories(self):
    self.calories

class Soda(Drink):
    def __init__(self, syrup = "none", water = "carbonated"):
      self.syrup = syrup
      self.water = water
      self.calories = 100

class Sprite(Soda):
    def __init__(self):
      super().__init__(self, 'Sprite')
    

class DietSprite(Soda):
    def __init__(self):
      super().__init__(self, 'Diet Sprite')
      self.calories = 0

class Coke(Soda):
    def __init__(self):
      super().__init__(self, 'Coke')
    

class DietCoke(Soda):
    def __init__(self):
      super().__init__(self, 'Diet Coke')
      self.calories = 0
