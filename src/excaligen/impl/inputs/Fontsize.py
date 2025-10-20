"""
Description: Helper for font size input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Fontsize:
    SIZE_MAPPING = {
        "s": 16,
        "m": 20,
        "l": 24,
        "xl": 32
    }

    @staticmethod
    def from_(size: int | str) -> int:
        """Set the font size by int or by string ('S', 'M', 'L', 'XL').

        Args:
            size (int | str): The font size to set.

        Raises:
            ValueError: If an invalid size string is provided.
            TypeError: If the size is not an int or a valid string.

        Returns:
            Self: The current instance of the Text class.
        """
        match size:
            case int():
                return size
            case str() as original_size:
                size = original_size.lower()
                if size in Fontsize.SIZE_MAPPING:
                    return Fontsize.SIZE_MAPPING[size]
                else:
                    raise ValueError(f"Invalid size '{original_size}'. Use 'S', 'M', 'L', 'XL'.")
            case _:
                raise TypeError("Font size must be an int or one of 'S', 'M', 'L', 'XL'.")
