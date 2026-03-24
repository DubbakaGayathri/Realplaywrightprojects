from playwright.sync_api import Page,expect

def test_reg(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    page.evaluate("window.scrollTo(0,900)")
    page.wait_for_timeout(500)
    page.get_by_label("Upload file").set_input_files("C:\\Users\\Gayathri\\OneDrive\\Documents\\Gayathri_Dubbaka_Resume_Manual QA.docx")
    page.wait_for_timeout(5000)
