# Firefox

from selenium.webdriver.firefox.options import Options
from selenium import webdriver

opts = Options()
opts.set_headless(headless=True)
assert opts.headless

driver = webdriver.Firefox(options=opts)
driver.get("http://www.google.com")

print(driver.title)



