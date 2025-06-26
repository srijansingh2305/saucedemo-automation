def test_checkout(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("class name", "shopping_cart_link").click()
    driver.find_element("id", "checkout").click()

    driver.find_element("id", "first-name").send_keys("Srijan")
    driver.find_element("id", "last-name").send_keys("Singh")
    driver.find_element("id", "postal-code").send_keys("12345")
    driver.find_element("id", "continue").click()
    driver.find_element("id", "finish").click()

    assert "Thank you for your order!" in driver.page_source
