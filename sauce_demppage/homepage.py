from playwright.sync_api import Page, expect

class homepage:
    def __init__(self, page: Page):
        self.page = page




        # Locators
        self.inventory_item=page.locator(".inventory_item")
        self.all_products=page.locator(".inventory_item_name")
        self.cart_button=page.locator("button:has-text('Add to cart')")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.menu_button=page.get_by_role("button", name="Open Menu")
        self.logout_link = page.get_by_role("link", name="Logout")


    def all_products_count(self):
        print("product count:",self.all_products.count())
        return self.all_products.count()
    def all_products_names(self):
        print("products name:",self.all_products.all_text_contents())
        return self.all_products.all_text_contents()
    def add_product(self,productname:str):
        product = self.page.locator(".inventory_item").filter(has_text=productname)
        product.locator("button:has-text('Add to cart')").click()

    def click_cart(self):
        self.cart_icon.click()

    def open_menu(self):
        self.menu_button.click()

    def logout(self):
        self.logout_link.wait_for(state="visible",timeout=5000)
        self.logout_link.click()

