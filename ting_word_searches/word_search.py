def search_on_line(word, file_info, add_content):
    result = []
    for index in range(len(file_info["linhas_do_arquivo"])):
        line = file_info["linhas_do_arquivo"][index]
        if word.lower() in line.lower():
            occurrences = {"linha": index + 1}
            if add_content:
                occurrences["conteudo"] = line
            result.append(occurrences)
    return result


def search_on_instance(word, instance, add_content=False):
    files_found = []
    for file_info in instance:
        occurrences = search_on_line(word, file_info, add_content)

        if occurrences:
            files_found.append(
                {
                    "palavra": word,
                    "arquivo": file_info["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return files_found


def exists_word(word, instance):
    return search_on_instance(word, instance)


def search_by_word(word, instance):
    return search_on_instance(word, instance, True)
