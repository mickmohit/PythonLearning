import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {"title": "foo", "body": "bar", "userId": 1}

headers = {'Content-type': 'application/json; charset=UTF-8'}

response = requests.post(url, headers=headers, json=data)
print(response.text)

def my_generator():
   for i in range(5):
    yield i

gen = my_generator()
print(next(gen))