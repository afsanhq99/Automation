# Hybrid Automation Framework

This framework is designed for automation testing of web applications. It follows a hybrid approach combining the Page Object Model (POM) with data-driven testing.

## Directory Structure

- `base/`: Contains the base class for setup and teardown of test cases.
- `config/`: Configuration files for the framework.
- `pages/`: Page Object Model (POM) classes.
- `reports/`: Directory for logs and screenshots.
- `screenshots/`: Directory for screenshots of failed tests.
- `tests/`: Test cases.
- `test_data/`: Data files for data-driven testing.
- `utilities/`: Utility modules.
- `conftest.py`: Pytest configuration.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Setup

1. Install the dependencies:

```sh
pip install -r requirements.txt
