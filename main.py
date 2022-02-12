from typing import List


def sentence_splitter(text: str) -> List[str]:
    word_separators = [' ', ',', ':', ';', '.', ',', '?', '!', '\n', '–', '(', ')', '«', '»', '…']
    words = []
    buffer = ''

    for index in range(len(text)):
        value = text[index]
        if value in word_separators:
            if len(buffer) >= 4:
                words.append(buffer.lower())
            buffer = ''
        else:
            buffer += value

    return words