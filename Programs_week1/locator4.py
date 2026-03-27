from playwright.sync_api import Page,expect

def test_locator4(page:Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button",name="Login").click()
    page.wait_for_timeout(5000)

def test_filters(page:Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    buttons =page.get_by_role("button",name="Add Element")
    for _ in range(5):
        buttons.click()
    delete_button=page.get_by_role("button",name="Delete")
    expect(delete_button).to_have_count(5)
    delete_button.first.click()
    delete_button.nth(1).click()
    page.wait_for_timeout(5000)


