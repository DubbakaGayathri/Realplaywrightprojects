import pytest
from pathlib import Path
from slugify import slugify


# -----------------------------------
# Screenshot + HTML report integration
# -----------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    # Execute only after test step
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")

        if (report.failed or (report.skipped and xfail)) and "page" in item.funcargs:
            page = item.funcargs["page"]

            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            file_name = slugify(item.nodeid) + ".png"
            screenshot_path = screenshot_dir / file_name

            page.screenshot(path=str(screenshot_path))

            if pytest_html:
                extra.append(pytest_html.extras.png(str(screenshot_path)))

        report.extra = extra
