"""
Description: Helper for thickness input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Thickness:
    @staticmethod
    def from_(thickness: int | str) -> int:
        """Parse thickness input and return corresponding stroke width.

        Args:
            thickness (int | str): The thickness to parse, specified as an integer (1, 2, 3) or a string ('thin', 'bold', 'extra-bold').

        Raises:
            ValueError: If an invalid thickness value is provided.

        Returns:
            int: The corresponding stroke width.
        """
        match thickness:
            case 1 | 2 | 3:
                return thickness
            case "thin":
                return 1
            case "bold":
                return 2
            case "extra-bold":
                return 4
            case _:
                raise ValueError(f"Invalid thickness '{thickness}'. Use 1, 2, 3 or 'thin', 'bold', or 'extra-bold'.")