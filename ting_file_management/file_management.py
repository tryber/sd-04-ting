import os
import sys


def txt_importer(path_file):
    _, file_extension = os.path.splitext(path_file)

    if file_extension not in ".txt":
        return sys.stderr.write("Formato inválido\n")

    if not os.path.exists(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    with open(path_file) as file:
        return [line.rstrip('\n') for line in file]
