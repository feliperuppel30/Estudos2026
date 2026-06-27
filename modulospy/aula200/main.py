from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'Screenshot_1.png'
NEW_IMAGE = ROOT_FOLDER / 'new.png'

pil_image = Image.open(ORIGINAL)

width, height = pil_image.size

new_width = 310
new_height = round(new_width * height / width)
print(width, height)
print(new_width, new_height)

new_image = pil_image.resize((new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize = True,
    quality=80
)