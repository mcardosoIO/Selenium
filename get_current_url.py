from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Creating an instance for Firefox web browser
browser = webdriver.Firefox()
#This is a method to navegate to website
browser.get('https://en.wikipedia.org/wiki/Main_Page')

#Creating a variable where will get the element found
element = browser.find_element_by_link_text('Wikibooks')

#This is a method to "click" on element
element.click()

#This will print the actual url
print(browser.current_url)
