import re


def exists_word(word, instance):
    output = list()
    obj = dict()
    for item in instance.elements:
        obj["palavra"] = word
        obj["arquivo"] = item["nome_do_arquivo"]
        obj["ocorrencias"] = list()
        for index, line in enumerate(item["linhas_do_arquivo"]):
            if re.search(word, line, re.IGNORECASE):
                obj["ocorrencias"].append({"linha": index + 1})
            else:
                return output
    output.append(obj)
    return output


def search_by_word(word, instance):
    output = list()
    obj = dict()
    for item in instance.elements:
        obj["palavra"] = word
        obj["arquivo"] = item["nome_do_arquivo"]
        obj["ocorrencias"] = list()
        for index, line in enumerate(item["linhas_do_arquivo"]):
            if re.search(word, line, re.IGNORECASE):
                obj["ocorrencias"].append(
                    {"linha": index + 1, "conteudo": line}
                )
            else:
                return output
    output.append(obj)
    return output
