#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments
in order to solve this challenge.
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    repo = argv[1]
    username = argv[2]
    URL = "https://api.github.com/repos/{}/{}/commits".format(repo, username)

    response = requests.get(URL)
    for commit in response.json():
        print(commit['sha'], end=': ')
        print(commit['commit']['author']['name'])
