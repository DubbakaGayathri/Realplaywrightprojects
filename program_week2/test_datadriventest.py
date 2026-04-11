import pytest

login_username=[("Admin","admin123","valid"),("Admin","admin1234","invalid"),("Admin","admin12345","invalid")]

from playwright.sync_api import Page,expect


@pytest.mark.parametrize("username,password,validity",login_username)
def test_reportstestcase(username,password,validity ,page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button",name="Login").click()
    if validity=="valid":
        expect(page.locator("h6")).to_have_text("Dashboard")
    else:
        expect(page.get_by_text("Invalid credentials", exact=True)).to_be_visible()
    page.wait_for_timeout(3000)