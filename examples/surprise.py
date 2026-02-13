"""
Description: Who will guess what this code will generate?
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder

s = SceneBuilder()

D = 42 * (42 * (42 * (42 * (42 * (42 * (42 * (42 * 3) + 25) + 26) + 2) + 28) + 30) + 8)

for y in range(8):
    for x in range(11):
        if (D >> ((y * 6) + abs(5 - x))) & 1:
            s.rectangle().position(x * 42, y * 42).size(42, 42).color('#ff4242').background("#ff4242").fill("solid").roundness('sharp').sloppiness('architect')

s.save("surprise.excalidraw")
