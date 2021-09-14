#!/usr/bin/python3
def multiple_returns(sentence):
    sentenceLen = len(sentence)
    if sentenceLen == 0:
        fstLetter = None
    else:
        fstLetter = sentence[0]
    new_tuple = (sentenceLen, fstLetter)
    return new_tuple
