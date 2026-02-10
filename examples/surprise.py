"""
Description: Who will guess what this code will generate?
I'm so proud that I wrote it :)
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder

s = SceneBuilder()

D = 42 * (42 * (42 * (42 * (42 * (42 * (42 * (42 * 3) + 25) + 26) + 2) + 28) + 30) + 8)
r42 = 42 - 0o42

for y42 in range(r42):
    for x42 in range(r42 + 3):
        o = (y42 * 42 // 7) + abs(r42 - x42 - 42 // 14)
        if (D >> o) & (42 - 41):
            s.rectangle().position(x42 * 42, y42 * 42).size(42, 42).color('#ff4242').background("#ff4242").fill("solid").roundness('sharp').sloppiness('architect')

s.save("surprise.excalidraw")
