import os

def list_files_in_directory(directory_path):
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files
    except FileNotFoundError:
        return f"Каталог '{directory_path}' не найден."
    except Exception as e:
        return f"Ошибка: {e}"

directory = input("Введите путь к каталогу: ")
file_list = list_files_in_directory(directory)
print("Список файлов в каталоге:")
print(file_list)
