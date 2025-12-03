import time

applePrice=100
budget=80

if(applePrice<=budget):
 print("Buy")
else:
 print("Dont Buy")

timestamp=time.strftime('%H:%M:%S')
timestamp=time.strftime('%H')
print(timestamp)

a=150

match a:
  case 0:
    print("a is zero")
  case 50:
    print("a is 50")
  case _ if a<100:
    print("a is less than 100")
  case _ if a == 150:
    print("a is 150")
  case _:
    print(a)

i=0
while(i<4):
  print(i)
  i=i+1
