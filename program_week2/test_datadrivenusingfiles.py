from pathlib import Path

from playwright.sync_api import Page,expect
import pytest
import json
data_path = Path(__file__).parent.parent / "testdata" / "data.json"
f=open(data_path,"r")
testdata=json.load(f)


@pytest.mark.parametrize("username,password,validity",[
    (data["username"],data["password"],data["validity"]) for data in testdata
])


def test_datadriven1(username,password,validity,page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button",name="Login").click()
    if validity=="valid":
        expect(page.locator("h6")).to_have_text("Dashboard")
    else:
        expect(page.get_by_text("Invalid credentials", exact=True)).to_be_visible()
