"""
Description: Who will guess what this code will generate?
This is not the style anyone should use for drawing diagrams, but the output will surprise you :)
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder
from math import floor

s = SceneBuilder()

M = 20
A = 2*42**4 + 12*42**3 + 15*42**2 + 16*42 + 12
B = 23*42**3 + 20*42**2 + 11*42 + 9

for y in range(8):
    d = A if y < 4 else B
    for x in range(11):
        bs = floor(6 * (y % 4))
        bo = bs + abs(5 - x)
        c = floor(floor(d / pow(2.0, bo)) % 2.0)
        if c == 1:
            s.rectangle().position(x * M, y * M).size(M, M).color('red').background("red").fill("solid").roundness('sharp')

s.save("surprise.excalidraw")
