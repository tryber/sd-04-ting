import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""

    try:
        if not path_file.endswith(".txt"):
            return sys.stderr.write("Formato inválido\n")

        with open(path_file, "r") as file:
            text = []
            lines = file.readlines()

            for line in lines:
                text.append(line.strip())
            return text

    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
