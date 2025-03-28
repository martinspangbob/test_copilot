import os
import shutil
from typing import List

def list_files_in_directory(path: str) -> List[str]:
    """Возвращает список всех файлов в указанной директории."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Директория {path} не найдена")
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_file_size(file_path: str) -> int:
    """Возвращает размер файла в байтах."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")
    return os.path.getsize(file_path)

def backup_file(file_path: str) -> str:
    """Создает резервную копию файла с суффиксом .bak."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")
    backup_path = f"{file_path}.bak"
    shutil.copy2(file_path, backup_path)
    return backup_path