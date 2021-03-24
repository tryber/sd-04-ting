import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            return print("Formato inválido", file=sys.stderr)

        with open(path_file) as file:
            data = file.readlines()
            new_data = []
            for linha in data:
                new_linha = linha.replace('\n', '')
                new_data.append(new_linha)
            return new_data
    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

# with open(path_file) as file:
#             texto = [a]
#             for linha in file:
#                 texto.append(linha)
#             return texto


# caminho = 'statics/arquivo_teste.txt'
# print(len(txt_importer(caminho)))
