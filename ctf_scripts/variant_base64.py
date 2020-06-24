#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:54:29 2020

@author: Casuall

用python实现base64编码，通过更改base64_charset可以实现base64的变体
"""

import base64

# 变体
# base64_charset = ['i', '5', 'j', 'L', 'W', '7', 'S', '0', 'G', 'X',
#                 '6', 'u', 'f', '1', 'c', 'v', '3', 'n', 'y', '4', 
#                 'q', '8', 'e', 's', '2', 'Q', '+', 'b', 'd', 'k', 
#                 'Y', 'g', 'K', 'O', 'I', 'T', '/', 't', 'A', 'x', 
#                 'U', 'r', 'F', 'l', 'V', 'P', 'z', 'h', 'm', 'o', 
#                 'w', '9', 'B', 'H', 'C', 'M', 'D', 'p', 'E', 'a', 
#                 'J', 'R', 'Z', 'N']

# 正常的base64编码表
base64_charset = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '+', '/']


def encode_base64(raw_string: str) -> str:
    pad_num = 3 - (len(raw_string) % 3) if len(raw_string) % 3 else 0
    base64_bytes = ['{:0>8b}'.format(ord(char)) for char in raw_string]
    pad_bytes = ['0' * 8] * pad_num
    base64_bytes.extend(pad_bytes)
    base64_bytes = ''.join(base64_bytes)

    enc_index = [base64_bytes[i:i+6] for i in range(0, len(base64_bytes), 6)]
    enc_index = list(map(lambda x: int(x, 2), enc_index[:-pad_num]))
    enc_string = ''.join([base64_charset[i] for i in enc_index]) + pad_num * '='
    return enc_string


def decode_base64(enc_string: str) -> str:
    base64_bytes = ["{:0>6b}".format(base64_charset.index(char)) if char != '=' else '0'*6 for char in enc_string]
    base64_bytes = ''.join(base64_bytes)

    list_ascii = [base64_bytes[i:i+8] for i in range(0, len(base64_bytes), 8)]
    dec_string = ''.join(list(map(lambda x: chr(int(x, 2)), list_ascii)))

    return dec_string


def main():
    text = 'abcd'
    enc = encode_base64(text)
    print(enc)
    dec = decode_base64(enc)
    print(dec)


if __name__ == "__main__":
    main()

