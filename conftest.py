import pytest
import allure
from pathlib import Path
from slugify import slugify


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")

        if (report.failed or (report.skipped and xfail)) and "page" in item.funcargs:
            page = item.funcargs["page"]

            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            file_name = slugify(item.nodeid) + ".png"
            screenshot_path = screenshot_dir / file_name

            # Take screenshot
            page.screenshot(path=str(screenshot_path))

            # Attach to pytest-html report
            if pytest_html:
                extra.append(pytest_html.extras.png(str(screenshot_path)))

            # Attach to Allure report
            allure.attach.file(
                str(screenshot_path),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        report.extra = extra