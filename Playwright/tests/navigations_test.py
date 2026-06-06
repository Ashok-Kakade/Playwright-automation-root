from pages.login import Login
from core.driver_factory import DriverFactory
from pages.Navigations import Navigations

# def test_navigations():
#     factory = DriverFactory()
#     page, browser, playwright = factory.launch_browser()
#     navigations = Navigations(page)
    
#     login_page = Login(page)
#     login_page.app_login('qatest@ngdata.com', '656KvjhjugSTCvgujJKYIU5G')
#     assert "NGDATA IEP" in page.title()

#     navigations.wait_until_page_load()
#     navigations.check_page_title('Insights')

#     navigations.click(navigations.build_identifier('Experience management'))
#     navigations.wait_for_text('Experience management')

#     navigations.click(navigations.build_identifier('Exports'))
#     navigations.wait_for_text('Exports')

#     navigations.click(navigations.build_identifier('Customer'))
#     navigations.wait_for_text('Customer DNA')

#     navigations.click(navigations.build_identifier('Product'))
#     navigations.wait_for_text('Product DNA')

#     browser.close()
#     playwright.stop()

def test_navigations(page):
    # REMOVED: manual DriverFactory launch lines
    
    navigations = Navigations(page)
    login_page = Login(page)
    
    login_page.app_login('qatest@ngdata.com', '656KvjhjugSTCvgujJKYIU5G')
    assert "NGDATA IEP" in page.title()

    navigations.wait_until_page_load()
    navigations.check_page_title('Insights')

    navigations.click(navigations.build_identifier('Experience management'))
    navigations.wait_for_text('Experience management')

    navigations.click(navigations.build_identifier('Exports'))
    navigations.wait_for_text('Exports')

    navigations.click(navigations.build_identifier('Customer'))
    navigations.wait_for_text('Customer DNA')

    navigations.click(navigations.build_identifier('Product'))
    navigations.wait_for_text('Product DNA')





    
    
