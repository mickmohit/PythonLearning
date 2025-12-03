f = open('myfile.txt', 'r')  #r is for read mode, w for write mode
text = f.read()
print(text)
f.close()

#with
with open('myfile2.txt', 'a') as f:
  f.write("Damn its working")


with open('myfile3.txt','r') as f:
  i=0
  while True:
    i=i+1
    line = f.readline()
    if not line:
     break
    m1=line.split(",")[0]  #first number before comma
    m2=line.split(",")[1]
    m3=line.split(",")[2]

    print(f"Marks of student {i} in Subject1: {m1}")
    print(f"Marks of student {i} in Subject2: {m2}")
    print(f"Marks of student {i} in Subject3: {m3}")
    print(line)


with open('myfile4.txt','r') as f:
  # f.write("hello brother")
   f.seek(4) #to start reading from 4th character
   data = f.read(7) #read only next 7 characters
   print(data)