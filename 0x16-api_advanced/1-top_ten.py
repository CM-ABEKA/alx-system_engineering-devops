#!/usr/bin/python3

"""Module that queries the Reddit API for top hot posts."""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The subreddit to search.

    Returns:
        None if the subreddit is invalid or an error occurs.
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except (requests.exceptions.RequestException, ValueError):
        print("None")
