#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

from urllib import request


def get_response(url: str):
    """
    Function that fecth source from url
    and return Body response
    """
    with request.urlopen(url) as response:
        html = response.read()
        return(f"""Body response:
\t- type: {type(html)}
\t- content: {html}
\t- utf8 content: {html.decode('utf-8')}""")


if __name__ == "__main__":
    print(get_response("https://intranet.hbtn.io/status"))
