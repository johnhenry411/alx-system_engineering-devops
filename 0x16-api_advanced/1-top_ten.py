#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests
import sys

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("Subreddit not found")
        return

    results = response.json().get("data")

    [print(c.get("data").get("title")) for c in results.get("children")]

if __name__ == "__main__":
    if len(sys.argv)!= 2:
        print("Usage: python3 hot_posts.py <subreddit>")
        sys.exit(1)

    subreddit = sys.argv[1]
    print("Hot posts on r/{}:".format(subreddit))
    top_ten(subreddit)