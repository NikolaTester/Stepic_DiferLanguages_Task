from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(15)
    browser.implicitly_wait(10)
    
assert EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), ""