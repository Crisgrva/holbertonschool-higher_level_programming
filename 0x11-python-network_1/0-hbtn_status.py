#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    from urllib import request
    url = "https://intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
