from playwright.sync_api import Page,expect

def test_reportstestcase(page:Page):
    page.goto("https://www.qa-practice.com/")
    expect(page.locator("h1:has-text('Hello!')")).to_be_visible()
    page.get_by_text("Forms", exact=True).click()
    page.get_by_role("link", name="Practice Form").click()
    page.get_by_label("First Name").fill("Gayathri")
    page.get_by_label("Last Name").fill("R")
    page.get_by_label("Email").fill("sana@gmail.com")
    page.get_by_role("radio", name="Female").check()
    page.get_by_placeholder("Mobile Number").fill("1231231231")
    page.locator("#submit-id-submit").click()
    page.locator("button:has-text('Close')").click()

def test_reportstestcase1(page:Page):
    page.goto("https://www.qaplayground.com/")
    expect(page.get_by_role("heading", name="Master Automation Testing With PlayGround")).to_be_visible()
