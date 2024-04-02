from zipfile import ZipFile #для работы с архивами

with ZipFile("tmp/hello.zip") as zip_file:
    print(zip_file.namelist()) #список файлов архива
    text = zip_file.read('hello.txt')
    print(text)
    zip_file.extract('hello.txt', path="tmp")

