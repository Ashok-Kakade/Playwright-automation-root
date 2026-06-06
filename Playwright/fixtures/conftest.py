import pytest
import base64

@pytest.fixture
def page():
    from core.driver_factory import DriverFactory
    factory = DriverFactory()
    page_instance, browser, playwright = factory.launch_browser()
    yield page_instance
    browser.close()
    playwright.stop()

def pytest_runtest_logreport(report):
    """
    Resilient v4.x hook that executes right when a test report is logged.
    """
    # Only target the runtime failure phase 
    if report.when == "call" and report.failed:
        # Access the internal pytest-html plugin instance safely
        html = pytest.config.pluginmanager.getplugin("html") if hasattr(pytest, "config") else None
        
        # If running via typical pytest session context:
        if not html:
            # Fallback to fetch from active internal plugin states
            try:
                import sys
                # Grab the running session's config object
                config = item.config if 'item' in locals() else None
            except Exception:
                config = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Standard hook to extract the live browser state and bind it to the report object.
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        if "page" in item.fixturenames:
            try:
                page_instance = item.funcargs["page"]
                
                # Take viewport screenshot with a low timeout barrier
                screenshot_bytes = page_instance.screenshot(full_page=False, timeout=5000)
                encoded = base64.b64encode(screenshot_bytes).decode("utf-8")
                
                html = item.config.pluginmanager.getplugin("html")
                if html:
                    # Construct data-uri string
                    image_data_uri = f"data:image/png;base64,{encoded}"
                    
                    # Attach it cleanly to the report object
                    if not hasattr(report, "extra"):
                        report.extra = []
                    report.extra.append(html.extras.image(image_data_uri, name="Failure Screenshot"))
                    
            except Exception as e:
                print(f"\n[Screenshot Capture Error]: {str(e)}")