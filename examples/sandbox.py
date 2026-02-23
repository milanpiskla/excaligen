from excaligen.SceneBuilder import SceneBuilder
import math

scene = SceneBuilder()

(
    scene.defaults()
    .stroke('solid')
    .thickness('bold')
    .fill('solid')
    .roundness('round')
    .sloppiness('architect')
    .font('Nunito')
)

central_topic = scene.ellipse('Central topic').center(0, 0)
subtopic = scene.rectangle('Subtopic').center(350, 100)
scene.arrow('points to').bind(central_topic, subtopic)

scene.save('sandbox.excalidraw')
