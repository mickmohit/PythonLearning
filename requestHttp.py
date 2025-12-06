import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {"title": "foo", "body": "bar", "userId": 1}

headers = {'Content-type': 'application/json; charset=UTF-8'}

response = requests.post(url, headers=headers, json=data)
print(response.text)


#Generators in Python
def my_generator():
  for i in range(5):
    yield i


gen = my_generator()
print(next(gen))
print(next(gen))

#lru caching via functools
import functools
import time


@functools.lru_cache(maxsize=None)
def fx(n):
  time.sleep(2)
  return n * 2


print(fx(2))
print(fx(4))
print(fx(2))
print(fx(4))
