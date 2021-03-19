def exists_word(word, instance):
    result = []
    counter_line = 0
    words = []
    for item in range(instance.__len__()):
        file = instance.search(item)
        counter_line += 1
        for item in file["linhas_do_arquivo"]:
            contains_word = word in item
            if contains_word is True:
                words.append({"linha": counter_line})
                result.append({
                    "palavra": f"{word}",
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": words,
                })
    return result


def search_by_word(word, instance):
    return []
