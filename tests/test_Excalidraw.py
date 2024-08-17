import pytest
from src.Excalidraw import Excalidraw


def test_Excalidraw():
    e = Excalidraw()
    e.ellipse().position(-100, -200).size(400, 200)
    e.rectangle().position(100, 200).size(200, 400)
    e.image().svg("<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><circle cx='100' cy='100' r='80' fill='green' /></svg>")
    
    try:
        with open('test.excalidraw', 'w', encoding='utf-8') as file:
            file.write(e.to_json())
            assert True

    except Exception as e:
        print(f"Error Writing {'test.excalidraw'}: {e}")
        assert False

