import requests

url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"

body = {
    "id": 2323,
    "title": "Very big project"
}


header = {
    "Content-Type": "application/json"
}


response = requests.post(url, json = body, headers = header)
print(response.text)