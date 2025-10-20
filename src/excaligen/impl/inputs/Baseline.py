"""
Description: Helper for the vertical text alignment input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Baseline:
    @staticmethod
    def from_(align: str) -> str:
        """
        Set the vertical text alignment.

        Args:
            align (str): The vertical text alignment to be applied. Must be one of 'top', 'middle', or 'bottom'.

        Raises:
            ValueError: If the provided align is not one of 'top', 'middle', or 'bottom'.
        """

        match align:
            case "top" | "middle" | "bottom":
                return align
            case _:
                raise ValueError(f"Invalid value '{align}' for vertical text alignment. Use 'top', 'middle', or 'bottom'.")