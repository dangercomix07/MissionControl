import requests

url = "http://127.0.0.1:8000/tasks"
data = {"name": "Develop CubeSat Power System", "status": "In Progress"}

response = requests.post(url, json=data)
print(response.json())
