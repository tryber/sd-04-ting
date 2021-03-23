# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue


def exists_word(word, instance):
    response = []
    for line in range(instance.__len__()):
        arquivo = instance.search(line)
        counter_line = 0
        occurencia = []
        for item in arquivo["linhas_do_arquivo"]:
            counter_line += 1
            contains_word = word in item
            if contains_word is True:
                occurencia.append({"linha": counter_line})
                response.append({
                    "palavra": f"{word}",
                    "arquivo": arquivo["nome_do_arquivo"],
                    "ocorrencias": occurencia,
                })
    return response


def search_by_word(word, instance):
    response = []
    for line in range(instance.__len__()):
        arquivo = instance.search(line)
        counter_line = 0
        occurencia = []
        for item in arquivo["linhas_do_arquivo"]:
            print(item)
            counter_line += 1
            contains_word = word.upper() in item.upper()
            if contains_word is True:
                occurencia.append(
                    {"linha": counter_line,
                     "conteudo": item})
                response.append({
                    "palavra": f"{word}",
                    "arquivo": arquivo["nome_do_arquivo"],
                    "ocorrencias": occurencia,
                })
        print(f"\n{response}")
    return response

# project = Queue()
# process("statics/nome_pedro.txt", project)
# search_by_word("pedro", project)
# process('statics/nome_pedro.txt', project)
# process('statics/arquivo_teste.txt', project)
# remove(project)
