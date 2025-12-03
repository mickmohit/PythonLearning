import pandas

print("hello")

"""
Hello Mohit how're you
"""
print("Hey I am good. \"how're you\"\nand"
" this going great.")

b="Singh"
print(b)
c=True
print(type(c))
d=complex(5,6)
print(d)
print(type(d))
dict1={"name":"Mohit","age":"33"}
print(dict1)

a1="1"
b1="2"
print(int(a1)+int(b1))

a2=input("whats your name: ")
print("My name is", a2)

print(a2[0])

for character in a2:
  print(character)

print(a2[0:2])
print(len(a2))

a="Harry! Hey"
print(a.upper())
print(a.rstrip("!"))
print(a.replace("Harry","John"))
print(a.split(" "))
print("count r character in string: ", a.count("r"))

b="He is an honest man, he's good."
print(b.find("is"))
print(b.index("is"))

a1=78
if(a1>19):
 print("you can drive")
else:
 print("you can't drive")