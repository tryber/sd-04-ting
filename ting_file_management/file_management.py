import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    return text.splitlines()
