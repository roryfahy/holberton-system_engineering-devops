#!/usr/bin/python3
"""query reddit api for num of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """return the number of subscribrers of a given subreddit"""
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    resp = requests.get(url, allow_redirects=False, headers=user_agent)
    if resp.status_code in (302, 404):
        return 0
    return resp.json().get('data').get('subscribers')
