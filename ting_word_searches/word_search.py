def generate_occurrence(index, line=None, show_content=False):
    occr = dict()
    occr["linha"] = index + 1
    if line and show_content:
        occr["conteudo"] = line
    return occr


def search_in_lines(word, lines, show_content=False):
    occurence = list()
    for index, line in enumerate(lines):
        if word.lower() in line.lower():
            occurence.append(generate_occurrence(index, line, show_content))
    return occurence


def search_lines(word, instance, show_content=False):
    if not len(instance.queue):
        return []
    results = list()
    for file in instance.queue:
        occurrences = search_in_lines(
            word, file["linhas_do_arquivo"], show_content
        )
        if occurrences:
            results.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return results


def exists_word(word, instance):
    return search_lines(word, instance)


def search_by_word(word, instance):
    return search_lines(word, instance, True)