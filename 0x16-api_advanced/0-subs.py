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
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/cmabe_'}
    res = requests.get(api_url, headers, allow_redirects=False)

    if res.status_code >= 400:
        return 0

    return res.json().get('data').get('subscribers')
