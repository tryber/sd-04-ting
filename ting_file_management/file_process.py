from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    txt = txt_importer(path_file)
    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt,
    }
    instance.enqueue(info)


def remove(instance):
    data = instance.dequeue()
    if data:
        print(
            f"Arquivo {data['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout,
        )


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
