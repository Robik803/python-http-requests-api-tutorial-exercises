import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")

project = response.json()

print(project["name"])