from playwright.sync_api import Page,expect

def test_dropdown(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    page.get_by_role("tab", name="Dropdowns").click(timeout=2000)
    page.evaluate("window.scrollBy(0,600)")
    page.get_by_label("Select City").select_option(index=2)
    page.get_by_label("Job Role").select_option(label="QA Engineer")
    page.get_by_test_id("skills-select").select_option(["Cypress","pytest","JIRA"])
    page.get_by_test_id("custom-dropdown-trigger").click()
    page.get_by_test_id("opt-playwright").click()
    page.wait_for_timeout(2000)

