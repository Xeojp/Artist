STYLES = {
    "vangogh": "в стиле Ван Гога",
    "picasso": "в стиле Пикассо",
    "monet": "в стиле Клода Моне",
    "abstract": "абстрактная живопись",
    "cyberpunk": "киберпанк стиль",
}

def get_style_prompt(style_name: str) -> str:
    return STYLES.get(style_name.lower(), "")