"""
Description: Helper for the arrowheads input processing.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

class Arrowheads:
    @staticmethod
    def from_(start: str | None = None, end: str | None = 'arrow') -> tuple[str | None, str | None]:
        """Set the arrowhead styles for the start and end of the arrow.

        Valid arrowheads values are None, 'arrow', 'bar', 'dot' and 'triangle'.

        Args:
            start (str, optional): The style of the start arrowhead. Defaults to None.
            end (str, optional): The style of the end arrowhead. Defaults to 'arrow'.

        Raises:
            ValueError: If an invalid arrowhead style is provided.

        Returns:
            tuple: A tuple containing the start and end arrowhead styles.
        """
        return (Arrowheads._convert(start), Arrowheads._convert(end))

    @staticmethod
    def _convert(head: str | None) -> str | None:
        valid_arrowheads = {None, 'arrow', 'bar', 'dot', 'triangle'}
        head = head.lower() if head is not None else None
        if head not in valid_arrowheads:
            raise ValueError(f"Invalid arrowhead '{head}'. Valid options are {valid_arrowheads}.")
        return head

