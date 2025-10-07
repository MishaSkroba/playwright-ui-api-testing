## Playwright UI & API testing suite

A portable set of browser tests powered by Playwright and pytest. It showcases:
- Filling and validating a web form, then asserting the rendered output
- Searching a product and adding it to the cart with price calculations verified
- A mixed UI/API workflow for a contacts service (network interception, auth, PATCH update, and teardown)

## Technology

- Python 3.12
- pytest
- Playwright via the `pytest-playwright` plugin
- HTML reporting with `pytest-html` (Allure can be plugged in if desired)

## Project layout

- `tests/`
  - `test_part1_test1.py`: enters data into a form, submits it, and checks the values shown on the results page.
  - `test_part2_test2.py`: performs product search, sorts by price, adds to cart, and verifies quantity plus line total.
  - `test_contacts_app.py`: authenticates via API, intercepts `POST /contacts` to enrich the payload, uses the token in requests, patches a field, then removes the created record.
- `screenshots/`: optional storage for screenshots.
- `reports/`: suggested folder for HTML reports.
- `final_report.json`: sample artifact produced by consumers of test results.

## Prerequisites

- Python 3.12 or newer
- Git
- Playwright browsers installed (see below)

## Installation

```bash
# In the repository root
pip install pipenv
pipenv install
```

Install browser binaries for Playwright (run once):
```bash
pipenv run python -m playwright install
```

Alternative without Pipenv (using a virtual environment):
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell
pip install -U pip pytest pytest-playwright pytest-html
python -m playwright install
```

## Running tests

Execute all tests (headless):
```bash
pipenv run pytest -q
```

Run a single file:
```bash
pipenv run pytest tests/test_contacts_app.py -q
```

Choose a browser explicitly:
```bash
pipenv run pytest --browser firefox
```

Run with the browser window visible (useful for debugging):
```bash
pipenv run pytest --headed -s
```

Filter by name expression:
```bash
pipenv run pytest -k "cart or contacts"
```

## HTML reporting

Produce an HTML report via `pytest-html`:
```bash
pipenv run pytest \
  --html=reports/report.html \
  --self-contained-html
```

Once finished, open `reports/report.html` in your browser.

## Test scenarios

### Form validation (`tests/test_part1_test1.py`)
- Navigate to the validation page
- Provide first name, last name, age, country, and notes
- Submit and assert the results view mirrors the submitted values

### E-commerce cart (`tests/test_part2_test2.py`)
- Search for an item and sort by price (descending)
- Open the item page, set quantity, and add to cart
- Verify product name, quantity, and computed line total

### Contacts hybrid (`tests/test_contacts_app.py`)
- Authenticate via API and obtain the token from the browser context cookies
- Intercept `POST /contacts` to append a field (e.g., `country`)
- Navigate to the contacts list UI and perform basic table checks
- Apply a `PATCH` to modify a field and validate the response
- Delete the created contact to restore server state

## Useful tips

- Prefer `--headed` with `--browser` when you need interactive debugging.
- Keep artifacts organized under `screenshots/` and `reports/`.
- Place any new tests in `tests/` and use descriptive names with clear assertions.
