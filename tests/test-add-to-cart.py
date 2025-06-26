def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("class name", "shopping_cart_link").click()

    cart_items = driver.find_elements("class name", "cart_item")
    assert any("Sauce Labs Backpack" in item.text for item in cart_items)
