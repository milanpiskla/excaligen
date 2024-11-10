from ..base.AbstractElement import AbstractElement
from .Point import Point
from typing import Optional

class ElbowConnection:
    def __init__(self, start_element: AbstractElement, end_element: AbstractElement, start_dir: str, end_dir: str):
        self._start_element = start_element
        self._end_element = end_element
        self._start_dir = start_dir
        self._end_dir = end_dir

    def points(self) -> list[Point]:
        return [self.__find_edge_point(self._start_element, self._start_dir), self.__find_edge_point(self._end_element, self._end_dir)]
    
    def __find_edge_point(self, element: AbstractElement, direction: str) -> Point:
        if direction not in ['N', 'W', 'S', 'E']:
            raise ValueError(f'Wrong direction {direction}, shoould be one of the N, W, S, E')
        
        cx, cy = element.get_center()
        a, b = element._width / 2, element._height / 2

        match direction:
            case 'N':
                return cx, cy - b
            case 'W':
                return cx - a, cy
            case 'S':
                return cx, cy + b
            case 'E':
                return cx + a, cy
