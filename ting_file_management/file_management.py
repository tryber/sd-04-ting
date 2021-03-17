# Referencia:
# https://stackoverflow.com/questions/5574702/
# how-to-print-to-stderr-in-python

from pathlib import Path
import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        if Path(path_file).is_file():
            txt_file = open(path_file, "r")
            txt_list = [line.replace("\n", "") for line in txt_file]
            return txt_list

        else:
            return print(
                f"Arquivo {path_file} não encontrado", file=sys.stderr
            )
    else:
        return print("Formato inválido", file=sys.stderr)
