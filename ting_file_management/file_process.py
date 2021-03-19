import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    lines = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    instance.enqueue(data)
    print(data)


def remove(instance):
    """Aqui irá sua implementação"""
    if (instance.__len__() == 0):
        print("Não há elementos")
    else:
        file_name = instance.search(0)['nome_do_arquivo']
        instance.dequeue()
        print(f"Arquivo {file_name} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
