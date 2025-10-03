from playwright.sync_api import sync_playwright, expect

def blank_username_password():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        try:
            page.goto("https://www.saucedemo.com/")
            print("1. Open Web")

            username_field = page.locator("#user-name")
            password_field = page.locator("#password")
            login_button = page.locator("#login-button")

            expect(username_field).to_be_visible()
            print("2. Username field is visible")

            expect(password_field).to_be_visible()
            print("3. Password field is visible")

            expect(login_button).to_be_visible()
            print("4. Login Button is visible")

            login_button.click()
            print("5. Click login button without input username & password")

            actual_error = page.locator("[data-test='error']").inner_text().strip()
            expected_error= "Epic sadface: Username is required"

            print("6. Verify actual error message is as expected")
            assert actual_error == expected_error, \
                f"Actual error message isn't as expected. Current: '{actual_error}', Expected: '{expected_error}'"
            print ("✅ Actual & Expected error message is match") 

        finally:
            browser.close()
            print("7. Browser closed")

if __name__ == "__main__":
    blank_username_password()