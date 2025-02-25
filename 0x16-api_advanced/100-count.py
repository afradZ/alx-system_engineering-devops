#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """ Queries the Reddit API, parses titles of hot articles,
    and prints a sorted count of given keywords (case-insensitive).
    If no posts match or the subreddit is invalid, prints nothing.
    """

    if not word_dict:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_word_count = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None  # Handles subreddit errors properly

    try:
        data = response.json().get("data", {})
        hot_posts = data.get("children", [])
        after = data.get("after")

        for post in hot_posts:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in word_dict:
                word_dict[word] += title.count(word)

    except ValueError:
        return None  # Handles invalid JSON responses

    count_words(subreddit, word_list, after, word_dict)

