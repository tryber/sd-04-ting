def exists_word(word, instance):
    """Aqui irá sua implementação"""
    file = []
    for i in range(len(instance)):
        search = instance.search(i)
        occurrence = []
        for index, line in enumerate(search['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrence.append({"linha": index + 1})
        if occurrence == []:
            return occurrence
        file.append({
            "arquivo": search['nome_do_arquivo'],
            "ocorrencias": occurrence,
            "palavra": word
        })
    return file


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
