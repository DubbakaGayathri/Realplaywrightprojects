from playwright.sync_api import Page,expect

def test_reg(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    page.get_by_placeholder("Ravi").fill("gayathri")
    page.get_by_label("Last Name").fill("dubbaka")
    page.get_by_role("button",name="Create Account").click()
    expect(page.get_by_text("Account created for gayathri dubbaka!")).to_be_visible()
    print("done reg")