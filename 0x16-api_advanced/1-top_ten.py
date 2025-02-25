#!/usr/bin/python3
'''
    This module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        Returns the top ten posts for a given subreddit
    '''
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get("data", {}).get("children", [])

            if not posts:
                print(None)
            else:
                for post in posts:
                    print(post["data"]["title"])
        except ValueError:  # Handles JSON decoding errors
            print(None)
    else:
        print(None)


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Usage: ./1-top_ten.py <subreddit>")

