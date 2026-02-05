from excaligen.SceneBuilder import SceneBuilder

scene = SceneBuilder()

# 1. Defaults - Set global styles for subsequent elements
# Let's make everything look "sketchy" and blue-ish by default
scene.defaults().sloppiness("artist").color("MidnightBlue").font("Comic Shaans")

scene.text("Global Defaults: Artist Style & Comic Shaans").position(50, 20).fontsize(20)

# 2. Stroke Styles
y_start = 80
scene.text("Stroke Styles:").position(50, y_start).fontsize(16).font("Normal")

scene.rectangle().label("Solid (Default)").position(50, y_start + 30).stroke("solid")
scene.rectangle().label("Dashed").position(200, y_start + 30).stroke("dashed")
scene.rectangle().label("Dotted").position(350, y_start + 30).stroke("dotted")

# 3. Thickness & Fill
y_start = 200
scene.text("Thickness & Fill:").position(50, y_start).fontsize(16).font("Normal")

scene.ellipse().label("Thin & Hachure").position(50, y_start + 30).thickness(1).fill("hatchure").background("LightCyan")
scene.ellipse().label("Bold & Cross-Hatch").position(200, y_start + 30).thickness(2).fill("cross-hatch").background("LightPink")
scene.ellipse().label("Extra Bold & Solid").position(350, y_start + 30).thickness(3).fill("solid").background("LightYellow")

# 4. Fonts
y_start = 350
scene.text("Font Families:").position(50, y_start).fontsize(16).font("Normal")

fonts = ["Hand-drawn", "Normal", "Code", "Excalifont", "Comic Shaans"]
for i, font_name in enumerate(fonts):
    scene.text(f"This is {font_name}").position(50 + i * 150, y_start + 40).font(font_name)

scene.save("styles_demo.excalidraw")
