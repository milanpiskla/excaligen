import pytest
from src.Excalidraw import Excalidraw


def test_Excalidraw():
    e = Excalidraw()
    e.ellipse().position(-100, -200).size(400, 200)
    e.rectangle().position(100, 200).size(200, 400)

    try:
        with open('test.excalidraw', 'w', encoding='utf-8') as file:
            file.write(e.to_json())
            assert True

    except Exception as e:
        print(f"Error Writing {'test.excalidraw'}: {e}")
        assert False

