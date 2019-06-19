from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

bookbutton = browser.find_element_by_id("book")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
bookbutton.click() 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

answer = browser.find_element_by_id("solve")
answer.click()

