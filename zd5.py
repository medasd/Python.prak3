import os
import time

def file_stats(filepath):
    try:
        if os.path.isfile(filepath):
            file_size = os.path.getsize(filepath)
            
            last_modified_time = time.ctime(os.path.getmtime(filepath))
            
            file_name, file_extension = os.path.splitext(os.path.basename(filepath))
            
            return {
                "size": file_size,  
                "last_modified": last_modified_time, 
                "name": file_name,  
                "extension": file_extension  
            }
        else:
            return f"Файл '{filepath}' не найден"
    
    except Exception as e:
        return f"Ошибка: {e}"

filepath = input("Введите путь к файлу: ")
stats = file_stats(filepath)
print("Информация о файле:")
print(stats)
