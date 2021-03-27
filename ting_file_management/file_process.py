import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    importer = txt_importer(path_file)
    for elemento in range(len(instance)):
        if instance.search(elemento)["nome_do_arquivo"] == path_file:
            return

    solution = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(importer),
        "linhas_do_arquivo": importer,
    }

    instance.enqueue(solution)
    return print(solution)


def remove(instance):
    if len(instance) > 0:
        removed = instance.dequeue()
        solution = removed['nome_do_arquivo']
        return print(f"Arquivo {solution} removido com sucesso")
    return print("Não há elementos")


def file_metadata(instance, position):
    try:
        search = instance.search(position)
        return print(search)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
