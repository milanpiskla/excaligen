"""
Description: Helper for stroke input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Stroke:
    @staticmethod
    def from_(stroke: str) -> str:
        """
        Set the stroke style by string ('solid', 'dashed', 'dotted').

        Args:
            stroke (str): The stroke style to set, specified as a string ('solid', 'dashed', 'dotted').

        Raises:
            ValueError: If an invalid stroke style is provided.
        """

        match stroke:
            case "solid" | "dashed" | "dotted":
                return stroke
            case _:
                raise ValueError(f"Invalid value '{stroke}' for stroke style. Use 'solid', 'dashed', or 'dotted'.")