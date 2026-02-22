# Class Color
Color class for handling RGB and HSL colors. Contains also a static method for parsing color strings.
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
## Methods
### __init__
```python
    def __init__(self):
```
Initialize self.  See help(type(self)) for accurate signature.

### darken
```python
    def darken(self, percent: int) -> "Self":
```
Darkens the color by a given percentage.
percent should be an integer between 0 and 100.
Calculation is absolute: new_lightness = current_lightness - percent

### from_
```python
    def from_(input_color: "str | Color") -> str:
```
Converts input color to string representation. Accepts either a Color instance or a string.

### hsl
```python
    def hsl(self, *args) -> "Self | tuple[int, int, int]":
```
Sets the color using HSL values, or returns the current HSL values if no arguments are provided.

### hsl_to_rgb
```python
    def hsl_to_rgb(h: int, s: int, l: int) -> tuple[int, int, int]:
```
Converts HSL values to RGB.

### lighten
```python
    def lighten(self, percent: int) -> "Self":
```
Lightens the color by a given percentage.
percent should be an integer between 0 and 100.
Calculation is absolute: new_lightness = current_lightness + percent

### rgb
```python
    def rgb(self, *args) -> "Self | tuple[int, int, int]":
```
Sets the color using RGB values, or returns the current RGB values if no arguments are provided.

### rgb_to_hsl
```python
    def rgb_to_hsl(r: int, g: int, b: int) -> tuple[int, int, int]:
```
Converts RGB values to HSL.

