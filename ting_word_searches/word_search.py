def occurrence_builder(line_counting, item=None):
    if item is None:
        return {
            "linha": line_counting
        }
    return {
        "linha": line_counting,
        "conteudo": item
    }


def result_builder(word, file, occurrence):
    return {
        "palavra": f"{word}",
        "arquivo": file["nome_do_arquivo"],
        "ocorrencias": occurrence
    }


def exists_word(word, instance):
    result = []
    for line in range(instance.__len__()):
        file = instance.search(line)
        line_counting = 0
        occurrence = []
        for item in file["linhas_do_arquivo"]:
            line_counting += 1
            is_word_present = word in item
            if is_word_present is True:
                occurrence.append(occurrence_builder(line_counting))
                result.append(result_builder(word, file, occurrence))
    return result


def search_by_word(word, instance):
    result = []
    for line in range(instance.__len__()):
        file = instance.search(line)
        line_counting = 0
        occurrence = []
        for item in file["linhas_do_arquivo"]:
            line_counting += 1
            is_word_present = word.upper() in item.upper()
            if is_word_present is True:
                occurrence.append(occurrence_builder(line_counting, item))
                result.append(result_builder(word, file, occurrence))
    return result
