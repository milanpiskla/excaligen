"""
Description: Helper for the horizontal text alignment input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Align:
    @staticmethod
    def from_(align: str) -> str:
        """
        Set the horizontal text alignment.

        Args:
            align (str): The horizontal text alignment to be applied. Must be one of 'left', 'center', or 'right'.

        Raises:
            ValueError: If the provided align is not one of 'left', 'center', or 'right'.
        """

        match align:
            case "left" | "center" | "right":
                return align
            case _:
                raise ValueError(f"Invalid horizontal text alignment '{align}'. Use 'left', 'center', or 'right'.")