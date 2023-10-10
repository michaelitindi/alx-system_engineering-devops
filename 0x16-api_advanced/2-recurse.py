#!/usr/bin/python3
""" returns hot article titles"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """ Function to return hot article titles """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    params = {"count": count, "after": after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code >= 400:
        return None
    hotl = hot_list + [child.get("data").get("title")
                       for child in response.json()
                       .get("data")
                       .get("children")]

    resp = response.json()
    if not resp.get("data").get("after"):
        return hotl
    return recurse(subreddit, hotl, resp.get("data").get("count"),
                   resp.get("data").get("after"))
