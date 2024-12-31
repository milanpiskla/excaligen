"""
Description: Directions defined as Up, Doww, Left or Right.

Copyright (c) 2024 Milan Piskla
Licensed under the MIT License - see LICENSE file for details
"""

import math

_DIRECTIONS = {
    'U': (0.0, -1.0),
    'L': (-1.0, 0.0),
    'D': (0.0, 1.0),
    'R': (1.0, 0.0)
}

class Directions:
    @staticmethod
    def keys() -> list[str]:
        return _DIRECTIONS.keys() # type: ignore

    @staticmethod
    def dxdy(direction: str) -> tuple[float, float]:
        return _DIRECTIONS[direction]
    
    @staticmethod
    def angle(direction: str) -> float:
        dx, dy = _DIRECTIONS[direction]
        return math.atan2(dy, dx)
    