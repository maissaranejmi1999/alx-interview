#!/usr/bin/python3
def validUTF8(data):
    data_len = len(data)
    i = 0

    while i < data_len:
        # Determine the length of the sequence
        if data[i] & 0b10000000 == 0:
            sequence = 1
        elif data[i] & 0b11100000 == 0b11000000:
            sequence = 2
        elif data[i] & 0b11110000 == 0b11100000:
            sequence = 3
        elif data[i] & 0b11111000 == 0b11110000:
            sequence = 4
        else:
            return False

        # Check if remaining bytes are enough for the sequence
        if i + sequence > data_len:
            return False

        # Validate the continuation bytes (10xxxxxx)
        for j in range(1, sequence):
            if data[i + j] & 0b11000000 != 0b10000000:
                return False

        # Move to the next character in the sequence
        i += sequence

    return True
