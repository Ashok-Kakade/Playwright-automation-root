from playwright.sync_api import sync_playwright

# p = sync_playwright().start()
# browser = p.chromium.launch(headless=False ,args=["--start-maximized"])
# page = browser.new_page(no_viewport=True)
# page.goto("https://qa04.dev.ngdata.com/auth/login")
# page.wait_for_load_state("networkidle")
# print(page.title())
# page.locator("//input[@name='email']").fill("qatest@ngdata.com") 
# page.locator("//button[@type='submit']").click()
# page.wait_for_load_state("networkidle")
# page.locator("//div[@data-test-id = 'qatest@ngdata.com']").click()
# page.locator("//input[@name='passwd']").wait_for(state='visible')
# page.locator("//input[@name='passwd']").fill('656KvjhjugSTCvgujJKYIU5G')
# page.locator("//input[@type='submit']").click()
# page.locator("//div[@class='sign-in-box ext-sign-in-box fade-in-lightbox']").wait_for(state='visible')
# page.locator("//input[@type='submit']").click()
# page.wait_for_load_state("networkidle")
# page.locator("//button[@id='options']").wait_for(state='visible')
# page.locator("//button[@id='options']").click()
# page.locator("//ul//a").filter(has_text="Tenant 1").click()
# page.locator("//button[@type='submit']").click()
# page.wait_for_load_state("networkidle")
# page.locator("//button[@type='submit']").wait_for(state="visible")
# print(page.title())
# print(page.url)

# #-------------------------------
# # click by name / property
# page.locator("//button[@type='button' and contains(@class, 'nav-toolbar__minimize')]").click()
# page.get_by_role("link", name="Experience management", exact=True).click()
# page.locator("//div[@data-ng='experience-management-offers']").wait_for(state='visible')

# print()


# implemented framework structure - understand it
# implement pytest and fixtures
# implement framework resources
# automate basic scenarios
# start with api
import subprocess
import time

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
user_data = r"C:\selenium\chrome_profile"

# Launch Chrome in the background
subprocess.Popen([
    chrome_path, 
    "--remote-debugging-port=9222", 
    f"--user-data-dir={user_data}"
])


from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.connect_over_cdp("http://localhost:9222")

context = browser.contexts[0]
page = context.pages[0]

page.goto("https://qa03.dev.ngdata.com/")

print(f"Successfully connected! Current page: {page.title()}")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Selenium connects to the SAME instance Playwright just used
driver = webdriver.Chrome(options=chrome_options)

# You are now in the same session, already logged in
print("Selenium title:", driver.title)
driver.find_element(By.XPATH, "//input[@placeholder='Email address']").send_keys('qatest@ngdata.com')
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("done")