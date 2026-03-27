from playwright.sync_api import Page,expect
def test_form(page:Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.locator("#dateOfBirthInput").click()
    page.wait_for_selector(".react-datepicker", timeout=10000)

    # === Select Year (2009) ===
    year_dropdown = page.locator(".react-datepicker__year-select")
    year_dropdown.select_option("2009")
    month_dropdown = page.locator(".react-datepicker__month-select")
    month_dropdown.select_option("March")
    day = page.locator(".react-datepicker__day").filter(has_text="15").first
    day.click()
    page.wait_for_timeout(5000)
