#!/usr/bin/python3
"""utf8 module"""


def validUTF8(data):
    """ Number of bytes remaining in the current UTF-8 character"""
    bytes_remaining = 0

    for num in data:
        """ Mask to get only the last 8 bits"""
        byte = num & 0xFF

        if bytes_remaining == 0:
            """ Determine the number of bytes for this character"""
            if (byte >> 5) == 0b110:
                bytes_remaining = 1
            elif (byte >> 4) == 0b1110:
                bytes_remaining = 2
            elif (byte >> 3) == 0b11110:
                bytes_remaining = 3
            elif (byte >> 7):
                return False
        else:
            """ Check continuation byte (must start with '10')"""
            if (byte >> 6) != 0b10:
                return False
            bytes_remaining -= 1

    return bytes_remaining == 0
