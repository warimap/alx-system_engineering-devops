#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit. If the subreddit is invalid,
    print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "reddit-top-ten/0.1"}
    params = {"limit": 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts:
                print(post['data'].get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)
