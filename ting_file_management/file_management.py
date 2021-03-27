import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file) as file:
            file = file.read()
            return file.splitlines()
    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
