import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return

    try:
        with open(path_file) as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    else:
        return content.split("\n")
