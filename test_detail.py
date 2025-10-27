from asyncio import wait_for
import asyncio
from playwright.sync_api import sync_playwright, expect

def test_vision():
    "Testing on both Chrome and Firefox in one function"
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

                page.goto("https://www.visionplus.id/webclient/")
                print("1. Buka Web")
                page.wait_for_timeout(500)
                
                home_text = page.get_by_text("Home")
                expect(home_text).to_have_text('Home')
                print("2. ✅ Text Home tampil")

                first_item = page.locator("div.node-poster").first
                first_item.click()
                print("3. Buka Detail Movie")
                page.wait_for_timeout(2000)

                trailer_text = page.get_by_text("Trailer")
                expect(trailer_text).to_be_visible()
                print("4. ✅ Text Trailer tampil")

                trailer_section = page.locator("div.cell-info")
                section_count = trailer_section.count()

                if section_count > 0:
                    print(f"✅ Ada {section_count} trailer section")
                else:
                    print("❌ Tidak ada trailer section")

                trailer_section.nth(2).click()
                print("5. Buka Trailer Movie")

                watch_button = page.locator('button.iris-raised-button:has-text("Watch")')
                is_visible = watch_button.is_visible()
                print("✅ Tombol Watch tampil")

                if is_visible : 
                    event_page = context.wait_for_event('page') 
                    watch_button.click()
                    print("✅ Tombol Watch berhasil diklik")

                    new_page = asyncio.wait_for(event_page, timeout=10000)
                    new_page.wait_for_load_state()
                    new_url = new_page.url
                    print("URL baru: {new_url}")                    
            
                expected_login_url = "supports.visionplus.id/yplus/auth/login"
                if expected_login_url in new_url:
                    print("✅ Berhasil redirect ke halaman login")
                else:
                    print("❌ URL tidak sesuai. Expected: {expected_login_url}, Actual: {new_url}")

            finally:
                browser.close()
                print("Browser closed")

if __name__ == "__main__":
    test_vision()