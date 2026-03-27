
from playwright.sync_api import Page,expect

def test_loginpage(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    expect(page).to_have_title("Playwright Practice Lab")
    titleofpage=page.title()
    print(titleofpage)
