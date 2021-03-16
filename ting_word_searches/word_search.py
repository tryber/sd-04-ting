def ocurrences_is_empty(data):
    # Checa se a palavra não foi encontrada em nenhum arquivo
    for ocurrence in data:
        if len(ocurrence["ocorrencias"]) > 0:
            return data

    return []


def exists_word(word, instance):
    data = list()

    for index_instance in range(len(instance)):
        obj_structure = {"palavra": word, "arquivo": "", "ocorrencias": []}

        folder = instance.search(index_instance)

        # Arquivo
        obj_structure["arquivo"] = folder["nome_do_arquivo"]

        # Ocorrências
        for index, line in enumerate(folder["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                obj_structure["ocorrencias"].append({"linha": index + 1})

        # Terminou a busca dentro de UM arquivo
        data.append(obj_structure)

    return ocurrences_is_empty(data)


def search_by_word(word, instance):
    data = list()

    for index_instance in range(len(instance)):
        obj_structure = {"palavra": word, "arquivo": "", "ocorrencias": []}
        folder = instance.search(index_instance)
        print("\nFOLDER:", folder)

        # Arquivo
        obj_structure["arquivo"] = folder["nome_do_arquivo"]

        # Ocorrências
        for index, line in enumerate(folder["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                obj_structure["ocorrencias"].append(
                    {"linha": index + 1, "conteudo": line}
                )

        # Terminou a busca dentro de UM arquivo
        data.append(obj_structure)

    return ocurrences_is_empty(data)
