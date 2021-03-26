def exists_word(word, instance):
    return search('exists', word, instance)


def search_by_word(word, instance):
    return search('by_word', word, instance)


def search(type, word, instance):
    result = []

    for file in instance.file_queue:
        search_result = [
            {'linha': index + 1}
            if type == 'exists'
            else {'linha': index + 1, 'conteudo': line}
            for index, line in enumerate(file['linhas_do_arquivo'])
            if word.lower() in line.lower()
        ]

        if search_result:
            result.append({
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": search_result
            })

    return(result)
