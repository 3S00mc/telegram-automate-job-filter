from config.keywords import INCLUDE, EXCLUDE, BONUS

def match_message(text: str):
    t = text.lower()

    for word in EXCLUDE:
        if word in t:
            return None

    if not any(word in t for word in INCLUDE):
        return None

    score = 50

    for word in BONUS:
        if word in t:
            score += 5

    return score
