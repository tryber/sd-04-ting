import sys


def txt_importer(path_file):
    if path_file.endswith("txt"):
        try:
            with open(path_file, "r") as file:
                txt = []
                file_lines = file.readlines()

                for line in file_lines:
                    txt.append(line.strip())
                return txt
        except FileNotFoundError:
            return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    sys.stderr.write("Formato inválido\n")
