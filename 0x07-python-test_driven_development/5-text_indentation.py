#!/usr/bin/python3
"""
4. Text indentation
"""


def text_indentation(text):
    """
    Write a function that prints a text with 2 new
    lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    p = 0
    ch = 0
    delim = [".", "?", ":"]

    for ch in range(len(text)):
        if text[ch] in delim:
            ch += 1
            tmp_text = text[p:ch].strip()
            new_text += tmp_text + "\n\n"
            p = ch

    new_text += text[p:].strip()

    print(new_text, end="")
