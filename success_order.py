from playwright.sync_api import sync_playwright, expect

def success_order():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        try:
            page.goto("https://www.saucedemo.com/")
            print("1. Open Web")

            username_field = page.locator("#user-name")
            username_field.fill("standard_user")
            print("2. Input valid username")

            password_field = page.locator("#password")
            password_field.fill("secret_sauce")
            print("3. Input valid password")

            login_button = page.locator("#login-button")
            login_button.click()
            print("4. Click login button")
            print("✅ User successfully logged into account")

            page.wait_for_timeout(1000)

            print("5. Add product to cart")
            add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
            expect(add_to_cart_button).to_be_visible()
            expect(add_to_cart_button).to_have_text("Add to cart")
            add_to_cart_button.click()
            print("✅ One product added to cart")

            cart_badge_value = page.locator(".shopping_cart_badge")
            expect(cart_badge_value).to_be_visible()
            expect(cart_badge_value).to_have_text("1")
            print("✅ Product added to cart = 1")
            
            print("6. Open cart page")
            cart_icon = page.locator("[data-test='shopping-cart-link']")
            cart_icon.click()
            title_cart_page = page.locator("text=Your Cart")
            expect(title_cart_page).to_be_visible()
            product_name = "Sauce Labs Backpack"
            expect(page.locator("[data-test='inventory-item-name']")).to_have_text(product_name)
            print("✅ Cart page loaded with correct item")
            
            print("7. Click Checkout button")
            checkout_button = page.locator("#checkout")
            checkout_button.click()

            print("8. Input user information")
            page.fill("#first-name", "Frisca")
            page.fill("#last-name", "Cantik")
            page.fill("#postal-code", "1234")
            print("✅ Checkout form filled")

            print("9. Click Checkout button")
            page.click("[data-test='continue']")

            print("10. Click Finish")
            finish_button = page.locator("#finish")
            finish_button.click()

            complete_header = page.locator("[data-test='complete-header']")
            expect(complete_header).to_have_text("Thank you for your order!")
            complete_desc = page.locator("[data-test='complete-text']")
            expect(complete_desc).to_contain_text("Your order has been dispatched")
            print("✅ Order completed successfully")
            
            print("11. Back Home Yuhuu")
            back_home = page.locator("#back-to-products")
            back_home.click()
            
            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
            expect(page.locator(".inventory_list")).to_be_visible()

        finally:
            browser.close()
            print("12. Browser closed")

if __name__ == "__main__":
    success_order()