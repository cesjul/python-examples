from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
IMAGE_PATH = ROOT_FOLDER / 'example.png'
NEW_PATH = ROOT_FOLDER / 'new.png'

pil_image = Image.open(IMAGE_PATH)

width, height = pil_image.size

multiplicator = 6
new_width = width * 6
new_height = height * 6

new_image = pil_image.resize((new_width, new_height))
new_image.save(
    NEW_PATH,
    
)