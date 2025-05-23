# E-commerce Website Test Automation Project (Pytest & Playwright)

## Overview

This project contains automated BDD (Behavior-Driven Development) tests for validating the core functionalities of a sample e-commerce website. It uses Python with **Pytest** as the test runner, **pytest-bdd** for Gherkin feature execution, and **Playwright** (via **pytest-playwright**) for robust browser automation.

The primary goal is to ensure key user flows work as expected, including:
* User Authentication (Login)
* Browse Products
* Adding/Removing items from the Shopping Cart
* Completing the Checkout Process

Test results can be viewed in an automatically generated HTML report thanks to **pytest-html**, and sensitive configuration (like usernames or passwords) can be managed using **python-dotenv**.

## Features Tested

The tests are organized into the following Gherkin feature files:

* `features/login.feature`: Covers user login scenarios.
* `features/products.feature`: Covers interactions on the product listing page.
* `features/cart.feature`: Covers interactions within the shopping cart.
* `features/checkout.feature`: Covers the entire checkout process.

## Tech Stack & Prerequisites

- **Language:** Python (3.8+ recommended)
- **Test Runner:** `pytest`
- **BDD Framework:** `pytest-bdd`
- **Browser Automation:** `playwright` (with `pytest-playwright`)
- **Reporting:** `pytest-html`
- **Configuration:** `python-dotenv`
- **Package Manager:** `pip`
- **Version Control:** `git`

> **Note:** Playwright manages its own browser binaries. You will need to install them after setting up the Python environment.

---

## Getting Started

Follow these steps to set up the project and run the tests locally:

### 1. Clone the Repository
```bash
git clone https://github.com/JakLasGit/SauceDemo_TestAutomation
cd SauceDemo_TestAutomation
```
### 2. Create a Virtual Environment and activate it
```bash
python -m venv .venv
.venv\Scripts\activate
```
### 3. Install Project Dependencies
```bash
pip install -r requirements.txt
```
### 4. Install Playwright Browsers
```bash
playwright install
```
### 5. Run the Tests and generate html report
```bash
pytest --html=report.html
```
