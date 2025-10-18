"""
Description: Helper for opacity input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Opacity:
    @staticmethod
    def from_(opacity: int) -> int:
        """
        Set the opacity value ensuring it's between 0 and 100.

        Args:
            opacity (int): The opacity value to set, specified as an integer between 0 and 100.

        Raises:
            ValueError: If the opacity value is not between 0 and 100.
        """

        if 0 <= opacity <= 100:
            return opacity
        else:
            raise ValueError(f"Invalid value '{opacity}' for opacity. Use an integer between 0 and 100.")