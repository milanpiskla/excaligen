# Welcome to Excaligen 🎨

**Excaligen** is a lightweight, zero-dependency Python library that lets you programmatically generate [Excalidraw](https://excalidraw.com/) files. 

If you've ever wanted to automate your diagrams creation, map out your cloud architecture, or generate mind maps directly from your Python code, you are in the right place!

---

## 🚀 Quick Glance

Excaligen uses a simple, fluent API (the builder pattern). You don't need to worry about complex JSON schemas—just tell the canvas what you want, and chain your styling methods together.

```python
from excaligen.SceneBuilder import SceneBuilder

# 1. Grab a fresh canvas
scene = SceneBuilder()

# 2. Drop some shapes onto the scene
central_topic = scene.ellipse('Central topic').center(0, 0)
subtopic = scene.rectangle('Subtopic').center(350, 100)

# 3. Bind them together with an arrow
scene.arrow('points to').bind(central_topic, subtopic)

# 4. Save your masterpiece!
scene.save('my_diagram.excalidraw')
```

(You can then drag and drop my_diagram.excalidraw directly into excalidraw.com!)
![Example](guide/images/binding.svg)

## 📚 Where to go next?
Ready to dive in? Choose your path:

### 📖 The Developer Guide
New to Excaligen? Start here. We will walk you through creating your first scene, styling elements, grouping objects, and embedding images.

[The Developer Guide](guide/index.md)

### ⚙️ API Reference
Already know the basics? Jump into the API docs to see every method, shape, and parameter available to you.

[API Reference](api/index.md)

### 🐙 GitHub Repository
Want to see the source code, report a bug, or contribute? Head over to our GitHub.

[GitHub Repository](https://github.com/milanpiskla/excaligen)