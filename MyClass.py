class MyClass:

  company = "Apple"

  def __init__(self, value):
    self._value = value
    self.__name = "MathewD"  #private Variable

  def show(self):
    print(f"Value is {self._value}")

  @property
  def ten_value(self):
    return 10 * self._value

  @ten_value.setter
  def ten_value(self, new_value):
    self._value = new_value / 10

  @property
  def value(self):
    return self._value

  @staticmethod
  def add(a, b):
    print(a + b)

  @classmethod
  def changeCompany(self, newCompany):
    self.company = newCompany


#Inheritance
class Programmer(MyClass):

  def __init__(self, value, lang):
    super().__init__(value)
    self.lang = lang

  def showLanguage(self):
    print("Default Language")


p = MyClass(10)
p.ten_value = 67
print(p.ten_value)
p.show()
p1 = Programmer(12, "Python")
p1.showLanguage()
p1.show()
print(p._MyClass__name)  #mingling to access private variable
print(MyClass.add(5, 1))  #static method calling

p3 = MyClass(11)
p3.changeCompany("Tesla")  #class method calling
print(p3.company)  #will directly update the class variable

print(p1.lang)
print(p1.value)