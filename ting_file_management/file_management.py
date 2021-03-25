import sys


def txt_importer(path_file):
    if path_file.endswith('.txt'):
        try:
            with open(path_file, 'r') as file:
                data = list()
                txt_lines = file.readlines()

                for line in txt_lines:
                    data.append(line.strip())
                return data
        except FileNotFoundError:
            return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    sys.stderr.write("Formato inválido\n")
