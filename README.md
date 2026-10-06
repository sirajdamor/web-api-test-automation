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
- Page Object Model: I keep locators and page actions in one class per page (login, inventory, cart, checkout), so when a locator changes I fix it in one place instead of in every test.
- Fixtures: my conftest.py has fixtures for the browser, a logged-in user and the API session, which removed the same login code from many tests.
- Explicit waits: I used WebDriverWait instead of time.sleep, so tests wait only as long as needed and are less flaky.
- CI problem I fixed: my first GitHub Actions run failed because requirements.txt was created outside my virtual environment and contained packages from other projects. I rewrote it with only the four packages this project needs and the pipeline passed.
- UI vs API tests: API tests run in seconds without a browser, while UI tests take about two minutes, so I use markers (smoke, regression, ui, api) to run only the group I need.
