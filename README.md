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

* **Language:** Python (3.8+ recommended)
* **Test Runner:** `pytest`
* **BDD Framework:** `pytest-bdd`
* **Browser Automation:** `playwright` (with `pytest-playwright`)
* **Reporting:** `pytest-html`
* **Configuration:** `python-dotenv`
* **Package Manager:** `pip`
* **Version Control:** `git`

**Important:** Playwright manages its own browser binaries. You will need to install them after setting up the Python environment.
