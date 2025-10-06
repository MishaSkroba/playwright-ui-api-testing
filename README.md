## Playwright UI & API testing project

A cross-browser test suite based on Playwright and pytest. It demonstrates:
- Form validation and verification of rendered results
- Product search and adding to cart with total amount checks
- Hybrid UI/API scenario for a contacts list (request interception, authorization, PATCH update, cleanup)

## Stack

- Python 3.12
- pytest
- Playwright (plugin `pytest-playwright`)
- HTML reports via `pytest-html` (optionally — Allure)

## Structure

- `tests/`
  - `test_part1_test1.py`: input form data, submit, and verify the displayed values.
  - `test_part2_test2.py`: product search, price sort, add to cart, check quantity and total.
  - `test_contacts_app.py`: API login, intercept `POST /contacts` with an extra field, use token in headers, partial update, and entity deletion.
- `screenshots/`: folder for screenshots (as needed).
- `reports/`: recommended location for HTML reports.
- `final_report.json`: example of a final artifact.

## Requirements

- Python 3.12+
- Git
- Installed Playwright browsers (see below)

## Setup

```bash
# From the project root
pip install pipenv
pipenv install
```

Install Playwright browsers (one-time):
```bash
pipenv run python -m playwright install
```

Alternative without Pipenv (local venv):
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell
pip install -U pip pytest pytest-playwright pytest-html
python -m playwright install
```

## How to run

Run the entire suite (headless):
```bash
pipenv run pytest -q
```

Run a specific file:
```bash
pipenv run pytest tests/test_contacts_app.py -q
```

Choose a browser:
```bash
pipenv run pytest --browser firefox
```

Headed mode (debug-friendly):
```bash
pipenv run pytest --headed -s
```

Filter by test name:
```bash
pipenv run pytest -k "cart or contacts"
```

## HTML report

Generate a report using `pytest-html`:
```bash
pipenv run pytest \
  --html=reports/report.html \
  --self-contained-html
```

After execution, open `reports/report.html` in your browser.

## Scenarios

### Form validation (`tests/test_part1_test1.py`)
- Navigate to the validation page
- Fill in first name, last name, age, country, notes
- Submit and verify the results page displays the submitted values

### E-commerce cart (`tests/test_part2_test2.py`)
- Search for a product, sort by price (descending)
- Open product page, set quantity, add to cart
- Check product name, quantity, and computed line total

### Contacts hybrid (`tests/test_contacts_app.py`)
- Log in via API and read token from the browser context cookies
- Intercept `POST /contacts` and add a field (e.g., `country`)
- UI navigation to the contacts list and basic table checks
- `PATCH` update of a specific field and assert the response
- Delete the created contact to clean up state

## Tips

- Use `--headed` and the desired `--browser` for local debugging.
- Store artifacts (screenshots/reports) in `screenshots/` and `reports/`.
- Add new tests under `tests/` with clear names and assertions.
