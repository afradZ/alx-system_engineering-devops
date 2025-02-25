#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # If the request fails (404, 403, etc.), return None
    if response.status_code != 200:
        return None
    
    try:
        results = response.json().get("data", {})
        after = results.get("after")
        count += results.get("dist", 0)
        for c in results.get("children", []):
            hot_list.append(c.get("data", {}).get("title"))

        if after:
            return recurse(subreddit, hot_list, after, count)
        return hot_list

    except ValueError:  # Handle JSON decoding errors
        return None

