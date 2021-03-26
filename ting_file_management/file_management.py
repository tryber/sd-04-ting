import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if path_file.endswith(".txt"):
        try:
            with open(path_file, "r") as txt:
                reader = list()
                for row in txt:
                    reader.append(row.strip())
                return reader

        except FileNotFoundError:
            return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        return sys.stderr.write("Formato inválido\n")
