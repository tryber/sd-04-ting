import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            # return sys.stderr.write("Formato inválido\n")
            print("Formato inválido", file=sys.stderr)

        with open(path_file, "r") as file:
            file_read = []

            for line in file.readlines():
                file_read.append(line.rstrip("\n"))

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    else:
        return file_read
