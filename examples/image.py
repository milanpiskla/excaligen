"""
Description: Minimal Excaligen example.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder

scene = SceneBuilder()

scene.image().file("assets/robot.svg").center(0, 0)
scene.text("Oh look, I'm expressing joy").center(0, -150)
scene.text("how utterly revolting").center(0, 130)

scene.save("image.excalidraw")
