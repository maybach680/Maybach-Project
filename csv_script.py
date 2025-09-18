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
data_to_write = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'London'],
    ['Bob', 25, 'New York'],
    ['Charlie', 35, 'Tokyo']
]

# 4. Откроем (или создадим) файл data.csv и запишем в него наши данные
with open('data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data_to_write)

print("Файл data.csv успешно создан!")

# 5. Теперь прочитаем его и выведем содержимое
print("\nЧитаем содержимое файла:")
with open('data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)