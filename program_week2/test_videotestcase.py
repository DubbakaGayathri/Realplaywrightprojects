from playwright.sync_api import expect, Playwright



def test_videotestcase(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)

    context=browser.new_context(record_video_dir="videos/")
    page=context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()
    page.wait_for_timeout(3000)
    context.close()
    browser.close()