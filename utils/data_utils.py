import json

def load_json(file_path):
    """Carrega dados de um arquivo JSON e retorna como um dicionário."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(file_path, data):
    """Salva um dicionário em um arquivo JSON."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def merge_dicts(dict1, dict2):
    """Mescla dois dicionários."""
    result = dict1.copy()
    result.update(dict2)
    return result
