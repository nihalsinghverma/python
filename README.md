# Python Automation and Database Utility

## Overview
This Python script automates package installation, manages configuration files for storing encrypted passwords, interacts with databases (Oracle, SQL Server, DP3), formats SQL queries, generates Excel reports, and automates web interactions using Selenium with Microsoft Edge.

## Features
- **Automatic Package Installation**: Ensures required Python packages are installed.
- **Configuration File Handling**: Creates and manages `config.ini` for storing encrypted passwords.
- **Database Interaction**:
  - Fetch records from SQL Server, Oracle, or DP3.
  - Use `sqlalchemy`, `cx_Oracle`, and `pyodbc` for connectivity.
- **SQL Query Formatting**: Uses `sql_formatter` to format SQL queries.
- **Excel Report Generation**: Saves multiple pandas DataFrames into an Excel file.
- **Web Automation**:
  - Uses Selenium with Microsoft Edge.
  - Opens URLs, finds elements, enters text, clicks elements, and extracts data.

## Installation
Ensure you have Python installed. Run the script to install missing dependencies automatically.

Alternatively, manually install dependencies using:
```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels scikit-learn cx_Oracle pyodbc sqlalchemy openpyxl sql_formatter selenium
```

## Usage
### 1. Running the Script
Execute the script to ensure dependencies are installed and configuration is set up.
```bash
python script.py
```

### 2. Database Operations
```python
query = "SELECT * FROM users"
df = fetchRecords(query, "SSMS")
print(df.head())
```

### 3. Password Management
```python
addPassword("account1", "mypassword")
print(readPassword("account1"))
updatePassword("account1", "newpassword")
removePassword("account1")
```

### 4. Generating Random Data and Excel Reports
```python
df1 = randomData(10)
df2 = randomData(20)
createExcel([df1, df2], "output.xlsx")
```

### 5. Selenium Web Automation
```python
driver = init_driver()
open_url(driver, "https://www.google.com")
enter_text(driver, By.NAME, "q", "Selenium with Edge")
search_box = wait_for_clickable(driver, By.NAME, "q")
search_box.send_keys(Keys.RETURN)
close_browser(driver)
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

## Author
- Nihal Singh Verma
