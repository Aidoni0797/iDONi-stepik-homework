from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Открываем нужную страницу
    link = "http://suninjuly.github.io/find_xpath_form"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем форму
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("iDONi")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Doni")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Semey")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Kazakhstan")

    # Находим кнопку по XPath и жмём её
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    # Ждём 10 секунд, чтобы скопировать код
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()

# В этом задании мы использовали метод поиска элемента по XPath.
# Код открывает страницу http://suninjuly.github.io/find_xpath_form.
# Находит поля ввода и заполняет их значениями: имя, фамилия, город и страна.
# Для кнопки отправки используется XPath:
# button = browser.find_element(By.XPATH, "//button[text()='Submit']")
# Такой селектор выбирает только ту кнопку, у которой текст равен Submit, поэтому не будут нажаты другие одинаковые кнопки.
# 4. После клика по кнопке программа ждёт 10 секунд, чтобы можно было скопировать результат, и затем закрывает браузер.
# Таким образом, решение задачи заключалось в том, чтобы правильно подобрать уникальный XPath-селектор для кнопки Submit.