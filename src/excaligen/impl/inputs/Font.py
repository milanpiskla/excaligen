"""
Description: Helper for the font input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Font:
    FONT_MAPPING = {
        "hand-drawn": 1,
        "normal": 2,
        "code": 3,
        "excalifont": 5,
        "comic-shaans": 8,
        "lilita-one": 7,
        "nunito": 6
    }

    @staticmethod
    def from_(family: str) -> int:
        """
        Set the font by string.

        Args:
            family (str): The font family to set. Acceptable values are:
                 - "Hand-drawn"
                 - "Normal"
                 - "Code"
                 - "Excalifont"
                 - "Comic-shaans"
                 - "Lilita-one"
                 - "Nunito"

        Raises:
            ValueError: If an invalid font value is provided.
        """
        family = family.lower().replace(" ", "-")
        if family in Font.FONT_MAPPING:
            return Font.FONT_MAPPING[family]
        else:
            raise ValueError(f"Invalid font '{family}'. Use one of {list(Font.FONT_MAPPING.keys())}.")
                
