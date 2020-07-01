import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def main():
    try:
        drv = webdriver.Chrome()
        drv.get('http://suninjuly.github.io/explicit_wait2.html')
        WebDriverWait(drv, 12).until(ec.text_to_be_present_in_element((By.ID,'price'), "$100"))
        drv.find_element_by_id('book').click()
        a = drv.find_element_by_id('input_value')
        b = drv.find_element_by_id('answer')
        b.send_keys(calc(str(a.text)))
        drv.find_element_by_css_selector('button[type="submit"]').click()


    finally:
        sleep(10)
        drv.quit()

main()
