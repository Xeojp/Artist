from diffusers import StableDiffusionPipeline
import torch
import os

MODEL_DIR = "models/stable-diffusion"
os.makedirs(MODEL_DIR, exist_ok=True)

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    cache_dir=MODEL_DIR
)
pipe.save_pretrained(MODEL_DIR)
print("Модель скачана и сохранена локально.")
