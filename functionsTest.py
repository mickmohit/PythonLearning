def calMean(a,b):
  mean=(a+b)/(b-a)
  print(mean)

a=10
b=20
calMean(a,b)

def avg(a=1,b=2):
 print(a+b/2)

avg()

def average(*numbers):
  sum=0
  for i in numbers:
   sum=sum+i
  print((sum)/len(numbers))

average(5,6,7,8)