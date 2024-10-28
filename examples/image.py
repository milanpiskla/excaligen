from src.Excaligen import Excaligen

xd = Excaligen()

xd.image().data('<svg xmlns="http://www.w3.org/2000/svg" id="mdi-home" viewBox="0 0 24 24" width="150" height="150" fill="#0000FF"><path d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" /></svg>').fit(100, 100)
xd.image().file('../symboliq/static/assets/material_design/wifi.svg').position(150, 200).fit(100, 100)
xd.image().file('c:/Users/Milan/Pictures/home.png').position(-150, 200).fit(100, 100)
xd.image().file('c:/Users/Milan/Pictures/Unity-logo.jpg').position(-150, -200).fit(100, 100)
xd.image().file('c:/Users/Milan/Pictures/arrow-point.gif').position(150, -200).fit(100, 100)

xd.save('image.excalidraw')