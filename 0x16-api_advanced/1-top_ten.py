#!/usr/bin/python3
"""query reddit api"""

import requests


def top_ten(subreddit):
    """print titles of first 10 hot posts listed for a given sub"""
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    resp = requests.get(url, allow_redirects=False, headers=user_agent)
    if resp.status_code in (302, 404):
        print(None)
    else:
        for post in resp.json().get('data').get('children'):
            print(post.get('data').get('title'))
