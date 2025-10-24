"""
Description: Helper for roundness input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Roundness:
    @staticmethod
    def from_(roundness: str) -> str | dict | None:
        """
        Set the roundness by string ('sharp', 'round') or by dict.

        Args:
            roundness (str): The roundness style to set. Acceptable values are:
                 - "sharp": Sets the shape to have sharp corners.
                 - "round": Sets the shape to have rounded corners.
        Raises:
            ValueError: If an invalid roundness value is provided.
        """

        match roundness:
            case "sharp":
                return None
            case "round":
                return { "type": 3 }
            case _:
                raise ValueError(f"Invalid roundness '{roundness}'. Use 'sharp', or 'round'.")