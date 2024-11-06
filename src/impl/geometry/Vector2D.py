import math

class Vector2D:
    @staticmethod
    def rotate(vx: float, vy: float, angle: float) -> tuple[float, float]:
        if angle != 0:
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            return vx * cos_a - vy * sin_a, vx * sin_a + vy * cos_a
        else:
            return vx, vy
        
