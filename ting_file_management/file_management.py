import sys


def txt_importer(path_file):
    '''valida extenção'''
    if path_file.endswith(".txt"):
        '''valida arquivo reto'''
        try:
            with open(path_file, "r") as file:
                text = []
                aux = file.readlines()

                for line in aux:
                    text.append(line.strip())
                return text

        except FileNotFoundError:
            return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    return sys.stderr.write("Formato inválido\n")
