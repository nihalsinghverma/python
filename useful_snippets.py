# Read Binary Excel File
import pandas as pd
import pyxlsb
df =  pd.read_excel('Customers.xlsb', engine='pyxlsb', sheet_name = 'Sheet1')
df.shape



# Read data from MySQL database
import mysql.connector
import pandas as pd
connection  = mysql.connector.connect(user='public',  password='text@321', host='localhost', database='test_db')
query = "SELECT * FROM dbn.table"
df = pd.read_sql_query(query, connection)

import pandas as pd

def unpivot_dataframe(df, id_vars, value_vars, var_name='variable', value_name='value'):
    """
    Unpivots a Pandas DataFrame from wide format to long format.

    Args:
        df (pd.DataFrame): The input DataFrame in wide format.
        id_vars (list): List of column names to use as identifier variables.
        value_vars (list): List of column names to unpivot. If None, all
                           columns not in `id_vars` will be used.
        var_name (str, optional): Name to use for the 'variable' column.
                                   Defaults to 'variable'.
        value_name (str, optional): Name to use for the 'value' column.
                                     Defaults to 'value'.

    Returns:
        pd.DataFrame: The unpivoted DataFrame in long format.
    """
    if value_vars is None:
        value_vars = [col for col in df.columns if col not in id_vars]

    unpivoted_df = pd.melt(df,
                            id_vars=id_vars,
                            value_vars=value_vars,
                            var_name=var_name,
                            value_name=value_name)
    return unpivoted_df

if __name__ == '__main__':
    # Example DataFrame in wide format
    data = {'ID': [1, 2, 3],
            'Product_A_Jan': [10, 15, 12],
            'Product_A_Feb': [12, 18, 15],
            'Product_B_Jan': [20, 22, 25],
            'Product_B_Feb': [23, 25, 28]}
    df_wide = pd.DataFrame(data)
    print("Original Wide DataFrame:")
    print(df_wide)

    # Unpivot the DataFrame
    id_columns = ['ID']
    value_columns = ['Product_A_Jan', 'Product_A_Feb', 'Product_B_Jan', 'Product_B_Feb']
    df_long = unpivot_dataframe(df_wide,
                                 id_columns,
                                 value_columns,
                                 var_name='Product_Month',
                                 value_name='Sales')
    print("\nUnpivoted Long DataFrame:")
    print(df_long)

    # Another example where value_vars is None
    data_wide_2 = {'ID': [101, 102],
                   'City': ['New York', 'London'],
                   'Temperature_2023_01': [35, 5],
                   'Temperature_2023_02': [38, 8],
                   'Rainfall_2023_01': [2.5, 1.0],
                   'Rainfall_2023_02': [3.0, 1.5]}
    df_wide_2 = pd.DataFrame(data_wide_2)
    print("\nOriginal Wide DataFrame 2:")
    print(df_wide_2)

    id_columns_2 = ['ID', 'City']
    df_long_2 = unpivot_dataframe(df_wide_2,
                                   id_columns_2,
                                   None,  # Unpivot all other columns
                                   var_name='Measurement_Month',
                                   value_name='Value')
    print("\nUnpivoted Long DataFrame 2:")
    print(df_long_2)
