from typing import Any
type Config = dict[str, Any]

DEFAULT_CONFIG: Config = {
    "isDeleted": False,
    "x" : 0,
    "y" : 0,
    "width": 100,
    "height": 100,
    "opacity": 100,
    "angle": 0,
    "index" : None,
    "roughness": 1,
    "stroke_style": "solid", 
    "stroke_width": 1,
    "stroke_color": "#000000",
    "background_color": "transparent",
    "fillStyle": "hachure",
    "roundness": None,
    "group_ids": [],
    "frame_id": None, 
    "font_size": 16,
    "font_family": 1,
    "text_align": "center",
    "vertical_align": "middle",
    "auto_resize": True,
    "line_height": 1.25,
    "link": None
}