# Class Ellipse
A class representing an elliptical shape element.
This class extends both AbstractStrokedElement and AbstractShape to create an
ellipse element that can be rendered with stroke properties. The ellipse
is defined by its center point and two radii (rx and ry).
> [!WARNING]
> Do not instantiate this class directly. Use `SceneBuilder.ellipse()` instead.
## Methods
### __init__
```python
    def __init__(self, defaults: Defaults, listener: AbstractPlainLabelListener, label: str | Text | None = None):
```
### background
```python
    def background(self, color: str | Color) -> Self:
```
Set the background (fill) color.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `color` | `str  or  Color` | The background color, specified as a hex string (#RRGGBB), a color name, or a Color object. |

#### Returns

**Type**: `Self`

The instance of the class for method chaining.

### center
```python
    def center(self, *args) -> Self | tuple[float, float]:
```
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
Set the fill style for the shape.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `style` | `str` | The fill style to be applied. Must be one of 'hachure', 'cross-hatch', or 'solid'. |

#### Returns

**Type**: `Self`

The instance of the shape with the updated fill style.

#### Raises

**ValueError**: If the provided style is not one of 'hachure', 'cross-hatch', or 'solid'.

### label
```python
    def label(self, text: Text | str) -> Self:
```
Set the label text for the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `text` | `Text  or  str` | The text element to set as the label or plain text. |

#### Returns

**Type**: `Self`

The current instance of the class.

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
    def size(self, width: float, height: float) -> Self:
```
Set the size of the ellipse.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `width` | `float` | The width of the ellipse. |
| `height` | `float` | The height of the ellipse. |

#### Returns

**Type**: `Self`

The instance of the ellipse with the updated size.

### sloppiness
```python
    def sloppiness(self, value: int | str) -> Self:
```
Set the stroke sloppiness by int (0, 1, 2) or by string ('architect', 'artist', 'cartoonist').

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `value` | `int  or  str` | The sloppiness value to set, specified as an integer (0, 1, 2) or a string ('architect', 'artist', 'cartoonist'). |

#### Returns

**Type**: `Self`

The current instance of the AbstractStrokedElement class.

#### Raises

**ValueError**: If an invalid sloppiness value is provided.

### stroke
```python
    def stroke(self, style: str) -> Self:
```
Set the stroke style (solid, dotted, dashed).

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `style` | `str` | The stroke style to set, specified as 'solid', 'dotted', or 'dashed'. |

#### Returns

**Type**: `Self`

The current instance of the AbstractStrokedElement class.

#### Raises

**ValueError**: If an invalid stroke style is provided.

### thickness
```python
    def thickness(self, thickness: int | str) -> Self:
```
Set the stroke thickness by int (1, 2, 3) or by string ('thin', 'bold', 'extra-bold').

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `thickness` | `int  or  str` | The thickness to set, specified as an integer (1, 2, 3) or a string ('thin', 'bold', 'extra-bold'). |

#### Returns

**Type**: `Self`

The current instance of the AbstractStrokedElement class.

#### Raises

**ValueError**: If an invalid thickness value is provided.

