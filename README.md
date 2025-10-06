# playwright-ui-api-testing

A small, cross-browser test suite demonstrating UI and API testing with Playwright and pytest. It includes:

- UI form validation and result verification
- E‑commerce flow: search, sort, add to cart, and pricing assertions
- Hybrid UI/API scenario for a contacts app with request interception, auth token retrieval, PATCH update, and cleanup

## Tech stack

- Python (Pipenv, Python 3.13)
- pytest
- Playwright (via `pytest-playwright` plugin)
- `pytest-html-plus` for HTML reporting

## Repository layout

- `tests/`
  - `test_part1_test1.py`: Validates a form and verifies submitted values on the results page.
  - `test_part2_test2.py`: Searches a product, sorts by price, adds to cart, and checks totals.
  - `test_contacts_app.py`: Logs in via API, intercepts network calls to add a contact with an extra field, reads auth token from cookies, updates via PATCH, and cleans up.
- `screenshots/`: Place to store screenshots (you can attach or generate as needed).
- `report_output/`: Suggested output folder for HTML reports.
- `final_report.json`: Example output artifact (if you aggregate results programmatically).

## Prerequisites

- Python 3.13 installed and available in PATH
- Git
- On first run: Playwright browsers must be installed

## Setup

```bash
# From the project root
pip install pipenv
pipenv install

# Install Playwright browsers (one time)
pipenv run playwright install
```

If you are on Windows PowerShell, the commands are the same. Ensure you run them in the project root directory.

## Running tests

Run the entire suite (headless by default):

```bash
pipenv run pytest
```

Run a specific test file:

```bash
pipenv run pytest tests/test_part2_test2.py
```

Open a visible browser (headed mode) for debugging:

```bash
pipenv run pytest --headed
```

Select a specific browser (Chromium, Firefox, WebKit):

```bash
pipenv run pytest --browser chromium
```

## HTML report

Generate an HTML report using `pytest-html-plus`:

```bash
pipenv run pytest \
  --html=report_output/report.html \
  --self-contained-html
```

After the run, open `report_output/report.html` in a browser.

## Test scenarios in detail

### 1) Form validation (`tests/test_part1_test1.py`)
- Navigates to `https://testpages.eviltester.com/styled/validation/input-validation.html`
- Fills out first name, last name, age, country, and notes
- Submits and asserts the echoed values match the input

### 2) E‑commerce add-to-cart (`tests/test_part2_test2.py`)
- Navigates to `https://practicesoftwaretesting.com/`
- Searches for a product (e.g., "hammer"), sorts by price (desc)
- Opens the first product, sets quantity, adds to cart
- Verifies product name, quantity, and calculated line total

### 3) Contacts app hybrid UI/API (`tests/test_contacts_app.py`)
- Base URL: `https://thinking-tester-contact-list.herokuapp.com`
- Intercepts `POST /contacts` to add `country: "USA"` to the payload and records the created entity
- Logs in via API, retrieves auth token from browser context cookies
- Visits the UI to add a contact and verifies table presence
- Sends a `PATCH /contacts/{id}` to change first name and asserts response
- Cleans up by deleting the created contact

## Tips

- Use `--headed` and `--browser` to debug locally in a chosen browser.
- Keep artifacts (screenshots, reports) under `screenshots/` and `report_output/` for cleanliness.
- If you add new tests, keep them under `tests/` with descriptive names and assertions.
