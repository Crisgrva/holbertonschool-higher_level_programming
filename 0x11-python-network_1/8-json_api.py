#!/usr/bin/python3
"""
Write a Python script that takes in a
letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter
as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": argv[1]} if len(argv) > 1 else ""

    response = requests.post(url, data=payload)
    try:
        data = response.json()
    except Exception as e:
        print("Not a valid JSON")

    if len(data) > 0:
        print("[{}] {}".format(data["id"], data["name"]))
    else:
        print("No result")