from playwright.sync_api import Page,expect

def test_assertions(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    expect(page).to_have_title("Playwright Practice Lab")
    expect(page).to_have_url("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    expect(page.get_by_role("button",name="Sign In")).to_be_visible()
    page.get_by_role("button", name="Sign In").click()
    expect(page.locator("#fileResult")).to_have_text("No file selected")
    inputname =page.get_by_label("First Name")
    inputname.fill("gayathri")
    expect(inputname).to_have_value("gayathri")
    page.get_by_role("tab",name="Buttons").click(timeout=2000)
    page.evaluate("window.scrollBy(0,800)")
    expect(page.get_by_role("button",name="Disabled")).to_be_disabled()
    page.get_by_role("button", name="Submit & Wait").click(timeout=2000)
    expect(page.get_by_role("button", name="Submit & Wait")).to_be_enabled()
