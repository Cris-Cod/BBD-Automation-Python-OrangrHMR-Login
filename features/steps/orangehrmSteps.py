from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given('launch chrome browser')
def launchBrowser(context):
    service_obj = Service()
    context.driver = webdriver.Chrome(service=service_obj)



@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



@then('verify that the logo present on page')
def verifyLogo(context):
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "img[alt='company-branding']")))
    status = context.driver.find_element(By.CSS_SELECTOR, "img[alt='company-branding']").is_displayed()
    print(status)
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
