
import math
import pytest
from pytest import approx
from src.excaligen.impl.elements.Rectangle import Rectangle
from src.excaligen.defaults.Defaults import Defaults
from src.excaligen.impl.elements.Text import Text
from src.excaligen.impl.base.AbstractPlainLabelListener import AbstractPlainLabelListener

class DummyListener(AbstractPlainLabelListener):
    def _on_text(self, text: str) -> Text:
        return Text(Defaults())

def test_orbit_element():
    defaults = Defaults()
    center_rect = Rectangle(defaults, DummyListener()).center(100, 100)
    orbiting_rect = Rectangle(defaults, DummyListener())
    
    # Orbit at radius 50, angle 0 (right)
    orbiting_rect.orbit(center_rect, 50, 0)
    
    cx, cy = orbiting_rect.get_center()
    assert cx == approx(150)
    assert cy == approx(100)
    
    # Orbit at radius 50, angle pi/2 (down)
    orbiting_rect.orbit(center_rect, 50, math.pi / 2)
    cx, cy = orbiting_rect.get_center()
    assert cx == approx(100)
    assert cy == approx(150)

def test_orbit_point():
    defaults = Defaults()
    orbiting_rect = Rectangle(defaults, DummyListener())
    
    # Orbit around (100, 100) at radius 50, angle 0 (right)
    orbiting_rect.orbit(100, 100, 50, 0)
    
    cx, cy = orbiting_rect.get_center()
    assert cx == approx(150)
    assert cy == approx(100)
    
    # Orbit around (100, 100) at radius 50, angle pi/2 (down)
    orbiting_rect.orbit(100, 100, 50, math.pi / 2)
    cx, cy = orbiting_rect.get_center()
    assert cx == approx(100)
    assert cy == approx(150)

def test_orbit_invalid_args():
    defaults = Defaults()
    rect = Rectangle(defaults, DummyListener())
    
    with pytest.raises(ValueError, match="Invalid arguments for orbit"):
        rect.orbit(100, 50, 0) # Missing y coordinate
    
    with pytest.raises(ValueError, match="Invalid arguments for orbit"):
        rect.orbit("invalid", 50, 0) # Invalid reference type

