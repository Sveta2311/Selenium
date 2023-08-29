import time

from testpage import OperationHelper
username = "Daras77745"
password = "ca90331158"
name = "Sveta"
email = "margaritka@mail.ru"
content = "Hello, world!"


def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("Daras77745")
    test_page1.enter_pswd("ca90331158")
    test_page1.click_button()
    time.sleep(3)

    test_page1.click_contact()
    time.sleep(3)

    test_page1.enter_name("Sveta")
    test_page1.enter_email("margaritka@mail.ru")
    test_page1.enter_content("Hello, world!")
    test_page1.click_button_contact()
    time.sleep(3)

    alert_text = 'Form successfully submitted'
    text = test_page1.get_alert_text()
    assert text == alert_text
