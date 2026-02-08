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

SUBTOPIC_RADIUS = 300
ITEMS_RADIUS = 550

CENTRAL_TOPIC_DIAMETER = 150
SUBTOPIC_DIAMETER = 130
ITEMS_DIAMETER = 110

class MindMap:
    def __init__(self):
        self.scene = SceneBuilder()
        self.central_element = None
        self.scene.defaults().arrowheads(None, 'triangle')
        self.branches_count = len(DATA["branches"])
        self.all_items_count = sum(len(branch["items"]) for branch in DATA["branches"])
        self.delta_angle = 2 * math.pi / self.branches_count
        self.start_angle = -math.pi / 2 if self.branches_count % 2 == 0 else -math.pi / 2 + self.delta_angle / 2
        self.delta_item_angle = 0.75 * 2 * math.pi / self.all_items_count

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
        self.scene.text(DATA["title"]).center(0, -700).fontsize("XL")

    def _draw_central_topic(self):
        text = self.scene.text(self._compact_text(DATA["central_topic"]) ).fontsize("L")
        self.central_element = (
            self.scene.ellipse(text)
                .center(0, 0)
                .size(150, 150)
        )

    def _draw_branches(self):
        for i, branch in enumerate(DATA["branches"]):
            self._draw_subtopic(branch, i * self.delta_angle + self.start_angle)

    def _draw_subtopic(self, branch, angle):
        text = self.scene.text(self._compact_text(branch["subtopic"])).fontsize("M")
        circle = (
            self.scene.ellipse(text)
                .center(math.cos(angle) * SUBTOPIC_RADIUS, math.sin(angle) * SUBTOPIC_RADIUS)
                .size(120, 120)
        )
        self.scene.arrow().bind(self.central_element, circle)
        self._draw_items(branch, angle, circle)

    def _draw_items(self, branch, angle, parent):
        items_start_angle = angle - self.delta_item_angle * (len(branch["items"]) - 1) / 2
        for i, item in enumerate(branch["items"]):
            item_angle = items_start_angle + i * self.delta_item_angle
            text = self.scene.text(self._compact_text(item)).fontsize("S")
            circle = (
                self.scene.ellipse(text)
                    .center(math.cos(item_angle) * ITEMS_RADIUS, math.sin(item_angle) * ITEMS_RADIUS)
                    .size(100, 100)
            )
            self.scene.arrow().curve(angle, item_angle - math.pi).bind(parent, circle)

    def _compact_text(self, text):
        return text.replace(" ", "\n")

    def _draw_notice(self):
        self.scene.text(DATA["notice"]).center(0, 700).fontsize("S")

if __name__ == "__main__":
    MindMap().spawn().save("mind_map.excalidraw")
