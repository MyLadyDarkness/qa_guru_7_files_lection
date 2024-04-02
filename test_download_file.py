import time

import requests
from selene import query
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test():
    file_path = "C:\\Users\\OBarkar\\PycharmProjects\\qa_guru_7_files_lection\\tmp"
    #file_path = "/Users/OBarkar/PycharmProjects/qa_guru_7_files_lection/tmp" с таким путем загружет не в tmp

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": file_path,
        #"savefile.default_directory": file_path, попытка фикса загрузки в нужную папку
        "download.prompt_for_download": False
    }

    #options.add_argument("--headless=new") попытка фикса загрузки в нужную папку
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    browser.config.driver = driver
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    browser.element("[data-testid='download-raw-button']").click()
    download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    content = requests.get(url=download_url).content #без content запрос возвращается полностью, content вернет только бинарное содержимое, можно утащиьт еще json  и не только

    # print("I AM CONTENT")
    # print(content)

    with open("tmp/readme2.rst", "wb") as file: #открыть файл, wb - запись в файл
        file.write(content) #записать контент в файл
    # #with - контекстный менеджер, он открывает файл по команде, позволяет с ним поработать и закрывает его автоматически

    with open("tmp/readme2.rst", "r") as file: #это уже другой файл
        file_content = file.read()
        assert "test_answer" in file_content
    time.sleep(10)

