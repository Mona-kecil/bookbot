def get_number_of_words(text: str) -> str:
    splitted_text = text.split()
    return len(splitted_text)

def get_number_of_chars(text: str) -> dict:
    chars = dict()
    text = text.lower()

    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    return chars

def sort_on(d: dict):
    return d["num"]

def sort_dict(raw: dict) -> dict:
    sorted_list = list()
    for ch in raw:
        sorted_list.append({"char": ch, "num": raw[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
