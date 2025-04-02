import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

time = response.json()

hours = time["hours"]
minutes = time["minutes"]
seconds = time["seconds"]

print(f"Current time: {hours} hrs {minutes} min and {seconds} sec")


