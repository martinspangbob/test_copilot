def reverse_string(text):
    """Переворачивает строку."""
    return text[::-1]

def count_vowels(text):
    """Подсчитывает количество гласных букв в строке."""
    vowels = 'аеёиоуыэюяaeiouy'
    return sum(1 for char in text.lower() if char in vowels)

def is_palindrome(text):
    """Проверяет, является ли строка палиндромом."""
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]