# Class Image
A class representing an image element that can be loaded from various sources.
This class provides functionality to load and manipulate images from files, URLs,
or raw data (bytes/SVG). It supports basic image operations like scaling and
fitting within bounds while maintaining aspect ratio.
> [!WARNING]
> Do not instantiate this class directly. Use `SceneBuilder.image()` instead.
## Methods
### __init__
```python
    def __init__(self, defaults: Defaults, listener: AbstractImageListener, loader: AbstractImageLoader):
```
Initialize self.  See help(type(self)) for accurate signature.

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

### data
```python
    def data(self, data: bytes | str) -> Self:
```
Set image data from raw bytes or SVG string.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `data` | `bytes  or  str` | The raw image data or SVG string. |

#### Returns

**Type**: `Self`

The current instance of the Image class.

### file
```python
    def file(self, path: str) -> Self:
```
Load image data from a file and set it.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `path` | `str` | The path to the image file. |

#### Returns

**Type**: `Self`

The current instance of the Image class.

### fit
```python
    def fit(self, max_width: float, max_height: float) -> Self:
```
Scale the image to fit within a bounding box while maintaining aspect ratio.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `max_width` | `float` | The maximum width of the bounding box. |
| `max_height` | `float` | The maximum height of the bounding box. |

#### Returns

**Type**: `Self`

The current instance of the Image class.

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

### url
```python
    def url(self, url: str) -> Self:
```
Load image data from a URL and set it.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `url` | `str` | The URL to the image. |

#### Returns

**Type**: `Self`

The current instance of the Image class.

