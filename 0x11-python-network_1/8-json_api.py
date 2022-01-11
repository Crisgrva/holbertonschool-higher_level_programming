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
    try:
        payload = {"q": argv[1]}
    except Exception as e:
        payload = {"q": ""}

    response = requests.post(url, data=payload)
    try:
        data = response.json()
    except ValueError as e:
        print("Not a valid JSON")

    if len(data) > 0:
        print("[{}] {}".format(data["id"], data["name"]))
    else:
        print("No result")
