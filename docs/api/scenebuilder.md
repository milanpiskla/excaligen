# Class SceneBuilder
The SceneBuilder class provides methods to add various diagram elements.
The elemnts include rectangles, diamonds, ellipses, arrows, lines, text, images, groups, and frames.
Additionally, it offers serialization of the diagram to JSON and allows saving it to a file.
The fluent API allows chaining method calls for a more concise code.
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

The [Arrow](arrow.md) element.

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

The [Color](color.md) object.

### defaults
```python
    def defaults(self) -> Defaults:
```
Retrieve the default parameters for elements.

#### Returns

**Type**: `Defaults`

The [Defaults](defaults.md) parameters for elements.

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

The [Diamond](diamond.md) element.

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

The [Ellipse](ellipse.md) element.

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

The [Frame](frame.md) element.

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

The [Group](group.md) container.

### image
```python
    def image(self) -> Image:
```
Add an image element to the diagram.

#### Returns

**Type**: `Image`

The [Image](image.md) element.

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

The [Line](line.md) element.

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

The [Rectangle](rectangle.md) element.

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

The [Text](text.md) element.

