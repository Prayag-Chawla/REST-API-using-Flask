import requests


url = 'http://127.0.0.1:5000/video/2'

data = {
    'name': 'Updated Video',
    'views': 150,
    'likes': 70
}

response = requests.put(url, json=data)


print(response.json())

