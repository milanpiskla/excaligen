"""
Description: Excaligen example for generating a pie chart.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details
 
from excaligen.SceneBuilder import SceneBuilder
import math

DATA = [
    {"label": "Code/AI", "value": 40, "color": "#f4f1de", "fill": "solid"},
    {"label": "Design", "value": 30, "color": "#81b29a", "fill": "cross-hatch"},
    {"label": "Coffee", "value": 20, "color": "#3d405b", "fill": "hachure"},
    {"label": "Sleep", "value": 10, "color": "#e07a5f", "fill": "cross-hatch"}
]

RADIUS = 150
CENTER = (0, 0)
LEGEND_X = 200
LEGEND_START_Y = -100
LEGEND_Y_STEP = 40

class PieChart:
    def __init__(self):
        self.scene = SceneBuilder()
        self.total = sum(item["value"] for item in DATA)

    def spawn(self):
        self._draw_chart_and_legend()
        self._draw_title()
        return self

    def save(self, file_name):
        self.scene.save(file_name)
        return self

    def _draw_chart_and_legend(self):
        current_angle = 0
        current_legend_y = LEGEND_START_Y

        for item in DATA:
            percentage = item["value"] / self.total
            angle_span = percentage * 2 * math.pi
            
            self._draw_slice(item, current_angle, angle_span)
            self._draw_legend_item(item, current_legend_y)
            
            current_legend_y += LEGEND_Y_STEP
            current_angle += angle_span

    def _draw_slice(self, item, start_angle, angle_span):
        arc = (self.scene.line()
            .roundness("sharp")
            .arc(0, 0, RADIUS, start_angle, angle_span)
            .append([CENTER])
            .close()
            .background(item["color"])
            .fill(item["fill"])
            .stroke("solid")
        )

    def _draw_legend_item(self, item, y):
        self.scene.rectangle().size(20, 20).position(LEGEND_X, y).background(item["color"]).fill(item["fill"])
        self.scene.text(f"{item['label']} ({item['value']}%)").position(LEGEND_X + 30, y).anchor(LEGEND_X + 30, y, "left", "top")

    def _draw_title(self):
        self.scene.text("Daily Developer Life").center(0, -200).fontsize("L")

if __name__ == "__main__":
    PieChart().spawn().save("pie_chart.excalidraw")
