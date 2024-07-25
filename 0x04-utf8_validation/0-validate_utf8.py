#!/usr/bin/python3
"""UTF-8 Validation"""


def get_leading_set_bits(num):
    """returns the no. of leading set bits (1)"""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """determines if a given dataset represents a valid UTF-8 encoding"""
    bits_count = 0
    for m in range(len(data)):
        if bits_count == 0:
            bits_count = get_leading_set_bits(data[m])
            '''1-byte (format: 0xxxxxxx)'''
            if bits_count == 0:
                continue
            '''a char in UTF-8 can be 1 to 4 bytes long'''
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            '''checks if the current byte has format 10xxxxxx'''
            if not (data[m] & (1 << 7) and not (data[m] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
