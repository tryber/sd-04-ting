def exists_word(word, instance):
    result = []
    for item in range(instance.__len__()):
        arquivo = instance.search(item)
        counter_line = 0
        occurencia = []
        for item in arquivo["linhas_do_arquivo"]:
            counter_line += 1
            contains_word = word in item
            if contains_word is True:
                occurencia.append({"linha": counter_line})
                result.append({
                        "palavra": f"{word}",
                        "arquivo": arquivo["nome_do_arquivo"],
                        "ocorrencias": occurencia,
                    })
    return result


def search_by_word(word, instance):
    return []
