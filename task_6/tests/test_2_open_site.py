from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

# поиск элемента
icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img1')
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')
