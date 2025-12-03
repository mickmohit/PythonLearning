marks=[3,5,6,7]
print(marks)
print(type(marks))

lst=[i*i for i in range(5) if(i%2==0)]
print(lst)

#tuple
tup=(1,)
print(tup)
print(tup[0])

tup1=("Germany","Spain","Italy","France")
tup2=list(tup1)
tup2.append("India")
tup2[2] = "England"
tup1=tuple(tup2)
print(tup1)

#formatted string
letter="Hey my name is {0} and i'm from {1}"
name="Mohit"
country="India"
print(letter.format(name,country))

print(f"Hey name is {name} and i'm from {country}")

price=49.9966
txt=f"for only {price:.3f} rupees"
print(txt)

def square(n):
 '''Takes in a number n, return the square of n
 '''
 print(n**2)

square(5)
print(square.__doc__)
