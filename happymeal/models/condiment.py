class Condiment:
    def __init__(self, name="General Condiment", calories=20):
      self.name = name
      self._calories = int(calories)

    def calories(self):
      return self._calories
