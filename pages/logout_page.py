from playwright.sync_api import Page

class LogoutPage:
    def __init__(self, page:Page):
        self.page = page
        self.logout_option = page.get_by_role("link", name= "Log out", exact = True)

    def click_logout(self):
        self.logout_option.click()