class Condiment:
    def __init__(self, name="General Condiment", calories=20):
      print("caloris for coniment", str(calories))
      self.name = name
      self.calories = int(calories)

    def total_calories(self):
      return self.calories
