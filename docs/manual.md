# Excaligen User Manual

If you appreciate the aesthetic of Excalidraw but require capabilities beyond simple manual drafting, Excaligen offers a bridge between code and visual expression.

It allows you to generate Excalidraw-compatible files directly from Python, enabling the visualization of data structures, automated reports, and complex algorithmic patterns with minimal boilerplate.

---

## Chapter 1: The First Sketch

We begin with the essential `SceneBuilder`.

Create a file named `hello_world.py`:

```python
from excaligen.SceneBuilder import SceneBuilder

scene = SceneBuilder()
scene.text("Hello, World!")
scene.save("hello_world.excalidraw")
```

Executing this script produces a file ready for Excalidraw. It is that straightforward.

---

## Chapter 2: Shapes & Styles

Excalidraw is known for its hand-drawn feel. Excaligen gives you full control over this aesthetic.

### Elemental Shapes
Add fundamental geometry with ease:

```python
scene.rectangle().label("Box")
scene.ellipse().label("Circle")
scene.diamond().label("Decision")
```

### The Art of Styling
You are not limited to defaults. Customize every aspect:

- **Stroke**: `solid`, `dashed`, or `dotted`.
- **Fill**: `solid`, `hachure`, or `cross-hatch`.
- **Thickness**: `thin` (1), `bold` (2), or `extra-bold` (3).
- **Fonts**: `Hand-drawn`, `Normal`, `Code`, and more.

```python
scene.rectangle().stroke("dashed").fill("cross-hatch").thickness(2)
scene.text("Code Font").font("Code")
```

### Colors
Express with precision using:
- **Named Colors**: `"MidnightBlue"`, `"Tomato"`, `"MintCream"`.
- **RGB**: `scene.color().rgb(100, 149, 237)`.
- **HSL**: `scene.color().hsl(200, 80, 60)`.

See `examples/styles_demo.py` for a gallery of these possibilities.

---

## Chapter 3: Connecting the Dots

diagrams are about relationships.

### Intelligent Binding
Link elements dynamically. If the nodes move, the connection adapts.

```python
scene.arrow().bind(start_node, end_node)
```

### Path Control
- **Elbow**: Orthogonal lines for structured diagrams.
- **Curve**: Elegant Bezier paths.
- **Arc**: Simple circular connections.

```python
scene.arrow().bind(a, b).elbow("R", "L") # Right to Left
```

Refer to `examples/arrows_demo.py` for comprehensive examples.

---

## Chapter 4: Consistency & Defaults

When creating a large diagram, repeating style method calls (`.font("Code").color("Blue")`) is redundant.

Use `scene.defaults()` to establish a baseline for your entire scene:

```python
# Set global style: "Artist" sloppiness, specific font, and color.
scene.defaults().sloppiness("artist").font("Nunito").color("DarkSlateGray")

# All subsequent elements inherit these traits
scene.text("I inherit the default style")
scene.rectangle().label("Me too")
```

This ensures visual consistency and keeps your code clean.

---

## Chapter 5: Algorithmic Generation

The true power of Excaligen lies in automation. You can visualize recursive structures or generate diagrams from data that would be tedious to draw by hand.

### Recursive Mind Map
Consider a mind map generated from a dictionary. With a simple recursive function, you can layout a tree structure where branches position themselves automatically.

See `examples/mind_map.py` for an implementation that turns a Python dictionary into a visual tree, handling node creation and connections recursively.

---

**Excaligen**. valid. plain. visual.
