from ..base.AbstractElement import AbstractElement

class ElementDecorator:
    def __init__(self, element: AbstractElement):
        self._element = element

    def get_center(self) -> tuple[float, float]:
        width = getattr(self._element, '_width', 0)
        height = getattr(self._element, '_height', 0)

        return (self._element._x + 0.5 * width, self._element._y + 0.5 * height)

#TODO add add_bound_element() and add_group_id()