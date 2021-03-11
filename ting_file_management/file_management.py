import sys
import os


def txt_importer(path_file):
    if not os.path.isfile(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return
    file_content = []
    with open(path_file, "r") as file:
        file_content = file.read().splitlines()
        file.close()

    return file_content
