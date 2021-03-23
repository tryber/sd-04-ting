# from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    txt = txt_importer(path_file)
    value = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt,
    }
    instance.enqueue(value)
    sys.stdout.write(f"{value}")


def remove(instance):
    data = instance.dequeue()
    if data:
        sys.stdout.write(
            f"Arquivo {data['nome_do_arquivo']} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(f"{data}")
    except IndexError:
        sys.stderr.write("Posição inválida")


# project = Queue()
# process('statics/nome_pedro.txt', project)
# process('statics/nome_pedro.txt', project)
# process('statics/arquivo_teste.txt', project)
# remove(project)
