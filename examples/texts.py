from src.Excalidraw import Excalidraw

xd = Excalidraw()
xd.text().content("Hello, World!").fontsize("L").font("Hand-drawn").align("center").baseline("top").spacing(1.5).color("#FF0000").autoresize(True)


try:
    with open('texts.excalidraw', 'w', encoding='utf-8') as file:
        file.write(xd.to_json())

except Exception as e:
    print(f"Error Writing {'texts.excalidraw'}: {e}")
