import re
from playwright.sync_api import Page, expect


def test_add_to_cart_and_verify_details(page: Page) -> None:
    # Test data
    SEARCH_TERM = "hammer"
    QUANTITY = "5"
    WAIT_TIMEOUT = 1000  # milliseconds

    # Open the main page
    page.goto("https://practicesoftwaretesting.com/")
    
    # Search for product
    search_input = page.locator("[data-test=\"search-query\"]")
    search_input.fill(SEARCH_TERM)
    page.locator("[data-test=\"search-submit\"]").click()

    # Wait for search results
    page.wait_for_timeout(WAIT_TIMEOUT)
    
    # Sort by price (high to low)
    page.locator("[data-test=\"sort\"]").select_option("price,desc")

    # Wait for sorted results
    page.wait_for_timeout(WAIT_TIMEOUT)
    
    # Open the first product
    first_product = page.locator("[data-test^=\"product-\"]").first
    first_product.click()
    
    # Save product details
    product_title = page.locator('[data-test="product-name"]').inner_text()
    price_text = page.locator('[data-test="unit-price"]').inner_text()
    
    # Extract numeric value from price
    price = float(re.sub(r'[^\d.]', '', price_text))
    
    # Set quantity and add to cart
    quantity_input = page.locator("[data-test=\"quantity\"]")
    quantity_input.fill(QUANTITY)
    page.locator("[data-test=\"add-to-cart\"]").click()
    
    # Go to cart
    page.locator("[data-test=\"nav-cart\"]").click()
    
    # Calculate expected total price
    expected_total_price = f"${price * int(QUANTITY):.2f}"
    
    # Assertions with meaningful messages
    expect(page.locator("[data-test=\"product-name\"]"), 
           "Product name in cart should match selected product").to_have_text(product_title)
    expect(page.locator("[data-test=\"quantity\"]"), 
           "Quantity in cart should match entered quantity").to_have_value(QUANTITY)
    expect(page.locator("[data-test=\"line-price\"]"), 
           "Total price should be calculated correctly").to_have_text(expected_total_price)