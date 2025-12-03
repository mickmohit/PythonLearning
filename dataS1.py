def fact(n):
 if(n==0 or n==1):
  return 1
 else:
   return n*fact(n-1)

print(fact(5))

#set
st={2,2,3,4,5,6}
print(st)

dic={
  344:"Mohit",
  345:"Rohit",
  346:"Sohit"
}
print(dic)
print(dic[346])

for key in dic.keys():
  print(dic[key])

print(dic.items())

for key,value in dic.items():
  print(f"key {key} and value {value}")

ep1={12:45,13:46,14:47}
ep2={15:48,16:49}

ep1.update(ep2)
print(ep1)

#for with else -- else will execute only when for loop will complete itself
for i in range(5):
 print(i)
else:
 print("no I provided")

