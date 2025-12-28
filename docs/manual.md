# Excaligen User Manual

If you appreciate the aesthetic of Excalidraw but require capabilities beyond simple manual drafting, **Excaligen** offers a bridge between code and visual expression.

It allows you to generate Excalidraw-compatible files directly from Python, enabling the visualization of data structures, automated reports, and complex algorithmic patterns with minimal boilerplate.

---

## Chapter 1: The First Sketch

We begin with the essential `SceneBuilder`. This is your canvas.

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

Excalidraw is beloved for its hand-drawn feel. Excaligen gives you full programmatic control over this unique aesthetic.

### Elemental Shapes
Excalidraw provides a set of core primitives. We expose them directly:

- **Rectangle**: The workhorse of diagrams. Perfect for nodes, heavy containers, or UI mockups.
- **Ellipse**: Great for states, start/end points, or emphasizing flow.
- **Diamond**: The classic decision node in flowcharts.

```python
scene.rectangle().label("Process")
scene.ellipse().label("Start")
scene.diamond().label("Decision")
```

### The Visual Vocabulary
A diagram communicates through more than just shapes. The *style* of a line tells a story.

#### Stroke Styles
How a line is drawn changes its meaning:
- **Solid**: A strong, definite relationship or boundary. The default.
- **Dashed**: Often implies a tentative connection, a future state, or a secondary boundary.
- **Dotted**: Used for weak links, annotations, or "ghost" elements.

```python
scene.rectangle().stroke("dashed")
```

#### Fill Styles
Excalidraw's fill styles are iconic. You can choose how your shapes are filled:
- **Hachure**: The classic, sketchy diagonal lines. Distinctively "Excalidraw".
- **Cross-Hatch**: Dense, crossed lines for a heavier, darker selection.
- **Solid**: A full, opaque fill.

```python
scene.ellipse().fill("hachure").background("LightBlue")
```

#### Sloppiness (Roughness)
This is the magic ingredient. It determines how "hand-drawn" your diagram looks.
- **Architect**: Precise, straight lines. Clean and professional.
- **Artist**: The default. A balanced, natural sketchiness.
- **Cartoonist**: Very messy and playful.

```python
scene.defaults().sloppiness("architect") # Clean lines for a tech spec
```

### Colors
Express with precision using:
- **Named Colors**: `"MidnightBlue"`, `"Tomato"`, `"MintCream"`.
- **RGB**: `scene.color().rgb(100, 149, 237)`.
- **HSL**: `scene.color().hsl(200, 80, 60)`.

---

## Chapter 3: Connecting the Dots

Diagrams are fundamentally about relationships.

### Intelligent Binding
In manual drawing, moving a box means redrawing the lines. In Excaligen, you **bind** arrows to elements. If the nodes move, the arrow adapts automatically.

```python
scene.arrow().bind(start_node, end_node)
```

### Path Control
The path an arrow takes is crucial for readability:
- **Elbow**: Orthogonal lines (90-degree turns). Essential for technical diagrams like org charts or circuit boards where clarity is paramount.
- **Curve**: Elegant Bezier paths. Natural and flowing.
- **Arc**: Simple circular connections, great for annotation or jumping over other lines.

```python
scene.arrow().bind(a, b).elbow("R", "L") # Leave Right, Enter Left
```

---

## Chapter 4: Consistency & Defaults

When creating a large diagram, repeating style method calls (`.font("Code").color("Blue")`) is redundant and error-prone.

Use `scene.defaults()` to establish a baseline for your entire scene. This sets the "theme" of your diagram.

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
