from ..base.AbstractElement import AbstractElement
from ..base.AbstractEdgedShape import AbstractEdgedShape
from ...config.Config import Config, DEFAULT_CONFIG

from typing import Self
import math

class Arrow(AbstractElement):
    def __init__(self, config: Config = DEFAULT_CONFIG):
        super().__init__("arrow", config)
        self.startBinding = None
        self.endBinding = None
        self.startArrowhead = config.get("startArrowhead", None)
        self.endArrowhead = config.get("endArrowhead", "arrow")
        self.points = []

    def bind(self, start: AbstractEdgedShape, end: AbstractEdgedShape) -> Self:
        end_center_x = end.x + end.width / 2
        end_center_y = end.y + end.height / 2

        start_x, start_y = self._calculate_edge_point(start, end_center_x, end_center_y)
        end_x, end_y = self._calculate_edge_point(end, start_x, start_y)

        self.points = [[start_x - start.x, start_y - start.y], 
                [end_x - start.x, end_y - start.y]]

        self.x = start.x
        self.y = start.y    
    
        self.startBinding = {
            "elementId": start.id, 
            "focus": 0,  # Focus at the edge
            "gap": 1  # Minimal gap
        }
        self.endBinding = {
            "elementId": end.id, 
            "focus": 0,  # Focus at the edge
            "gap": 1  # Minimal gap
        }

        # TODO notify binding

        return self

    def _calculate_edge_point(self, element, target_x, target_y):
        x, y, width, height = element.x, element.y, element.width, element.height
        cx, cy = x + width / 2, y + height / 2
        
        dx, dy = target_x - cx, target_y - cy
        angle = math.atan2(dy, dx)
        
        if abs(dx) > abs(dy):
            ex = cx + (width / 2) * (1 if dx > 0 else -1)
            ey = cy + (width / 2) * dy / abs(dx)
        else:
            ey = cy + (height / 2) * (1 if dy > 0 else -1)
            ex = cx + (height / 2) * dx / abs(dy)
        
        return ex, ey