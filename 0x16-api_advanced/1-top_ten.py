import requests

def top_ten(subreddit):
    """
    Retrieves the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The subreddit to search.

    Returns:
        None if the subreddit is invalid or if an error occurs.
    """
    try:
        # Make a GET request to the Reddit API
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        # Check if the response is a valid subreddit
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]

            # Print the titles of the first 10 hot posts
            for post in posts[:10]:
                title = post["data"]["title"]
                print(title)
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print("None")
