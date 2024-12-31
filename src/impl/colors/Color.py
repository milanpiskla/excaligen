"""
Description: Color class for handling RGB and HSL colors. Contains also a static method for parsing color strings.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

from typing import Self

class Color:
    _COLOR_NAMES = {
        "AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood",
        "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGrey",
        "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkSlateGrey",
        "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DimGrey", "DodgerBlue", "FireBrick", "FloralWhite", "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite",
        "Gold", "GoldenRod", "Gray", "Grey", "Green", "GreenYellow", "HoneyDew", "HotPink", "IndianRed", "Indigo", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen",
        "LemonChiffon", "LightBlue", "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGrey", "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen",
        "LightSkyBlue", "LightSlateGray", "LightSlateGrey", "LightSteelBlue", "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine", "MediumBlue",
        "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream", "MistyRose",
        "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed",
        "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue", "Purple", "RebeccaPurple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown",
        "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray", "SlateGrey", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle", "Tomato",
        "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke", "Yellow", "YellowGreen"
    }

    def __init__(self):
        self._r = 0
        self._g = 0
        self._b = 0

    def rgb(self, r: int, g: int, b: int) -> Self:
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("RGB values must be in the range 0-255.")
        self._r, self._g, self._b = r, g, b
        return self

    def hsl(self, h: int, s: int, l: int):
        if not (0 <= h <= 360 and 0 <= s <= 100 and 0 <= l <= 100):
            raise ValueError("HSL values must be in the range H: 0-360, S/L: 0-100.")
        c = (1 - abs(2 * l / 100 - 1)) * (s / 100)
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = l / 100 - c / 2

        match h:
            case h if 0 <= h < 60:
                r, g, b = c, x, 0
            case h if 60 <= h < 120:
                r, g, b = x, c, 0
            case h if 120 <= h < 180:
                r, g, b = 0, c, x
            case h if 180 <= h < 240:
                r, g, b = 0, x, c
            case h if 240 <= h < 300:
                r, g, b = x, 0, c
            case _:
                r, g, b = c, 0, x

        self._r, self._g, self._b = [round((v + m) * 255) for v in (r, g, b)]
        return self
    
    def __str__(self) -> str:
        return f"#{self._r:02X}{self._g:02X}{self._b:02X}"

    @staticmethod
    def _string(color: str) -> str:
        color = color.strip()
        if color.startswith("#"):
            if len(color) == 7 and all(c in "0123456789ABCDEFabcdef" for c in color[1:]):
                return color.upper()
            else:
                raise ValueError(f"Invalid hex color: {color}")
        for valid_color in Color._COLOR_NAMES:
            if color.casefold() == valid_color.casefold():
                return valid_color
        raise ValueError(f"Invalid color name: {color}")

    @staticmethod
    def from_input(input_color: "str | Color") -> str:
        match input_color:
            case Color() as color:
                return str(color)
            case str() as color_str:
                return Color._string(color_str)
            case _:
                raise TypeError("Invalid input type. Expected str or Color.")