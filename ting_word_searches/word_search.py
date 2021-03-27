def exists_word(word, instance):
    result = []
    count = 0
    find = []
    for elemento in range(len(instance)):
        file = instance.search(elemento)
        count += 1
        if word in file["linhas_do_arquivo"][0]:
            find.append({"linha": count})
            result.append({
                "palavra": f"{word}",
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": find,
            })
    return result


def search_by_word(word, instance):
    result = []
    count = 0
    find = []
    for elemento in range(instance.__len__()):
        file = instance.search(elemento)
        count += 1
        for line in file["linhas_do_arquivo"]:
            if word in line:
                conteudo = {
                    "linha": count,
                    "conteudo": line,
                }
                find.append(conteudo)
                conteudo_result = {
                    "palavra": f"{word}",
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": find,
                }
                result.append(conteudo_result)
    return result