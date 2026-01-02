# Class Line
A line element that draws a straight or curved line segments between the given points.
This class represents a line element in the drawing canvas.
It provides functionality for creating and manipulating straight pr curved lines with specified
configurations for styling and positioning.
## Methods
### __init__
```python
    def __init__(self, defaults: Defaults):
```
### background
```python
    def background(self, color: str | Color) -> Self:
```
Set the background (fill) color of the shape created by a closed line segments.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `color` | `str  or  Color` | The background color, specified as a hex string (#RRGGBB), a color name, or a Color object. |

#### Returns

**Type**: `Self`

The instance of the class for method chaining.

### center
```python
    def center(self, x: float, y: float) -> Self:
```
Centers the element at the given (x, y) coordinates.
This method sets the element's position such that its center is located
at the specified (x, y) coordinates. It also marks the element as centered.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `x` | `float` | The x-coordinate to center the element. |
| `y` | `float` | The y-coordinate to center the element. |

#### Returns

**Type**: `Self`

The instance of the element, allowing for method chaining.

### close
```python
    def close(self):
```
Close the line by connecting the last point to the first point.

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
Set the fill style for the shape created by a closed line segments.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `style` | `str` | The fill style to be applied. Must be one of 'hatchure', 'cross-hatch', or 'solid'. |

#### Returns

**Type**: `Self`

The instance of the shape with the updated fill style.

#### Raises

**ValueError**: If the provided style is not one of 'hatchure', 'cross-hatch', or 'solid'.

### get_center
```python
    def get_center(self) -> tuple[float, float]:
```
Calculate and return the center coordinates of the element.

#### Returns

**Type**: `tuple[float, float]`

A tuple containing the x and y coordinates of the center of the element.

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

### points
```python
    def points(self, points: list[Point]) -> Self:
```
Sets the points for the line and calculates the width and height.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `points` | `list[Point]` | A list of Point objects representing the coordinates of the line. Returns: Self: The instance of the class with updated points, width, and height. |

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

### roundness
```python
    def roundness(self, roundness: str) -> Self:
```
Set the roundness style of the shape.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `roundness` | `str` | The roundness style to set. Acceptable values are: - "sharp": Sets the shape to have sharp corners. - "round": Sets the shape to have rounded corners. |

#### Returns

**Type**: `Self`

The instance of the shape with the updated roundness style.

#### Raises

**ValueError**: If the provided roundness style is not "sharp" or "round".

### size
```python
    def size(self, width: float, height: float) -> Self:
```
Set the size of the shape.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `width` | `float` | The width of the shape. |
| `height` | `float` | The height of the shape. |

#### Returns

**Type**: `Self`

The instance of the shape with the updated size.

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

