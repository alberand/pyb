#!/usr/bin/python

'''
Small script to display numbers in HEX, decimal and binary formats. I tired of
googling for "hex to dec", "dec to hex" etc. This can be done by python or bash
but it's easier and doesn't force you to remember commands.

Doesn't work with negative numbers.

Usage:
    $ pyb 0b01010101
    $ pyb 0xFF
    $ pyb 123

TODO:
    * Negative numbers
    * Octal number representation
    * ASCII

Author:
    Andrey Albershteyn <andrey.albershteyn@gmail.com>
'''

import sys

def is_bin(num):
    return num[0:2] == '0b'

def is_hex(num):
    return num[0:2] == '0x'

def is_dec(num):
    return num.isdigit()

def from_bin(num):
    return int(num, 2)

def from_hex(num):
    return int(num, 16)

def from_dec(num):
    return int(num)

def convert(num):
    d = 0
    if is_bin(num):
        d = from_bin(num)
    if is_hex(num):
        d = from_hex(num)
    if is_dec(num):
        d = from_dec(num)

    return d

def int_size(num):
    size = 0
    while True:
        if num < pow(2, size):
            return size
        size = size + 4


def output(d):
    size = int_size(d)

    tmpl = '\tBIN: {{bin:#0{}b}}\n\tHEX: {{hex:0{}x}}\n\tDEC: {{dec}}'.format(
            size + 2, size/4)

    print(tmpl.format(bin=d, hex=d, dec=d))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    number = sys.argv[1]
    
    output(convert(number))
