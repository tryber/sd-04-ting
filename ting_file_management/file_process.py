import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return

    data = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }

    instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos", file=sys.stdout)
    file_name = instance.search(0)["nome_do_arquivo"]
    print(f"Arquivo {file_name} removido com sucesso", file=sys.stdout)
    instance.dequeue()


def file_metadata(instance, position):
    if position > len(instance):
        return print("Posição inválida", file=sys.stderr)

    metadata = instance.search(position)

    print(metadata, file=sys.stdout)
