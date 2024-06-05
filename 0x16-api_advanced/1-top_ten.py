#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}  # Custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 sub.py <subreddit>")
        sys.exit(1)

    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)
    print("Subscribers on {}: {}".format(subreddit, subscribers))