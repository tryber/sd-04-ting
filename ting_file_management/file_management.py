import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)

    try:
        f = open(path_file, 'r')
        content = f.read()
        return content.split("\n")

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        print("arquivo manipulado e fechado com sucesso")
        f.close()
