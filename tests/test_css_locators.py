from playwright.sync_api import Page, expect

def test_css_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    item=page.locator("#small-searchterms")
    item.fill("blue jeans")
    item=page.locator("input.button-1.search-box-button")
    expect(item).to_be_visible()
    item.click()
    page.wait_for_timeout(1000)

    page.goto("https://demowebshop.tricentis.com/search?q=blue+jeans")
    item=page.get_by_text("Blue Jeans", exact=True)
    expect(item).to_be_visible()
    item.click()



