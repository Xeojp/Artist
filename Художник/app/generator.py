from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

class VirtualArtist:
    def __init__(self, model_name="../models/stable-diffusion", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.torch_dtype = torch.float16 if self.device == "cuda" else torch.float32
        try:
            self.pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=self.torch_dtype)
            self.pipe = self.pipe.to(self.device)
        except Exception as e:
            raise RuntimeError(f"Ошибка при загрузке модели: {e}")

    def generate_image(self, prompt: str, width=512, height=512, num_inference_steps=50, guidance_scale=7.5, num_images=1) -> Image.Image:
        if not prompt.strip():
            raise ValueError("Промпт не может быть пустым")
        try:
            result = self.pipe(prompt, width=width, height=height, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale, num_images_per_prompt=num_images)
            return result.images if num_images > 1 else result.images[0]
        except Exception as e:
            raise RuntimeError(f"Ошибка при генерации изображения: {e}")
