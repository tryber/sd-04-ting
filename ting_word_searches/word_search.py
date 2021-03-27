import re


def exists_word(word, instance):
    solution = []
    count = 0
    historic = []
    for elemento in range(len(instance)):
        count += 1
        search = instance.search(elemento)
        for step in search["linhas_do_arquivo"]:
            if re.findall(word, step, re.IGNORECASE):
                historic.append({"linha": count})
                solution.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": search["nome_do_arquivo"],
                        "ocorrencias": historic,
                    }
                )
    return solution


def search_by_word(word, instance):
    return []
