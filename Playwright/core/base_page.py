
class BasePage():
    def __init__(self, page:object):
        self.page = page
        self.title_identifier = "//h2[text()='$']"

    def build_title_identifier(self, text):
        return self.title_identifier.replace("$", text)
    def build_identifier_by_text(self, text:str):
        return self.page.get_by_text(text)

    def click(self, locator):
        self.page.click(locator)

    def click_by_text(self, text:str):
        self.build_identifier_by_text(text).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)
        
    def wait_until_page_load(self):
        self.page.wait_for_load_state("networkidle", timeout=100000)

    def wait_for_element_visible(self, locator):
        self.page.locator(locator).wait_for(state='visible', timeout=100000)
    
    def check_element_text(self, locator, expected_text):
        actual_text = self.page.locator(locator).inner_text()
        assert actual_text == expected_text, f"Expected text: {expected_text}, but got: {actual_text}"

    def get_element_text(self, locator):
        return self.page.locator(locator).inner_text()

    def wait_for_text(self, expected_text):       
        self.page.locator(self.build_title_identifier(expected_text)).wait_for(state='visible', timeout=150000)
        actual_text = self.get_element_text(self.build_title_identifier(expected_text))
        assert actual_text == expected_text, f"Expected text: {expected_text}, but got: {actual_text}"

    def is_enabled(self, locator):
        self.page.locator(locator).is_enabled()

    def select_tenant(self):
        self.click_by_text('Select tenant')
        self.wait_for_element_visible("//ul[@class='dropdown-menu show']")
        self.click_by_text('Tenant 1')
        self.click("//button[text()='Select']")