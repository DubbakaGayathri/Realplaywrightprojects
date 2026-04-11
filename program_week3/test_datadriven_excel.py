from pathlib import Path

from playwright.sync_api import Page,expect
import pytest
import openpyxl

login_data=[]
workbook=openpyxl.load_workbook(Path(__file__).parent.parent / "testdata" / "data.xlsx")
sheet=workbook.active
for row in sheet.iter_rows(min_row=2,values_only=True):
    username,password,validity=row
    login_data.append((
        str(username or ""),
        str(password or ""),
        str(validity or "")
    ))

workbook.close()

@pytest.mark.parametrize("username,password,validity",login_data)

def test_datadriven1(username,password,validity,page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button",name="Login").click()
    if validity=="valid":
        expect(page.locator("h6")).to_have_text("Dashboard")
    else:
        expect(page.get_by_text("Invalid credentials", exact=True)).to_be_visible()
