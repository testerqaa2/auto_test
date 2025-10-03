from playwright.sync_api import sync_playwright, expect

def login_locked_out_user():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        try:
            page.goto("https://www.saucedemo.com/")
            print("1. Open Web")

            username_field = page.locator("#user-name")
            password_field = page.locator("#password")
            login_button = page.locator("#login-button")

            username_field.fill("locked_out_user")
            print("2. Input locked out username")

            password_field.fill("secret_sauce")
            print("3. Input valid password")

            login_button.click()
            print("4. Click login button")

            actual_error = page.locator("[data-test='error']").inner_text().strip()
            expected_error= "Epic sadface: Sorry, this user has been locked out."

            print("5. Verify actual error message is as expected")
            assert actual_error == expected_error, \
                f"Actual error message isn't as expected. Current: '{actual_error}', Expected: '{expected_error}'"
            print ("✅ Actual & Expected error message is match") 

        finally:
            browser.close()
            print("6. Browser closed")

if __name__ == "__main__":
    login_locked_out_user()