from playwright.sync_api import Page,expect

class logintestpage:

    def __init__(self,page:Page):
        self.page=page
        self.username=page.get_by_label("Username")
        self.password=page.get_by_label("Password")
        self.login_button=page.get_by_role("button",name="Submit")

    def loginpage(self,username:str,password:str):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")
        self.username.fill("student")
        self.password.fill("Password123")
        self.login_button.click()
        expect(self.page.locator("h1")).to_have_text("Logged In Successfully")
        expect(self.page.locator("#loop-container > div > article > div.post-content > p.has-text-align-center")).to_contain_text("Congratulations student. You successfully logged in!")
        output=self.page.locator("h1").inner_text()
        print(output)
