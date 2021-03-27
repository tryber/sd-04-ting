def exists_word(word, instance):
    line_list = []
    result = []
    for index in range(len(instance)):
        file_checked = instance.search(index)
        file_line = file_checked["linhas_do_arquivo"]
        if word in file_line[0]:
            line_list.append({"linha": index + 1})
            result.append({
                "palavra": f"{word}",
                "arquivo": file_checked["nome_do_arquivo"],
                "ocorrencias": line_list
            })
    return result


def search_by_word(word, instance):
    line_list = []
    result = []
    for index in range(len(instance)):
        file_checked = instance.search(index)
        file_line = file_checked["linhas_do_arquivo"]
        for i, line in enumerate(file_line):
            if word.lower() in line.lower():
                line_list.append({
                    "linha": i + 1,
                    "conteudo": f"{line}"
                })
                result.append({
                    "palavra": f"{word}",
                    "arquivo": file_checked["nome_do_arquivo"],
                    "ocorrencias": line_list
                })
    return result
# bug fixed with leandro marten support
