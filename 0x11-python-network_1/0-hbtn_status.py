#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request


def get_response(url: str):
    """
    Function that fecth source from url
    and return Body response
    """
    with urllib.request.urlopen(url) as response:
        html = response.read()
        return(f"""Body response:
    - type: {type(html)}
    - content: {html}
    - utf8 content: {html.decode('utf-8')}""")


if __name__ == "__main__":
    print(get_response("https://intranet.hbtn.io/status"))
