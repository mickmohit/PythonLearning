import threading
import time
from concurrent.futures import ThreadPoolExecutor


def func(seconds):
  print(f"sleeping for {seconds} seconds")
  time.sleep(seconds)
  return seconds


#Normal way of calling
func(1)
func(2)

print("----")

start = time.perf_counter()
# Same code using Threads
t1 = threading.Thread(target=func, args=[1])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[3])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.perf_counter()
print(end - start)

print("----")
#new standard in python for multithreading


def poolingDemo():
  with ThreadPoolExecutor() as executor:
    future1 = executor.submit(func, 1)
    future2 = executor.submit(func, 2)
    future3 = executor.submit(func, 3)
    print(future1.result())
    print(future2.result())
    print(future3.result())

    print("----")
    l = [1, 2, 3, 4]
    results = executor.map(func, l)
    for result in results:
      print(result)


poolingDemo()
