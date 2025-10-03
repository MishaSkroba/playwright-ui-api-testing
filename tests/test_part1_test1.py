import re
from playwright.sync_api import Page, expect


def test_input_validation_form_submission(page: Page) -> None:
    # Test data
    test_data = {
        "first_name": "Misha",
        "last_name": "Last_Name_Test",
        "age": "34",
        "country": "Belarus",
        "notes": "test notes"
    }
    
    # Navigate to the test page
    page.goto("https://testpages.eviltester.com/styled/validation/input-validation.html")

    # Fill out the form 
    page.get_by_role("textbox", name="First name:").fill(test_data["first_name"])
    page.get_by_role("textbox", name="Last name:").fill(test_data["last_name"])
    page.get_by_role("spinbutton", name="Age:").fill(test_data["age"])
    page.get_by_label("Country:").select_option(test_data["country"])
    page.get_by_role("textbox", name="Notes:").fill(test_data["notes"])

    # Submit the form
    page.get_by_role("button", name="Submit").click()

    # Verify the submitted values
    expect(page.locator("#firstname-value"), "First name should match the submitted value").to_contain_text(test_data["first_name"])
    expect(page.locator("#surname-value"), "Last name should match the submitted value").to_contain_text(test_data["last_name"])
    expect(page.locator("#age-value"), "Age should match the submitted value").to_contain_text(test_data["age"])
    expect(page.locator("#country-value"), "Country should match the selected option").to_contain_text(test_data["country"])
    expect(page.locator("#notes-value"), "Notes should match the submitted text").to_contain_text(test_data["notes"])