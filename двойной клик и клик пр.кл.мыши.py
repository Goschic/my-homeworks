from selenium import webdriver
from time import sleep
import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

file = open("log.txt","w")
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/buttons')
driver.maximize_window()

sleep(1)

double_click_button = driver.find_element(By.XPATH,'//*[@id="doubleClickBtn"]')
right_click_button = driver.find_element(By.XPATH,'//*[@id="rightClickBtn"]')
standart_click_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button')

action = ActionChains(driver)
action.duble_click(double_click_button).perform()
action.context_click(right_click_button).perform()
standart_click_button.click()

file.close()
driver.quit()