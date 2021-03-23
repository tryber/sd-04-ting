import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            with open(path_file, "r") as file:
                data = list()
                for line in file:
                    data.append(line.strip())
            return data
        except FileNotFoundError:
            sys.stderr.write(
                f"Arquivo {path_file} não encontrado\n")
    else:
        return sys.stderr.write("Formato inválido\n")
