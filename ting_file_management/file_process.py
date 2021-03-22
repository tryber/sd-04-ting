import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in range(len(instance)):
        if path_file == instance.search(item)["nome_do_arquivo"]:
            return

    txt_imported = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_imported),
        "linhas_do_arquivo": txt_imported,
    }

    sys.stdout.write(f"{data}")
    instance.enqueue(data)


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
    except IndexError:
        sys.stderr.write("Posição inválida")
    else:
        sys.stdout.write(f"{data}")
