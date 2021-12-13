class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width


class Vehicle:
  def __init__(self, max_speed=200, mileage=0):
    self.max_speed = max_speed
    self.mileage = mileage

class Bus(Vehicle):
  def __init__(self, max_speed=200, mileage=0):
    super().__init__(max_speed, mileage)

"""
Empty Vehicle Class

class Vehicle:
  pass


"""
