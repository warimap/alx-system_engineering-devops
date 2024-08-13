#!/usr/bin/python3
"""
Module that contains a recursive function to query the Reddit API and
return a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all
    hot articles for the given subreddit.
    
    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): List of titles of hot articles (used for recursion).
        after (str): The `after` parameter for pagination (used internally).
    
    Returns:
        list: A list containing the titles of all hot articles, or None if the
        subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "reddit-recurse/0.1"}
    params = {"limit": 100, "after": after}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        
        data = response.json().get('data', {})
        children = data.get('children', [])
        
        for child in children:
            hot_list.append(child['data'].get('title'))
        
        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    
    except requests.RequestException:
        return None
