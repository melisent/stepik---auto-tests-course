from selenium import webdriver
import math

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

browser.execute_script("window.scrollBy(0, 100);")

option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

option2 =browser.find_element_by_css_selector("[for='robotsRule']")
option2.click()

option3 = browser.find_element_by_class_name("btn")
option3.click()
