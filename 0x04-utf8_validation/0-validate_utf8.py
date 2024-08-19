#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determines if the given data set represents a valid UTF-8 encoding.
    """
    remaining_bytes = 0
    first_bit_mask = 1 << 7
    second_bit_mask = 1 << 6

    for byte_value in data:
        byte_value = byte_value & 0xFF

        if remaining_bytes == 0:
            if (byte_value & first_bit_mask) == 0:
                continue
            elif (byte_value & (first_bit_mask >> 1)) == 0:
                return False
            elif (byte_value & (first_bit_mask >> 2)) == 0:
                remaining_bytes = 1
            elif (byte_value & (first_bit_mask >> 3)) == 0:
                remaining_bytes = 2
            elif (byte_value & (first_bit_mask >> 4)) == 0:
                remaining_bytes = 3
            else:
                return False
        else:
            if not (
                byte_value & first_bit_mask and
                not (byte_value & second_bit_mask)
            ):
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
