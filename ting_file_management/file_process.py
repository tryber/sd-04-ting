import sys
from .file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    new_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    if instance.enqueue(new_file):
        return print(f"{new_file}", file=sys.stdout)
    return None


def remove(instance):
    file = instance.dequeue()
    if not file:
        return print("Não há elementos")
    print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return print(file)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
