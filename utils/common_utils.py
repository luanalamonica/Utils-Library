import random
import string

def generate_random_string(length=10):
    """Gera uma string aleatória com o comprimento especificado."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def is_number(s):
    """Verifica se a string pode ser convertida para um número."""
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_current_time():
    """Retorna o horário atual no formato YYYY-MM-DD HH:MM:SS."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
