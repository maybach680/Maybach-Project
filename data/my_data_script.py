# Модуль os для работы с файловой системой - ВАЖНО для DE!
import os
# Модуль csv для работы с CSV-файлами
import csv

# 1. Получим текущую рабочую директорию
current_dir = os.getcwd()
print("Мы находимся здесь:", current_dir)

# 2. Посмотрим, что лежит в папке
print("Содержимое папки:", os.listdir(current_dir))

# 3. Создадим данные для записи в CSV.
# Часто тебе придется готовить данные именно в таком виде - список списков.
products_data = [
    ['Product_id', 'Product_name', 'Price'],
    ['1', "Apple", 69],
    ['2', "Beer", 80],
    ['3', "Hotdog", 210],
    ['4', "Shaurma", 250],
    ['5', "Chocolate", 79]
]

# 4. Откроем (или создадим) файл data.csv и запишем в него наши данные
file_path = 'products.csv'
with open(file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(products_data)

print(f"Файл {file_path} успешно создан!")

# 5. Теперь прочитаем его и выведем содержимое
print("\nСписок названий товаров:")
with open(file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if csv_reader.line_num == 1:  # Пропускаем заголовок
            continue
        print(row[2])  # Выводим только название (второй столбец)