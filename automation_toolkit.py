"""
Script Name: Automation & Data Processing Toolkit
Author: Nihal Singh Verma
Date Created: 2023-04-27
Description: This script automates various tasks such as package installation, configuration management,
             database operations, Excel file creation, and web automation using Selenium.
"""

import os
import sys
import logging
import subprocess
import configparser
from importlib.util import find_spec

# Third-party imports (lazy-loaded to avoid unnecessary imports)
try:
    import pandas as pd
    import numpy as np
    import cx_Oracle
    import pyodbc
    from sqlalchemy import create_engine
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.edge.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from sql_formatter.core import format_sql
except ImportError as e:
    logging.error(f"Import error: {e}")
    sys.exit(1)

# Constants
REQUIRED_PACKAGES = [
    "pandas", "numpy", "matplotlib", "seaborn", "scipy", "statsmodels", "sklearn",
    "cx_Oracle", "pyodbc", "sqlalchemy", "openpyxl", "sql_formatter", "selenium"
]
CONFIG_FILE = r"C:\Users\nihal\Prod\Python\script\pyconfig.ini"
OUTPUT_DIR = r"C:\Users\nihal\Prod\Python\output"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def install_packages(packages):
    """Install missing packages using pip."""
    missing_packages = [pkg for pkg in packages if not find_spec(pkg)]
    if missing_packages:
        logging.info(f"Installing missing packages: {', '.join(missing_packages)}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_packages])
    else:
        logging.info("All required packages are already installed.")

class ConfigManager:
    """Manages configuration file operations."""
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        if not os.path.exists(self.config_file):
            self._create_default_config()

    def _create_default_config(self):
        """Create a default config file if it doesn't exist."""
        self.config["DEFAULT"] = {"password": "password"}
        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)
        logging.info(f"Config file created at {self.config_file}")

    def encrypt_password(self, password):
        """Encrypt the password using a simple substitution cipher."""
        return "".join([chr(ord(char) + 1) for char in password])

    def decrypt_password(self, encrypted):
        """Decrypt the password using a simple substitution cipher."""
        return "".join([chr(ord(char) - 1) for char in encrypted])

    def add_password(self, account, password):
        """Add a password for the specified account."""
        self.config.read(self.config_file)
        self.config[account] = {"password": self.encrypt_password(password)}
        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)
        logging.info(f"Password added for account: {account}")

    def read_password(self, account):
        """Read the password for the specified account."""
        self.config.read(self.config_file)
        if account not in self.config:
            logging.warning(f"Account '{account}' not found in config file.")
            return None
        return self.decrypt_password(self.config[account]["password"])

    def remove_password(self, account):
        """Remove the password for the specified account."""
        self.config.read(self.config_file)
        if account not in self.config:
            logging.warning(f"Account '{account}' not found in config file.")
            return False
        self.config.remove_section(account)
        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)
        logging.info(f"Password removed for account: {account}")
        return True

    def update_password(self, account, password):
        """Update the password for the specified account."""
        self.config.read(self.config_file)
        if account not in self.config:
            logging.warning(f"Account '{account}' not found in config file.")
            return False
        self.config[account] = {"password": self.encrypt_password(password)}
        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)
        logging.info(f"Password updated for account: {account}")
        return True

    def list_accounts(self):
        """List all accounts in the config file."""
        self.config.read(self.config_file)
        return self.config.sections()

def fetch_records(query, server_type):
    """Fetch records from the database based on the server type."""
    if server_type == "SSMS":
        conn_str = (
            r"Driver={SQL Server};"
            r"Server=your_server_name;"
            r"Database=your_database_name;"
            r"Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(conn_str)
    elif server_type == "Oracle":
        conn = cx_Oracle.connect("username/password@hostname:port/SID")
    elif server_type == "DP3":
        engine = create_engine("your_dp3_connection_string")
        conn = engine.connect()
    else:
        raise ValueError("Unsupported server type")

    try:
        df = pd.read_sql(query, conn)
        return df
    finally:
        conn.close()

def create_excel(dataframes, path):
    """Create an Excel file from a list of dataframes."""
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        for idx, df in enumerate(dataframes):
            sheet_name = f"Sheet{idx + 1}"
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    logging.info(f"Excel file created at {path}")

def random_data(n):
    """Generate random data using numpy."""
    data = np.random.randn(n, 4)
    return pd.DataFrame(data, columns=list("ABCD"))

class WebDriverManager:
    """Manages Selenium WebDriver operations."""
    def __init__(self, driver_path="drivers/msedgedriver.exe"):
        self.driver_path = driver_path
        self.driver = None

    def init_driver(self):
        """Initialize and return an Edge WebDriver."""
        service = Service(self.driver_path)
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Edge(service=service, options=options)
        return self.driver

    def open_url(self, url):
        """Open the given URL in the browser."""
        self.driver.get(url)
        logging.info(f"Opened URL: {url}")

    def find_element(self, locator_type, locator_value, timeout=10):
        """Find an element using explicit wait."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )

    def click_element(self, locator_type, locator_value):
        """Find and click an element."""
        element = self.find_element(locator_type, locator_value)
        element.click()
        logging.info(f"Clicked on element: {locator_value}")

    def enter_text(self, locator_type, locator_value, text, clear_first=True):
        """Find an input field and enter text into it."""
        element = self.find_element(locator_type, locator_value)
        if clear_first:
            element.clear()
        element.send_keys(text)
        logging.info(f"Entered text '{text}' into {locator_value}")

    def get_text(self, locator_type, locator_value):
        """Retrieve text from an element."""
        element = self.find_element(locator_type, locator_value)
        return element.text

    def wait_for_clickable(self, locator_type, locator_value, timeout=10):
        """Wait until an element is clickable."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((locator_type, locator_value))
        )

    def scroll_to_element(self, locator_type, locator_value):
        """Scroll the page to make an element visible."""
        element = self.find_element(locator_type, locator_value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        logging.info(f"Scrolled to element: {locator_value}")

    def close_driver(self):
        """Close the WebDriver."""
        if self.driver:
            self.driver.quit()
            logging.info("Browser closed.")

if __name__ == "__main__":
    install_packages(REQUIRED_PACKAGES)
    config_manager = ConfigManager(CONFIG_FILE)


"""
# Example usage of ConfigManager
config_manager = ConfigManager(CONFIG_FILE)
config_manager.add_password("account1", "password123")
print(config_manager.read_password("account1"))

# Example usage of WebDriverManager
driver_manager = WebDriverManager()
try:
    driver = driver_manager.init_driver()
    driver_manager.open_url("https://www.google.com")
    search_box = driver_manager.wait_for_clickable(By.NAME, "q")
    driver_manager.enter_text(By.NAME, "q", "Selenium with Edge")
    search_box.send_keys(Keys.RETURN)
    first_result = driver_manager.wait_for_clickable(By.XPATH, "(//h3)[1]")
    first_result.click()
finally:
    driver_manager.close_driver()
"""

if __name__ == "__main__":
    install_packages(REQUIRED_PACKAGES)
    config_manager = ConfigManager(CONFIG_FILE)
