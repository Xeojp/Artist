import gradio as gr
from app.generator import VirtualArtist
from app.prompts import enhance_prompt
from app.utils import save_image, enhance_image, OUTPUT_DIR
import os
from PIL import Image

artist = VirtualArtist()

def generate_artwork(user_prompt, style, brightness, contrast, sharpness):
    prompt = enhance_prompt(user_prompt, style)
    image = artist.generate_image(prompt)
    image = enhance_image(image, brightness, contrast, sharpness)
    save_path = save_image(image)
    gallery_images = get_gallery_images()
    
    return image, save_path, gallery_images

def get_gallery_images():
    files = sorted([os.path.join(OUTPUT_DIR, f) for f in os.listdir(OUTPUT_DIR) if f.endswith(".png")],
                   key=os.path.getmtime, reverse=True)
    images = [Image.open(f) for f in files]
    return images

styles_list = ["vangogh", "picasso", "monet", "abstract", "cyberpunk"]

interface = gr.Interface(
    fn=generate_artwork,
    inputs=[
        gr.Textbox(label="Введите описание картины"),
        gr.Dropdown(choices=styles_list, label="Выберите стиль"),
        gr.Slider(0.5, 2.0, value=1.0, label="Яркость"),
        gr.Slider(0.5, 2.0, value=1.0, label="Контраст"),
        gr.Slider(0.5, 2.0, value=1.0, label="Резкость")
    ],
    outputs=[
        gr.Image(type="pil", label="Сгенерированная картина"),
        gr.Textbox(label="Путь к сохранённой картине"),
        gr.Gallery(label="Галерея всех картин").style(grid=[3], height="auto")
    ],
    title="Виртуальный художник",
    description="Генерация картин в стиле разных художников с помощью Stable Diffusion с постобработкой и галереей"
)

if __name__ == "__main__":
    interface.launch()
