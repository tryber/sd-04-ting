from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue
import sys


# lidos = set()


def process(path_file, instance):

    for item in range(len(instance)):
        # busca = instance.search(item)
        if instance.search(item)['nome_do_arquivo'] == path_file:
            return

    dados = txt_importer(path_file)

    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(dados),
        'linhas_do_arquivo': dados,
    }

    instance.enqueue(result)
    return print(result, file=sys.stdout)


def remove(instance):
    if (instance.__len__() == 0):
        return print('Não há elementos', file=sys.stdout)
    instance.dequeue()
    return print("Arquivo statics/arquivo_teste.txt removido com sucesso",
                 file=sys.stdout)
    # removido = instance.dequeue()
    # if removido:
    # print("Arquivo statics/arquivo_teste.txt removido com sucesso",
    #       file=sys.stdout)


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)


# projeto = Queue()
# caminho = "statics/arquivo_teste.txt"
# process(caminho, projeto)

# print(f"serch, {projeto.search(0)}")
# print(f"primeiro {process(caminho, projeto)}")
# print(f"segundo {process(caminho, projeto)}")
