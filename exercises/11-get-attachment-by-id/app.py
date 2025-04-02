import requests

def get_attachment_by_id(attachment_id):
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    attachement = None
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()
        
        # Getting the posts
        posts = data["posts"]

        for _post in posts:
            if "attachments" in _post:
                for _attachement in _post["attachments"]:
                    if _attachement["id"] == attachment_id:
                        return _attachement["title"]
    else:
        print("Failed to fetch data from the endpoint.")
    