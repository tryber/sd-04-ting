import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)

    try:
        file = open(path_file, "r")
        text = file.read()
        file.close()
        new_text = text.splitlines()
        return new_text

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
