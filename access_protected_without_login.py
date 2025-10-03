from playwright.sync_api import sync_playwright, expect

def access_protected_without_login():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        try:
            page.goto("https://www.saucedemo.com/cart.html")
            print("1. Go to specific url without login")

            actual_error = page.locator("[data-test='error']").inner_text().strip()
            expected_error= "Epic sadface: You can only access '/cart.html' when you are logged in."

            print("2. Verify actual error message is as expected")
            assert actual_error == expected_error, \
                f"Actual error message isn't as expected. Current: '{actual_error}', Expected: '{expected_error}'"
            print ("✅ Actual & Expected error message is match") 

        finally:
            browser.close()
            print("3. Browser closed")

if __name__ == "__main__":
    access_protected_without_login()