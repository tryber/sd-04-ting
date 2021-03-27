import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if not path_file.endswith('.txt'):
            return print('Formato inválido', file=sys.stderr)

        with open(path_file) as file:
            data = file.readlines()
            list_data = []
            for x in data:
                linha = x.replace('\n', '')
                list_data.append(linha)
            return list_data
    except FileNotFoundError:
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
