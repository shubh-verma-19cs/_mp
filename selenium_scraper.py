from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.set_window_size(1200, 900)
driver.get('https://www.google.com/recaptcha/api2/demo')

captcha = driver.find_element_by_css_selector('iframe[role=presentation]')
driver.switch_to.frame(captcha)

print('\nPlease solve the captcha now')
wait = WebDriverWait(driver, 120)
try:
    wait.until(ec.presence_of_element_located(('css selector', 'span[aria-checked="true"]')))
except TimeoutException:
    print('\nFailed to solve captcha in the expected time')
else:
    print('\nCaptcha solved successfully, proceeding to click!')
    driver.switch_to.parent_frame()
    driver.find_element_by_css_selector('#recaptcha-demo-submit').click()