import sys
# from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    importer = txt_importer(path_file)
    process_archive = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(importer),
        "linhas_do_arquivo": importer
    }

    instance.enqueue(process_archive)
    print(process_archive)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        actual = instance._data[0]["nome_do_arquivo"]
        instance.dequeue()
        print(f"Arquivo {actual} removido com sucesso")


def file_metadata(instance, position):
    if position > len(instance):
        print("Posição inválida", file=sys.stderr)
    else:
        data = instance.search(position)
        found_archive = {
            "nome_do_arquivo": data["nome_do_arquivo"],
            "qtd_linhas": data["qtd_linhas"],
            "linhas_do_arquivo": data["linhas_do_arquivo"]
        }
        print(found_archive)
