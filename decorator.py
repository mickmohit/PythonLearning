def greet(fx):
  def decorator(*args, **kwargs):
     print("Good Morning")
     fx(*args, **kwargs)
     print("Thanks for using this fucntion")
  return decorator

@greet
def add(a,b):
  print(a+b)

#greet(add)(1,2)
add(1,2)