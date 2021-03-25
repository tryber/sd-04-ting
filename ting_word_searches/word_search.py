def search_ocurrences(word, file_search, add_content):
    list_ocurrences = list()
    content = file_search["linhas_do_arquivo"]
    for linha in range(len(content)):
        if word.lower() in content[linha].lower():
            if add_content:
                list_ocurrences.append({"linha": linha + 1,
                                        "conteudo": content[linha]})
            else:
                list_ocurrences.append({"linha": linha + 1})

    return list_ocurrences


def search_word(word, instance, add_content):
    list_files = list()

    for index in range(len(instance)):
        file_search = instance.search(index)
        list_ocurrences = search_ocurrences(word, file_search, add_content)

        if len(list_ocurrences) > 0:
            list_files.append({
                "palavra": word,
                "arquivo": file_search["nome_do_arquivo"],
                "ocorrencias": list_ocurrences
            })

    return list_files


def exists_word(word, instance):
    return search_word(word, instance, False)


def search_by_word(word, instance):
    return search_word(word, instance, True)
