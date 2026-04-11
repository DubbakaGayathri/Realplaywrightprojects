from playwright.sync_api import Page,expect
import datetime

def test_videotestcase(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    timestamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    page.screenshot(path=f"screenshot/homepage_{timestamp}.png")
    page.screenshot(path=f"screenshot/homepage_{timestamp}.png",full_page=True)
    logo=page.locator("img[alt='Tricentis Demo Web Shop']")
    logo.screenshot(path=f"screenshot/logo_{timestamp}.png")