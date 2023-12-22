#!/usr/bin/env python3
from secret import FLAG, KEY

CHARACTER_SET = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ """

def caesar(message: str, key: int):
    """ Caesar Cipher with a custom character set """
    key %= len(CHARACTER_SET)
    return message.translate(str.maketrans(CHARACTER_SET, CHARACTER_SET[key:]+CHARACTER_SET[:key]))

def encrypt(message: str, key: int):
    """ Recursive encryption of caesar """
    if len(message) < 2:
        return caesar(message, key)
    return caesar(message[0] + encrypt(message[1:-1], key+1) + message[-1], key)

print(encrypt(FLAG, KEY))
