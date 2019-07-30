DPI = 1.0
REFERENCE_DPI = 80


def inches(pixels) -> float:
    return pixels / REFERENCE_DPI


def dp(pixels) -> float:
    return inches(pixels) * DPI
