# Class SceneBuilder
The SceneBuilder class provides methods to add various diagram elements.
The elemnts include rectangles, diamonds, ellipses, arrows, lines, text, images, groups, and frames.
Additionally, it offers serialization of the diagram to JSON and allows saving it to a file.
## Methods
### __init__
```python
    def __init__(self):
```
### arrow
```python
    def arrow(self, label: str | Text | None = None) -> Arrow:
```
Add an arrow element to the diagram.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `label` | `str  or  Text  or  None` | The text label for the arrow. |

#### Returns

**Type**: `Arrow`

The arrow element.

### background
```python
    def background(self, color: str) -> Self:
```
Set the background color of the diagram.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `color` | `str` | The background color. |

#### Returns

**Type**: `Self`

The current instance of the Excaligen class.

### color
```python
    def color(self) -> Color:
```
Create a color object.
It can be used as an argument for setting stroke and background colors.

#### Returns

**Type**: `Color`

The color object.

### defaults
```python
    def defaults(self) -> Defaults:
```
Retrieve the default parameters for elements.

#### Returns

**Type**: `Defaults`

The default parameteres for elements.

### diamond
```python
    def diamond(self, label: str | Text | None = None) -> Diamond:
```
Add a diamond element to the diagram.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `label` | `str  or  Text  or  None` | The text label for the diamond. |

#### Returns

**Type**: `Diamond`

The diamond element.

### ellipse
```python
    def ellipse(self, label: str | Text | None = None) -> Ellipse:
```
Add an ellipse element to the diagram.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `label` | `str  or  Text  or  None` | The text label for the ellipse. |

#### Returns

**Type**: `Ellipse`

The ellipse element.

### frame
```python
    def frame(self, title: str | None = None) -> Frame:
```
Add a frame element to the diagram.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `title` | `str  or  None` | The title of the frame. |

#### Returns

**Type**: `Frame`

The frame element.

### grid
```python
    def grid(self, size: int, step: int, enabled: bool) -> Self:
```
Set the grid properties for the diagram.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `size` | `int` | The size of the grid. |
| `step` | `int` | The step size of the grid. |
| `enabled` | `bool` | Whether the grid is enabled. |

#### Returns

**Type**: `Self`

The current instance of the Excaligen class.

### group
```python
    def group(self) -> Group:
```
Generate a group (virtual container).

#### Returns

**Type**: `Group`

The group container.

### image
```python
    def image(self) -> Image:
```
Add an image element to the diagram.

#### Returns

**Type**: `Image`

The image element.

### json
```python
    def json(self) -> str:
```
Serialize the diagram to a JSON string.

#### Returns

**Type**: `str`

The JSON representation of the diagram.

### line
```python
    def line(self) -> Line:
```
Add a line element to the diagram.

#### Returns

**Type**: `Line`

The line element.

### rectangle
```python
    def rectangle(self, label: str | Text | None = None) -> Rectangle:
```
Add a rectangle element to the diagram.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `label` | `str  or  Text  or  None` | The text label for the rectangle. |

#### Returns

**Type**: `Rectangle`

The rectangle element.

### save
```python
    def save(self, file: str) -> Self:
```
Save the current diagram to a file.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `file` | `str` | The path to the file where the diagram will be saved. |

#### Returns

**Type**: `Self`

The current instance of the Excaligen class.

### text
```python
    def text(self, text: str | None = None) -> Text:
```
Add a text element to the diagram.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `text` | `str  or  None` | The text string. |

#### Returns

**Type**: `Text`

The text element.

