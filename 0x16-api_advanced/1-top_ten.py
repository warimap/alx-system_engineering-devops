import requests

def top_ten(subreddit):
    # Define the base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set a custom User-Agent to avoid being rate-limited by Reddit
    headers = {"User-Agent": "reddit-top-ten/0.1"}
    
    try:
        # Send a GET request to the subreddit URL
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            # Extract and print the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            # Print None if the subreddit is invalid or response code is not 200
            print(None)
    except requests.RequestException:
        # Print None if there was an issue with the request
        print(None)
