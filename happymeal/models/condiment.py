class Condiment:
    def __init__(self, name="General Condiment", calories=20):
      self.name = name
      self.calories = int(calories)

    def total_calories(self):
      return self.calories
