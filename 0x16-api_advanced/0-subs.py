#!/usr/python3

"""
Function returning  number of subscribers in a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function returns the number of subscribers in a subreddit
    """

    # Default Urls
    api_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(api_url,
                       headers={'User-Agent': 'ALX - 0x16.advanced.api'},
                       allow_redirects=False)

    if res.status_code in [302, 404]:
        return 0

    return res.json().get('data').get('subscribers')
