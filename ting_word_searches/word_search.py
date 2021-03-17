def exists_word(word, instance):
    print(instance)
    for i, line in enumerate(instance):
        if word in line["linhas_do_arquivo"][0]:
            ret_dict = [
                {
                    "palavra": f"{word}",
                    "arquivo": f"{line['nome_do_arquivo']}",
                    "ocorrencias": [{"linha": i + 1}],
                }
            ]
            return ret_dict
        else:
            return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
