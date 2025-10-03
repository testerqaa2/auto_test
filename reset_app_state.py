from playwright.sync_api import sync_playwright, expect

def reset_app_state():
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

            print("5. Add product to cart")
            add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
            expect(add_to_cart_button).to_be_visible()
            expect(add_to_cart_button).to_have_text("Add to cart")
            add_to_cart_button.click()
            print("✅ One product added to cart")

            cart_badge = page.locator(".shopping_cart_badge")
            expect(cart_badge).to_be_visible()
            expect(cart_badge).to_have_text("1")
            print("✅ Cart badge shows '1'")

            cart_badge = page.locator(".shopping_cart_badge")
            cart_badge.is_visible()
            initial_count = cart_badge.text_content()
            print(f"Cart already has {initial_count} items, deleting by reset app state ...")
            page.click("#react-burger-menu-btn")
            page.wait_for_timeout(1000)
            page.click("#reset_sidebar_link")
            page.wait_for_timeout(1000)
            page.click("#react-burger-cross-btn")
            page.wait_for_timeout(1000)
            print("✅ Cart is empty (Reset app state done!)")

        finally:
            browser.close()
            print("6. Browser closed")

if __name__ == "__main__":
    reset_app_state()