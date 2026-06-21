from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.login = self.page.get_by_role("link", name="Log in", exact=True)
        self.username = self.page.locator("#loginusername")
        self.password = self.page.locator("#loginpassword")
        self.login_button = self.page.get_by_role("button",name="Log in", exact=True)

    def click_login(self):
        self.login.click()

    def input_username(self, u_name):
        self.username.fill("")
        self.username.fill(u_name)

    def input_password(self, p_word):
        self.password.fill("")
        self.password.fill(p_word)

    def click_login_button(self):
        self.login_button.click()

    def do_login(self, u_name, p_word):
        self.click_login()
        self.input_username(u_name)
        self.input_password(p_word)
        self.click_login_button()






