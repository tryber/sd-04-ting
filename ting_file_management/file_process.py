from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return
            # procura cada arquivo
    data = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    instance.enqueue(result)
    return print(result, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        return print("Não há elementos", file=sys.stdout)
    instance.dequeue()
    return print(
        "Arquivo statics/arquivo_teste.txt removido com sucesso",
        file=sys.stdout,
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
