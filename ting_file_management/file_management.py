import sys


def txt_importer(path_file):
    try:
        if path_file.endswith(".txt"):
            with open(path_file, "r") as file_txt:
                reader = list()
                for line in file_txt:
                    reader.append(line.replace("\n", ""))
                return reader
        return sys.stderr.write("Formato inválido\n")
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
