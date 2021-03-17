import re


def exists_word(word, instance):
    list = []
    count = 0

    for i in range(len(instance)):
        search = instance.search(i)
        ocorrence = []
        count += 1
        for i in search["linhas_do_arquivo"]:
            if re.search(word, i, re.IGNORECASE):
                ocorrence.append({
                    "linha": count,
                })
                list.append({
                    "palavra": f"{word}",
                    "arquivo": search["nome_do_arquivo"],
                    "ocorrencias": ocorrence,
                })

    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
