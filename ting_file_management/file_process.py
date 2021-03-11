import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return

    imported_file = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(imported_file),
        "linhas_do_arquivo": imported_file,
    }

    instance.enqueue(result)
    print(result)


def remove(instance):
    if not instance or not instance.__len__():
        return print("Não há elementos")
    removed_file_name = instance.dequeue()["nome_do_arquivo"]
    return print(f"Arquivo {removed_file_name} removido com sucesso")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
