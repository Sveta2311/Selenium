from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/input""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/text""")
    LOCATOR_SAVE_BTN = (By.XPATH, """*[@id="create-item"]/div/div/div[7]/div/button/span/""")
    LOCATOR_RES_LBL = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_NAME = (By.XPATH, """[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_MAIL = (By.XPATH, """[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT = (By.XPATH, """[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_SEND = (By.XPATH, """[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):

    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_user_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=2)
        text = user_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_HELLO[1]}")
        return text

    def click_new_post_btn(self):
        logging.info("Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_title(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_DESCRIPTION[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_save_btn(self):
        logging.info("Click save button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

    def get_res_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_RES_LBL, time=2)
        text = user_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_RES_LBL[1]}")
        return text

    def click_contact_link(self):
        logging.info("Click contact link")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def enter_contact_name(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTACT_NAME[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME)
        login_field.clear()
        login_field.send_keys(word)

    def enter_contact_mail(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTACT_MAIL[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_MAIL)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content_content(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_contact_send_btn(self):
        logging.info("Click send contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_SEND).click()

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text








