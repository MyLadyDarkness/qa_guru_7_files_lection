# with open("hello", "a") as file: # rt - default, w - запись/перезапись,
#     # a - добавление в конец, r - чтение, x - запрет перезаписи файла
#     file.write("Hello, world!\n")

import os.path
import shutil

print(os.path.abspath(__file__))  # вывести текущий каталог, в котором запущен скрипт
print(os.path.abspath("script_file.py"))  # найти место расположения конкретного скрипта

current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)

TMP_DIR = os.path.join(current_dir, "tmp")  # константа
print(TMP_DIR)

if not os.path.exists("tmp2"):
    os.mkdir("tmp2")
    print("Created")
else:
    print("Not created")

shutil.rmtree(os.path.join(current_dir, "tmp2")) #удаление всего дерева, лучше использовать абсоютный путь