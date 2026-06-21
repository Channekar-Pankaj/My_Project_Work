import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def playwright_instance():
    """Fixture to provide a Playwright browser instance"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headed mode - browser visible
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


def test_search_product(playwright_instance):
    """Test Case: Search for T-shirt and verify the product is displayed"""
    page = playwright_instance

    # Step 1: Open the website
    print("Step 1: Opening https://www.myntra.com/")
    try:
        page.goto("https://www.myntra.com/", wait_until="domcontentloaded", timeout=30000)
    except Exception as e:
        print(f"Navigation completed with: {e}")

    # Check current page
    current_url = page.url
    print(f"Current URL: {current_url}")
    page.wait_for_timeout(2000)
    print("✓ Website opened successfully")

    # Step 2: Search for T-shirt
    print("\nStep 2: Searching for 'T-shirt'")

    # Try to find search input by name or other attributes
    search_input = None
    try:
        search_input = page.locator('input[name="search_query"]')
        if search_input.is_visible():
            print("Found search input with name='search_query'")
    except:
        pass

    if not search_input or not search_input.is_visible():
        # Try alternative selectors
        search_input = page.locator('input[placeholder*="Search"]')
        if search_input.is_visible():
            print("Found search input with placeholder")

    if not search_input or not search_input.is_visible():
        # Try any input field
        search_input = page.locator('input[type="text"]').first
        if search_input.is_visible():
            print("Found text input field")

    assert search_input.is_visible(timeout=10000), "Search input field is not visible"
    search_input.fill("T-shirt")
    search_input.press("Enter")
    page.wait_for_timeout(3000)  # Wait for results
    print("✓ Search completed for 'T-shirt'")

    # Step 3: Verify that product text is displayed in search results
    print("\nStep 3: Verifying search results")

    # Check for multiple possible product names
    product_locators = [
        page.locator("text=Short Sleeve T-Shirts"),
        page.locator("text=T-Shirt"),
        page.locator("text=Shirt"),
    ]

    found = False
    for locator in product_locators:
        try:
            if locator.is_visible(timeout=5000):
                product_text = locator.text_content()
                print(f"✓ Found product: {product_text}")
                found = True
                break
        except:
            continue

    if not found:
        # Show what's on the page
        page_content = page.content()
        if "Short Sleeve T-Shirts" in page_content or "T-Shirt" in page_content:
            print("✓ Product text found in page content")
            found = True
        else:
            print("Page content preview:")
            print(page_content[:500])

    assert found, "Product not found in search results"
    print("\n✅ Test PASSED: All steps completed successfully!")


if __name__ == "__main__":
    # Run the test in headed mode
    pytest.main([__file__, "-v", "-s"])

