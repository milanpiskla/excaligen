"""
Description: Who will guess what this code will generate?
This is not the style anyone should use for drawing diagrams, but the output will surprise you :)
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder
from math import floor

s = SceneBuilder()
# Constants derived from your GLSL
SPRITE_WIDTH = 11
MSB = 5  # The Center Axis (Middle Significant Bit)
M = 20

for y in range(8):
    # Select the correct 24-bit float based on row
    d = 7139592.0 if y < 4 else 1739775.0
    
    for x in range(SPRITE_WIDTH):
        # 1. Calculate the Bit Sector (Row offset in bits)
        # Matches: floor(BITS_PER_ROW * mod(y, SPRITE_HALF_HEIGHT))
        bs = floor(6 * (y % 4))
        
        # 2. Calculate Bit Offset (The Fix)
        # GLSL: bitSector + abs(MSB - floor(st.s * SPRITE_WIDTH))
        # Python: x is already floor(st.s * width)
        bo = bs + abs(MSB - x)
        
        # 3. Extract Bit
        c = floor(floor(d / pow(2.0, bo)) % 2.0)
        
        if c == 1:
            # Invert Y for drawing because usually canvas Y goes down, 
            # while Shader Y goes up. (Optional, depending on pref)
            s.rectangle().position(x * M, y * M).size(M, M).background("black").fill("solid").roundness('sharp')

s.save("surprise.excalidraw")
