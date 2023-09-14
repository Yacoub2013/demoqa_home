from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
class SwagLab(BasePage):

    def exist_icon(self):

        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True
    def click_icon(self):
        self.find_element(locator='div.login_logo').click()


    def exist_user_name(self):

        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True

    def exist_password(self):

        try:
            self.find_element(locator='#login_button_container > div > form > div.error-message-container')
        except NoSuchElementException:
            return False
        return True