from playwright.sync_api import Page,expect

class loginpage:
    def __init__(self, page:Page):
        self.page=page
        self.username=page.get_by_placeholder("Username")
        self.password=page.get_by_placeholder("Password")
        self.login_button=page.locator("#login-button")

    def login_test(self,user:str,password:str):
        self.page.goto("https://www.saucedemo.com/")
        self.username.clear()
        self.username.type(user,delay=80)
        self.password.clear()
        self.password.type(password,delay=80)
        self.login_button.click()
        self.page.wait_for_timeout(2000)

    

