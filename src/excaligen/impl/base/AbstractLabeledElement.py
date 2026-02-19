"""
Description: Mixin for elements that support labels.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from typing import Self, override, overload
from ..elements.Text import Text
from ..base.AbstractPlainLabelListener import AbstractPlainLabelListener
from ..base.AbstractElement import AbstractElement

class AbstractLabeledElement(AbstractElement):
    LABEL_HORIZONTAL_INSET = 10
    LABEL_VERTICAL_INSET = 6

    def _init_labels(self, listener: AbstractPlainLabelListener, label: str | Text | None):
        # Do NOT call super().__init__ here as this is a mixin and we don't want to re-initialize AbstractElement state
        self.__listener = listener
        self.__label: Text | None = None
        if label is not None:
            self.label(label)

    def label(self, text: Text | str) -> Self:
        """Set the label text for the element.

        Args:
            text (Text | str): The text element to set as the label or plain text.

        Returns:
            Self: The current instance of the class.
        """
        match text:
            case Text():
                self.__label = text
            case str():
                self.__label = self.__listener._on_text(text)
            case _:
                raise ValueError("Invalid type for label. Use Text or str.")

        self._justify_label()
        self._add_bound_element(self.__label)
        self.__label._container_id = self._id
        return self

    @override
    def position(self, x: float, y: float) -> Self:
        return super().position(x, y)._justify_label()

    @overload
    def center(self) -> tuple[float, float]: ...

    @overload
    def center(self, x: float, y: float) -> Self: ...

    @override
    def center(self, *args) -> Self | tuple[float, float]:
        match args:
            case ():
                return super().center()
            case (x, y):
                super().center(x, y)
                return self._justify_label()
            case _:
                raise ValueError("Invalid arguments for center. Expected () or (x, y).")
    
    @override
    def rotate(self, angle: float) -> Self:
        if self.__label:
            self.__label.rotate(angle)
        return super().rotate(angle)

    @override
    def _size(self, width: float, height: float) -> Self:
        return super()._size(width, height)._justify_label()

    def _justify_label(self) -> Self:
        """Justify the label within the element."""
        if self.__label:
            x, y = self._x + self.LABEL_HORIZONTAL_INSET, self._y + self.LABEL_VERTICAL_INSET
            w, h = self._width - 2 * self.LABEL_HORIZONTAL_INSET, self._height - 2 * self.LABEL_VERTICAL_INSET
            self.__label.justify(x, y, w, h)
        
        return self

    def _add_group_id(self, id: str) -> None:
        """Add a group ID to the element.

        Args:
            id (str): The group ID to add.
        """
        super()._add_group_id(id)
        if hasattr(self, '__label') and self.__label:
            self.__label._group_ids.append(id)
