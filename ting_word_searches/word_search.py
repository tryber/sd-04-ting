def exists_word(word, instance):
    result_list = list()
    word_ocur = list()
    line_index = 0

    for item in range(instance.__len__()):
        data = instance.search(item)

        for line in data["linhas_do_arquivo"]:
            line_index += 1
            contain_word = word in line
            if contain_word:
                word_ocur.append({"linha": line_index})
                result_list.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": data["nome_do_arquivo"],
                        "ocorrencias": word_ocur,
                    }
                )
    return result_list


def search_by_word(word, instance):
    result_list = list()

    return result_list
