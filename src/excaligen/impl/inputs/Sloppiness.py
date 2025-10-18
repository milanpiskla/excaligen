"""
Description: Helper for roughness input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Sloppiness:
    @staticmethod
    def from_(sloppiness: int | str) -> str | float | None:
        """
        Set the sloppiness by int (0, 1, 2) or by string ('architect', 'artist', 'cartoonist').

        Args:
            value (int | str): The sloppiness value to set, specified as an integer (0, 1, 2) or a string ('architect', 'artist', 'cartoonist').

        Raises:
            ValueError: If an invalid sloppiness value is provided.
        """

        match sloppiness:
            case 0 | 1 | 2:
                return sloppiness
            case "architect":
                return 0
            case "artist":
                return 1
            case "cartoonist":
                return 2
            case _:
                raise ValueError(f"Invalid value '{sloppiness}' for sloppiness. Use 0, 1, 2 or 'architect', 'artist', 'cartoonist'.")
