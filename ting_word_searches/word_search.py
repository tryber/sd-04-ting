def exists_word(word, instance):
    """Aqui irá sua implementação"""

    obj_file = [{
        "palavra": word,
        "arquivo": "",
        "ocorrencias": []
    }]

    for element in range(len(instance)):
        file = instance.search(element)
        # print('teste', file)

        obj_file[0]["arquivo"] = file["nome_do_arquivo"]
        # obj_file["ocorrencias"] = list()
        # obj_file["palavra"] = word
        for index, row in enumerate(file["linhas_do_arquivo"]):
            if word in row:
                obj_file[0]["ocorrencias"].append({"linha": index + 1})

        if len(obj_file[0]["ocorrencias"]) != 0:
            return obj_file
        else:
            return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    obj_file = [{
        "palavra": word,
        "arquivo": "",
        "ocorrencias": []
    }]

    for index in range(len(instance)):
        file = instance.search(index)

        obj_file[0]["arquivo"] = file["nome_do_arquivo"]

        for index, row in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in row.lower():
                obj_file[0]["ocorrencias"].append({
                    "linha": index + 1,
                    "conteudo": row
                })

        if len(obj_file[0]["ocorrencias"]) != 0:
            return obj_file
        else:
            return []
