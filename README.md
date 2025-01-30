# Automation Toolkit

This Python script is a multi-purpose automation tool designed to handle various tasks, including package installation, configuration management, database operations, Excel file creation, and web automation using Selenium.

---

## Features

- **Package Installation**: Automatically installs required Python packages if they are missing.
- **Configuration Management**: Manages passwords and configurations in a secure and encrypted manner.
- **Database Operations**: Fetches records from databases (SSMS, Oracle, DP3).
- **Excel File Creation**: Generates Excel files from a list of Pandas DataFrames.
- **Web Automation**: Uses Selenium for browser automation tasks like opening URLs, clicking elements, and entering text.

---

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.8 or higher
- Required Python packages (listed in the script)
- Microsoft Edge WebDriver (for Selenium automation)

---

## Installation

1. Clone this repository or download the script.
2. Install the required Python packages by running the script. It will automatically install any missing packages.

---

## Usage

### 1. Package Installation
The script will automatically check for and install missing packages when run.

### 2. Configuration Management
Use the `ConfigManager` class to manage passwords and configurations:
```python
config_manager = ConfigManager("path/to/config.ini")
config_manager.add_password("account1", "password123")
print(config_manager.read_password("account1"))
```

### 3. Database Operations
Fetch records from a database:
```python
query = "SELECT * FROM your_table"
df = fetch_records(query, "SSMS")
print(df)
```

### 4. Generating Random Data and Excel Reports
Create an Excel file from a list of DataFrames:
```python
df1 = random_data(10)
df2 = random_data(20)
create_excel([df1, df2], "output.xlsx")
```

### 5. Selenium Web Automation
Use the WebDriverManager class for browser automation:
```python
driver_manager = WebDriverManager()
driver = driver_manager.init_driver()
driver_manager.open_url("https://www.google.com")
driver_manager.close_driver()
```
## Configuration
- The script creates a `pyconfig.ini` file to store encrypted passwords.
- Modify `configFileInfo` variable to change the file path.

## Dependencies
- Python 3.x
- Required packages (automatically installed if missing)

## Notes
- Ensure Edge WebDriver (`msedgedriver.exe`) is available at `drivers/msedgedriver.exe`.
- Modify database connection parameters before use.

## License
This project is open-source and can be modified as needed.

## Script Structure
**ConfigManager**: Handles configuration file operations.

**WebDriverManager**: Manages Selenium WebDriver operations.

**fetch_records**: Fetches data from databases.

**create_excel**: Creates Excel files from DataFrames.

**random_data**: Generates random data for testing.

## Author
- Nihal Singh Verma
- 2023-04-27

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## Support
For any questions or issues, please contact nihalsinghverma@hotmail.com or open an issue in the repository.

### **Example File Structure**

automation_toolkit/
├── automation_toolkit.py
├── README.md
├── drivers/
│ └── msedgedriver.exe
└── config/
└── pyconfig.ini
