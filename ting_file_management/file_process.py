from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    '''preprocessamento do conteúdo'''
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return

    lines = txt_importer(path_file)
    new = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    instance.enqueue(new)
    print(new, file=sys.stdout)


def remove(instance):
    '''remove arquivo'''
    if len(instance) > 0:
        arquivo = instance.dequeue()
        print(f"Arquivo {arquivo['nome_do_arquivo']} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    '''apresentar as informações superficiais dos arquivos processado'''
    try:
        print(instance.search(position))
    except IndexError:
        sys.stderr.write("Posição inválida")
