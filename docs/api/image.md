# Class Image
A class representing an image element that can be loaded from various sources.
This class provides functionality to load and manipulate images from files, URLs,
or raw data (bytes/SVG). It supports basic image operations like scaling and
fitting within bounds while maintaining aspect ratio.
## Methods
### __init__
```python
    def __init__(self, defaults: Defaults, listener: AbstractImageListener, loader: AbstractImageLoader):
```
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

