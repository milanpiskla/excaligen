# 📐 Excaligen: **Excalidraw File Generator** ✨

![Pyrhon to Excalidraw](./assets/py2ex.svg)

Excaligen is a Python library to generate [Excalidraw](https://excalidraw.com/) files. 
If you wish to automate creating visualizations in Excalidraw style, this library is for you.

## Why This Library?
[Excalidraw](https://excalidraw.com/) is an amazing tool for sketching diagrams and visualizing ideas. However, creating diagrams programmatically isn't fully supported out of the box. This library bridges that gap, allowing you to generate Excalidraw-compatible JSON files with Python code.

## Features 🚀
- Generate Excalidraw files using Python — add shapes, text, images, and more.
- Full Customization: Control position, size, colors, opacity, and styles.
- Image Support: Embed SVG, PNG, and JPEG images directly into your diagrams.
- Group and Frame Elements: Organize your diagrams better.
- Export to Excalidraw: Generate JSON files ready to be imported into Excalidraw.

## Installation 🛠️
```
pip install excaligen
```

## How to use 💡
Excaligen exposes a fluent API, using a builder pattern.
Example:
```python
from excaligen.SceneBuilder import SceneBuilder

scene = SceneBuilder()
central_topic = scene.ellipse('Central topic').center(0, 0)
subtopic = scene.rectangle('Subtopic').center(350, 100)
scene.arrow('points to').bind(central_topic, subtopic)

scene.save('binding.excalidraw')
```
The code above creates a simple diagram with a central topic and subtopic, connected by an arrow.

![Binding](./docs/manual/images/binding.svg)

Please refer to the detailed documentation for more information:
- [User Manual](./docs/manual/index.md)
- [Detailed API](./docs/api/index.md)

## What you can build 🏗️
The limit is your imagination. Here are some examples:

![Mind Map](./docs/manual/images/example_mind_map.svg)

![Workflows](./docs/manual/images/example_workflow_arrows.svg)

![Pie Chart](./docs/manual/images/example_pie_chart.svg)

![Options](./docs/manual/images/example_options.svg)

Developed by **Milan Piskla** with 💜 for connecting code and creativity.
