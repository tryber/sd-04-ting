import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, 'r') as file:
            lines = file.readlines()
            text = []
            for line in lines:
                text.append(line.replace('\n', ''))
        return text
    except FileNotFoundError:
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
