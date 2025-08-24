import re


def my_slugify(s: str) -> str:
    return re.sub(r"[^-a-zA-Z0-9]", "", s.strip().lower().replace(" ", "-"))
