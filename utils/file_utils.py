import os

def read_file(file_path):
    """Lê o conteúdo de um arquivo e retorna como uma string."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """Escreve o conteúdo em um arquivo."""
    with open(file_path, 'w') as file:
        file.write(content)

def file_exists(file_path):
    """Verifica se um arquivo existe no caminho especificado."""
    return os.path.isfile(file_path)
