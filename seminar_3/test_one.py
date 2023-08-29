import time

from testpage import OperationHelper
username = "1234"
password = "qwerty"


def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("1234")
    test_page1.enter_pswd("qwerty")
    test_page1.click_button()
    assert test_page1.get_error_msg() == "401"
    time.sleep(3)
