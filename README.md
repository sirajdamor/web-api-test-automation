# Web and API Test Automation Framework

Automated tests written in Python for a demo shopping website (UI) and a public REST API.

## What is tested
- **UI** (Selenium + Pytest, Page Object Model) on https://www.saucedemo.com: login, products and sorting, cart, checkout
- **API** (Requests + Pytest) on https://jsonplaceholder.typicode.com: GET, POST, PUT, PATCH, DELETE, filtering, error codes

## Tech stack
Python, Pytest, Selenium WebDriver, Requests, pytest-html, GitHub Actions

## Project structure
- `pages/` page objects (one class per page)
- `tests/ui/` browser tests
- `tests/api/` API tests
- `tests/conftest.py` fixtures (browser, logged-in user, API session) and screenshot on failure

## Run locally
Google Chrome must be installed.

    python -m venv venv
    venv\Scripts\activate.bat
    pip install -r requirements.txt
    pytest

Useful commands:

    pytest -m smoke                 # only smoke tests
    pytest -m api                   # only API tests
    pytest -m ui                    # only browser tests
    set HEADLESS=1 && pytest        # no browser window (Windows)
    pytest --html=report.html --self-contained-html

## Continuous integration
Every push runs the tests on GitHub Actions and uploads an HTML report (and failure screenshots).

## What I learned
(Write 3 or 4 lines in your own words: for example a locator that failed, why explicit waits are better than sleep, and how fixtures removed repeated code.)
