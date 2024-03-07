#!/usr/bin/python3

"""Module for task 2"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the Reddit API and returns all hot posts of the subreddit.

    Args:
        subreddit (str): The subreddit to search.
        hot_list (list, optional): The list of hot
        post titles. Defaults to None.
        after (str, optional): The parameter to get the
        next set of posts. Defaults to None.

    Returns:
        list: The list of hot post titles, or None if the subreddit is invalid.
    """
    hot_list = hot_list or []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code >= 400:
        return None

    hot_list.extend(
        child.get("data").get("title")
        for child in response.json().get("data").get("children", [])
    )

    after = response.json().get("data", {}).get("after")

    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after)
