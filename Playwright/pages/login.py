
from core.base_page import BasePage
from config.settings import settings

class Login(BasePage):
    def __init__(self, page):
        super().__init__(page)
            
        self.user_input = "//input[@type='email']"
        self.password = "//input[@name='passwd']"
        self.login_button = "Sign in"
        self.confirmation_yes = "Yes"
        self.ms_user = "//div[@data-test-id = 'qatest@ngdata.com']"
        self.lightbox = "//div[@class='sign-in-box ext-sign-in-box fade-in-lightbox']"

    def app_login(self, username, password):
        self.page.goto(settings.BASE_URL)
        self.wait_until_page_load()
        self.fill(self.user_input, username)
        self.click_by_text(self.login_button)
        self.wait_until_page_load()
        self.click(self.ms_user)
        self.fill(self.password, password)
        self.click_by_text(self.login_button)
        self.wait_for_element_visible(self.lightbox)
        self.click_by_text(self.login_button)
        self.wait_until_page_load()
        self.click_by_text(self.confirmation_yes)
        self.wait_until_page_load()
        self.select_tenant()


         