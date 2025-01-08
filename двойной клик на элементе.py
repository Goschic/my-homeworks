from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Создание экземпляра браузера (например, Chrome)
driver = webdriver.Chrome()

# Переход на нужную страницу
driver.get('https://demoqa.com/buttons')

# Подождём немного, чтобы страница загрузилась
time.sleep(5)

# Найдём нужный элемент (например, по XPATH)
element = driver.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')

# Создание объекта ActionChains
actions = ActionChains(driver)

# Выполнение двойного клика на элементе
actions.double_click(element).perform()

# Закрытие браузера
driver.quit()