# Class Group
A container class that represents a group of elements.
This class allows for organizing and managing multiple elements as a single unit. Elements
within a group can be manipulated together while maintaining their individual properties.
Each group is identified by a unique UUID.
> [!WARNING]
> Do not instantiate this class directly. Use `SceneBuilder.group()` instead.
## Methods
### __init__
```python
    def __init__(self, defaults: Defaults):
```
Initialize self.  See help(type(self)) for accurate signature.

### elements
```python
    def elements(self, *elements: Element) -> Self:
```
Add elements to the group.

#### Arguments

| Name | Type | Description |
|------|------|-------------|
| `elements` | `Element` | The elements to add to the group. |

#### Returns

**Type**: `Self`

The current instance of the Group class.

