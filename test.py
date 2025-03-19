from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#setup Webdriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#login 
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

#add product(s) to cart
add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
add_to_cart_button.click()
time.sleep(3)

#check if button text changed or not
add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='Remove']")
assert add_to_cart_button.text == "Remove", "Button didn't change to 'Remove'"

#check if cart badge updated to the product(s) added or not
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
assert cart_badge.text == "1", "Cart count didn't update accordingly"

#access to Cart screen
cart_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
)
cart_link.click()
time.sleep(3)

#check product details: name, description, price
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
)
cart_item = driver.find_element(By.CLASS_NAME, "cart_item")
product_name = cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text
product_desc = cart_item.find_element(By.CLASS_NAME, "inventory_item_desc").text
product_price = cart_item.find_element(By.CLASS_NAME, "inventory_item_price").text

assert product_name != "", "Product name is missing!"
assert product_desc != "", "Product description is missing!"
assert product_price != "", "Product price is missing!"

#click Checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(3)

#fill in the required information (using unique data)
driver.find_element(By.ID, "first-name").send_keys("Jordan")
driver.find_element(By.ID, "last-name").send_keys("Lee")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()
time.sleep(3)

#check the product details again: name, description and price
summary_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
summary_desc = driver.find_element(By.CLASS_NAME, "inventory_item_desc").text
summary_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

assert summary_name == product_name, "Product's name mismatch!"
assert summary_desc == product_desc, "Product's description mismatch!"
assert summary_price == product_price, "Product's price mismatch!"

#click Finish
driver.find_element(By.ID, "finish").click()
time.sleep(3)

#checkout complete
checkout_complete = driver.find_element(By.CLASS_NAME, "complete-header").text
assert checkout_complete == "Thank you for your order!", "Checkout didn't complete successfully!"

print("Tests passed: automation completed successfully!!!")

driver.quit()