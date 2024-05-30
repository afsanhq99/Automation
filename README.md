# Automated Test Cases

## Test Case 1: Positive LogIn test
- **Description:** Verify successful login functionality.
- **Steps:**
  1. Open the login page.
  2. Type "student" into the Username field.
  3. Type "Password123" into the Password field.
  4. Click the Submit button.
- **Expected Results:**
  - The new page URL contains "practicetestautomation.com/logged-in-successfully/".
  - The new page contains the expected text ("Congratulations" or "successfully logged in").
  - The Log out button is displayed on the new page.

## Test Case 2: Negative username test
- **Description:** Verify error message for invalid username.
- **Steps:**
  1. Open the login page.
  2. Type "incorrectUser" into the Username field.
  3. Type "Password123" into the Password field.
  4. Click the Submit button.
- **Expected Results:**
  - An error message is displayed.
  - The error message text is "Your username is invalid!".

## Test Case 3: Negative password test
- **Description:** Verify error message for invalid password.
- **Steps:**
  1. Open the login page.
  2. Type "student" into the Username field.
  3. Type "incorrectPassword" into the Password field.
  4. Click the Submit button.
- **Expected Results:**
  - An error message is displayed.
  - The error message text is "Your password is invalid!".
