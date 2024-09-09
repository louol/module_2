def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if word.lower() in root_word.lower() or root_word.lower() in word.lower():
            same_words.append(word)
    return same_words

result1 = single_root_words('Сталь', 'хрусталь', 'ваза', 'усталь', 'Таль')
result2 = single_root_words('сортир', 'Сортировщица', 'сор', 'Футбол', 'Сорт')
print(result1)
print(result2)