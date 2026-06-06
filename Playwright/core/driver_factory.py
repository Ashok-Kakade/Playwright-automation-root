import pytest
from playwright.sync_api import sync_playwright

class DriverFactory:
    def launch_browser(self):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False ,args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)
        return page, browser, playwright
    
    @pytest.fixture(autouse=True)
    def set_default_timeout(page):
        page.set_default_timeout(100000)
            