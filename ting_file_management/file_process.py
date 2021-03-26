import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_data = txt_importer(path_file)

    file_info = {
       "nome_do_arquivo": path_file,
       "qtd_linhas": len(file_data),
       "linhas_do_arquivo": file_data
    }
    if instance.enqueue(file_info):
        return print(file_info, file=sys.stdout)

    return None


def remove(instance):
    removed_file = instance.dequeue()

    if not removed_file:
        print("Não há elementos")
        return

    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return print(file)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
