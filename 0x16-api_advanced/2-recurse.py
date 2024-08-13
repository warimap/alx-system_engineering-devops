mport requests

def recurse(subreddit, hot_list=[], after=None):
    # Define the base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "reddit-hot-articles/0.1"}
    
    # Set up the query parameters
    params = {"limit": 100}  # Limit the number of posts per request (maximum allowed is 100)
    if after:
        params["after"] = after
    
    try:
        # Send a GET request to the subreddit URL
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the response status is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            # Extract titles and append to hot_list
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            
            # Check if there's another page of results
            after = data['data']['after']
            if after is not None:
                # Recursive call to fetch the next page
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None

