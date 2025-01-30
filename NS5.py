import subprocess
import sys

# List of required packages:
# required_packages = ["pandas", "numpy", "matplotlib", "seaborn", "scipy", "statsmodels", "sklearn", "xgboost", "lightgbm", "catboost", "tensorflow", "keras"]
required_packages = ["pandas", "numpy", "matplotlib", "seaborn", "scipy", "statsmodels", "sklearn", "cx_Oracle", "pyodbc", "sqlalchemy", "openpyxl", "sql_formatter", "selenium"]

def installPackages(packages):
    """
    Importing the required packages in this function and checking if they are already installed. If not, this function will install them using the subprocess module.
    """
    for package in packages:
        try:
            __import__(package)
            print(f"{package} already installed.")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Importing the required packages

try:
    import os
    import re
    import configparser
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import cx_Oracle
    import warnings
    import openpyxl
    import pyodbc
    import cx_Oracle
    from sqlalchemy import create_engine
    # import seaborn as sns
    # import scipy
    # import statsmodels
    # import sklearn
    # import sqlalchemy
    # import xgboost
    # import lightgbm
    # import catboost
    # import tensorflow as tf
    # import keras
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.edge.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC    
    from sql_formatter.core import format_sql
except ImportError as e:
    print(f"Error: {e}")
    print("Installing required packages...")
    # installPackages(required_packages)

outds = r"C:\Users\nihal\Prod\Python\output"

# Check for config.ini file if it does not exist, create it new file and store the password in it.

configFileInfo = r"C:\Users\nihal\Prod\Python\script\pyconfig.ini"

def checkConfigFile():
    """
    Check for the existence of the config.ini file. If it does not exist, create a new file and store the password in it.
    """
    if not os.path.exists(configFileInfo):
        config = configparser.ConfigParser()
        config["DEFAULT"] = {"password": "password"}
        with open(configFileInfo, "w") as configfile:
            config.write(configfile)
        print(f"Config file created at {configFileInfo}")

def encryptPassword(password):
    """
    Encrypt the password using a simple substitution cipher.
    """
    encrypted = "".join([chr(ord(char) + 1) for char in password])
    return encrypted

def decryptPassword(encrypted):
    """
    Decrypt the password using a simple substitution cipher.
    """
    decrypted = "".join([chr(ord(char) - 1) for char in encrypted])
    return decrypted

def addPassword(account, password):
    """
    Add the password to the config.ini file.
    """
    config = configparser.ConfigParser()
    config.read(configFileInfo)
    config[account] = {"password": encryptPassword(password)}
    with open(configFileInfo, "w") as configfile:
        config.write(configfile)
    print(f"Password added for account: {account}")

def readPassword(account):
    """
    Read the password from the config.ini file.
    """
    config = configparser.ConfigParser()
    config.read(configFileInfo)
    password = config.get(account, "password")
    return decryptPassword(password)

def removePassword(account):
    """
    Remove the password from the config.ini file.
    """
    config = configparser.ConfigParser()
    config.read(configFileInfo)
    config.remove_section(account)
    with open(configFileInfo, "w") as configfile:
        config.write(configfile)
    print(f"Password removed for account: {account}")

def updatePassword(account, password):
    """
    Update the password in the config.ini file.
    """
    config = configparser.ConfigParser()
    config.read(configFileInfo)
    config[account] = {"password": encryptPassword(password)}
    with open(configFileInfo, "w") as configfile:
        config.write(configfile)
    print(f"Password updated for account: {account}")

def listAccounts():
    """
    List the accounts in the config.ini file.
    """
    config = configparser.ConfigParser()
    config.read(configFileInfo)
    accounts = config.sections()
    return accounts

    def fetchRecords(query, server_type):
        """
        Fetch all records by passing the query and type of server (SSMS, Oracle, DP3).
        """
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
            engine = create_engine('your_dp3_connection_string')
            conn = engine.connect()
        else:
            raise ValueError("Unsupported server type")

        try:
            df = pd.read_sql(query, conn)
            return df
        finally:
            conn.close()

def formatSql(query):
    """
    Format the SQL query using the sql_formatter package.
    """
    formatted_sql = format_sql(query)
    return formatted_sql

def createExcel(dataframes, path):
    """
    Create an Excel file by giving a list of dataframes and the path.
    """
    with pd.ExcelWriter(path, engine='openpyxl') as writer:
        for idx, df in enumerate(dataframes):
            sheet_name = f"Sheet{idx + 1}"
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print(f"Excel file created at {path}")

def randomData(n):
    """
    Generate random data using numpy.
    """
    data = np.random.randn(n, 4)
    df = pd.DataFrame(data, columns=list("ABCD"))
    return df

# pathXl = os.path.join(outds, "output.xlsx")
# df1 = randomData(10)
# df2 = randomData(20)
# createExcel([df1, df2], pathXl)

# addPassword("account1", "password1")
# print(listAccounts())
# updatePassword("account1", "newpassword")
# print(readPassword("account1"))
# removePassword("account1")

# Edge Documentation:
print("Edge Docs \n https://learn.microsoft.com/en-gb/microsoft-edge/webdriver-chromium/?tabs=c-sharp&form=MA13LH")

# Initialize WebDriver for Edge
def init_driver(driver_path="drivers/msedgedriver.exe"):
    """Initialize and return an Edge WebDriver."""
    service = Service(driver_path)
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")  # Maximize window
    driver = webdriver.Edge(service=service, options=options)
    return driver

# Open a URL
def open_url(driver, url):
    """Open the given URL in Edge."""
    driver.get(url)
    print(f"Opened URL: {url}")

# Find an element with waiting
def find_element(driver, locator_type, locator_value, timeout=10):
    """Find an element using explicit wait."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((locator_type, locator_value))
    )

# Click an element
def click_element(driver, locator_type, locator_value):
    """Find and click an element."""
    element = find_element(driver, locator_type, locator_value)
    element.click()
    print(f"Clicked on element: {locator_value}")

# Enter text into a field
def enter_text(driver, locator_type, locator_value, text, clear_first=True):
    """Find an input field and enter text into it."""
    element = find_element(driver, locator_type, locator_value)
    if clear_first:
        element.clear()
    element.send_keys(text)
    print(f"Entered text '{text}' into {locator_value}")

# Get text from an element
def get_text(driver, locator_type, locator_value):
    """Retrieve text from an element."""
    element = find_element(driver, locator_type, locator_value)
    return element.text

# Wait for an element to be clickable
def wait_for_clickable(driver, locator_type, locator_value, timeout=10):
    """Wait until an element is clickable."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((locator_type, locator_value))
    )

# Scroll to an element
def scroll_to_element(driver, locator_type, locator_value):
    """Scroll the page to make an element visible."""
    element = find_element(driver, locator_type, locator_value)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    print(f"Scrolled to element: {locator_value}")

# Close the browser
def close_browser(driver):
    """Close the Edge browser."""
    driver.quit()
    print("Browser closed.")


# Example usage of the Edge WebDriver

# # Initialize Edge WebDriver
# driver = init_driver()

# # Open Google
# open_url(driver, "https://www.google.com")

# # Wait until the search box is clickable
# search_box = wait_for_clickable(driver, By.NAME, "q")

# # Enter text and search
# enter_text(driver, By.NAME, "q", "Selenium with Edge")
# search_box.send_keys(Keys.RETURN)

# # Wait for first search result and click it
# clickable_result = wait_for_clickable(driver, By.XPATH, "(//h3)[1]")
# clickable_result.click()

# # Close browser
# close_browser(driver)


if __name__ == "__main__":
    installPackages(required_packages)
    checkConfigFile()