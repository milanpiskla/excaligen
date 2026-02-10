"""
Description: Excaligen example for generating a visualization with curves and arrows.
"""
# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from excaligen.SceneBuilder import SceneBuilder
import math

DATA = {
    'primitive': {
        'name': 'The "Primitive" Era (Before 2042)',
        'technologies': ['Spice Navigation', 'Cryo Sleeper', 'Fold Drive', 'Orion Drive', 'Infinite\n Improbability', 'Hyperdrive', 'Warp Drive']
    },
    'enlightened': {
        'name': 'The "Enlightened" Era (After 2042)',
        'technologies': ['Teleportation', 'Mass Relay', 'Boom Tube', 'Slipstream', 'Holtzman Engine', 'Omega Molecule', 'Bistromathics']
    },
}

OPTS_PER_ERA = len(DATA['primitive']['technologies'])
RADIUS = 800
XOFFSET = -200
CENTER_SIZE = 120
OPTION_WIDTH = 140
OPTION_HEIGHT = 80
PANELS_HEIGHT = 2.1 * (RADIUS + XOFFSET)
BK_WIDTH = 2.1 * RADIUS
BK_HEIGHT = 1.1 * PANELS_HEIGHT

class Options:
    def __init__(self):
        self.scene = SceneBuilder()
        self.center_element = None

    def spawn(self):
        self._draw_title()
        self._draw_background()
        self._draw_center()
        self._draw_options()
        self._draw_pro_tip()
        return self

    def save(self, file):
        self.scene.save(file)
        return self

    def _draw_title(self):
        self._draw_panel('How To Escape Our Galaxy', 0, 0, BK_WIDTH, BK_HEIGHT, 'WhiteSmoke')

    def _draw_background(self):
        self._draw_panel(DATA['primitive']['name'], -RADIUS / 2, 0, RADIUS, PANELS_HEIGHT, 'AliceBlue')
        self._draw_panel(DATA['enlightened']['name'], RADIUS / 2, 0, RADIUS, PANELS_HEIGHT, 'PaleGoldenRod')

    def _draw_center(self):
        label = (
            self.scene.text('Options')
            .fontsize('L')
            .color('White')
        )
        self.center_element = (
            self.scene.ellipse(label)
            .center(0, 0)
            .size(CENTER_SIZE, CENTER_SIZE)
            .background('Brown')
            .fill('solid')
        )

    def _draw_options(self):
        for i in range(-(OPTS_PER_ERA // 2), OPTS_PER_ERA // 2 + 1):
            angle = i * math.pi / (2 * OPTS_PER_ERA)
            
            text = DATA['enlightened']['technologies'][i + OPTS_PER_ERA // 2]
            self._draw_option_with_arrow(text, XOFFSET, 0, OPTION_WIDTH, OPTION_HEIGHT, angle, False)
            
            text = DATA['primitive']['technologies'][i + OPTS_PER_ERA // 2]
            self._draw_option_with_arrow(text, -XOFFSET, 0, OPTION_WIDTH, OPTION_HEIGHT, angle + math.pi, True)

    def _draw_option_with_arrow(self, name, x, y, w, h, angle, is_left):
        option = (self.scene.rectangle(name)
            .orbit(x, y, RADIUS, angle)
            .size(w, h)
            .background('White')
            .fill('solid')
        )

        start_dir, end_dir = ('L', 'R') if is_left else ('R', 'L')
        self.scene.arrow().curve(start_dir, end_dir).bind(self.center_element, option).arrowheads(None, 'arrow')

    def _draw_panel(self, label_text, x, y, w, h, bkcolor):
        label = self.scene.text(label_text).align('center').baseline('top').fontsize('L')
        (
            self.scene.rectangle(label)
                .center(x, y)
                .size(w, h)
                .color(bkcolor)
                .background(bkcolor)
                .fill("solid")
                .sloppiness('architect')
                .roundness('sharp')
        )

    def _draw_pro_tip(self):
        self.scene.text(f'Pro-Tip: Always carry a towel. It’s the only thing that works with all {2 * OPTS_PER_ERA} technologies').fontsize('S').center(0, BK_HEIGHT / 2 - 20).color('Gray')

if __name__ == "__main__":
    Options().spawn().save("options.excalidraw")