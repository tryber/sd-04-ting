import re


def exists_word(word, instance):
    result = []
    line_count = 0
    found_words = []
    for item in range(instance.__len__()):
        line_count += 1
        file = instance.search(item)
        for line in file["linhas_do_arquivo"]:
            if re.findall(word, line, re.IGNORECASE):
                found_words.append({"linha": line_count})
                result.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": file["nome_do_arquivo"],
                        "ocorrencias": found_words,
                    }
                )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
