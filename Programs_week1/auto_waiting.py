from playwright.sync_api import Page,expect

def test_autowait(page:Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading")
    page.get_by_role("link", name="Example 1: Element on page").click()
    loading =page.get_by_role("button",name="Start")
    expect(page.get_by_role("button",name="Start")).to_be_visible()
    loading.click()
    # Wait for loading to complete
    page.locator("#loading").wait_for(state="hidden", timeout=15000)

    # Assert and capture in one go
    expect(page.locator("#finish")).to_have_text("Hello World!", timeout=8000)
    output=page.locator("#finish").inner_text()
    print (output)

def test_autowait2(page:Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading")
    page.get_by_role("link", name="Example 2: Element rendered after the fact").click()
    loading = page.get_by_role("button", name="Start")
    loading.click()
    page.locator("#loading").wait_for(state="hidden", timeout=15000)
    expect(page.locator("#finish")).to_have_text("Hello World!", timeout=8000)
    output = page.locator("#finish").inner_text()
    print(output)



def test_login_with_wait_for_url(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    # Fill login form
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")

    # Click Login → this causes URL change to /secure
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/secure",timeout=2000)








