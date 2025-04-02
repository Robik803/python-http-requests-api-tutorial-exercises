import requests

def get_titles():
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    titles = []
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()
        
        # Getting the posts
        posts = data["posts"]

        for _post in posts:
            titles.append(_post["title"])
    else:
        print("Failed to fetch data from the endpoint.")
    return titles

print(get_titles())