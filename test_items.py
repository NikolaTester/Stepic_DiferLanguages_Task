from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    assert EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), ""