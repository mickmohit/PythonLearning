class MyClass:

  def __init__(self, value):
    self._value = value
    self.__name="Mathew"

  def show(self):
    print(f"Value is {self._value}")

  @property
  def ten_value(self):
    return 10 * self._value

  @ten_value.setter
  def ten_value(self, new_value):
    self._value = new_value / 10

  @property
  def name(self):
    return self.__name


#Inheritance
class Programmer(MyClass):

  def showLanguage(self):
    print("Default Language")


p = MyClass(10)
p.ten_value = 67
print(p.ten_value)
p.show()
p1 = Programmer(12)
p1.showLanguage()
p1.show()
print(p.name)