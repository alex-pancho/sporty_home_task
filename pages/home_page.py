from locators import HomePageLocator


class HomePage(HomePageLocator):

    def __init__(self, driver, URL = ""):
        super().__init__(driver)
        self.main_page_url = URL + "/login"

    def enter_email(self, email):
        email_field = self.item.input_email_locator
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.item.input_password_locator
        password_field.send_keys(password)

    def click_login(self):
        self.item.login_button_locator.click()

    def is_error_message_presented(self):
        return self.item.error_message_locator.is_displayed()

    def is_still_on_login_page(self):
        return self.driver.current_url == self.main_page_url

    def is_logout_button_presented(self):
        return self.item.logout_button_locator.is_displayed()


if __name__ == "__main__":
    driver = ""
    my_home = HomePage(driver)
    item = my_home.item.menu_home
    print(item)
