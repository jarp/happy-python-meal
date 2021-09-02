class Hamburger:

  def __init__(self, condiments=[]  ):
    self.name = "Hamburger"
    self.base_calories = 300
    self.condiments = condiments

  def __repr__(self):
    self.name

  def calories(self):
    sum = 0
    for c in self.condiments:
      if hasattr(c, 'calories'):
        # print('cals: ', c.calories)
        sum = sum + c.calories
    return self.base_calories + sum
