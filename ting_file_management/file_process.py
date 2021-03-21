from ting_file_management.file_management import txt_importer
import sys


def format(path_file, lines_file):
    return {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines_file),
        "linhas_do_arquivo": lines_file
    }


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return

    lines_file = txt_importer(path_file)
    new_file = format(path_file,  lines_file)
    instance.enqueue(new_file)
    print(new_file, file=sys.stdout)


def remove(instance):
    if len(instance) > 0:
        file = instance.dequeue()
        return print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")
    else:
        return print("Não há elementos")


def file_metadata(instance, position):
    try:
        data_file = print(instance.search(position))
    except IndexError:
        sys.stderr.write("Posição inválida")
    else:
        sys.stdout.write(f"{data_file}")
