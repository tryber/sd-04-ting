import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""

    file_data = dict()
    count_file = 0

    for index in range(len(instance)):
        file = instance.search(index)
        if path_file == file["nome_do_arquivo"]:
            count_file += 1
            return

    if count_file == 0:
        file_txt = txt_importer(path_file)
        print('TEste', file_txt)
        file_data["nome_do_arquivo"] = path_file
        file_data["qtd_linhas"] = len(file_txt)
        file_data["linhas_do_arquivo"] = file_txt

    instance.enqueue(file_data)
    sys.stdout.write(f"{file_data}")
    # return file_data


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        # file = instance.search(0)
        path_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(
            f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        find_data = instance.search(position)
    except IndexError:
        sys.stderr.write("Posição inválida")
    else:
        print(find_data)
