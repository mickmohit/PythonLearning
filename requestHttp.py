import requests

url = "https://jsonholder.typicode.com/posts"

data = {"title": "foo", "body": "bar", "userId": 1}

headers = {'Content-type': 'application/json; charset=UTF-8'}

response = requests.post(url, headers=headers, json=data)
print(response.text)
