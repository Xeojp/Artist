from .styles import get_style_prompt

def enhance_prompt(user_prompt: str, style: str) -> str:
    style_prompt = get_style_prompt(style)
    full_prompt = f"{user_prompt}, {style_prompt}" if style_prompt else user_prompt
    return full_prompt
