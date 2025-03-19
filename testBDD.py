from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Background: Set up before running tests
def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

# Step Definitions
@given("I am on the login page")
def step_impl(context):
    assert "Swag Labs" in context.driver.title

@when("I log in with valid credentials")
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

@when("I add a product to the cart")
def step_impl(context):
    add_to_cart_button = context.driver.find_element(By.XPATH, "//button[text()='Add to cart']")
    add_to_cart_button.click()
    time.sleep(2)

@then("the button should change to \"Remove\"")
def step_impl(context):
    updated_button = context.driver.find_element(By.XPATH, "//button[text()='Remove']")
    assert updated_button.text == "Remove", "Button did not change to Remove"

@then("the cart badge should show \"1\"")
def step_impl(context):
    cart_badge = context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Cart count is incorrect"

# Teardown: Close the browser after tests
def after_all(context):
    context.driver.quit()