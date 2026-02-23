# Class Frame
A visual container that can hold other elements and automatically adjusts its size.
Frame is a fundamental layout component that serves as a container for other elements.
It can automatically calculate its dimensions based on its contents or be explicitly
sized. Frames can also have titles and background colors, making them useful for
grouping related elements and creating visual hierarchies in the layout.
> [!WARNING]
> Do not instantiate this class directly. Use `SceneBuilder.frame()` instead.
## Methods
### __init__
```python
    def __init__(self, defaults: Defaults, title: str | None = None):
```
Initialize self.  See help(type(self)) for accurate signature.

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
Get or set the center coordinates of the element.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `*args` | `None` | Supports two signatures: 1. center() -> tuple[float, float] Returns the (x, y) coordinates of the center. 2. center(x, y) -> Self Sets the center to (x, y) and returns self for chaining. |

#### Returns

**Type**: `tuple[float, float]  or  Self`

Depending on the arguments.

### elements
```python
    def elements(self, *elements: AbstractElement) -> Self:
```
Add elements to the frame and adjust the frame size accordingly.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `elements` | `AbstractElement` | The elements to add to the frame. |

#### Returns

**Type**: `Self`

The current instance of the Frame class.

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

### title
```python
    def title(self, title: str) -> Self:
```
Set the title of the frame.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `title` | `str` | The title of the frame. |

#### Returns

**Type**: `Self`

The current instance of the Frame class.

