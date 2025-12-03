try:
  for i in range(1,10):
    if(i==9):
      print(i/0)
    else:
      print(i)
except Exception as e:
  print("error",e)
finally:
  print("finally")


a=2
b=3
print("A") if a>b else print("=") if a==b else print("B")

marks=[1,2,3,4,5,5,6]

for index, mark in enumerate(marks):
 print(mark)
 if(index==3):
  print("awesome")

import jasc as j

j.welcome()


  