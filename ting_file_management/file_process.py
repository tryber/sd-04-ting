import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = txt_importer(path_file)
    name_exists = [
        True
        for file in instance.file_queue
        if file['nome_do_arquivo'] == path_file
    ]

    if True in name_exists:
        return

    new_metadata = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines
    }

    instance.enqueue(new_metadata)
    sys.stdout.write(f'{new_metadata}')


def remove(instance):
    removed = instance.dequeue()

    if removed:
        sys.stdout.write(
            f"Arquivo {removed['nome_do_arquivo']} removido com sucesso\n"
        )


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        sys.stderr.write('Posição inválida\n')
