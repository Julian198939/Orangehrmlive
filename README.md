# Orangehrmlive Test Automation

This project is a test suite for automating the testing of basic orangehrmlive login functionality using Selenium, pytest.The project supports multiple browsers, including Chrome, Firefox, and Safari.

---

## Project Structure

```
Orangehrmlive/
├── tests/ # Test code
│ ├── login/
│ │ ├── test_login.py # Login-related tests
│ ├── page/
│ ├── login_page.py # Page Object implementation for the login page
│ ├── conftest.py # Pytest configuration and browser management
├── utils/ # Utility modules
│ ├── browser_options.py # Browser startup options
│ ├── screenshot.py # Screenshot utilities
│ ├── wait_utilities.py # Wait utilities
├── .gitignore # Git ignore rules
├── geckodriver.log # Firefox WebDriver logs
├── README.md # Documentation (this file)

```

## Setup and Run Instructions

The following instructions will help anyone download, build, and run this project successfully.

## 1. Clone the Repository

Run the following commands to clone the repository and navigate to the project folder:

```bash
git clone https://github.com/JulianQA01/Orangehrmlive.git
```

```bash
cd Orangehrmlive
```

## 2. Install Prerequisites

**"Python"**:
Ensure Python 3.8+ is installed. Verify with:

```bash
python --version
```

**"Browser"**:

-**Chrome**:
[Download and install the latest version of Google Chrome](https://www.google.com/chrome/)

-**Firefox**:
[Download and install the latest version of Mozilla Firefox](https://www.mozilla.org/firefox/)

-**Safari**:

Safari is pre-installed on macOS. To enable WebDriver:

1. Go to **Safari > Preferences > Advanced**, and check **Show Develop menu in the menu bar**.
2. From the Develop menu, enable **Allow Remote Automation**.
3. Run the following command to enable the WebDriver:

```bash
safaridriver --enable
```

## 3. Set Up a Virtual Environment and Install Dependencies

Step 1: Create a Virtual Environment

Run the following command in the project directory:

````bash
python -m venv venv
```

Step 2: Activate the Virtual Environment

•macOS/Linux:

```bash
source venv/bin/activate
````

•Windows:

```bash
venv\Scripts\activate
```

Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

The requirements.txt file will ensure that the latest versions of all required packages are installed:

```
selenium
webdriver-manager
pytest

```

Step 4: Run Tests

To run tests using Chrome:

```bash
pytest tests/login/test_login.py --browser chrome
```

To run tests using Firefox:

```bash
pytest tests/login/test_login.py --browser firefox
```

To run tests using Safari:

```bash
pytest tests/login/test_login.py --browser safari
```

If no --browser argument is provided, tests will run on Chrome by default:

```bash
pytest tests/login/test_login.py
```

Step 5: Test Output and Screenshots
• Test results will be displayed in the terminal.
• If any test requires a screenshot, the images will be saved in the screenshots folder at the project root.

Expected Output

If all tests pass successfully, the terminal will display output like the following:

```
=============================== test session starts ================================
platform darwin -- Python 3.13.0, pytest-7.4.2
collected 3 items

tests/login/test_login.py ...                                               [100%]

=============================== 3 passed in 42.64s ================================

```

## Troubleshooting

1. Safari Tests Not Running
   • Ensure Safari WebDriver is enabled, run:

```bash
safaridriver --enable
```

• Confirm Allow Remote Automation is enabled in Safari’s developer settings.
