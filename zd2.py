def write_and_read_file(filename, content=None):
    try:
        if content is not None:
            with open(filename, 'w') as file:
                file.write(content)  
        
        with open(filename, 'r') as file:
            result = file.read()
        
        return result  
    
    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Ошибка: {e}"  

filename = input("Введите имя файла: ")

write = input("хотите записать что-то в файл? (yes/no): ").lower()

if write == 'да':
    content = input("Введите строку для записи в файл: ")
    file_content = write_and_read_file(filename, content)  
else:
    file_content = write_and_read_file(filename)  

print("Содержимое файла:", file_content)
