from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given('I launch Chorme browser')
def step_impl(context):
    service_obj = Service()
    context.driver = webdriver.Chrome(service=service_obj)

@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
    context.driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(user)
    context.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()


@then(u'User must succesfully login to the Dashboard page')
def step_impl(context):
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']/h6")))
    txt_dashboard = context.driver.find_element(By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']/h6").text
    assert txt_dashboard == "Dashboard"
    context.driver.close()
