# Class Text
A class representing text elements in excaligen.
The Text class is designed to handle and manipulate text elements within the excaligen
framework. It provides various text customization options including font styles, sizes,
alignments, and colors. The class supports auto-resizing capabilities and multiple font
families.
> [!WARNING]
> Do not instantiate this class directly. Use `SceneBuilder.text()` instead.
## Methods
### __init__
```python
    def __init__(self, defaults: Defaults, text: str | None = None):
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

### anchor
```python
    def anchor(self, x: float, y: float, align: str | None = None, baseline: str | None = None) -> Self:
```
Anchor the text element to a specific point (x, y).
It takes horizontal and vertical alignment into account.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `x` | `float` | The x-coordinate to anchor to. |
| `y` | `float` | The y-coordinate to anchor to. |
| `align` | `str  or  None, optional` | The horizontal alignment ('left', 'center', 'right'). |
| `baseline` | `str  or  None, optional` | The vertical alignment ('top', 'middle', 'bottom'). |

#### Returns

**Type**: `Self`

The current instance of the Text class.

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

### baseline
```python
    def baseline(self, baseline: str) -> Self:
```
Set the vertical text alignment (top, middle, bottom).

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `baseline` | `str` | The vertical alignment to set. |

#### Returns

**Type**: `Self`

The current instance of the Text class.

#### Raises

**ValueError**: If an invalid vertical alignment is provided.

### center
```python
    def center(self, *args) -> Self | tuple[float, float]:
```
Get or set the center coordinates of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `*args` | `None` | Supports two signatures: 1. center() -> tuple[float, float] Returns the (x, y) coordinates of the center. 2. center(x, y) -> Self Sets the center to (x, y) and returns self for chaining. |

#### Returns

**Type**: `tuple[float, float]  or  Self`

Depending on the arguments.

### color
```python
    def color(self, color: str | Color) -> Self:
```
Set the text color as #RRGGBB, color name or Color object.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `color` | `str  or  Color` | The color to set. |

#### Returns

**Type**: `Self`

The current instance of the Text class.

### content
```python
    def content(self, text: str) -> Self:
```
Set the text content and automatically calculate width and height.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `text` | `str` | The text content to set. |

#### Returns

**Type**: `Self`

The current instance of the Text class.

### font
```python
    def font(self, family: str) -> Self:
```
Set the font family ('Excalifont', 'Comic Shaans', 'Lilita One', 'Nunito', 'Hand-drawn', 'Normal', 'Code').

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `family` | `str` | The font family to set. |

#### Returns

**Type**: `Self`

The current instance of the Text class.

#### Raises

**ValueError**: If an invalid font family is provided.

### fontsize
```python
    def fontsize(self, size: int | str) -> Self:
```
Set the font size by int or by string ('S', 'M', 'L', 'XL').

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `size` | `int  or  str` | The font size to set. |

#### Returns

**Type**: `Self`

The current instance of the Text class.

#### Raises

**ValueError**: If an invalid size string is provided.

**TypeError**: If the size is not an int or a valid string.

### justify
```python
    def justify(self, x: float, y: float, width: float, height: float) -> Self:
```
Justify the text element within a rectangle defined by (x, y, width, height).

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `x` | `float` | The x-coordinate of the rectangle's top-left corner. |
| `y` | `float` | The y-coordinate of the rectangle's top-left corner. |
| `width` | `float` | The width of the rectangle. |
| `height` | `float` | The height of the rectangle. |

#### Returns

**Type**: `Self`

The current instance of the Text class.

### link
```python
    def link(self, target: "str | AbstractElement") -> Self:
```
Establishes a link to the given target, which can be either a string URL or an AbstractElement instance.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `target` | `str  or  AbstractElement` | The target to link to. If it's an AbstractElement, a URL will be generated using its ID. If it's a string, it will be used directly as the link. |

#### Returns

**Type**: `Self`

The instance of the current object with the updated link.

#### Raises

**ValueError**: If the target is neither a string nor an AbstractElement.

### opacity
```python
    def opacity(self, opacity: int) -> Self:
```
Set the opacity of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `opacity` | `int` | The opacity value to set, must be in the range 0-100. 100 is fully opaque, 0 is fully transparent. |

#### Returns

**Type**: `Self`

The instance of the element with updated opacity.

#### Raises

**ValueError**: If the opacity value is not within the range 0-100.

### orbit
```python
    def orbit(self, *args) -> Self:
```
Positions the element relative to a reference using polar coordinates.
This method allows placing the element such that its center will be at (radius, angle)
from a reference. The reference can be either another AbstractElement or a point (x, y).

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `*args` | `None` | Supports two signatures: 1. orbit(element, radius, angle) |
| `element` | `AbstractElement` | The reference element to orbit around. |
| `radius` | `float` | The distance from the center of the reference. |
| `angle` | `float` | The angle to position the element at, in radians. |

#### Returns

**Type**: `Self`

The instance of the element.

#### Raises

**ValueError**: If the arguments do not match the expected signatures.

### position
```python
    def position(self, x: float, y: float) -> Self:
```
Sets the position of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `x` | `float` | The x-coordinate of the element. |
| `y` | `float` | The y-coordinate of the element. |

#### Returns

**Type**: `Self`

The instance of the element with updated position.

### rotate
```python
    def rotate(self, angle: float) -> Self:
```
Rotate the element clockwise by a specified angle.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `angle` | `float` | The angle to rotate the element clockwise by, in radians. |

#### Returns

**Type**: `Self`

The instance of the element after rotation.

### size
```python
    def size(self, *args) -> Self | tuple[float, float]:
```
Get or set the size of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `*args` | `None` | Supports two signatures: 1. size() -> tuple[float, float] Returns the (width, height) of the element. 2. size(width, height) -> Self Sets the size to (width, height) and returns self for chaining. |

#### Returns

**Type**: `tuple[float, float]  or  Self`

Depending on the arguments.

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

