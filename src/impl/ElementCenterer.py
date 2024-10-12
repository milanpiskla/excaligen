class ElementCenterer:
    def __init__(self, element: any):
        self._element = element
        self._is_active = False

    def is_active(self) -> bool:
        return self._is_active

    def center(self, x: float, y: float) -> None:
        self._is_active = True
        self._element._x = x - 0.5 * self._element._width
        self._element._y = y - 0.5 * self._element._height

    def size(self, width: float, height: float) -> None:
        if self._is_active:
            self._element._x = self._element._x + 0.5 * self._element._width - 0.5 * width
            self._element._y = self._element._y + 0.5 * self._element._height - 0.5 * height
