from playwright.sync_api import Page,expect

class loginpage:

    def __init__(self,page:Page):
        self.page = page
        self.username=page.get_by_label("Username")
        self.password=page.get_by_label("Password")
        self.login=page.get_by_role("button",name="Login")
        self.flash=page.locator("#flash")


    def test_login(self,username:str,password:str):
        self.page.goto("https://the-internet.herokuapp.com/login")
        self.username.fill(username)
        self.password.fill(password)
        self.login.click()
        self.page.wait_for_url("**/secure")
        expect(self.page.locator("h2")).to_have_text("Secure Area")
        expect(self.flash).to_contain_text("You logged into a secure area!")
