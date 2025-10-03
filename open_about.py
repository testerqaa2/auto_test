from playwright.sync_api import sync_playwright, expect

def open_about():
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

            print("2. Open sidebar menu")
            menu_button = page.locator("#react-burger-menu-btn")
            expect(menu_button).to_be_visible()
            menu_button.click()

            print("3. Click About")
            about_link = page.locator("#about_sidebar_link")
            expect(about_link).to_be_visible()
            about_link.click()

            expect(page).to_have_url("https://saucelabs.com/", timeout=10000)
            print("✅ Redirected to saucelabs.com")
            
        except Exception as e:
            current_url = page.url
            print(f"❌ Navigation failed. Current URL: {current_url}")
            print(f"Error: {e}")

        finally:
            browser.close()
            print("4. Browser closed")

if __name__ == "__main__":
    open_about()