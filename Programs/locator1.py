from playwright.sync_api import Page,expect

def test_locatorstesting(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    page.get_by_label("Email").fill("gaya@gmail.com")
    page.get_by_label("Password").fill("123456")
    page.get_by_role("button",name="Sign In").click()
    page.wait_for_timeout(3000)

