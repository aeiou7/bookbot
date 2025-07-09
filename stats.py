def word_count(text: str):
    count = 0
    for w in text.split():
        if w != "":
            count += 1
    return count


def char_count(text: str):
    list: dict[str, int] = dict()
    for w in text:
        w = w.lower()
        for c in w:
            if c in list:
                list[c] += 1
            else:
                list[c] = 1
    return list


def sort_dict(dic: dict[str, int]):
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
