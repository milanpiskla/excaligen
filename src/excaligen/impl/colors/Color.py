"""
Description: Color class for handling RGB and HSL colors. Contains also a static method for parsing color strings.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from typing import Self, overload


class Color:
    """ Color class for handling RGB and HSL colors. Contains also a static method for parsing color strings.
    The following color names are supported (case insensitive):
    ```
    AliceBlue, AntiqueWhite, Aqua, Aquamarine, Azure, Beige,
    Bisque, Black, BlanchedAlmond, Blue, BlueViolet, Brown, BurlyWood,
    CadetBlue, Chartreuse, Chocolate, Coral, CornflowerBlue, Cornsilk, Crimson, Cyan,
    DarkBlue, DarkCyan, DarkGoldenRod, DarkGray, DarkGrey, DarkGreen, DarkKhaki, DarkMagenta, DarkOliveGreen, DarkOrange, DarkOrchid, DarkRed, DarkSalmon, DarkSeaGreen, DarkSlateBlue, DarkSlateGray, DarkSlateGrey, DarkTurquoise, DarkViolet, DeepPink, DeepSkyBlue, DimGray, DimGrey, DodgerBlue,
    FireBrick, FloralWhite, ForestGreen, Fuchsia,
    Gainsboro, GhostWhite, Gold, GoldenRod, Gray, Grey, Green, GreenYellow, 
    HoneyDew, HotPink,
    IndianRed, Indigo, Ivory, 
    Khaki, 
    Lavender, LavenderBlush, LawnGreen, LemonChiffon, LightBlue, LightCoral, LightCyan, LightGoldenRodYellow, LightGray, LightGrey, LightGreen, LightPink, LightSalmon, LightSeaGreen, LightSkyBlue, LightSlateGray, LightSlateGrey, LightSteelBlue, LightYellow, Lime, LimeGreen, Linen,
    Magenta, Maroon, MediumAquaMarine, MediumBlue, MediumOrchid, MediumPurple, MediumSeaGreen, MediumSlateBlue, MediumSpringGreen, MediumTurquoise, MediumVioletRed, MidnightBlue, MintCream, MistyRose, Moccasin,
    NavajoWhite, Navy,
    OldLace, Olive, OliveDrab, Orange, OrangeRed, Orchid,
    PaleGoldenRod, PaleGreen, PaleTurquoise, PaleVioletRed, PapayaWhip, PeachPuff, Peru, Pink, Plum, PowderBlue, Purple,
    RebeccaPurple, Red, RosyBrown, RoyalBlue, 
    SaddleBrown, Salmon, SandyBrown, SeaGreen, SeaShell, Sienna, Silver, SkyBlue, SlateBlue, SlateGray, SlateGrey, Snow, SpringGreen, SteelBlue,
    Tan, Teal, Thistle, Tomato, Transparent, Turquoise,
    Violet,
    Wheat, White, WhiteSmoke,
    Yellow, YellowGreen
    ```
    """
    _COLOR_NAMES = {
        "AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure",
        "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood",
        "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan",
        "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGrey",
        "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkSlateGrey", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DimGrey", "DodgerBlue",
        "FireBrick", "FloralWhite", "ForestGreen", "Fuchsia",
        "Gainsboro", "GhostWhite", "Gold", "GoldenRod", "Gray", "Grey", "Green", "GreenYellow",
        "HoneyDew", "HotPink",
        "IndianRed", "Indigo", "Ivory",
        "Khaki",
        "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGrey", "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen", "LightSkyBlue", "LightSlateGray", "LightSlateGrey", "LightSteelBlue", "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine", "MediumBlue",
        "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream", "MistyRose", "Moccasin",
        "NavajoWhite", "Navy",
        "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed", "Orchid",
        "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue", "Purple",
        "RebeccaPurple", "Red", "RosyBrown", "RoyalBlue",
        "SaddleBrown", "Salmon", "SandyBrown", "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray", "SlateGrey", "Snow", "SpringGreen", "SteelBlue",
        "Tan", "Teal", "Thistle", "Tomato", "Transparent", "Turquoise",
        "Violet",
        "Wheat", "White", "WhiteSmoke",
        "Yellow", "YellowGreen"
    }

    def __init__(self):
        self._r = 0
        self._g = 0
        self._b = 0

    @overload
    def rgb(self, r: int, g: int, b: int) -> Self: ...

    @overload
    def rgb(self, hex: str) -> Self: ...

    @overload
    def rgb(self) -> tuple[int, int, int]: ...

    def rgb(self, *args) -> "Self | tuple[int, int, int]":
        """ 
        Sets the color using RGB values, or returns the current RGB values if no arguments are provided.
        """
        match args:
            case ():
                return (self._r, self._g, self._b)
            case (int(r), int(g), int(b)):
                if not Color._is_valid_rgb(r, g, b):
                    raise ValueError("RGB values must be in the range 0-255.")
                self._r, self._g, self._b = r, g, b
                return self
            case (str(hex_str),):
                self._r, self._g, self._b = Color._hex_to_rgb(hex_str)
                return self
            case _:
                raise TypeError("Invalid arguments for rgb(). Expected (r, g, b) or ().")

    @overload
    def hsl(self, h: int, s: int, l: int) -> Self: ...

    @overload
    def hsl(self) -> tuple[int, int, int]: ...

    def hsl(self, *args) -> "Self | tuple[int, int, int]":
        """ 
        Sets the color using HSL values, or returns the current HSL values if no arguments are provided. 
        """
        match args:
            case ():
                return Color.rgb_to_hsl(self._r, self._g, self._b)
            case (int(h), int(s), int(l)):
                if not Color._is_valid_hsl(h, s, l):
                    raise ValueError("HSL values must be in the range H: 0-360, S/L: 0-100.")
                r, g, b = Color.hsl_to_rgb(h, s, l)
                self._r, self._g, self._b = r, g, b
                return self
            case _:
                raise TypeError("Invalid arguments for hsl(). Expected (h, s, l) or ().")
    

    def lighten(self, percent: int) -> "Self":
        """ 
        Lightens the color by a given percentage. 
        percent should be an integer between 0 and 100.
        Calculation is absolute: new_lightness = current_lightness + percent
        """
        if not 0 <= percent <= 100:
            raise ValueError("Percentage must be between 0 and 100.")

        h, s, l = self.hsl()
        return self.hsl(h, s, min(l + percent, 100))

    def darken(self, percent: int) -> "Self":
        """ 
        Darkens the color by a given percentage. 
        percent should be an integer between 0 and 100.
        Calculation is absolute: new_lightness = current_lightness - percent
        """
        if not 0 <= percent <= 100:
            raise ValueError("Percentage must be between 0 and 100.")

        h, s, l = self.hsl()
        return self.hsl(h, s, max(l - percent, 0))
    
    @staticmethod
    def rgb_to_hsl(r: int, g: int, b: int) -> tuple[int, int, int]:
        """ Converts RGB values to HSL. """
        if not Color._is_valid_rgb(r, g, b):
            raise ValueError("RGB values must be in the range 0-255.")
        r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
        c_max = max(r_norm, g_norm, b_norm)
        c_min = min(r_norm, g_norm, b_norm)
        delta = c_max - c_min

        l = (c_max + c_min) / 2

        if delta == 0:
            h = 0
            s = 0
        else:
            s = delta / (1 - abs(2 * l - 1))
            if c_max == r_norm:
                h = ((g_norm - b_norm) / delta) % 6
            elif c_max == g_norm:
                h = (b_norm - r_norm) / delta + 2
            else:
                h = (r_norm - g_norm) / delta + 4
            h *= 60

        return (round(h), round(s * 100), round(l * 100))

    @staticmethod
    def hsl_to_rgb(h: int, s: int, l: int) -> tuple[int, int, int]:
        """ Converts HSL values to RGB. """
        if not Color._is_valid_hsl(h, s, l):
            raise ValueError("HSL values must be in the range H: 0-360, S/L: 0-100.")
        
        c = (1 - abs(2 * l / 100 - 1)) * (s / 100)
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = l / 100 - c / 2

        match h:
            case h if 0 <= h < 60:
                r_temp, g_temp, b_temp = c, x, 0
            case h if 60 <= h < 120:
                r_temp, g_temp, b_temp = x, c, 0
            case h if 120 <= h < 180:
                r_temp, g_temp, b_temp = 0, c, x
            case h if 180 <= h < 240:
                r_temp, g_temp, b_temp = 0, x, c
            case h if 240 <= h < 300:
                r_temp, g_temp, b_temp = x, 0, c
            case _:
                r_temp, g_temp, b_temp = c, 0, x

        return (round((r_temp + m) * 255), round((g_temp + m) * 255), round((b_temp + m) * 255))
    
    def __str__(self) -> str:
        return f"#{self._r:02X}{self._g:02X}{self._b:02X}"

    @staticmethod
    def _string(color: str) -> str:
        color = color.strip()
        if color.startswith("#"):
            if Color._is_valid_hex_color(color):
                return color.upper()
            else:
                raise ValueError(f"Invalid hex color: {color}")
        for valid_color in Color._COLOR_NAMES:
            if color.casefold() == valid_color.casefold():
                return valid_color
        raise ValueError(f"Invalid color name: {color}")

    @staticmethod
    def from_(input_color: "str | Color") -> str:
        """ Converts input color to string representation. Accepts either a Color instance or a string. """
        match input_color:
            case Color() as color:
                return str(color)
            case str() as color_str:
                return Color._string(color_str)
            case _:
                raise TypeError("Invalid input type. Expected str or Color.")

    @staticmethod
    def _hex_to_rgb(hex: str) -> tuple[int, int, int]:
        """ Converts hex color to RGB. """
        if not Color._is_valid_hex_color(hex):
            raise ValueError(f"Invalid hex color: {hex}")
        return (int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16))

    @staticmethod
    def _is_valid_hex_color(hex: str) -> bool:
        """ Checks if a hex color is valid. """
        return len(hex) == 7 and all(c in "0123456789ABCDEFabcdef" for c in hex[1:])

    @staticmethod
    def _is_valid_rgb(r: int, g: int, b: int) -> bool:
        """ Checks if RGB values are valid. """
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    @staticmethod
    def _is_valid_hsl(h: int, s: int, l: int) -> bool:
        """ Checks if HSL values are valid. """
        return 0 <= h <= 360 and 0 <= s <= 100 and 0 <= l <= 100