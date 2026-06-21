from playwright.sync_api import Page
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


@pytest.mark.parametrize("u_name, p_name", [("pankaj8", "channekar"), ("nayana11", "dhone"), ("gauri28", "dhone")])
def test_login_page(page: Page, u_name, p_name):
    page.goto("https://demoblaze.com/index.html")
    login__page = LoginPage(page)
    login__page.do_login(u_name, p_name)

    home__page = HomePage(page)
    home__page.add_product_to_cart()
    home__page.view_cart_list()

    logout__page = LogoutPage(page)
    logout__page.click_logout()
