# 🌐 Automated Test Cases for Login Page

## URL: [Practice Test Automation - Login](https://practicetestautomation.com/practice-test-login/)

## 📝 Overview

This repository contains automated test cases to verify the login functionality of the practice test website. The tests cover both positive and negative scenarios.

### 🔒 Test Case 1: Positive Login Test
- **Description:** Verify successful login functionality.
- **Steps:**
  1. Open the login page.
  2. Type `student` into the Username field.
  3. Type `Password123` into the Password field.
  4. Click the Submit button.
- **Expected Results:**
  - The new page URL contains `practicetestautomation.com/logged-in-successfully/`.
  - The new page contains the expected text ("Congratulations" or "successfully logged in").
  - The Log out button is displayed on the new page.

### 🚫 Test Case 2: Negative Username Test
- **Description:** Verify error message for invalid username.
- **Steps:**
  1. Open the login page.
  2. Type `incorrectUser` into the Username field.
  3. Type `Password123` into the Password field.
  4. Click the Submit button.
- **Expected Results:**
  - An error message is displayed.
  - The error message text is "Your username is invalid!".

### 🚫 Test Case 3: Negative Password Test
- **Description:** Verify error message for invalid password.
- **Steps:**
  1. Open the login page.
  2. Type `student` into the Username field.
  3. Type `incorrectPassword` into the Password field.
  4. Click the Submit button.
- **Expected Results:**
  - An error message is displayed.
  - The error message text is "Your password is invalid!".

---

## 🛒 Additional Tests on Monarch Mart Website

### 🆕 Registration
- **Tested functionality:** User registration process.
- **Expected Results:** Successful registration redirects to the welcome page, and a confirmation email is sent.

### 🔑 Login
- **Tested functionality:** User login process.
- **Expected Results:** Successful login redirects to the user dashboard.

### 🔍 Search Product
- **Tested functionality:** Product search functionality.
- **Expected Results:** Relevant products are displayed based on the search query.

### ➕ Add to Cart
- **Tested functionality:** Adding products to the shopping cart.
- **Expected Results:** Products are added to the cart and displayed in the cart summary.

### 🛒 Checkout
- **Tested functionality:** Checkout process.
- **Expected Results:** Successful checkout process completes the order and displays an order confirmation.

