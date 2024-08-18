def to_uppercase(s):
    """Converte uma string para maiúsculas."""
    return s.upper()

def to_lowercase(s):
    """Converte uma string para minúsculas."""
    return s.lower()

def capitalize_words(s):
    """Capitaliza a primeira letra de cada palavra em uma string."""
    return s.title()

def is_palindrome(s):
    """Verifica se uma string é um palíndromo."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]
