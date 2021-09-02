class Drink:
  def __init__(self):
    self.syrup = "Water"
    self.water = "plain"
    self._calories = 0
    self.ice_ratio = 0

  def __repr__(self):
      return self.syrup

  def calories(self):
    return self._calories

class Soda(Drink):
    def __init__(self, syrup = "none", water = "carbonated"):
      self.syrup = syrup
      self.water = water
      self._calories = 100

class Sprite(Soda):
    def __init__(self):
      super().__init__('Sprite')

class DietSprite(Soda):
    def __init__(self):
      super().__init__('Diet Sprite')
      self._calories = 0

class Coke(Soda):
    def __init__(self):
      super().__init__('Coke')
    

class DietCoke(Soda):
    def __init__(self):
      super().__init__('Diet Coke')
      self._calories = 0
