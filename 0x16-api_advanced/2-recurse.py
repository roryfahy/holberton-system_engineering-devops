#!/usr/bin/python3
"""query reddit api"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=''):
    """recursively return list containing hot post titles for a given sub"""
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json?after={}&count={}".format(
        subreddit,
        after,
        count
    )
    resp = requests.get(url, allow_redirects=False, headers=user_agent)
    if resp.status_code in (302, 404):
        return None
    if len(resp.json().get('data').get('children')) == 0:
        if count == 0:
            return None
        return hot_list
    after = resp.json().get('data').get('after')
    count += resp.json().get('data').get('dist')
    for post in resp.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
    recurse(subreddit, hot_list=hot_list, count=count, after=after)
