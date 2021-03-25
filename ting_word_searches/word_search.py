def exists_word(word, instance):
    ''''valida exist palavra em arquivos processados'''
    result = []
    count = 0
    found = []
    for i in range(len(instance)):
        arquivo = instance.search(i)
        count += 1
        if word in arquivo["linhas_do_arquivo"][0]:
            found.append({"linha": count})
            result.append({
                "palavra": f"{word}",
                "arquivo": arquivo["nome_do_arquivo"],
                "ocorrencias": found,
            })
    return result


def search_by_word(word, instance):
    return []
    '''teste'''
