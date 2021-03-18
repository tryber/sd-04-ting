def exists_word(word, instance):
    result = []
    counter = 0
    word_occurency = []

    for item in range(instance.__len__()):
        file = instance.search(item)

        for line in file["linhas_do_arquivo"]:
            counter += 1
            contains_word = word in line
            if contains_word:
                word_occurency.append({"linha": counter})
                result.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": file["nome_do_arquivo"],
                        "ocorrencias": word_occurency,
                    }
                )
    return result


def search_by_word(word, instance):
    return []
