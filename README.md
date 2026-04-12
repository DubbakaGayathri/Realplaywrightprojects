

## Features
- Proper explicit waits (`wait_for_url`, `locator.wait_for`, loading bar hidden, etc.)
- Never uses `time.sleep()`
- Uses `pytest` + Playwright sync API
- Clean, commented, refactored code
- All tests green

## Pages Covered
- Dynamic Loading (Example 1 & 2)
- Dynamic Controls
- Login (success + failure with URL wait)
- Locators ,assertions ,actions ,Checkboxes, Dropdown, JavaScript Alerts, Frames, Hovers, Infinite Scroll, File Upload, Sortable Tables

## How to Run
```bash
pip install -r requirements.txt
playwright install
pytest -v
