from playwright.sync_api import Page

class HomePage:
    def __init__(self,page:Page):
        self.page=page
        self.cart_list = page.locator("#cartur")
        self.select_product = page.get_by_role("link" , name = "Samsung galaxy s6", exact = True)
        # self.add_to_cart = page.get_by_role("link", name= "Add to cart", exact = True)

    def add_product_to_cart(self):
        self.select_product.click()

    # def add_to_cart(self):
    #     self.page.on("dialog", lambda d: d.accept())
    #     self.add_to_cart.click()
    #
    def view_cart_list(self):
        self.cart_list.click()

    # def add_product_to_cart_and_view_cart(self):
    #     self.add_product_to_cart()
    #     self.add_to_cart()
    #     self.view_cart_list()