from playwright.sync_api import sync_playwright, expect

def success_login():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        try:
            page.goto("https://www.saucedemo.com/")
            print("1. Open Web")

            username_field = page.locator("#user-name")
            password_field = page.locator("#password")
            login_button = page.locator("#login-button")

            username_field.fill("standard_user")
            print("2. Input valid username")

            password_field.fill("secret_sauce")
            print("3. Input valid password")

            login_button.click()
            print("4. Click login button")
            print("✅ User successfully logged into account")

            page.wait_for_timeout(1000)

            actual_page = page.locator("[data-test='title']").inner_text().strip()
            expected_page = "Products"

            print("5. Verify actual page is Product page")
            assert actual_page == expected_page, \
                f"Actual page isn't as expected. Current: '{actual_page}', Expected: '{expected_page}'"
            print ("✅ Actual page is Product page") 

            first_product_name = page.locator("[data-test='inventory-item-name']").first
            expected_product_name = "Sauce Labs Backpack"
            expect(first_product_name).to_have_text(expected_product_name)
            print("✅ First Product name match as expected")

        except AssertionError:
            actual_product_name = first_product_name.text_content()
            print(f"❌ Product name mismatch! Actual: '{actual_product_name}', Expected: '{expected_product_name}")

        finally:
            browser.close()
            print("6. Browser closed")

if __name__ == "__main__":
    success_login()