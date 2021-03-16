import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in instance.elements:
        if item["nome_do_arquivo"] == path_file:
            return
    output = dict()
    lines_list = txt_importer(path_file)
    output["nome_do_arquivo"] = path_file
    output["qtd_linhas"] = len(lines_list)
    output["linhas_do_arquivo"] = lines_list
    instance.enqueue(output)
    print(output)


def remove(instance):
    if not len(instance):
        print("Não há elementos")
    else:
        file = instance.search(0)
        path_file = file["nome_do_arquivo"]
        instance.dequeue()
        print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
    else:
        print(data)
