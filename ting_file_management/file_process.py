import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    count_same_name = 0
    for index in range(len(instance)):
        element = instance.search(index)
        if path_file == element["nome_do_arquivo"]:
            count_same_name += 1
            break

    if count_same_name == 0:
        txt_file = txt_importer(path_file)

        processed_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_file),
            "linhas_do_arquivo": txt_file
        }

        instance.enqueue(processed_data)

        sys.stdout.write(f"{processed_data}")


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.dequeue()['nome_do_arquivo']
        message = f"Arquivo {path_file} removido com sucesso\n"

        sys.stdout.write(f"{message}")


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
    except IndexError:
        sys.stderr.write("Posição inválida")
    else:
        sys.stdout.write(f"{file_data}")
