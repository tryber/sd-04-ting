from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    bof = txt_importer(path_file)
    counterLines = 0
    for line in bof:
        counterLines += 1
    arquivo = {
         "nome_do_arquivo": path_file,
         "qtd_linhas": counterLines,
         "linhas_do_arquivo": bof,
    }
    print("arquivo", arquivo)
    instance.enqueue(arquivo)


def remove(instance):
    dequeueR = instance.dequeue()
    if dequeueR is not False:
        print(f"Arquivo {dequeueR['nome_do_arquivo']} removido com sucesso",
              file=sys.stdout,)
    else:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
