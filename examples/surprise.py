"""
Description: Who will guess what this code will generate?
I'm so proud that I wrote this code :)
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder

s = SceneBuilder()

D = 42 * (42 * (42 * (42 * (42 * (42 * (42 * (42 * 3) + 25) + 26) + 2) + 28) + 30) + 8)

for y42 in range(42 - 34):
    for x42 in range(42 - 31):
        o = (y42 * 42 // 7) + abs(42 - 37 - x42)
        if (D >> o) & (42 - 41):
            s.rectangle().position(x42 * 42, y42 * 42).size(42, 42).color('#ff4242').background("#ff4242").fill("solid").roundness('sharp').sloppiness('architect')

s.save("surprise.excalidraw")
