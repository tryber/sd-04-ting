from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in range(len(instance)):
        element = instance.search(item)
        if path_file == element["nome_do_arquivo"]:
            return

    file = txt_importer(path_file)

    result_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    print(result_file)
    instance.enqueue(result_file)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")
    deleted_file = instance.dequeue()["nome_do_arquivo"]
    return print(f"Arquivo {deleted_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
