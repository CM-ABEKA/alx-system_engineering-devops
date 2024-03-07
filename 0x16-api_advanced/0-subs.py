#!/usr/python3

"""
Function returning  number of subscribers in a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function returns the number of subscribers in a subreddit
    - if not a valid redit return 0
    """

    # Default Urls
    api_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'info@leetwork.com'}
    res = requests.get(api_url, headers, allow_redirects=False)

    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    else:
        return 0
