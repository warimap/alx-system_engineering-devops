#!/usr/bin/python3
"""
Module to recursively query the Reddit API, parse the title of all hot articles,
and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None, counts={}):
    """
    Recursively queries the Reddit API, counts occurrences of given keywords
    in titles of hot articles, and prints the counts sorted by frequency and alphabetically.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of keywords to count.
        hot_list (list): List of titles of hot articles (used for recursion).
        after (str): The `after` parameter for pagination (used internally).
        counts (dict): Dictionary to keep track of word counts (used for recursion).
    
    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "reddit-count/0.1"}
    params = {"limit": 100, "after": after}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        children = data.get('children', [])
        
        # Initialize word counts if not done already
        if not counts:
            counts = {word.lower(): 0 for word in word_list}
        
        # Count occurrences of each keyword in the titles
        for child in children:
            title = child['data'].get('title').lower().split()
            for word in word_list:
                word_lower = word.lower()
                counts[word_lower] += title.count(word_lower)
        
        # Pagination: recursively call the function if there's more data
        after = data.get('after')
        if after is not None:
            return count_words(subreddit, word_list, hot_list, after, counts)
        else:
            # Sort and print the results
            sorted_counts = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
            return None
    
    except requests.RequestException:
        return None
