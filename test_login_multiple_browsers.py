from playwright.sync_api import sync_playwright, expect

def test_login_multiple_browsers():
    """Test login on both Chrome and Firefox in one function"""
    browsers = ['chromium', 'firefox']
    
    for browser_type in browsers:
        with sync_playwright() as p:
            if browser_type == 'chromium':
                browser = p.chromium.launch(headless=False)
                browser_name = "Chrome"
            else:
                browser = p.firefox.launch(headless=False)
                browser_name = "Firefox"
                
            context = browser.new_context()
            page = context.new_page()
            
            try:
                print(f"\n=== Testing on {browser_name} ===")
                
                # Navigate to login page
                page.goto("https://www.saucedemo.com/")
                print(f"1. Open Web")

                # Locate elements
                username_field = page.locator("#user-name")
                password_field = page.locator("#password")
                login_button = page.locator("#login-button")

                # Input credentials
                username_field.fill("standard_user")
                print(f"2. Input valid username")

                password_field.fill("secret_sauce")
                print(f"3. Input valid password")

                # Click login button
                login_button.click()
                print(f"4. Click login button")
                print(f"✅  User successfully logged into account")

                page.wait_for_timeout(1000)

                # Verify page title
                actual_page = page.locator("[data-test='title']").inner_text().strip()
                expected_page = "Products"

                print(f"5. Verify actual page is Product page")
                assert actual_page == expected_page, \
                    f"Actual page isn't as expected. Current: '{actual_page}', Expected: '{expected_page}'"
                print(f"💡 Actual page is Product page")

                # Verify first product name
                first_product_name = page.locator("[data-test='inventory-item-name']").first
                expected_product_name = "Sauce Labs Backpack"
                expect(first_product_name).to_have_text(expected_product_name)
                print(f"✅  First Product name match as expected")

            except AssertionError as e:
                actual_product_name = first_product_name.text_content()
                print(f"❌ Product name mismatch! Actual: '{actual_product_name}', Expected: '{expected_product_name}'")
                raise e

            finally:
                browser.close()
                print(f"6. Browser closed")

if __name__ == "__main__":
    test_login_multiple_browsers()