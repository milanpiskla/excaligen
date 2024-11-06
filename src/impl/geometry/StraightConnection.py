from ..base.AbstractElement import AbstractElement
from .HalfLineIntersection import HalfLineIntersection

class StraightConnection:
    def __init__(self, start_element: AbstractElement, end_element: AbstractElement):
        self._start_element = start_element
        self._end_element = end_element

    def points(self) -> list[tuple[float, float]]:
        return None
