import re


def my_slugify(s: str) -> str:
    # use regex to get substring containing only alphanumerics and dash
    # from stripped, lowercased given string s with spaces replaces by dash
    return re.sub(r"[^-a-zA-Z0-9]", "", s.strip().lower().replace(" ", "-"))
