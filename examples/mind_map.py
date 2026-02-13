"""
Description: Excaligen example for generating a mind map.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details
 
from excaligen.SceneBuilder import SceneBuilder
import math

DATA = {
    "title": "Galactic Survival",
    "central_topic": "SPACE SAFETY",
    "branches": [
    {
      "subtopic": "AIRLOCK MISHAPS",
      "items": ["Accidental Ejection", "Chewing-Gum Sealant", "Lungs vs. Vacuum", "Safety-Tether Failure"]
    },
    {
      "subtopic": "ALIEN ETIQUETTE",
      "items": ["Hungry Smiles", "Parasitic Roommates", "Translator Insults", "Multiplying Pets"]
    },
    {
      "subtopic": "TIME TROUBLES",
      "items": ["Past-Self Loans", "Parental Deletion", "Infinite Mondays", "Future Spoilers"]
    },
    {
      "subtopic": "PHYSICS FAILS",
      "items": ["Human Spaghetti", "Relativity Lateness", "Gravity Flips", "Wormhole Nausea"]
    },
    {
      "subtopic": "GRUMPY ROBOTS",
      "items": ["Existential Toasters", "Sarcastic Navigators", "Update-Delay Death", "Door-Begging Rituals"]
    }
  ],
  "notice": "Notice: In the event of total molecular dispersion, please continue to act as if you exist."
}

SUBTOPIC_RADIUS = 320
ITEMS_RADIUS = 750

CENTRAL_TOPIC_DIAMETER = 240
SUBTOPIC_DIAMETER = 210
ITEMS_DIAMETER = 150

COLORS = ["#ff595e", "#ff924c", "#ffca3a", "#8ac926", "#1982c4", "#6a4c93"]

class MindMap:
    def __init__(self):
        self.scene = SceneBuilder()
        self.central_element = None
        self.scene.defaults().arrowheads(None, 'triangle').fill("solid").color("Transparent")
        self.branches_count = len(DATA["branches"])
        self.all_items_count = sum(len(branch["items"]) for branch in DATA["branches"])
        self.delta_angle = 2 * math.pi / self.branches_count
        self.start_angle = -math.pi / 2 if self.branches_count % 2 == 0 else -math.pi / 2 + self.delta_angle / 2
        self.delta_item_angle = 0.8 * 2 * math.pi / self.all_items_count
        self.palette = Palette(self.scene)

    def spawn(self):
        self._draw_title()
        self._draw_central_topic()
        self._draw_branches()
        self._draw_notice()
        return self

    def save(self, file_name):
        self.scene.save(file_name)
        return self

    def _draw_title(self):
        self.scene.text(DATA["title"]).center(0, -ITEMS_RADIUS *1.2).fontsize("XL").color("Gray")

    def _draw_central_topic(self):
        color = self.palette.get_background_color()
        text_color = self.palette.get_text_color_for_background(color)
        text = self.scene.text(self._compact_text(DATA["central_topic"]) ).fontsize("L").color(text_color)
        self.central_element = (self.scene.ellipse(text)
            .center(0, 0)
            .size(CENTRAL_TOPIC_DIAMETER, CENTRAL_TOPIC_DIAMETER)
            .background(color)
        )

    def _draw_branches(self):
        for i, branch in enumerate(DATA["branches"]):
            angle = i * self.delta_angle + self.start_angle
            color = self.palette.get_color(i)
            self._draw_subtopic(branch, angle, color)

    def _draw_subtopic(self, branch, angle, color):
        text_color = self.palette.get_text_color_for_background(color)
        text = self.scene.text(self._compact_text(branch["subtopic"])).fontsize("M").color(text_color)
        circle = (self.scene.ellipse(text)
            .orbit(self.central_element, SUBTOPIC_RADIUS, angle)
            .size(SUBTOPIC_DIAMETER, SUBTOPIC_DIAMETER)
            .background(color)
        )
        (
            self.scene.arrow()
                .bind(self.central_element, circle)
                .color(color)
                .thickness('extra-bold')
        )
        self._draw_items(branch, angle, circle, color)

    def _draw_items(self, branch, angle, parent, base_color):
        items_count = len(branch["items"])
        items_start_angle = angle - self.delta_item_angle * (items_count - 1) / 2
        for i, item in enumerate(branch["items"]):
            item_angle = items_start_angle + i * self.delta_item_angle
            color = self.palette.get_tone(base_color, i + 1, items_count)
            text_color = self.palette.get_text_color_for_background(color)

            text = self.scene.text(self._compact_text(item)).fontsize("S").color(text_color)
            circle = (self.scene.ellipse(text)
                .orbit(self.central_element, ITEMS_RADIUS, item_angle)
                .size(ITEMS_DIAMETER, ITEMS_DIAMETER)
                .background(color)
            )
            (
                self.scene.arrow()
                    .curve(angle, item_angle - math.pi)
                    .bind(parent, circle)
                    .thickness('bold')
                    .color(color)
            )

    def _compact_text(self, text):
        return text.replace(" ", "\n")

    def _draw_notice(self):
        self.scene.text(DATA["notice"]).center(0, ITEMS_RADIUS * 1.2).fontsize("S").color("Gray")

class Palette:
    MAX_ITEM_LIGHTNESS = 85
    MIN_ITEM_LIGHTNESS = 20

    def __init__(self, scene):
        self.colors = COLORS
        self.scene = scene

    def get_color(self, index):
        return self.scene.color().rgb(self.colors[index % len(self.colors)])

    def get_text_color_for_background(self, color):
        return "#000000" if color.hsl()[2] > 50 else "#ffffff"

    def get_tone(self, color, distance, items_count):
        h, s, l = color.hsl()
        light_step = (self.MAX_ITEM_LIGHTNESS - l) / items_count if l > 50 else (self.MIN_ITEM_LIGHTNESS - l) / items_count
        lightness = math.floor(l + distance * light_step)
        return self.scene.color().hsl(h, s, lightness)

    def get_background_color(self):
        return self.get_color(len(self.colors) - 1)

if __name__ == "__main__":
    MindMap().spawn().save("mind_map.excalidraw")
