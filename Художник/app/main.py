import argparse
from generator import VirtualArtist
from prompts import enhance_prompt
from utils import save_image, enhance_image

def main():
    parser = argparse.ArgumentParser(description="Виртуальный художник - генерация картин из CLI")
    parser.add_argument("--prompt", type=str, required=True, help="Описание картины")
    parser.add_argument("--style", type=str, default="", help="Стиль художника")
    parser.add_argument("--brightness", type=float, default=1.0, help="Яркость")
    parser.add_argument("--contrast", type=float, default=1.0, help="Контраст")
    parser.add_argument("--sharpness", type=float, default=1.0, help="Резкость")
    
    args = parser.parse_args()
    
    artist = VirtualArtist()
    full_prompt = enhance_prompt(args.prompt, args.style)
    
    image = artist.generate_image(full_prompt)
    image = enhance_image(image, args.brightness, args.contrast, args.sharpness)
    
    save_path = save_image(image)
    print(f"Картина сохранена по пути: {save_path}")

if __name__ == "__main__":
    main()
