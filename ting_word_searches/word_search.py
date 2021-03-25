def exists_word(word, instance):
    result = []
    counter = 0
    word_occurrence = []

    for item in range(instance.__len__()):
        file = instance.search(item)

        for line in file["linhas_do_arquivo"]:
            counter += 1
            has_word = word in line
            if has_word:
                word_occurrence.append({"linha": counter})
                result.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": file["nome_do_arquivo"],
                        "ocorrencias": word_occurrence,
                    }
                )
    return result


def search_by_word(word, instance):
    return []
