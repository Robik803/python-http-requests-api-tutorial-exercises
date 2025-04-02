import requests

response = requests.post("https://assets.breatheco.de/apis/fake/sample/post.php")

print(response.text)
