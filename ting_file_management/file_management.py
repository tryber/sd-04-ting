import os
import sys


def txt_importer(path_file):
    if not os.path.isfile(path_file):
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)

    read_file = open(path_file, "r")
    read_file_lines = [line.replace("\n", "") for line in read_file]
    return read_file_lines
