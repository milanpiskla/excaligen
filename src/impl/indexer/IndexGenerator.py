"""
Description: Generates indexes for Excalidraw elements.
Excalidraw generates fractional indexes according to 
https://observablehq.com/@dgreensp/implementing-fractional-indexing

We just need to generate a sequece of fractional indexes for the fixed amount 
of elements in the diagram.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class IndexGenerator:
    _BASE62_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def __init__(self, initial_value='a0'):
        """
        Initialize the generator with the given initial value.
        
        :param initial_value: The starting value of the index, default is 'Zz' to get first next value 'a0'.
        """
        self._current = initial_value

    def next(self):
        """
        Generate the next index in the sequence.

        :return: The next fractional index as a string.
        """
        # Increment the current value
        self._current = self._increment(self._current)

        # Handle transitions like 'az' -> 'b00'
        if all(c == self._BASE62_CHARS[0] for c in self._current[1:]):
            self._current += self._BASE62_CHARS[0]

        return self._current


    def _increment(self, value):
        """
        Increment a Base62 string value with proper carry-over.

        :param value: The Base62 string to increment.
        :return: The incremented Base62 string.
        """
        chars = list(value)
        i = len(chars) - 1
        carry = True

        while i >= 0 and carry:
            char_index = self._BASE62_CHARS.index(chars[i]) + 1
            if char_index < len(self._BASE62_CHARS):
                chars[i] = self._BASE62_CHARS[char_index]
                carry = False
            else:
                chars[i] = self._BASE62_CHARS[0]
                i -= 1

        if carry:
            chars.insert(0, self._BASE62_CHARS[0])

        return ''.join(chars)