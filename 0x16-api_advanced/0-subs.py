import requests

def number_of_subscribers(subreddit):
    # Define the base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid being rate-limited by Reddit
    headers = {"User-Agent": "subreddit-subscriber-checker/0.1"}
    
    try:
        # Send a GET request to the subreddit URL
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # Return 0 if the subreddit is invalid or response code is not 200
            return 0
    except requests.RequestException:
        # Return 0 if there was an issue with the request
        return 0

