import sys
from .file_management import txt_importer


def process(path_file, instance):
    text_file = txt_importer(path_file)
    processed_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text_file),
        "linhas_do_arquivo": text_file
    }

    if (instance.enqueue(processed_file)):
        return print(f"{processed_file}", file=sys.stdout)
    return None


def remove(instance):
    removed_file = instance.dequeue()
    if not removed_file:
        return print("Não há elementos")
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        searched_file = instance.search(position)
        return print(searched_file)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
