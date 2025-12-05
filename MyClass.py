class MyClass:

  company = "Apple"

  def __init__(self, id, value):
    self.id = id  #public variable
    self._value = value  #protected variable
    self.__name = "MathewD"  #private Variable

  def show(self):
    print(f"Value is {self._value}")

  @property
  def ten_value(self):
    return 10 * self._value

  #setter to set property value
  @ten_value.setter
  def ten_value(self, new_value):
    self._value = new_value / 10

  @staticmethod
  def add(a, b):
    print(a + b)

  #class method to change class variable
  @classmethod
  def changeCompany(self, newCompany):
    self.company = newCompany


#Inheritance
class Programmer(MyClass):

  #calling parent class constrcutor via super()
  def __init__(self, id, value, lang):
    super().__init__(id, value)
    self.lang = lang

  def showLanguage(self):
    print("Default Language")


p = MyClass(1, 10)
p.ten_value = 67
print(p.ten_value)
p.show()
p1 = Programmer(1, 12, "Python")
p1.showLanguage()
p1.show()
print(p._MyClass__name)  #mingling to access private variable
print(MyClass.add(5, 1))  #static method calling

p3 = MyClass(1, 11)
p3.changeCompany("Tesla")  #class method calling
print(p3.company)  #will directly update the class variable

#accessing all types of varibale from child class to parent
print(p1.lang)
print(p1._value)
print(p1.id)
