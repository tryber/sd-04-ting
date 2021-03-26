from ting_file_management.file_management import txt_importer
import sys


# Receber o caminho e a instancia do Queue
def process(path_file, instance):
    data = txt_importer(path_file)

    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return

    new_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    instance.enqueue(new_data)
    return print(new_data, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos", file=sys.stdout)

    instance.dequeue()
    return print(
        "Arquivo statics/arquivo_teste.txt removido com sucesso",
        file=sys.stdout,
    )


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        return print('Posição inválida', file=sys.stderr)
