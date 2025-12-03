def test(fx, value):
  return 6*fx(value)

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3

print(double(5))
print(cube(3))
print(avg(1,2,3))
print(test(cube,2))

#Map function
lst=[1,2,3,4,5,6]
newlst=list(map(lambda x:x*x*x,lst))
print(newlst)

#filter
newlst=list(filter(lambda x:x>3,lst))
print(newlst)

#reduce
from functools import reduce
newlst=reduce(lambda x,y:x+y,lst)
print(newlst)