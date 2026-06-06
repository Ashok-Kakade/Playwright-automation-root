from core.base_page import BasePage

class Navigations(BasePage):
    def __init__(self, page):
        super().__init__(page)
       
        self.page_title = "//h2[@data-ng='page-wrapper-title']"
        self.navigation_menu = "//a[@role='link']//div[text()='$']"
        

    def build_identifier(self, menu_name):
        return self.navigation_menu.replace("$", menu_name)
    
    def check_page_title(self, menu_name):
        self.check_element_text(self.page_title, menu_name)
        