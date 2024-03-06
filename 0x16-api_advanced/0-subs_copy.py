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
    print('Url loading ...')
    api_url = 'https://dummyjson.com/{}'.format(subreddit)
    print('loaded url {}'.format(api_url))
    res = requests.get(api_url,
            headers={'User-Agent': '0x16.advanced.api'},
            allow_redirects=False)
    print('response = '.format(res)
    if res.status_code in [302, 404]:
        return 0
    return res.json().get('data').get('subscribers')
