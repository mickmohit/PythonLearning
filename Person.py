class Person:
  name = "Mathew"
  occupation = "SDE"
  age = 28

  def __init__(self):
    print("Hey I am a person")

  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
a.info()
