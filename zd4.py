import os

def ensure_directory_exists(directory_path):
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            return f"Каталог '{directory_path}' создан"
        else:
            return f"Каталог '{directory_path}' уже существует"
    except Exception as e:
        return f"Ошибка: {e}"

# Пример использования:
directory = input("Введите путь к каталогу: ")
result = ensure_directory_exists(directory)
print(result)
