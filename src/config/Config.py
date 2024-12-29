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
    "roughness": 1,
    "strokeStyle": "solid", 
    "strokeWidth": 1,
    "strokeColor": "#000000",
    "backgroundColor": "transparent",
    "fillStyle": "hachure",
    "roundness": None,
    "fontSize": 16,
    "fontFamily": 1,
    "textAlign": "center",
    "verticalAlign": "middle",
    "autoResize": True,
    "lineHeight": 1.25,
    "link": None
}