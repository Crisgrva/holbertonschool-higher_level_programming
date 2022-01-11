#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

from urllib import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        html = response.read()
        print(f"""Body response:
    - type: {type(html)}
    - content: {html}
    - utf8 content: {html.decode('utf-8')}""")
