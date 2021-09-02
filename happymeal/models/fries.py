class Fries:
    def __init__(self):
      self._calories = 150
      self.name = "Fries"
      self.sodium = 20

    def __repr__(self):
        return self.name

    def calories(self):
        return self._calories
