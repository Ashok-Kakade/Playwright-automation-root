from pages.login import Login
from core.driver_factory import DriverFactory

def test_login():
    factory = DriverFactory()
    page, browser, playwright = factory.launch_browser()
    
    login_page = Login(page)
    # login_page.app_login('tomsmith', 'SuperSecretPassword!')
    login_page.app_login('qatest@ngdata.com', '656KvjhjugSTCvgujJKYIU5G')    
    assert "NGDATA IEP" in page.title()    
    browser.close()
    playwright.stop()

