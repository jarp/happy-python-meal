class HappyMeal:
  def __init__(self, drink, main, side, toy):
    self.price = 3.59
    self.drink = drink
    self.main = main
    self.side = side
    self.toy = toy

  def set_price(self, price):
    self.price = price

  def calories(self):
    return self.drink.calories + self.side.calories + self.main.calories()

  def to_string(self):
    return "This happy meal is composed of {}, {}, {}, and a {}".format(self.drink, self.main, self.side,self.toy)
