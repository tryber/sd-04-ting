def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = []
    counter = 0
    find = []

    for item in range(len(instance)):
        file = instance.search(item)
        counter += 1
        # Procura a palavra nas linhas
        if word in file["linhas_do_arquivo"][0]:
            find.append({"linha": counter})
            result.append(
                {
                    "palavra": f"{word}",
                    "arquivo": f'{file["nome_do_arquivo"]}',
                    "ocorrencias": find,
                }
            )
        return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    return []
