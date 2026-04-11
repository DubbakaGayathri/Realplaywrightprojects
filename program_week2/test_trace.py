from playwright.sync_api import expect, Playwright



def test_tracecase(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)

    context=browser.new_context()
    context.tracing.start(screenshots=True,snapshots=True)
    page=context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()
    page.wait_for_timeout(3000)

    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()