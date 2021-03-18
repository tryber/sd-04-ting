# from ting_file_management.queue import Queue
# from ting_file_management.file_process import process


def exists_word(word, instance):
    all_files = []
    for item in instance._data:
        ocorrencia = []
        for index, sentence in enumerate(item["linhas_do_arquivo"]):
            if word.lower() in sentence.lower():
                ocorrencia.append({"linha": index + 1})
            else:
                return ocorrencia
        archive = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": ocorrencia
        }
        all_files.append(archive)
    return all_files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
