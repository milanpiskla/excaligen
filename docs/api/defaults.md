# Class Defaults
A class to hold default values for various element properties.
This class provides a centralized way to manage default settings for elements/
The initial values are:
```
size(130, 80)
opacity(100)
rotate(0)
sloppiness('artist')
roundness('round')
stroke('solid')
thickness(1)
color('#000000')
background('transparent')
fill('hachure')
fontsize(16)
font('Hand drawn')
align('center')
baseline('middle')
autoresize(True)
spacing(1.25)
arrowheads(None, 'arrow')
```
## Methods
### __init__
```python
    def __init__(self):
```
### align
```python
    def align(self, align: str) -> Self:
```
Set the horizontal text alignment (left, center, right).

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `align` | `str` | The horizontal alignment to set. |

#### Returns

**Type**: `Self`

The current instance of the Text class.

#### Raises

**ValueError**: If an invalid alignment is provided.

### arrowheads
```python
    def arrowheads(self, start: str | None, end: str | None) -> Self:
```
Set the arrowhead styles for the start and end of the arrow.
Valid arrowheads values are None, 'arrow', 'bar', 'dot' and 'triangle'.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `start` | `str, optional` | The style of the start arrowhead. |
| `end` | `str, optional` | The style of the end arrowhead. |

#### Returns

**Type**: `Self`

The current instance of the Arrow class.

#### Raises

**ValueError**: If an invalid arrowhead style is provided.

### autoresize
```python
    def autoresize(self, enabled: bool) -> Self:
```
Enable or disable automatic text box resizing.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `enabled` | `bool` | Whether to enable automatic resizing. |

#### Returns

**Type**: `Self`

The current instance of the Text class.

### background
```python
    def background(self, color: str | Color) -> Self:
```
Sets the background color of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `color` | `str  or  Color` | The background color, specified as a hex string (#RRGGBB), a color name, or a Color object. |

#### Returns

**Type**: `Self`

The instance defaults with updated background color.

### baseline
```python
    def baseline(self, align: str) -> Self:
```
Set the vertical text alignment (top, middle, bottom).

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `align` | `str` | The vertical alignment to set. |

#### Returns

**Type**: `Self`

The current instance of the Text class.

#### Raises

**ValueError**: If an invalid vertical alignment is provided.

### color
```python
    def color(self, color: str | Color) -> Self:
```
Set the stroke (outline) color as #RRGGBB, color name or Color object.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `color` | `str  or  Color` | The color to set, specified as a hex string $RRGGBB, color name, or Color object. |

#### Returns

**Type**: `Self`

The current instance of the AbstractStrokedElement class.

### fill
```python
    def fill(self, style: str) -> Self:
```
Sets the fill style of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `style` | `str` | The fill style to be applied. Must be one of 'hatchure', 'cross-hatch', or 'solid'. |

#### Returns

**Type**: `Self`

The instance defaults with updated fill style.

### font
```python
    def font(self, family: str) -> Self:
```
Sets the font family of the text element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `family` | `str` | The font family to set, specified as a string ('Excalifont', 'Comic Shaans', 'Lilita One', 'Nunito', 'Hand-drawn', 'Normal', 'Code'). |

#### Returns

**Type**: `Self`

The instance defaults with updated font family.

### fontsize
```python
    def fontsize(self, size: int | str) -> Self:
```
Sets the font size of the text element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `size` | `int  or  str` | The font size to set, specified as an integer (e.g., 12, 14, 16) or a string ('small', 'medium', 'large'). |

#### Returns

**Type**: `Self`

The instance defaults with updated font size.

### opacity
```python
    def opacity(self, opacity: int) -> Self:
```
Sets the opacity of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `opacity` | `int` | The opacity of the element (0-100). |

#### Returns

**Type**: `Self`

The instance defaults with updated opacity.

#### Raises

**ValueError**: If the opacity value is not within the range 0-100.

### rotate
```python
    def rotate(self, angle: float) -> Self:
```
Sets the rotation angle of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `angle` | `float` | The rotation angle in radians. |

#### Returns

**Type**: `Self`

The instance defaults with updated angle.

### roundness
```python
    def roundness(self, roundness: str) -> Self:
```
Sets the roundness style of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `roundness` | `str` | The roundness style to set. Acceptable values are: - "sharp": Sets the shape to have sharp corners. - "round": Sets the shape to have rounded corners. Returns: Self: The instance defaults with updated roundness style. |

### size
```python
    def size(self, width: float, height: float) -> Self:
```
Sets the size of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `width` | `float` | The width of the element. |
| `height` | `float` | The height of the element. |

#### Returns

**Type**: `Self`

The instance defaults with updated size.

### sloppiness
```python
    def sloppiness(self, sloppiness: int | str) -> Self:
```
Sets the sloppiness of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `sloppiness` | `int  or  str` | The sloppiness value to set, specified as an integer (0, 1, 2) or a string ('architect', 'artist', 'cartoonist'). |

#### Returns

**Type**: `Self`

The instance defaults with updated sloppiness.

### spacing
```python
    def spacing(self, height: float) -> Self:
```
Set the line height manually.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `height` | `float` | The line height to set. |

#### Returns

**Type**: `Self`

The current instance of the Text class.

### stroke
```python
    def stroke(self, style: str) -> Self:
```
Sets the stroke style of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `stroke` | `str` | The stroke style to set, specified as a string ('solid', 'dashed', 'dotted'). |

#### Returns

**Type**: `Self`

The instance defaults with updated stroke style.

### thickness
```python
    def thickness(self, thickness: int | str) -> Self:
```
Sets the stroke thickness of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `thickness` | `int  or  str` | The thickness to set, specified as an integer (1, 2, 3) or a string ('thin', 'bold', 'extra-bold'). |

#### Returns

**Type**: `Self`

The instance defaults with updated stroke thickness.

