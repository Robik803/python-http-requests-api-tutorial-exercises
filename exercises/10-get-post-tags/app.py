import requests

def get_post_tags(post_id):
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    tags = None
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()
        
        # Getting the posts
        posts = data["posts"]

        for _post in posts:
            if _post["id"] == post_id:
                tags = _post["tags"]
    else:
        print("Failed to fetch data from the endpoint.")
    return tags


print(get_post_tags(146))