from email.policy import strict

from playwright.sync_api import Page, expect

def test_clickaction(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    page.get_by_role("tab",name="Buttons").click(timeout=2000)
    page.get_by_role("button",name="Primary").click(timeout=2000)
    page.get_by_role("button",name="Secondary").click()
    page.get_by_test_id("btn-outline").click()
    page.get_by_role("button",name="Ghost").click()
    page.get_by_role("button",name="Medium").click()
    expect(page.locator("#btnVariantResult")).to_have_text("✅ Clicked: Medium button")

def test_doubleclickaction(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    page.get_by_role("tab", name="Buttons").click(timeout=2000)
    page.evaluate("window.scrollBy(0,600)")
    page.get_by_role("button",name="Double Click me").dblclick()
    page.get_by_role("button",name="Right Click me").click(button="right")
    page.get_by_role("button",name="Hover Over me").hover()
    page.locator("#longPressBtn").click(delay=2000)


def test_keyboardaction(page:Page):
    page.goto("file:///C:/Users/Gayathri/Downloads/playwright_practice.html")
    page.get_by_role("tab", name="Buttons").click(timeout=2000)
    page.evaluate("window.scrollBy(0,900)")
    page.get_by_test_id("key-input").type("gayathri",delay=80)
    page.keyboard.press("Enter")
    page.get_by_test_id("key-input").clear()
    page.get_by_test_id("key-input").type("sana", delay=80)
    page.keyboard.press("Control+A")
    page.get_by_test_id("loading-btn").click()
    expect(page.get_by_test_id("loading-btn")).to_be_disabled()
    expect(page.get_by_test_id("loading-btn")).to_be_enabled()
    expect(page.locator("#loadingResult")).to_have_text("✅ Request complete! Button re-enabled.")
    output=page.locator("#loadingResult").inner_text()
    expect(page.get_by_role("button", name="Delete")).to_be_visible()
    page.get_by_role("button",name="Delete").hover()
    page.wait_for_timeout(3000)
    print(output)

