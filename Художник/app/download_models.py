from diffusers import StableDiffusionPipeline
import torch
import os

MODEL_DIR = "../models/stable-diffusion"

os.makedirs(MODEL_DIR, exist_ok=True)

def download_model(model_name="runwayml/stable-diffusion-v1-5"):
    print(f"Скачиваем модель {model_name} в {MODEL_DIR}...")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        cache_dir=MODEL_DIR
    )
    pipe.save_pretrained(MODEL_DIR)
    print("Модель успешно скачана и сохранена локально!")

if __name__ == "__main__":
    download_model()
