#!/usr/bin/python3
import marshal

s = open('hidden_4.pyc', 'rb')
s.seek(8)
code_obj = marshal.load(s)

print(code_obj)
