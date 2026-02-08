"""
Description: Excaligen example for generating a workflow with arrows, kind of Chevron diagram.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details
 
from excaligen.SceneBuilder import SceneBuilder
import math

DATA = {
    "title": "The Intergalactic Bureaucracy Workflow",
    "steps": [
        "SUBMIT PLANNING PERMIT",
        "DON'T PANIC (YET)",
        "GRAB YOUR TOWEL",
        "IGNORE THE PHYSICS",
        "THE ANSWER IS 42"
    ],
    "note": "Estimated Time: 5 to 500,000,000 years\n(subject to local hyperspace bypass construction)."
}

COLORS = ["#7c6a0a","#babd8d","#ffdac6","#fa9500","#eb6424"]

ARROW_BASE_WIDTH = 120
ARROW_BASE_HEIGHT = 90
ARROW_ANGLE = 120 * math.pi / 180
ARROW_TIP_LENGTH = ARROW_BASE_HEIGHT / 2 / math.tan(ARROW_ANGLE / 2)
ARROW_SPACING = ARROW_BASE_WIDTH * 1.4

class Workflow:
    def __init__(self):
        self.scene = SceneBuilder()
        self.arrow_base_points = self._calculate_base_arrow_points()

    def spawn(self):
        self._draw_title()
        self._draw_workflow()
        return self

    def save(self, file_name):
        self.scene.save(file_name)
        return self

    def _draw_title(self):
        self.scene.text(DATA["title"]).center(0, -160).fontsize("L")
        self.scene.text(DATA["note"]).center(0, 160).fontsize("S")

    def _draw_workflow(self):
        for i, step in enumerate(DATA["steps"], -len(DATA["steps"]) // 2 + 1):
            self._draw_arrow(i * ARROW_SPACING, 0, step, COLORS[i])

    def _draw_arrow(self, x, y, text, color):
        arrow_points = [(base_x + x, base_y + y) for base_x, base_y in self.arrow_base_points]
        shadow_points = [(x + 4, y + 9) for x, y in arrow_points]
        shadow = (self.scene.line()
            .points(shadow_points)
            .close()
            .roundness("sharp")
            .color("transparent")
            .background("lightgray")
            .fill("solid")
        )
        arrow = (self.scene.line()
            .points(arrow_points)
            .close()
            .roundness("sharp")
            .background(color)
            .fill("solid")
        )
        text = (self.scene.text(text.replace(" ", "\n"))
            .center(x, y)
            .fontsize("S")
        )

        self.scene.group().elements(shadow, arrow, text)
            
    def _calculate_base_arrow_points(self):
        xll = -ARROW_BASE_WIDTH / 2 - ARROW_TIP_LENGTH
        xr = xll + ARROW_BASE_WIDTH + ARROW_TIP_LENGTH
        xl = xll + ARROW_TIP_LENGTH
        xrr = xl + ARROW_BASE_WIDTH + ARROW_TIP_LENGTH

        yu = -ARROW_BASE_HEIGHT / 2
        yd = ARROW_BASE_HEIGHT / 2
        return [(xll, yu), (xr, yu), (xrr, 0), (xr, yd), (xll, yd), (xl, 0)]

if __name__ == "__main__":
    Workflow().spawn().save("workflow_arrows.excalidraw")
