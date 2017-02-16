from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.get('http://www.which.co.uk/about-which/contact-us/email/')

#this method will colect the website source code.
doc = driver.page_source

#this is a regular expression to filter the emails address
all_emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for e in all_emails:
   print e
