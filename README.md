## Playwright UI & API testing suite

A lightweight collection of Playwright + pytest checks. It covers:
- Completing a web form and validating that the page reflects submitted data
- Finding a product and adding it to the cart with verification of price math
- A combined UI/API flow for a contacts service (request interception, authentication, partial updates, and cleanup)

## Technology

- Python 3.12
- pytest
- Playwright via the `pytest-playwright` plugin
- HTML reporting with `pytest-html` (Allure can be plugged in if desired)

## Project layout

- `tests/`
  - `test_part1_test1.py`: populates a form, submits it, and asserts the values shown on the results screen.
  - `test_part2_test2.py`: executes a product search, applies price sorting, adds to cart, and validates quantity plus computed total.
  - `test_contacts_app.py`: signs in via API, intercepts `POST /contacts` to enrich payload, uses the token for requests, updates a field via PATCH, and deletes the created record.
- `screenshots/`: optional directory to store screenshots.
- `reports/`: preferred location for generated HTML reports.
- `final_report.json`: example artifact that downstream tooling can consume.

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

Install Playwright browser binaries (run once):
```bash
pipenv run python -m playwright install
```

Alternative without Pipenv (virtual environment):
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

Generate an HTML report with `pytest-html`:
```bash
pipenv run pytest \
  --html=reports/report.html \
  --self-contained-html
```

After the run completes, open `reports/report.html` in your browser.

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

- For interactive debugging, combine `--headed` with a specific `--browser`.
- Keep artifacts tidy under `screenshots/` and `reports/`.
- Add any new tests under `tests/` with clear names and focused assertions.
