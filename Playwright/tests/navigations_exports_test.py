from pages.login import Login
from core.driver_factory import DriverFactory
from pages.Navigations import Navigations

def test_navigations():
    factory = DriverFactory()
    page, browser, playwright = factory.launch_browser()
    navigations = Navigations(page)
    
    login_page = Login(page)
    login_page.app_login('qatest@ngdata.com', '656KvjhjugSTCvgujJKYIU5G')
    assert "NGDATA IEP" in page.title()

    navigations.wait_until_page_load()

    navigations.click(navigations.build_identifier('Exports'))
    navigations.wait_for_text('Exports')


    browser.close()
    playwright.stop()





    
    
