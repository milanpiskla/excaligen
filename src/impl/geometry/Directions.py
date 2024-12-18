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
        return _DIRECTIONS.keys()

    @staticmethod
    def dxdy(direction: str) -> tuple[float, float]:
        return _DIRECTIONS[direction]
    
    @staticmethod
    def angle(direction: str) -> float:
        dx, dy = _DIRECTIONS[direction]
        return math.atan2(dy, dx)
    