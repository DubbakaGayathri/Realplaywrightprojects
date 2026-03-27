from playwright.sync_api import Page,expect

def test_checkbox(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    page.get_by_role("tab", name="Checks & Radios").click(timeout=2000)
    page.get_by_label("Python").check()
    page.get_by_label("Pytest").check()
    page.get_by_label("Playwright").check()
    expect(page.get_by_label("Playwright")).to_be_checked()
    page.get_by_label("Pytest").uncheck()
    page.get_by_role("button",name="Uncheck All").click()

def test_radiobutton(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    page.get_by_role("tab", name="Checks & Radios").click(timeout=2000)
    page.evaluate("window.scrollBy(0,900)")
    page.get_by_test_id("radio-mid").check()
    expect(page.get_by_test_id("radio-mid")).to_be_checked()




