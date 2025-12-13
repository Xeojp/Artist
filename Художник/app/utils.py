from PIL import Image, ImageEnhance
import os
from datetime import datetime

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_image(image: Image.Image, prefix="artwork") -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.png"
    path = os.path.join(OUTPUT_DIR, filename)
    image.save(path)
    return path

def enhance_image(image: Image.Image, brightness=1.0, contrast=1.0, sharpness=1.0) -> Image.Image:
    image = ImageEnhance.Brightness(image).enhance(brightness)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = ImageEnhance.Sharpness(image).enhance(sharpness)
    return image
