# Class Arrow
A class representing an arrow element in Excalidraw with various connection styles.
It creates arrow elements that can connect different elements
in various ways including straight lines, curves, arcs and elbowed connections. It supports
customizable arrowheads, gaps between connected elements, and different binding behaviors.
The arrow can be styled with:
- Different connection types (straight, arc, curve, elbow)
- Customizable start and end arrowheads
- Adjustable gaps between connected elements
- Binding capabilities to connect elements
- Various arrow directions and angles
> [!WARNING]
> Do not instantiate this class directly. Use `SceneBuilder.arrow()` instead.
## Methods
### __init__
```python
    def __init__(self, defaults: Defaults, listener: AbstractPlainLabelListener, label: str | Text | None = None) -> None:
```
Initialize self.  See help(type(self)) for accurate signature.

### append
```python
    def append(self, points: list[Point]) -> Self:
```
Appends points to the line.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `points` | `list[Point]` | A list of Point objects to append. Returns: Self: The instance of the class with updated points, width, and height. |

### arc
```python
    def arc(self, radius: float) -> Self:
```
Approximate an arc between the bound elements with the given radius.
The center of the arc is determined by the radius and the positions of the bound elements
by assuming the center of the start element and the center of the end element are oriented clockwise.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `radius` | `float` | The radius of the arc. |

#### Returns

**Type**: `Self`

The current instance of the Arrow class.

### arrowheads
```python
    def arrowheads(self, start: str | None = None, end: str | None = 'arrow') -> Self:
```
Set the arrowhead styles for the start and end of the arrow.
Valid arrowheads values are None, 'arrow', 'bar', 'dot' and 'triangle'.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `start` | `str, optional` | The style of the start arrowhead. Defaults to None. |
| `end` | `str, optional` | The style of the end arrowhead. Defaults to 'arrow'. |

#### Returns

**Type**: `Self`

The current instance of the Arrow class.

#### Raises

**ValueError**: If an invalid arrowhead style is provided.

### bind
```python
    def bind(self, start: AbstractElement, end: AbstractElement) -> Self:
```
Bind the arrow between two elements, supporting different connection styles.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `start` | `AbstractElement` | The start element. |
| `end` | `AbstractElement` | The end element. |

#### Returns

**Type**: `Self`

The current instance of the Arrow class.

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
Set the stroke (outline) color as #RRGGBB, color name or Color object.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `color` | `str  or  Color` | The color to set, specified as a hex string $RRGGBB, color name, or Color object. |

#### Returns

**Type**: `Self`

The current instance of the AbstractStrokedElement class.

### curve
```python
    def curve(self, start_angle: float | str, end_angle: float | str) -> Self:
```
Generate a curve between the bound elements using the given start and end tangent angles.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `start_angle` | `float  or  str` | The start tangent angle. It's either float value in radians or one of the strings 'L', 'R', 'U', 'D', representing left, right, up, or down respectively. |
| `end_angle` | `float  or  str` | The end tangent angle. It's either float value in radians or one of the strings 'L', 'R', 'U', 'D', representing left, right, up, or down respectively. |

#### Returns

**Type**: `Self`

The current instance of the Arrow class.

### elbow
```python
    def elbow(self, start_direction: str, end_direction: str) -> Self:
```
Set the arrow to have an elbow (right-angle turn).

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `start_direction` | `str` | The direction of the start elbow. It's one of the strings 'L', 'R', 'U', 'D', representing left, right, up, or down respectively. |
| `end_direction` | `str` | The direction of the end elbow. It's one of the strings 'L', 'R', 'U', 'D', representing left, right, up, or down respectively. |

#### Returns

**Type**: `Self`

The current instance of the Arrow class.

### gap
```python
    def gap(self, gap: float, end_gap: float | None = None) -> Self:
```
Set the gap at the start and end of the arrow.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `gap` | `float` | The gap at the start of the arrow. |
| `end_gap` | `float, optional` | The gap at the end of the arrow. Defaults to the value of `gap`. |

#### Returns

**Type**: `Self`

The current instance of the Arrow class.

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

### points
```python
    def points(self, points: list[Point]) -> Self:
```
Set the points of the arrow.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `points` | `list[Point]` | The points of the arrow. |

#### Returns

**Type**: `Self`

The current instance of the Arrow class.

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

### prepend
```python
    def prepend(self, points: list[Point]) -> Self:
```
Prepends points to the line.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `points` | `list[Point]` | A list of Point objects to prepend. Returns: Self: The instance of the class with updated points, width, and height. |

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

