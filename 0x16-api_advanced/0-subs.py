#!/usr/bin/python3
""" returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """ Function to return no of subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    return response.json().get("data").get("subscribers")
