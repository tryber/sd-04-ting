def generate_occurrence(index, line=None, show_content=False):
    occurrence_dict = dict()
    occurrence_dict["linha"] = index + 1
    if line and show_content:
        occurrence_dict["conteudo"] = line
    return occurrence_dict


def search_in_lines(word, lines, show_content=False):
    lines_that_occurs = list()
    for index, line in enumerate(lines):
        if word.lower() in line.lower():
            lines_that_occurs.append(
                generate_occurrence(index, line, show_content)
            )
    return lines_that_occurs


def search_lines_by_word(word, instance, show_content=False):
    if not len(instance.queue):
        return []
    result_list = list()
    for file in instance.queue:
        occurrences = search_in_lines(
            word, file["linhas_do_arquivo"], show_content
        )
        if occurrences:
            result_list.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return result_list


def exists_word(word, instance):
    return search_lines_by_word(word, instance)


def search_by_word(word, instance):
    return search_lines_by_word(word, instance, True)
