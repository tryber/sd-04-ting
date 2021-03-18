import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        txt_file = open(path_file, "r")
        text = txt_file.read()
        txt_file.close()
        new_text = text.splitlines()
        return new_text
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
