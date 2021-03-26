def serch_each_line(word, file, show_content):
    ocorrencias = []
    for index in range(file["qtd_linhas"]):
        line = file["linhas_do_arquivo"][index]
        if word.lower() in line.lower():
            info = {"linha": index + 1}
            if show_content:
                info["conteudo"] = line
            ocorrencias.append(info)

    return ocorrencias


def search_word(word, instance, show_content=False):
    files_with_word = []
    for file in instance:
        ocorrencias = serch_each_line(word, file, show_content)
        if ocorrencias:
            files_with_word.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )

    return files_with_word


def exists_word(word, instance):
    return search_word(word, instance)


def search_by_word(word, instance):
    return search_word(word, instance, True)
