#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

import requests
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t - content: {response.text}")
